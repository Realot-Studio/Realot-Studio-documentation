"""Accuracy patches applied to content fragments, driven by facts extracted from engine source."""
import re
from bs4 import BeautifulSoup
from html import escape

INTERNAL = re.compile(r'^_')
API_MODULE = {
 'Transform':'TransformAPI','SpriteRenderer':'SpriteAPI','ShapeRenderer':'ShapeAPI','TextRenderer':'TextAPI','StrokePath':'StrokePathAPI',
 'SpeechBubble':'SpeechBubbleAPI','ChatLog':'ChatLogAPI','TextInput':'TextInputAPI','Joystick':'JoystickAPI','Rigidbody2D':'RigidbodyAPI','Collider2D':'ColliderAPI',
 'Joint2D':'JointAPI','CharacterController':'ControllerAPI','SpriteAnimation':'AnimatorAPI','Camera':'CameraAPI','AudioSource':'AudioAPI','AudioListener':'AudioListenerAPI',
 'Light':'LightAPI','ShadowCaster':'ShadowCasterAPI','LightingSettings':'LightingSettingsAPI','NavAgent2D':'NavAgentAPI'}

TEXT_FIXES = [
 ('standalone runtime directory/', '<code>project/player/</code>'),
 ('standalone runtime directory', '<code>project/player/</code>'),
]

def first_sentence(s, n=240):
    s = re.sub(r'\s+', ' ', s).strip()
    s = re.sub(r'^(?:runtime/scripting/components/[^ ]+\s*)', '', s)
    m = re.match(r'(.{20,%d}?[.!?])(?:\s|$)' % n, s)
    if m: return m.group(1)
    if len(s) <= n: return s
    return s[:n].rsplit(' ', 1)[0].rstrip(',;:( -') + '…'

def fmt_default(f):
    d = f['default']
    if f['kind'] == 'array' or d.startswith('['):
        pts = re.findall(r'\{[^{}]*\}', d)
        return '[' + ', '.join(re.sub(r'\s+', '', p) for p in pts) + ']' if pts else '[]'
    return d

def kind_label(f, enums):
    k = f['kind'] or ''
    if k.startswith('enum:'):
        enum_name = k[5:]
        vals = list(enums.get(enum_name, {}).values())
        return f'{enum_name} enum' + (': ' + ' | '.join(vals) if vals else '')
    d = f['default']
    if f['name'] in ('color', 'backgroundColor', 'fillColor', 'barColor') or (k == 'string' and d.startswith('#')): return 'hex color string'
    return {'boolean': 'boolean', 'number': 'number', 'string': 'string', 'array': 'array', 'object': 'object', 'null': 'nullable value'}.get(k, k or 'value')

def component_table_rows(tb):
    rows = {}
    for tr in tb.find_all('tr')[1:]:
        td = tr.find_all('td')
        if len(td) >= 4:
            rows[td[0].get_text(strip=True)] = [c.decode_contents() for c in td]
    return rows

def patch_component_table(soup, name, facts):
    comp = facts['components'].get(name)
    if not comp: return []
    h = next((x for x in soup.find_all('h2') if x.get_text(strip=True) == 'Component data'), None)
    if not h: return []
    tb = h.find_next('table')
    if not tb: return []
    rows = component_table_rows(tb); changes = []; body = []
    for f in comp['fields']:
        if INTERNAL.match(f['name']): continue
        old = rows.get(f['name']); dflt = fmt_default(f); typ = kind_label(f, facts['enums'])
        comment = first_sentence(f.get('comment', ''), 320)
        purpose = escape(comment) if comment else ''
        if old:
            old_default = BeautifulSoup(old[3], 'html.parser').get_text(strip=True)
            if old_default != dflt: changes.append(f'{name}.{f["name"]} default → {dflt}')
            old_purpose = BeautifulSoup(old[2], 'html.parser').get_text(' ', strip=True)
            # Prefer source comments. Retain carefully authored documentation where source has no field comment.
            if not purpose: purpose = old[2]
            elif old_purpose and not purpose: purpose = old[2]
        else:
            changes.append(f'{name}.{f["name"]} added')
            purpose = purpose or 'Inspector field stored on this component.'
        body.append([f'<code>{escape(f["name"])}</code>', escape(typ), purpose, f'<code>{escape(dflt)}</code>'])
    extra = set(rows) - {f['name'] for f in comp['fields'] if not INTERNAL.match(f['name'])}
    if extra: changes.append(f'{name}: removed stale fields ' + ', '.join(sorted(extra)))
    th = ''.join(f'<th>{c.get_text(strip=True)}</th>' for c in tb.find_all('th'))
    trs = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in body)
    new = BeautifulSoup(f'<table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table>', 'html.parser')
    tb.replace_with(new)
    return changes

def patch_api_table(soup, name, facts):
    mod = API_MODULE.get(name)
    if not mod: return []
    api = facts['api'].get(mod)
    if not api: return []
    h = next((x for x in soup.find_all('h2') if x.get_text(strip=True) == 'Script API'), None)
    if not h: return []
    tb = h.find_next('table')
    if not tb: return []
    old_rows = {}
    for tr in tb.find_all('tr')[1:]:
        cells = tr.find_all('td')
        if len(cells) >= 3:
            raw = cells[0].get_text(strip=True)
            name_only = re.sub(r'\(.*', '', raw)
            old_rows[name_only] = [raw, cells[1].get_text(' ', strip=True), cells[2].decode_contents()]
    allowed = sorted({m for s in api['member_sets'].values() for m in s})
    body = []; changes = []
    for m in allowed:
        e = api['members'].get(m, {})
        old = old_rows.get(m)
        is_method = bool(e.get('method'))
        incomplete = name == 'Joint2D' and m == 'flexibility' and not (e.get('get') or e.get('set') or e.get('method'))
        kind = 'Allow-listed but not implemented' if incomplete else ('Method' if is_method else ('Property (read-only)' if e.get('get') and not e.get('set') else 'Property (write-only)' if e.get('set') and not e.get('get') else 'Property (read/write)'))
        # Preserve the authored argument list when available; source whitelist still controls exact member names.
        signature = (e.get('signature') if is_method and e.get('signature') else None) or (old[0] if old and (old[0] == m or old[0].startswith(m + '(')) else (m + '(…)' if is_method else m))
        source_doc = first_sentence(e.get('doc', ''), 320)
        old_doc = old[2] if old else ''
        old_doc_text = BeautifulSoup(old_doc, 'html.parser').get_text(' ', strip=True)
        # Prefer meaningful implementation comments, otherwise retain curated explanation.
        doc = ('The JointAPI allow-list contains this name, but no getter or setter is implemented. Reads return undefined and writes do not update Joint2D.flexibility. Set Flexibility (%) in the Inspector instead.' if incomplete else (escape(source_doc) if source_doc and len(source_doc) > 35 and not source_doc.startswith('runtime/scripting/') else (old_doc if old_doc_text else 'Exposed by this script module.')))
        body.append([f'<code>{escape(signature)}</code>', kind, doc])
        if not old: changes.append(f'{name} script API + {m}')
        elif old[1] != kind: changes.append(f'{name} script API kind corrected: {m}')
    extras = set(old_rows) - set(allowed)
    if extras: changes.append(f'{name}: removed non-exposed script API entries ' + ', '.join(sorted(extras)))
    th = ''.join(f'<th>{c.get_text(strip=True)}</th>' for c in tb.find_all('th'))
    trs = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in body)
    new = BeautifulSoup(f'<table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table>', 'html.parser')
    tb.replace_with(new)
    return changes

def apply(html, meta, path, facts, log):
    for a, b in TEXT_FIXES:
        if a in html: html = html.replace(a, b); log.append(f'{path}: text fix {a!r}')
    m = re.match(r'api/components/(\w+)$', path)
    if m:
        name = next((c for c in facts['components'] if c.lower() == m.group(1)), None)
        if name:
            soup = BeautifulSoup(html, 'html.parser')
            log += [f'{path}: {c}' for c in patch_component_table(soup, name, facts)]
            log += [f'{path}: {c}' for c in patch_api_table(soup, name, facts)]
            html = str(soup)
    return html
