#!/usr/bin/env python3
"""Extract ground-truth facts (component fields/defaults, enums, script-API member sets)
from the Realot Studio engine source so the documentation can be generated and verified from code.
Usage: extract_source_facts.py <engine_root> <out.json>"""
import re, json, sys
from pathlib import Path

def strip_comments(s):
    s = re.sub(r'/\*.*?\*/', '', s, flags=re.S)
    return re.sub(r'(?<!:)//[^\n]*', '', s)

def parse_enums(text):
    enums = {}
    for m in re.finditer(r'export const (\w+)\s*=\s*(?:Object\.freeze\()?\{(.*?)\}\)?;', text, re.S):
        vals = {k: v for k, v in re.findall(r'(\w+)\s*:\s*"([^"]*)"', strip_comments(m.group(2)))}
        enums[m.group(1)] = vals
    return enums

def split_top(body):
    depth = 0; cur = ''; parts = []; instr = None
    for ch in body:
        if instr:
            cur += ch
            if ch == instr: instr = None
            continue
        if ch in '"\'`': instr = ch; cur += ch; continue
        if ch in '([{': depth += 1
        if ch in ')]}': depth -= 1
        if ch == ',' and depth == 0: parts.append(cur); cur = ''
        else: cur += ch
    parts.append(cur)
    return parts

def field_comments(raw_body):
    """Map field name -> nearby comment text (preceding // block or trailing // comment)."""
    comments = {}; pending = []
    for line in raw_body.split('\n'):
        s = line.strip()
        if s.startswith('//'): pending.append(s.lstrip('/ ').strip()); continue
        if s.startswith('/*') or s.startswith('*') or s.endswith('*/'):
            t = s.strip('/* ').strip()
            if t: pending.append(t)
            continue
        m = re.match(r'(\w+)\s*=', s)
        if m:
            trailing = re.search(r'//\s*(.*)$', s)
            txt = ' '.join(pending + ([trailing.group(1)] if trailing else []))
            if txt: comments[m.group(1)] = re.sub(r'\s+', ' ', txt).strip()
            pending = []
        elif not s: pending = []
    return comments


def braced_object_end(text, start):
    """Find the matching brace for a JS object while skipping comments/strings."""
    depth = 0; i = start; state = None
    while i < len(text):
        ch = text[i]; nxt = text[i + 1] if i + 1 < len(text) else ''
        if state == 'line':
            if ch == '\n': state = None
        elif state == 'block':
            if ch == '*' and nxt == '/': state = None; i += 1
        elif state in ('single', 'double', 'template'):
            if ch == '\\': i += 1
            elif (state == 'single' and ch == "'") or (state == 'double' and ch == '"') or (state == 'template' and ch == '`'):
                state = None
        else:
            if ch == '/' and nxt == '/': state = 'line'; i += 1
            elif ch == '/' and nxt == '*': state = 'block'; i += 1
            elif ch == "'": state = 'single'
            elif ch == '"': state = 'double'
            elif ch == '`': state = 'template'
            elif ch == '{': depth += 1
            elif ch == '}':
                depth -= 1
                if depth == 0: return text[start:i + 1]
        i += 1
    return text[start:]

def member_details(text, names):
    """Classify only names present in a module's explicit allow-list.

    This deliberately scans accessors and methods separately from the allow-list:
    Proxy traps named get/set must never be mistaken for public API members.
    """
    out = {}
    for name in names:
        esc = re.escape(name)
        found = {'get': False, 'set': False, 'method': False, 'doc': ''}
        signatures = []
        patterns = [
            ('get', re.compile(r'(?m)^[ \t]*get\s+' + esc + r'\s*\([^)]*\)')),
            ('set', re.compile(r'(?m)^[ \t]*set\s+' + esc + r'\s*\([^)]*\)')),
            ('method', re.compile(r'(?m)^[ \t]*' + esc + r'\s*\(([^)]*)\)\s*\{')),
            ('method', re.compile(r'(?m)^[ \t]*' + esc + r'\s*:\s*function\s*\(([^)]*)\)')),
        ]
        matches = []
        for kind, pattern in patterns:
            for m in pattern.finditer(text):
                found[kind] = True
                matches.append((m.start(), kind, m))
                if kind == 'method':
                    params = m.group(1) if m.lastindex else ''
                    sig = name + '(' + re.sub(r'\s+', ' ', params.strip()) + ')'
                    if sig not in signatures: signatures.append(sig)
        # Some APIs are assembled with Object.defineProperties(), where
        # descriptors are nested objects (name: { get, set }) instead of
        # class/object-literal accessors. Recognize those explicitly.
        descriptor_matches = list(re.finditer(r'(?m)^[ \t]*' + esc + r'\s*:\s*\{', text))
        for dm in descriptor_matches:
            open_brace = text.find('{', dm.start(), dm.end())
            descriptor = braced_object_end(text, open_brace) if open_brace >= 0 else ''
            if re.search(r'\bget\s*:', descriptor): found['get'] = True
            if re.search(r'\bset\s*:', descriptor): found['set'] = True
            vm = re.search(r'\bvalue\s*:\s*function\s*\(([^)]*)\)', descriptor)
            if vm:
                found['method'] = True
                sig = name + '(' + re.sub(r'\s+', ' ', vm.group(1).strip()) + ')'
                if sig not in signatures: signatures.append(sig)
        if matches:
            matches.sort(key=lambda item: item[0])
            # Use a JSDoc block only when it directly precedes this declaration.
            prefix = text[:matches[0][0]]
            doc_match = re.search(r'/\*\*(.*?)\*/[ \t\r\n]*$', prefix, re.S)
            if doc_match:
                lines = [re.sub(r'^\s*\*\s?', '', line) for line in doc_match.group(1).split('\n')]
                found['doc'] = re.sub(r'\s+', ' ', ' '.join(line for line in lines if line.strip())).strip()
        if signatures:
            found['signature'] = signatures[0]
        out[name] = found
    return out

def main(root, out):
    root = Path(root); comp_dir = root / 'project/runtime/components'
    enums = {}
    for f in list(comp_dir.glob('*.js')) + list((root / 'project/runtime/systems').glob('*.js')): enums.update(parse_enums(f.read_text()))
    components = {}
    for f in sorted(comp_dir.glob('*.js')):
        t = f.read_text()
        m = re.search(r'constructor\s*\(\s*\{(.*?)\}\s*=\s*\{\}\s*\)', t, re.S)
        if not m: continue
        raw = m.group(1); comments = field_comments(raw)
        body = strip_comments(raw); fields = []
        for p in split_top(body):
            p = p.strip()
            if not p: continue
            k, _, v = p.partition('=')
            k = k.strip(); v = re.sub(r'\s+', ' ', v.strip())
            resolved = v; kind = None
            em = re.fullmatch(r'(\w+)\.(\w+)', v)
            if em and em.group(1) in enums and em.group(2) in enums[em.group(1)]:
                resolved = enums[em.group(1)][em.group(2)]; kind = 'enum:' + em.group(1)
            elif v in ('true', 'false'): kind = 'boolean'
            elif re.fullmatch(r'-?\d+(\.\d+)?', v): kind = 'number'
            elif re.fullmatch(r'"[^"]*"|\'[^\']*\'', v): resolved = v[1:-1]; kind = 'string'
            elif v == 'null': kind = 'null'
            elif v.startswith('['): kind = 'array'
            elif v.startswith('{'): kind = 'object'
            fields.append({'name': k, 'default': resolved, 'kind': kind, 'comment': comments.get(k, '')})
        cls = re.search(r'export class (\w+)', t)
        head = re.search(r'/\*\*(.*?)\*/', t, re.S)
        summary = ''
        if head:
            lines = [re.sub(r'^\s*\*\s?', '', l) for l in head.group(1).split('\n')]
            summary = re.sub(r'\s+', ' ', ' '.join(l for l in lines[2:] if l.strip() and 'RUNTIME-ONLY' not in l)).strip()
        components[cls.group(1) if cls else f.stem] = {'file': str(f.relative_to(root)), 'fields': fields, 'header': summary}
    api = {}
    for f in sorted((root / 'project/runtime/scripting/components').glob('*.js')):
        text = f.read_text()
        sets = {n: re.findall(r'"([^"]+)"', b) for n, b in re.findall(r'const\s+([A-Z_0-9]*MEMBERS[A-Z_0-9]*)\s*=\s*new Set\(\[(.*?)\]\)', text, re.S)}
        # per-member JSDoc + kind (getter/setter/method) so docs can be generated from source comments
        members = {}
        for m in re.finditer(r'(?:/\*\*(.*?)\*/\s*)?(?:^|\n)\s*(get|set)?\s*(\w+)\s*(?:\([^)]*\)\s*\{|:\s*function\s*\()', text, re.S):
            doc, acc, name = m.group(1), m.group(2), m.group(3)
            if name in ('if', 'for', 'while', 'switch', 'function', 'catch', 'return'): continue
            e = members.setdefault(name, {'get': False, 'set': False, 'method': False, 'doc': ''})
            if acc == 'get': e['get'] = True
            elif acc == 'set': e['set'] = True
            else: e['method'] = True
            if doc and not e['doc']:
                lines = [re.sub(r'^\s*\*\s?', '', l) for l in doc.split('\n')]
                e['doc'] = re.sub(r'\s+', ' ', ' '.join(l for l in lines if l.strip())).strip()
            if e['method'] and not e.get('signature'):
                esc = re.escape(name)
                sigs = re.findall(r'^\s*' + esc + r'\s*:\s*function\s*\(([^)]*)\)', text, re.M)
                if not sigs:
                    sigs = re.findall(r'^\s*' + esc + r'\s*\(([^)]*)\)\s*\{', text, re.M)
                if sigs:
                    e['signature'] = name + '(' + re.sub(r'\s+', ' ', sigs[0].strip()) + ')'
        allowed_names = sorted({member for group in sets.values() for member in group})
        # The allow-list decides what exists. Scan those exact names to classify
        # readable/writable properties and real method signatures, without
        # accidentally publishing Proxy implementation traps as API.
        exact_members = member_details(text, allowed_names)
        for name in allowed_names:
            prior = members.get(name, {})
            current = exact_members.get(name, {})
            if not current.get('doc') and prior.get('doc'):
                current['doc'] = prior['doc']
            if not current.get('signature') and prior.get('signature'):
                current['signature'] = prior['signature']
            exact_members[name] = current
        api[f.stem] = {'file': str(f.relative_to(root)), 'member_sets': sets, 'members': exact_members}
    # AI Bridge contracts are part of the engine surface too. Keep the
    # hosted relay tool schemas and the optional local companion list in the
    # same source-derived facts file so docs and AI catalogs stay in sync.
    ai_bridge = {'sharedRelayTools': [], 'localBridgeTools': [], 'config': {}}
    tools_file = root / 'relay/tools.json'
    if tools_file.exists():
        ai_bridge['sharedRelayTools'] = json.loads(tools_file.read_text())
    local_file = root / 'mcp-bridge/server.mjs'
    if local_file.exists():
        local_text = local_file.read_text()
        start = local_text.find('const TOOL_DEFS')
        end = local_text.find('];', start) if start >= 0 else -1
        if start >= 0 and end > start:
            ai_bridge['localBridgeTools'] = re.findall(r'\bname:\s*\"([^\"]+)\"', local_text[start:end])
    config_file = root / 'project/editor/bridge/bridge-config.js'
    if config_file.exists():
        cfg = config_file.read_text()
        for key, pattern in {
            'defaultRelayUrl': r'export const DEFAULT_RELAY_URL = \"([^\"]*)\"',
            'aiMinutesPerDay': r'export const AI_MINUTES_PER_DAY = (\d+)',
            'idleGraceSeconds': r'export const AI_IDLE_GRACE_SECONDS = (\d+)',
            'relayRepoUrl': r'export const RELAY_REPO_URL = \"([^\"]*)\"',
        }.items():
            match = re.search(pattern, cfg)
            if match:
                value = match.group(1)
                ai_bridge['config'][key] = int(value) if value.isdigit() else value
    tags_file = root / 'project/editor/state/Tags.js'
    physics_file = root / 'project/editor/state/PhysicsLayers.js'
    nav_file = root / 'project/editor/state/NavAreas.js'
    editor_settings = {'tagDefaults': ['Untagged', 'Player', 'Enemy'], 'physicsLayerCount': 16,
                       'physicsLayerDefault': 'Default', 'navAreaCount': 16,
                       'navAreaDefaults': ['Ground', 'Water']}
    if tags_file.exists():
        m = re.search(r'const DEFAULT_TAGS = \[([^\]]*)\]', tags_file.read_text())
        if m: editor_settings['tagDefaults'] = re.findall(r'\"([^\"]+)\"', m.group(1))
    if physics_file.exists():
        m = re.search(r'export const LAYER_COUNT = (\d+)', physics_file.read_text())
        if m: editor_settings['physicsLayerCount'] = int(m.group(1))
    if nav_file.exists():
        m = re.search(r'const names = \[([^\]]*)\]', nav_file.read_text())
        if m: editor_settings['navAreaDefaults'] = re.findall(r'\"([^\"]+)\"', m.group(1))
    Path(out).write_text(json.dumps({'enums': enums, 'components': components, 'api': api,
                                     'aiBridge': ai_bridge, 'editorSettings': editor_settings}, indent=1))
    print('components', len(components), 'enums', len(enums), 'api modules', len(api),
          'shared relay tools', len(ai_bridge['sharedRelayTools']),
          'local MCP tools', len(ai_bridge['localBridgeTools']))

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
