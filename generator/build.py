#!/usr/bin/env python3
"""Realot Studio documentation site generator.

  python3 build.py [--out DIR] [--origin https://docs.example.com] [--facts source-facts.json]

Renders content/**/*.html fragments into a fully static, crawlable site (every page is complete HTML;
JavaScript only enhances it), plus Markdown twins, llms.txt / llms-full.txt, search index, sitemap,
robots.txt and machine-readable API catalogs. Verified against source-facts.json (extract with
tools/extract_source_facts.py <engine_root> source-facts.json)."""
import argparse, json, re, shutil, sys, datetime
from pathlib import Path
from html import escape
from bs4 import BeautifulSoup
from markdownify import markdownify as md
sys.path.insert(0, str(Path(__file__).parent))
from lib.icons import svg
from lib.htmlx import process, slugify
from lib import patch

HERE = Path(__file__).parent
ap = argparse.ArgumentParser()
ap.add_argument('--out', default=str(HERE.parent))
ap.add_argument('--origin', default='')
ap.add_argument('--facts', default=str(HERE / 'source-facts.json'))
args = ap.parse_args()
OUT = Path(args.out); ORIGIN = args.origin.rstrip('/')
V = 'docs'
SITE = 'Realot Studio Documentation'
FACTS = json.loads(Path(args.facts).read_text())
CONTENT = HERE / 'content'

# ------------------------------------------------------------------ navigation
def easing_gallery():
    data = json.loads((HERE / 'easings.json').read_text(encoding='utf-8'))['easings']
    fam = [('Basic', ['linear','smoothstep','smootherstep'])]
    for f in ['Quad','Cubic','Quart','Quint','Sine','Expo','Circ','Back','Elastic','Bounce']:
        fam.append((f, ['easeIn'+f,'easeOut'+f,'easeInOut'+f]))
    by = {e['label']: e for e in data}
    out = []
    for fname, names in fam:
        cards = []
        for n in names:
            e = by[n]; lo = min(0.0, e['min']); hi = max(1.0, e['max']); span = (hi - lo) or 1
            pts = e['samples']; n_ = len(pts) - 1
            d = ' '.join(('M' if i == 0 else 'L') + f'{8 + 84*i/n_:.2f} {92 - 84*(v-lo)/span:.2f}' for i, v in enumerate(pts))
            y0 = 92 - 84*(0-lo)/span; y1 = 92 - 84*(1-lo)/span
            cards.append(f'<div class="easing-card"><svg viewBox="0 0 100 100" role="img" aria-label="{n} easing curve"><line class="g" x1="8" y1="{y0:.2f}" x2="92" y2="{y0:.2f}"/><line class="g" x1="8" y1="{y1:.2f}" x2="92" y2="{y1:.2f}"/><path d="{d}"/></svg><code>{n}</code></div>')
        out.append(f'<h3 id="easing-{fname.lower()}">{fname}</h3><div class="easing-grid">{"".join(cards)}</div>')
    names_tbl = '<div class="table-wrap"><table><thead><tr><th>Family</th><th>Names</th></tr></thead><tbody>' + ''.join(f'<tr><td>{f}</td><td>{", ".join("<code>"+n+"</code>" for n in ns)}</td></tr>' for f, ns in fam) + '</tbody></table></div>'
    return names_tbl + ''.join(out)


NAV = [
 ('Get started', 'rocket', [('Overview','index'),('Use Realot Studio','getting-started/installation'),('The Realot Hub','getting-started/hub'),('Build your first game','getting-started/first-game'),('Scripting quickstart','getting-started/scripting')]),
 ('Concepts', 'layers', [('Architecture','concepts/architecture'),('Entities & components','concepts/entities-components'),('Game loop & scenes','concepts/game-loop-scenes'),('Coordinate system','reference/coordinate-system')]),
 ('Editor', 'grid', [('Editor overview','editor/overview'),('Controls & exact locations','editor/controls'),('Editor settings & performance','editor/settings'),('Hierarchy & Inspector','editor/hierarchy-inspector'),('Scenes & projects','editor/scenes-projects'),('Assets & animation','editor/assets-animation'),('Prefab workflow','editor/prefabs'),('Physics authoring','editor/physics'),('Navigation authoring','editor/navigation'),('Lighting, audio & UI','editor/lighting-audio-ui'),('Tilemaps & tilesets','editor/tilemaps'),('Component workflows','editor/component-workflows'),('Complete feature workflows','editor/complete-feature-workflows')]),
 ('Scripting', 'code', [('Lifecycle','scripting/lifecycle'),('Global API','scripting/globals'),('Tween API','scripting/tween'),('Time scale & game speed','scripting/time-scale'),('Entity context (this)','scripting/entity-context'),('Entity shortcuts','scripting/entity-shortcuts'),('Finding & spawning','scripting/finding-entities'),('Input','scripting/input'),('Physics scripting','scripting/physics'),('Collisions & triggers','scripting/collisions'),('Pathfinding','scripting/navigation'),('Navigation: complete setup','scripting/navigation-complete'),('State & messaging','scripting/state-messaging'),('Timers, state & messaging','scripting/timers-state'),('Persistence','scripting/persistence'),('Save data','scripting/saving'),('Errors & debugging','scripting/errors'),('API cookbook','scripting/api-cookbook')]),
 ('API reference', 'braces', [('API index','api/index'),('Runtime modules','api/runtime'),('Script module member index','api/script-modules'),('this (EntityContext)','api/this'),('Option schemas (opts)','api/options'),('Requirements & usage map','api/requirements')]),
 ('Export & deploy', 'package', [('Export overview','export/index'),('HTML5 & PWA','export/web'),('Export window reference','export/export-window'),('Android APK','export/android')]),
 ('Reference', 'book', [('Tuning guide','reference/tuning-guide'),('Scene JSON','reference/scene-format'),('Project format','reference/project-format'),('Engine conventions','reference/rules'),('Debugging','reference/debugging'),('Security & play origin','reference/security'),('Live updates','reference/live-updates'),('Source map','reference/source-map')]),
 ('AI & machine access', 'bot', [('AI Bridge and MCP','reference/ai-bridge'),('AI & crawlers','reference/ai-crawling'),('For AI assistants & LLMs','reference/llm-guide')]),
]
COMPONENT_GROUPS = [
 ('Rendering & UI', ['Transform','SpriteRenderer','ShapeRenderer','TextRenderer','StrokePath','SpeechBubble','ChatLog','TextInput','Joystick']),
 ('Physics & movement', ['Rigidbody2D','Collider2D','Joint2D','CharacterController']),
 ('Animation, camera & audio', ['SpriteAnimation','Camera','AudioSource','AudioListener']),
 ('Lighting', ['Light','ShadowCaster','LightingSettings']),
 ('Navigation & tiles', ['NavAgent2D','NavWorld2D','Tileset','Tilemap']),
 ('Scripting', ['Script']),
]
COMP_NAMES = [c for _, cs in COMPONENT_GROUPS for c in cs]
assert set(COMP_NAMES) == set(FACTS['components']) - {'StrokePathGeometry'}, set(FACTS['components']) ^ set(COMP_NAMES)
COMP_SUMMARY = {}

SCRIPT_MODULE_CONTEXT = {
 'AnimatorAPI': ('this.animator', 'SpriteAnimation component'), 'AudioAPI': ('this.audio', 'AudioSource component'),
 'AudioListenerAPI': ('this.ear', 'AudioListener component'), 'CameraAPI': ('this.camera', 'Camera component'),
 'ChatLogAPI': ('this.chat', 'ChatLog component'), 'ColliderAPI': ('this.collider', 'Collider2D component'),
 'ControllerAPI': ('this.controller', 'CharacterController component. This module combines members for several movement types; a member is available only when the component is set to a compatible type (Character, Platformer, Top-Down, Car, Follow or Patrol). Free mode exposes only its small common surface.'), 'JointAPI': ('this.joint', 'Joint2D component'),
 'JoystickAPI': ('this.joystick', 'Joystick component'), 'LightAPI': ('this.light', 'Light component'),
 'LightingSettingsAPI': ('scene.lighting', 'Scene lighting settings; exposed through the scene global'),
 'NavAgentAPI': ('this.navAgent', 'NavAgent2D component'), 'RigidbodyAPI': ('this.rigidbody', 'Rigidbody2D component'),
 'SaveAPI': ('save', 'Global save store; no entity component required'), 'ShadowCasterAPI': ('this.shadowCaster', 'ShadowCaster component'),
 'ShapeAPI': ('this.shape', 'ShapeRenderer component'), 'SpeechBubbleAPI': ('this.speechBubble', 'SpeechBubble component'),
 'SpriteAPI': ('this.sprite', 'SpriteRenderer component'), 'StateAPI': ('this.state', 'Available on every entity; no component required'),
 'StrokePathAPI': ('this.strokePath', 'StrokePath component'), 'TextAPI': ('this.text', 'TextRenderer component'),
 'TextInputAPI': ('this.textInput', 'TextInput component'), 'TouchTrackAPI': ('this.myTouch', 'Available on every entity; no component required'),
 'TransformAPI': ('this.transform', 'Available on every entity; no component required')
}

GLOBAL_API_SURFACE = {
 'Entity lookup functions': ['findFirst(name)', 'findAll(name)', 'findFirstWithTag(tag)', 'findAllWithTag(tag)', 'findWithTag(tag)', 'findById(id)', 'findInRadius(x, y, radius, opts)'],
 'Scene (`scene`)': ['findFirst(name)', 'findAll(name)', 'findFirstWithTag(tag)', 'findAllWithTag(tag)', 'findWithTag(tag)', 'findById(id)', 'load(sceneName)', 'restart()', 'pause()', 'resume()', 'isPaused (read-only)', 'current (read-only)', 'lighting'],
 'Physics (`physics`)': ['raycast(x1, y1, x2, y2, opts)', 'layer(...indices)'],
 'Navigation (`nav`)': ['findPath(x1, y1, x2, y2, opts)', 'isWalkable(x, y)', 'bake()', 'areaIndex(name)', 'areaMask(...names)', 'areaCosts(costsByName)'],
 'Input (`input`)': ['keyDown(key)', 'keyPressed(key)'],
 'Mouse (`mouse`)': ['x, y (world-space)', 'screenX, screenY (canvas pixels)', 'over (read-only)', 'down(button?)', 'pressed(button?)', 'released(button?)', 'isOver(entityOrName, opts)', 'clickedOn(entityOrName, opts, button?)'],
 'Touch (`touch`)': ['count, first, anyJustStarted, anyJustEnded', 'per-touch: id, x, y, screenX, screenY, startX, startY, dx, dy, distance, justStarted, justEnded', 'swipe: active, direction, dx, dy, distance', 'pinch: active, scale, delta, distance', 'isOver(entityOrName, opts)', 'tappedOn(entityOrName, opts)'],
 'Time (`time`)': ['deltaTime', 'unscaledDeltaTime', 'elapsed', 'scale'],
 'Random (`random`)': ['int(min, max)', 'float(min, max)'],
 'Math helpers (`mathx`)': ['lerp(a, b, t)', 'smoothstep(a, b, value)', 'clamp(value, min, max)', 'moveToward(current, target, maxDelta)', 'remap(value, inMin, inMax, outMin, outMax)', 'approximately(a, b, epsilon?)'],
 'Global state (`global`)': ['Read, write and test arbitrary named in-memory values shared by scripts; resets when the game page is reloaded.'],
 'Debug HUD (`debug`)': ['show(on?)', 'showFps(on?)', 'log(label, value)', 'clear(label)', 'clearAll()'],
 'Object pools (`pool`)': ['create(name, options)', 'find(name)', 'get(name, x, y)', 'release(entity)'],
 'Global functions': ['spawn(nameOrTag, opts)', 'wait(seconds, callback)', 'cancelWait(timerId)', 'repeat(seconds, callback)', 'cancelRepeat(timerId)', 'sendMessage(tagOrEntity, message, data)', 'broadcastMessage(message, data)', 'tween(target, properties, duration, easing?, onComplete?)', 'cancelTween(tweenId)', 'smoothstep(a, b, value)'],
}

def existing_component_api_rows(component):
    path = CONTENT / 'api' / 'components' / (component.lower() + '.html')
    if not path.exists(): return {}
    soup = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')
    h = next((x for x in soup.find_all('h2') if x.get_text(strip=True) == 'Script API'), None)
    table = h.find_next('table') if h else None
    out = {}
    if table:
        for tr in table.find_all('tr')[1:]:
            cells = tr.find_all('td')
            if len(cells) >= 3:
                raw = cells[0].get_text(' ', strip=True)
                out[re.sub(r'\(.*', '', raw)] = (raw, cells[1].get_text(' ', strip=True), cells[2].get_text(' ', strip=True))
    return out

def script_modules_html(facts):
    module_to_component = {v:k for k,v in patch.API_MODULE.items()}
    out = ['<p>This is the complete member-name index for the script modules exposed by the supplied engine source. The allow-list in each module is the authority: entries not listed here are not part of that module’s supported script surface. Use the matching component page for full field meanings and examples.</p>']
    for module in sorted(facts['api']):
        api = facts['api'][module]
        context, requirement = SCRIPT_MODULE_CONTEXT.get(module, (module, 'See the module source'))
        component = module_to_component.get(module)
        existing = existing_component_api_rows(component) if component else {}
        allowed = sorted({m for values in api['member_sets'].values() for m in values})
        rows = []
        for member in allowed:
            e = api['members'].get(member, {})
            prior = existing.get(member)
            method = bool(e.get('method')) or (prior and prior[1].lower() == 'method')
            if e.get('get') and not e.get('set'): kind = 'Read-only property'
            elif e.get('set') and not e.get('get'): kind = 'Write-only property'
            elif e.get('get') and e.get('set'): kind = 'Read/write property'
            elif method: kind = 'Method'
            elif prior and 'read-only' in prior[1].lower(): kind = 'Read-only property'
            elif prior and prior[1].lower().startswith('property'): kind = prior[1]
            else: kind = 'Exposed member'
            signature = e.get('signature') if method else None
            if not signature and prior: signature = prior[0]
            if not signature: signature = member + '(…)' if method else member
            doc = patch.first_sentence(e.get('doc',''), 320)
            if module == 'JointAPI' and member == 'flexibility' and not (e.get('get') or e.get('set') or e.get('method')):
                kind = 'Allow-listed but not implemented'
                doc = 'The proxy allow-list contains this name, but the current JointAPI target has no getter or setter for it. Reads return undefined and writes do not update Joint2D.flexibility. Set Flexibility (%) in the Inspector instead.'
            elif not doc or doc.startswith('runtime/scripting/components/'):
                doc = prior[2] if prior else 'Member name confirmed by the module allow-list. See the corresponding component or scripting guide for usage details.'
            rows.append(f'<tr><td><code>{escape(signature)}</code></td><td>{escape(kind)}</td><td>{escape(doc)}</td></tr>')
        out.append(f'<h2 id="{module.lower()}">{escape(module)}</h2><p><strong>Access:</strong> <code>{escape(context)}</code>. <strong>Requirement:</strong> {escape(requirement)}. <strong>Source:</strong> <code>{escape(api["file"])}</code>.</p>')
        out.append('<div class="table-wrap"><table><thead><tr><th>Member</th><th>Access</th><th>Purpose</th></tr></thead><tbody>' + ''.join(rows) + '</tbody></table></div>')
    out.append('<h2 id="global-runtime-objects">Global runtime objects and functions</h2><p>The global runtime API is separate from per-entity component modules. The exact global members and common option shapes are described in <a href="runtime.html">Runtime modules</a>, <a href="../scripting/globals.html">Global API</a>, <a href="../scripting/input.html">Input</a>, and <a href="../scripting/persistence.html">Persistence</a>.</p>')
    for heading, members in GLOBAL_API_SURFACE.items():
        out.append(f'<h3>{escape(heading)}</h3><ul>' + ''.join(f'<li><code>{escape(x)}</code></li>' for x in members) + '</ul>')
    return ''.join(out)

def render_ai_bridge_tools(facts):
    bridge = facts.get('aiBridge', {})
    tools = bridge.get('sharedRelayTools', [])
    groups = {
        'Project and scene inspection': [],
        'Entities and components': [],
        'Scripts, play mode and diagnostics': [],
        'Assets and uploads': [],
        'Animation': [],
        'Tilesets and tilemaps': [],
        'Navigation and physics': [],
        'Tags, folders and prefabs': [],
        'Export and project files': [],
        'Editor controls': [],
    }
    for tool in tools:
        n = tool.get('name', '')
        if n in {'get_editor_state', 'list_scenes', 'list_entities', 'get_entity'}:
            group = 'Project and scene inspection'
        elif n in {'create_entity', 'update_entity', 'update_component', 'add_component', 'remove_component', 'delete_entities', 'select_entities', 'create_scene', 'switch_scene', 'rename_scene', 'delete_scene', 'duplicate_scene'}:
            group = 'Entities and components'
        elif n in {'list_scripts', 'get_script', 'write_script', 'attach_script', 'delete_script', 'set_script_enabled', 'set_playing', 'set_paused', 'get_console', 'screenshot', 'undo', 'redo'}:
            group = 'Scripts, play mode and diagnostics'
        elif 'asset' in n or n in {'rename_asset', 'delete_asset'}:
            group = 'Assets and uploads'
        elif 'animation' in n or 'frame' in n or n in {'create_animation_clip', 'update_animation_clip', 'delete_animation_clip', 'move_animation_frame', 'add_animation_frames'}:
            group = 'Animation'
        elif 'tileset' in n or 'tilemap' in n or n in {'set_tileset_slot', 'slice_asset_into_tileset', 'paint_tilemap'}:
            group = 'Tilesets and tilemaps'
        elif 'navigation' in n or 'navworld' in n or 'physics' in n or 'collider' in n:
            group = 'Navigation and physics'
        elif any(x in n for x in ('tag', 'prefab', 'folder')):
            group = 'Tags, folders and prefabs'
        elif any(x in n for x in ('export', 'project_zip', 'save_project')):
            group = 'Export and project files'
        elif any(x in n for x in ('editor_panel', 'editor_tool')):
            group = 'Editor controls'
        else:
            group = 'Editor controls'
        groups[group].append(tool)
    out = []
    for heading, entries in groups.items():
        if not entries: continue
        rows = []
        for item in entries:
            name = item.get('name', '')
            desc = item.get('description', '').replace('a .realot/.zip project', 'a .realot project')
            schema = item.get('inputSchema', {})
            props = schema.get('properties', {})
            required = set(schema.get('required', []))
            arg_parts = []
            for key, spec in props.items():
                typ = spec.get('type', 'any')
                if isinstance(typ, list): typ = '|'.join(typ)
                suffix = ''
                if spec.get('enum'): suffix = ' [' + ', '.join(str(x) for x in spec['enum']) + ']'
                label = '<code>' + escape(key) + '</code>: ' + escape(str(typ)) + escape(suffix)
                if key in required: label = '<strong>' + label + ' (required)</strong>'
                arg_parts.append(label)
            arg_html = '<div class="tool-args"><span>Inputs:</span> ' + ('; '.join(arg_parts) or 'none') + '</div>'
            rows.append(f'<tr><td><code>{escape(name)}</code>{arg_html}</td><td>{escape(desc)}</td></tr>')
        out.append(f'<h3>{escape(heading)}</h3><div class="table-wrap"><table><thead><tr><th>Tool</th><th>What it does</th></tr></thead><tbody>{"".join(rows)}</tbody></table></div>')
    return ''.join(out)

def url_of(key):  # page key -> stable, unversioned path relative to site root
    return f'{V}/index.html' if key == 'index' else f'{V}/{key}.html'

# ------------------------------------------------------------------ load + patch content
log = []; PAGES = {}
for f in sorted(CONTENT.rglob('*.html')):
    key = f.relative_to(CONTENT).with_suffix('').as_posix()
    raw = f.read_text(encoding='utf-8')
    if key == 'api/script-modules': raw = raw.replace('<!--SCRIPT_MODULES-->', script_modules_html(FACTS))
    if key == 'reference/ai-bridge': raw = raw.replace('<!--AI_BRIDGE_TOOLS-->', render_ai_bridge_tools(FACTS))
    m = re.match(r'<!--meta (.*?) -->\n', raw, re.S)
    meta = json.loads(m.group(1)); body = raw[m.end():]
    body = patch.apply(body, meta, key, FACTS, log)
    PAGES[key] = {'key': key, 'meta': meta, 'body': body}

group_of = {}
for gname, gicon, items in NAV:
    for t, k in items: group_of[k] = (gname, t)
for c in COMP_NAMES: group_of[f'api/components/{c.lower()}'] = ('Components', c)
missing = [k for k in PAGES if k not in group_of and k != 'index']
assert not missing, missing
unused = [k for k in group_of if k not in PAGES]
assert not unused, unused

# ------------------------------------------------------------------ rendering pieces
def rel(root, target): return root + target
def sidebar(root, current):
    out = []
    def link(t, key, cls=''):
        cur = ' aria-current="page"' if key == current else ''
        return f'<a href="{root}{url_of(key)}"{cur}>{escape(t)}</a>'
    for gname, gicon, items in NAV:
        open_ = ' open' if any(k == current for _, k in items) or gname == 'Get started' and current == 'index' else ''
        out.append(f'<details class="side-group"{open_}><summary>{svg(gicon)}<span>{escape(gname)}</span>{svg("chevron","icon chev")}</summary><div class="side-links">' + ''.join(link(t, k) for t, k in items) + '</div></details>')
    comp_open = ' open' if current.startswith('api/components/') else ''
    inner = ''
    for gname, cs in COMPONENT_GROUPS:
        inner += f'<div class="side-sub">{escape(gname)}</div>' + ''.join(link(c, f'api/components/{c.lower()}') for c in cs)
    out.append(f'<details class="side-group"{comp_open}><summary>{svg("box")}<span>Components</span>{svg("chevron","icon chev")}</summary><div class="side-links">{inner}</div></details>')
    return '\n'.join(out)

def topbar(root, section):
    def a(label, href, key=None):
        cur = ' aria-current="true"' if key and key == section else ''
        return f'<a href="{root}{href}"{cur}>{label}</a>'
    return f'''<header class="topbar"><div class="topbar-inner">
<button class="icon-btn menu-toggle" type="button" data-menu-toggle aria-label="Toggle navigation" aria-controls="sidebar">{svg("menu")}</button>
<a class="brand" href="{root}index.html"><img class="brand-mark" src="{root}favicon.svg" alt=""><span>Realot Studio</span><small>Docs</small></a>
<nav class="topnav" aria-label="Primary">{a("Guides", V+"/getting-started/installation.html", "guides")}{a("Scripting", V+"/scripting/lifecycle.html", "scripting")}{a("API", V+"/api/index.html", "api")}{a("Reference", V+"/reference/tuning-guide.html", "reference")}{a("For AI", V+"/reference/llm-guide.html", "ai")}</nav>
<div class="top-spacer"></div>
<button class="search-btn" type="button" data-search-open aria-label="Search documentation" aria-keyshortcuts="Control+K Meta+K /">{svg("search")}<span>Search docs…</span><kbd data-mod>Ctrl K</kbd></button>
<button class="icon-btn" type="button" data-theme-toggle aria-label="Toggle color theme">{svg("sun","icon i-sun")}{svg("moon","icon i-moon")}</button>
</div></header>'''

def section_of(key):
    if key.startswith('scripting/'): return 'scripting'
    if key.startswith('api/'): return 'api'
    if key.startswith('reference/ai') or key.startswith('reference/llm'): return 'ai'
    if key.startswith('reference/'): return 'reference'
    return 'guides'

THEME_BOOT = "<script>(function(){try{var t=localStorage.getItem('realot-docs-theme');if(!t)t=matchMedia('(prefers-color-scheme: light)').matches?'light':'dark';document.documentElement.setAttribute('data-theme',t)}catch(e){document.documentElement.setAttribute('data-theme','dark')}})()</script>"

def head(root, title, desc, path, extra='', md_path=None, jsonld=None, og_type='article'):
    canon = f'<link rel="canonical" href="{ORIGIN}/{path}">' if ORIGIN else ''
    ogurl = f'<meta property="og:url" content="{ORIGIN}/{path}">' if ORIGIN else ''
    mdl = f'<link rel="alternate" type="text/markdown" href="{Path(md_path).name}" title="Markdown version">' if md_path else ''
    ld = f'<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False, separators=(",", ":"))}</script>' if jsonld else ''
    return f'''<!doctype html>
<html lang="en" data-theme="dark" data-root="{root or './'}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc, quote=True)}">
<meta name="robots" content="index,follow,max-snippet:-1">
<meta name="theme-color" content="#0a0c11">
<meta name="generator" content="Realot Studio docs build">
<meta property="og:site_name" content="{SITE}"><meta property="og:type" content="{og_type}"><meta property="og:title" content="{escape(title, quote=True)}"><meta property="og:description" content="{escape(desc, quote=True)}">{ogurl}
<meta name="twitter:card" content="summary">
{canon}{mdl}
<link rel="icon" href="{root}favicon.svg" type="image/svg+xml">
<link rel="icon" href="{root}favicon.ico" sizes="any">
<link rel="icon" href="{root}icons/icon-48.png" type="image/png" sizes="48x48">
<link rel="icon" href="{root}icons/icon-192.png" type="image/png" sizes="192x192">
<link rel="apple-touch-icon" href="{root}icons/apple-touch-icon.png">
<link rel="search" type="application/opensearchdescription+xml" title="Realot Studio Docs" href="{root}opensearch.xml">
{THEME_BOOT}
<link rel="stylesheet" href="{root}assets/site.css">
{extra}{ld}
</head>'''

def crumbs_html(root, key, title):
    g = group_of.get(key)
    parts = [f'<a href="{root}index.html">Realot Studio</a>', f'<a href="{root}{url_of("index")}">Docs</a>']
    if g and key != 'index':
        first = next((k for gn, _, items in NAV if gn == g[0] for _, k in items), None) if g[0] != 'Components' else 'api/index'
        parts.append(f'<a href="{root}{url_of(first)}">{escape(g[0])}</a>')
    parts.append(f'<span aria-current="page">{escape(title)}</span>')
    return '<nav class="crumbs" aria-label="Breadcrumb">' + '<span class="sep">/</span>'.join(parts) + '</nav>', parts

def flat_order():
    order = []
    for _, _, items in NAV: order += [k for _, k in items]
    order += [f'api/components/{c.lower()}' for c in COMP_NAMES]
    return order
ORDER = flat_order()

def pager(root, key):
    if key not in ORDER: return ''
    i = ORDER.index(key); out = ''
    if i > 0:
        p = ORDER[i-1]; out += f'<a class="pn prev" href="{root}{url_of(p)}" rel="prev"><small>← Previous</small><b>{escape(PAGES[p]["meta"]["title"])}</b></a>'
    if i < len(ORDER)-1:
        n = ORDER[i+1]; out += f'<a class="pn next" href="{root}{url_of(n)}" rel="next"><small>Next →</small><b>{escape(PAGES[n]["meta"]["title"])}</b></a>'
    return f'<nav class="pager" aria-label="Previous and next pages">{out}</nav>'

def footer(root):
    return f'''<footer class="foot"><span>Realot Studio · live documentation</span><nav aria-label="Footer"><a href="{root}index.html">Home</a><a href="{root}{url_of('index')}">Guides</a><a href="{root}search.html">Search</a><a href="{root}llms.txt">AI guide</a><a href="{root}llms-full.txt">Full text</a><a href="{root}search-index.json">Search index</a><a href="{root}api/index.json">API JSON</a><a href="{root}sitemap.html">Site map</a></nav></footer>'''

def toc_html(heads):
    if len(heads) < 2: return ''
    lis = ''.join(f'<li class="l{lv}"><a href="#{i}">{escape(t)}</a></li>' for lv, t, i in heads)
    return f'<aside class="toc" aria-label="On this page"><h2>On this page</h2><ol>{lis}</ol></aside>'

def plain(html):
    s = BeautifulSoup(html, 'html.parser')
    for x in s.select('.anchor, .copy, svg, script, style'): x.decompose()
    return re.sub(r'\s+', ' ', s.get_text(' ', strip=True))

RENDERED = {}
def write(rel_path, content):
    p = OUT / rel_path; p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding='utf-8'); return p

def render_doc(key, title, desc, lede, body_html, page_path, kind='Guide', jsonld_type='TechArticle', md_source=True):
    depth = len(Path(page_path).parts) - 1; root = '../' * depth
    if '<!--EASINGS-->' in body_html: body_html = body_html.replace('<!--EASINGS-->', easing_gallery())
    body, heads = process(body_html, key, root)
    gname = group_of.get(key, ('Docs', title))[0]
    crumb, crumb_parts = crumbs_html(root, key, title)
    md_name = Path(page_path).with_suffix('.md').as_posix()
    tools = ''
    if md_source:
        tools = f'<div class="page-tools"><button class="chip-btn" type="button" data-copy-md>{svg("copy")}Copy page as Markdown</button><a class="chip-btn" href="{Path(md_name).name}">{svg("filecode")}View as Markdown</a><a class="chip-btn" href="{root}llms.txt">{svg("bot")}llms.txt</a></div>'
    ld = {'@context': 'https://schema.org', '@graph': [
        {'@type': 'TechArticle', 'headline': title, 'description': desc, 'inLanguage': 'en', 'isPartOf': {'@type': 'WebSite', 'name': SITE}, 'about': 'Realot Studio 2D game engine', **({'url': f'{ORIGIN}/{page_path}'} if ORIGIN else {})},
        {'@type': 'BreadcrumbList', 'itemListElement': [{'@type': 'ListItem', 'position': i+1, 'name': re.sub('<[^>]+>', '', c)} for i, c in enumerate(crumb_parts)]}]}
    cur = key
    html = (head(root, f'{title} · {SITE}' if key != 'index' else SITE, desc, page_path, md_path=md_name if md_source else None, jsonld=ld) +
      f'''\n<body data-layout="docs" data-page="{escape(key)}"><a class="skip" href="#main">Skip to content</a><div id="nav-progress"></div>
{topbar(root, section_of(key))}
<div class="shell"><aside class="sidebar" id="sidebar" aria-label="Documentation navigation">{sidebar(root, cur)}</aside>
<main id="main" class="main"><div class="doc-grid"><article class="doc">{crumb}<div class="eyebrow">{escape(gname)}</div><h1>{escape(title)}</h1><p class="lede">{escape(lede)}</p>{tools}{body}{pager(root, key)}{footer(root)}</article>{toc_html(heads)}</div></main></div>
<script src="{root}assets/site.js" defer></script></body></html>''')
    write(page_path, html)
    # markdown twin
    mdsoup = BeautifulSoup(body, 'html.parser')
    for x in mdsoup.select('.anchor, .copy, svg, header'): x.decompose()
    for c in mdsoup.select('div.callout'):
        t = c.select_one('.ctitle'); label = (t.get_text(strip=True) if t else 'Note')
        if t: t.decompose()
        c.replace_with(BeautifulSoup('<blockquote><strong>' + escape(label) + ':</strong> ' + c.get_text(' ', strip=True) + '</blockquote>', 'html.parser'))
    for cb in mdsoup.select('div.codeblock'):
        lang = cb.get('data-lang', '')
        cb.replace_with(BeautifulSoup('<pre><code class="language-' + lang + '">' + escape(cb.find('pre').get_text()) + '</code></pre>', 'html.parser'))
    md_body = md(str(mdsoup), heading_style='ATX', code_language_callback=lambda el: (el.get('class') or [''])[0].replace('language-', ''), bullets='-')
    md_body = re.sub(r'\n{3,}', '\n\n', md_body).strip()
    md_url = (ORIGIN + '/' if ORIGIN else '') + page_path
    md_text = f'# {title}\n\n> {desc}\n\n- Source: {md_url}\n\n{md_body}\n'
    write(md_name, md_text)
    toks = []
    for cel in BeautifulSoup(body, 'html.parser').select('code'):
        for t in re.findall(r'[A-Za-z_$][\w$]{2,}', cel.get_text()):
            if t not in toks: toks.append(t)
    RENDERED[key] = {'code': ' '.join(toks[:320]), 'title': title, 'desc': desc, 'url': page_path, 'group': gname, 'heads': heads, 'text': plain(body), 'md': md_body}
    return root

# ------------------------------------------------------------------ pages
for key, p in PAGES.items():
    if key == 'index': continue
    m = p['meta']
    render_doc(key, m['title'], m['description'] or m['lede'], m['lede'] or m['description'], p['body'], url_of(key))

# component summaries (from patched pages) for cards
for c in COMP_NAMES:
    soup = BeautifulSoup(PAGES[f'api/components/{c.lower()}']['body'], 'html.parser')
    h = next((x for x in soup.find_all('h2') if x.get_text(strip=True) == 'What it does'), None)
    COMP_SUMMARY[c] = h.find_next('p').get_text(' ', strip=True) if h else ''

# docs home
def home_body():
    n_comp = len(COMP_NAMES); n_pages = len(PAGES) + 1
    cards = ''
    icons = {'Get started':'rocket','Concepts':'layers','Editor':'grid','Scripting':'code','API reference':'braces','Export & deploy':'package','Reference':'book','AI & machine access':'bot'}
    blurb = {'Get started':'Run the editor, build a first game and learn the scripting model.','Concepts':'Architecture, the entity–component model, the game loop and coordinates.','Editor':'Every panel, menu path, shortcut and authoring workflow.','Scripting':'Lifecycle, globals, input, physics, navigation, saving and debugging.','API reference':'Component fields, script members, option shapes and prerequisites.','Export & deploy':'HTML5, installable PWA and Android APK builds.','Reference':'Tuning rules, scene and project formats, live updates and source map.','AI & machine access':'llms.txt, Markdown twins, JSON catalogs and guidance for assistants.'}
    for gname, gicon, items in NAV:
        first = next(k for _, k in items if k != 'index') if gname != 'Get started' else 'getting-started/installation'
        cards += f'<div class="card"><h3><a href="{url_of(first).replace(V+"/","")}">{escape(gname)}</a></h3><p>{escape(blurb[gname])}</p><p class="muted">{len(items)} pages</p></div>'
    comp_chips = ''.join(f'<a class="api-card" href="api/components/{c.lower()}.html"><strong>{c}</strong><span>{escape(first_line(COMP_SUMMARY[c]))}</span></a>' for c in COMP_NAMES)
    return f'''<div class="callout info"><strong>What is Realot Studio?</strong><div>A browser-based 2D game engine with a visual editor, JavaScript gameplay scripting, PixiJS rendering and Rapier2D physics. The hosted engine is updated by publishing its web files; users do not need a separate engine installer.</div></div>
<h2 id="start-here">Start here</h2>
<div class="cards"><div class="card"><h3><a href="getting-started/installation.html">Open Realot Studio</a></h3><p>Use the hosted editor or serve the static distribution yourself.</p></div><div class="card"><h3><a href="getting-started/first-game.html">Build your first game</a></h3><p>Entities, components and a first script in a few steps.</p></div><div class="card"><h3><a href="getting-started/scripting.html">Scripting quickstart</a></h3><p>onStart, onUpdate, <code>this</code> and the component modules.</p></div><div class="card"><h3><a href="editor/controls.html">Editor controls</a></h3><p>Exact menu paths, panels and keyboard shortcuts.</p></div></div>
<h2 id="browse-by-topic">Browse by topic</h2><div class="cards">{cards}</div>
<h2 id="component-reference">Component reference</h2><p>{n_comp} components, each documented with serialized fields, defaults, script API and editor location.</p><div class="api-list">{comp_chips}</div>
<h2 id="for-automated-systems">For automated systems</h2><p>Every page is complete static HTML with a Markdown twin (same URL, <code>.md</code>). Machine entry points: <a href="../llms.txt">llms.txt</a>, <a href="../llms-full.txt">llms-full.txt</a> (all documentation in one file), <a href="../search-index.json">search-index.json</a>, <a href="../api/index.json">api/index.json</a>, <a href="../sitemap.xml">sitemap.xml</a> and <a href="../robots.txt">robots.txt</a>. See <a href="reference/ai-crawling.html">AI &amp; crawlers</a>.</p>'''
def first_line(s, n=120):
    s = re.sub(r'\s+', ' ', s).strip(); return s if len(s) <= n else s[:n].rsplit(' ', 1)[0] + '…'
render_doc('index', 'Realot Studio documentation', 'Source-aligned documentation for Realot Studio: editor workflows, scripting API, components, physics, navigation and export.', 'Everything you need to build 2D games with Realot Studio, verified against the supplied engine source.', home_body(), url_of('index'))

# ------------------------------------------------------------------ site-level pages
def simple_page(page_path, title, desc, body, section='guides', layout='docs', extra_head=''):
    depth = len(Path(page_path).parts) - 1; root = '../' * depth
    html = (head(root, f'{title} · {SITE}', desc, page_path) + f'''\n<body data-layout="{layout}" data-page=""><a class="skip" href="#main">Skip to content</a><div id="nav-progress"></div>{topbar(root, section)}
<div class="shell"><aside class="sidebar" id="sidebar" aria-label="Documentation navigation">{sidebar(root, '')}</aside><main id="main" class="main"><div class="doc-grid"><article class="doc">{body}{footer(root)}</article></div></main></div><script src="{root}assets/site.js" defer></script></body></html>''')
    write(page_path, html)

# Documentation pages use one stable, unversioned URL tree under /docs/.

# html sitemap
sm = ''
for gname, gicon, items in NAV:
    sm += f'<div><h2>{escape(gname)}</h2><ul>' + ''.join(f'<li><a href="{url_of(k)}">{escape(t)}</a></li>' for t, k in items) + '</ul></div>'
sm += '<div><h2>Components</h2><ul>' + ''.join(f'<li><a href="{V}/api/components/{c.lower()}.html">{c}</a></li>' for c in COMP_NAMES) + '</ul></div>'
simple_page('sitemap.html', 'Site map', 'Every page in the Realot Studio documentation.', f'<div class="eyebrow">Docs</div><h1>Site map</h1><p class="lede">All {len(PAGES)} documentation pages, grouped by section.</p><div class="sitemap-grid">{sm}</div>')
write('404.html', head('', 'Page not found · ' + SITE, 'The page may have moved. Search the current Realot Studio documentation.', '404.html').replace('<meta charset="utf-8">', '<meta charset="utf-8"><script>(function(){var p=location.pathname.split("/");var b=(/github\\.io$/.test(location.hostname)&&p[1])?"/"+p[1]+"/":"/";document.write("<base href=\\\""+b+"\\\">")})()</script>',1) + f'''
<body data-layout="static"><main class="notfound-wrap"><a class="brand notfound-brand" href="index.html"><img class="brand-mark" src="favicon.svg" alt=""><span>Realot Studio</span><small>Docs</small></a><section class="notfound"><div class="notfound-art" aria-hidden="true"><span>4</span><span class="notfound-orbit">✦</span><span>4</span></div><div class="notfound-kicker">PAGE NOT FOUND</div><h1>This page went off the map.</h1><p class="notfound-copy">The link may be old or the page may have moved. Search the current documentation or use one of the shortcuts below.</p><form class="notfound-search" action="search.html" method="get"><input type="search" name="q" placeholder="Search guides, APIs and features…" aria-label="Search documentation"><button type="submit">Search docs</button></form><div class="notfound-actions"><a class="btn primary" href="docs/index.html">Browse documentation</a><a class="btn" href="sitemap.html">View site map</a><a class="btn" href="llms.txt">AI / text index</a></div><p class="notfound-code">ERROR 404 <span>·</span> REALOT STUDIO DOCUMENTATION</p></section></main></body></html>''')

# ------------------------------------------------------------------ landing page
def landing():
    root = ''
    n_api_members = sum(len(m['members']) for m in FACTS['api'].values())
    feats = [('grid','Editor, end to end','Hierarchy, Inspector, viewport tools, prefabs, physics layers and nav areas — with exact menu paths and shortcuts.',f'{V}/editor/overview.html'),
             ('code','JavaScript scripting','Lifecycle hooks, <code>this</code> context, globals, timers, messaging and typed errors.',f'{V}/scripting/lifecycle.html'),
             ('atom','Rapier2D physics','Dynamic, kinematic and static bodies, 16-layer filtering, joints and one-way platforms.',f'{V}/editor/physics.html'),
             ('route','Grid navigation','NavWorld2D bake &amp; paint, 16 areas with costs, NavAgent2D steering and avoidance.',f'{V}/scripting/navigation-complete.html'),
             ('lightning','2D lighting','Six light types, shadow casters and quad or raymarched shadows.',f'{V}/editor/lighting-audio-ui.html'),
             ('zap','Tween & time control','tween() with 33 easings, cancelTween(), and time.scale for slow motion or freeze.',f'{V}/scripting/tween.html'),
             ('package','Ship your game','Export HTML5 or PWA in the browser, or build a debug-signed Android APK through the configured service.',f'{V}/export/android.html')]
    fh = ''.join(f'<a href="{u}"><span class="fi">{svg(i)}</span><h3>{t}</h3><p>{d}</p></a>' for i,t,d,u in feats)
    chips = ''.join(f'<a href="{V}/api/components/{c.lower()}.html">{c}</a>' for c in COMP_NAMES)
    hero_code = '''function onStart() {
  this.speed = 220;
}

function onUpdate(dt) {
  if (input.keyDown("ArrowRight")) {
    this.x += this.speed * dt;
  }
  if (input.keyPressed("Space")) {
    this.rigidbody.addImpulse(0, -350);
  }
}'''
    hc = process('<pre><code>' + escape(hero_code) + '</code></pre>', 'landing')[0]
    html = (head('', f'{SITE} — build 2D games in the browser', 'Source-aligned documentation for Realot Studio, a browser-based 2D game engine: visual editor, JavaScript scripting, Rapier2D physics, navigation, lighting and export.', 'index.html', jsonld={'@context':'https://schema.org','@type':'WebSite','name':SITE,'description':'Documentation for the Realot Studio 2D game engine.', **({'url': ORIGIN + '/'} if ORIGIN else {})}, og_type='website') + f'''\n<body class="landing" data-layout="static" data-page="home"><a class="skip" href="#main">Skip to content</a>
{topbar('', '').replace('<button class="icon-btn menu-toggle" type="button" data-menu-toggle aria-label="Toggle navigation" aria-controls="sidebar">'+svg("menu")+'</button>','')}
<main id="main" class="main">
<section class="hero"><div class="hero-in"><div><span class="pill">Browser-based · live documentation</span><h1>Build 2D games<br>in the <span class="grad">browser</span>.</h1><p class="sub">Realot Studio is a browser-based 2D game engine with a visual editor, JavaScript scripting, Rapier2D physics, navigation, lighting and web export.</p><div class="btn-row"><a class="btn primary" href="{V}/getting-started/first-game.html">Build your first game {svg("arrow")}</a><a class="btn" href="{V}/index.html">Browse the docs</a><button class="btn" type="button" data-search-open>{svg("search")}Search <kbd data-mod>Ctrl K</kbd></button></div></div><div class="hero-code">{hc}</div></div></section>
<section class="section"><h2>Everything the engine does, documented</h2><p class="sub">Pages are written from the shipped source: field names, defaults, script members and menu paths are checked, not guessed.</p><div class="feat">{fh}</div></section>
<section class="section"><h2>A clear path in</h2><p class="sub">New to Realot Studio? Follow these three pages in order.</p><div class="path"><a href="{V}/getting-started/installation.html"><h3>Open the browser editor</h3><p>Open the hosted site. No separate engine installer is required.</p></a><a href="{V}/getting-started/first-game.html"><h3>Make something move</h3><p>Add a sprite, physics and a script, then press Play.</p></a><a href="{V}/export/index.html"><h3>Ship it</h3><p>Export to HTML5 or PWA, or build a debug-signed APK through the configured service.</p></a></div></section>
<section class="section"><h2>Component reference</h2><p class="sub">{len(COMP_NAMES)} components, each with serialized fields, defaults, script API, tuning rules and the exact editor entry point.</p><div class="chips">{chips}</div></section>
<section class="section"><div class="split"><div class="panel"><h3>For developers</h3><p>Precise, prerequisite-aware API pages.</p><ul>{''.join(f'<li>{svg("check")}<span>{t}</span></li>' for t in ['Every component and script member with types and defaults','Option (<code>opts</code>) shapes for raycasts, spawning and navigation','Editor shortcuts and conditional tools, exactly as implemented'])}</ul></div><div class="panel"><h3>For AI assistants &amp; crawlers</h3><p>Static HTML and unversioned URLs, with a complete machine-readable search index.</p><ul>{''.join(f'<li>{svg("check")}<span>{t}</span></li>' for t in ['<a href="llms.txt">llms.txt</a> index and <a href="llms-full.txt">llms-full.txt</a> full text','A Markdown twin of every page (same URL, <code>.md</code>)','JSON catalogs: <a href="api/index.json">API</a>, <a href="search-index.json">search</a>, <a href="sitemap.xml">sitemap</a>'])}</ul></div></div></section>
<div class="cta"><div class="cta-in"><div><h2>Ready to build?</h2><p>Start with the first game guide, or jump straight into scripting.</p></div><div class="btn-row"><a class="btn primary" href="{V}/getting-started/installation.html">Get started {svg("arrow")}</a><a class="btn" href="{V}/scripting/lifecycle.html">Scripting lifecycle</a></div></div></div>
<div class="landing-foot">{footer('')}</div></main><script src="assets/site.js" defer></script></body></html>''')
    write('index.html', html)
landing()

# ------------------------------------------------------------------ static assets
(OUT / 'assets').mkdir(parents=True, exist_ok=True)
shutil.copy2(HERE / 'static/css/site.css', OUT / 'assets/site.css')
shutil.copy2(HERE / 'static/js/site.js', OUT / 'assets/site.js')
shutil.copy2(HERE / 'static/icons/favicon.svg', OUT / 'favicon.svg')
shutil.copy2(HERE / 'static/favicon.ico', OUT / 'favicon.ico')
(OUT / 'icons').mkdir(exist_ok=True)
for _i in ('icon-16.png','icon-32.png','icon-48.png','icon-192.png','icon-512.png','apple-touch-icon.png'):
    shutil.copy2(HERE / 'static/icons' / _i, OUT / 'icons' / _i)

# ------------------------------------------------------------------ machine-readable outputs
featured = {'index','getting-started/installation','getting-started/first-game','getting-started/scripting','scripting/lifecycle','scripting/globals','api/index','editor/controls','scripting/api-cookbook','reference/llm-guide'}
def search_terms(text):
    words = re.findall(r'[a-z0-9_.$+-]{2,}', text.lower())
    stop = {'the','and','for','with','from','that','this','what','when','where','your','you','are','can','how','into','use','using','does','not','all','has','have','will','then','than','their','they','them','its','our','was','were','but','or','as','is','a','an','of','to','in','on','by','be'}
    return list(dict.fromkeys(w for w in words if w not in stop))
search = []
for key, r in RENDERED.items():
    component_file = FACTS['components'][r['title']]['file'].split('/')[-1] if r['title'] in FACTS['components'] else ''
    heading_text = [t for _, t, _ in r['heads']]
    kw = ' '.join([r['title'], r['group'], component_file] + heading_text)
    fulltext = r['text']
    terms = search_terms(' '.join([r['title'], r['desc'], kw, r['code'], fulltext]))
    search.append({'title': r['title'], 'description': r['desc'], 'section': r['group'], 'url': r['url'], 'headings': heading_text, 'keywords': terms, 'content': fulltext,
                   't': r['title'], 'd': first_line(r['desc'], 170), 'k': kw, 's': r['group'], 'u': r['url'], 'h': [[t, i] for _, t, i in r['heads']][:40], 'c': r['code'], 'x': fulltext, **({'f': 1} if key in featured else {})})
search.sort(key=lambda x: x['url'])
write('search-index.json', json.dumps(search, ensure_ascii=False, separators=(',', ':')))

def link_line(r): return f"- [{r['title']}]({r['url']}): {first_line(r['desc'], 160)}"
llms = [
    '# Realot Studio documentation',
    '',
    '> Realot Studio is a browser-based 2D game engine with a visual editor, JavaScript gameplay scripting, PixiJS rendering and Rapier2D physics. The hosted engine and its documentation are published in place; there are no versioned documentation paths.',
    '',
    '## Start here when you only have the documentation URL',
    '',
    'Treat the directory containing this file as the documentation site root. Keep any deployment prefix (for example a GitHub Pages repository path) when resolving these relative paths.',
    '',
    '1. Fetch `llms.txt` at the documentation root. You do not need to know any guide or API page path in advance.',
    '2. Send the user question as a URL-encoded `q` parameter to `api/search?q=...`. This endpoint ranks the full documentation index and returns the closest matching pages with their titles, snippets, relevance scores and relative URLs.',
    '3. Fetch the top result URLs returned by the search endpoint. Use those returned URLs exactly; do not guess page paths. For exact API questions, also retrieve `api/index.json`.',
    '4. For broad questions, fetch `llms-full.txt`. For a manual fallback, fetch `search-index.json` and rank its records by title, description, headings, keywords and full page content.',
    '',
    'The human-facing `search.html` uses the same ranked search endpoint when it is deployed on Cloudflare Pages. The browser search falls back to the local full-text index if the endpoint is unavailable.',
    ''
]
for gname, gicon, items in NAV:
    llms += [f'## {gname}', ''] + [link_line(RENDERED[k]) for _, k in items] + ['']
llms += ['## Components', ''] + [link_line(RENDERED[f'api/components/{c.lower()}']) for c in COMP_NAMES] + ['']
llms += ['## Machine-readable resources', '', '- [Full documentation](llms-full.txt)', '- [Question search endpoint](api/search?q=your%20question)', '- [Full-text search index](search-index.json)', '- [Engine API catalog](api/index.json)',
    '- [Complete script-module reference](docs/api/script-modules.html)', '- [API catalog manifest](api/manifest.json)', '- [AI Bridge tool schemas](api/index.json#aiBridge)', '- [HTML site map](sitemap.html)', '- [XML site map](sitemap.xml)', '']
write('llms.txt', '\n'.join(llms))
full = ['# Realot Studio — complete documentation', '', f'Generated {datetime.date.today().isoformat()} from the supplied Realot Studio engine source. {len(RENDERED)} pages follow; each page is identified by its stable URL.', '']
for key in ['index'] + ORDER:
    r = RENDERED[key]
    full += ['', '---', '', f'<!-- page: {r["url"]} -->', f'# {r["title"]}', '', f'> {r["desc"]}', '', r['md'], '']
write('llms-full.txt', '\n'.join(full))

# API catalog (from source facts + documentation summaries)
lifecycle = ['onClone','onStart','onUpdate','onFixedUpdate','onDestroy','onClick','onCollision','onCollisionEnter','onCollisionStay','onCollisionExit','onTriggerEnter','onTriggerExit','onMessage','onStateEnter','onStateExit','onStateUpdate','onHearSound','onLoseSound']
cat = {'engine': 'Realot Studio', 'generatedFrom': 'project/runtime/components/*.js, project/runtime/scripting/components/*API.js, relay/tools.json and project/editor state', 'runtimeEntry': 'project/runtime/index.js', 'componentTypes': COMP_NAMES, 'lifecycle': lifecycle, 'enums': FACTS['enums'], 'globalApi': GLOBAL_API_SURFACE, 'editorSettings': {'performancePreferences': {'editorFpsFocused': 60, 'editorFpsUnfocused': 24, 'gameFps': {'default': 60, 'allowed': [30, 60, 120, 0], 'zeroMeans': 'unlimited'}, 'backgroundRendering': True, 'vsync': True, 'showComponentNotes': False}, 'projectRegistries': FACTS.get('editorSettings', {}), 'note': 'These are stored implementation defaults and project registries; the supplied editor has no general Settings dialog to edit performance preferences.'}, 'aiBridge': {'defaultRelayUrl': FACTS.get('aiBridge', {}).get('config', {}).get('defaultRelayUrl'), 'sharedRelayActiveMinutesPer24Hours': FACTS.get('aiBridge', {}).get('config', {}).get('aiMinutesPerDay'), 'idleGraceSeconds': FACTS.get('aiBridge', {}).get('config', {}).get('idleGraceSeconds'), 'sharedRelayTools': FACTS.get('aiBridge', {}).get('sharedRelayTools', []), 'localCompanionTools': FACTS.get('aiBridge', {}).get('localBridgeTools', []), 'localCompanionStatus': 'Included source only; the editor-side installer has no call site in the supplied startup path.'}, 'scriptModules': {}, 'components': {}}
for c in COMP_NAMES:
    comp = FACTS['components'][c]; mod = patch.API_MODULE.get(c); api = FACTS['api'].get(mod) if mod else None
    allowed = sorted({m for s in api['member_sets'].values() for m in s}) if api else []
    cat['components'][c] = {'summary': COMP_SUMMARY[c], 'docs': f'{V}/api/components/{c.lower()}.html', 'source': comp['file'], 'sceneFields': [{'name': f['name'], 'default': f['default'], 'type': f['kind'] or 'value'} for f in comp['fields'] if not f['name'].startswith('_')],
        'scriptModule': ('this.' + {'Transform':'transform','SpriteRenderer':'sprite','ShapeRenderer':'shape','TextRenderer':'text','StrokePath':'strokePath','SpeechBubble':'speechBubble','ChatLog':'chat','TextInput':'textInput','Joystick':'joystick','Rigidbody2D':'rigidbody','Collider2D':'collider','Joint2D':'joint','CharacterController':'controller','SpriteAnimation':'animator','Camera':'camera','AudioSource':'audio','AudioListener':'ear','Light':'light','ShadowCaster':'shadowCaster','LightingSettings':'(scene.lighting)','NavAgent2D':'navAgent'}[c]) if mod else None,
        'scriptMembers': [{'name': m, 'kind': ('allow-listed but not implemented' if c == 'Joint2D' and m == 'flexibility' and not (api['members'].get(m, {}).get('get') or api['members'].get(m, {}).get('set') or api['members'].get(m, {}).get('method')) else ('method' if api['members'].get(m, {}).get('method') else ('read-only property' if api['members'].get(m, {}).get('get') and not api['members'].get(m, {}).get('set') else 'write-only property' if api['members'].get(m, {}).get('set') and not api['members'].get(m, {}).get('get') else 'read/write property' if api['members'].get(m, {}).get('get') and api['members'].get(m, {}).get('set') else 'exposed member'))), 'signature': api['members'].get(m, {}).get('signature'), 'doc': ('The JointAPI proxy allow-list contains this name, but no getter or setter is implemented. Reads return undefined and writes do not update Joint2D.flexibility. Set Flexibility (%) in the Inspector instead.' if c == 'Joint2D' and m == 'flexibility' and not (api['members'].get(m, {}).get('get') or api['members'].get(m, {}).get('set') or api['members'].get(m, {}).get('method')) else patch.first_sentence(api['members'].get(m, {}).get('doc', ''), 200))} for m in allowed] if api else []}
for module, api in FACTS['api'].items():
    context, requirement = SCRIPT_MODULE_CONTEXT.get(module, (module, 'See source'))
    allowed = sorted({m for values in api['member_sets'].values() for m in values})
    members = []
    for member in allowed:
        e = api['members'].get(member, {})
        kind = 'method' if e.get('method') else ('read-only property' if e.get('get') and not e.get('set') else 'write-only property' if e.get('set') and not e.get('get') else 'read/write property' if e.get('get') and e.get('set') else 'exposed member')
        doc = patch.first_sentence(e.get('doc',''), 320)
        if module == 'JointAPI' and member == 'flexibility' and not (e.get('get') or e.get('set') or e.get('method')):
            kind = 'allow-listed but not implemented'
            doc = 'The proxy allow-list contains this name, but the current JointAPI target has no getter or setter. Reads return undefined and writes do not update Joint2D.flexibility. Set Flexibility (%) in the Inspector instead.'
        members.append({'name': member, 'signature': e.get('signature'), 'kind': kind, 'doc': doc})
    cat['scriptModules'][module] = {'access': context, 'requirement': requirement, 'source': api['file'], 'members': members}
write('api/index.json', json.dumps(cat, indent=1, ensure_ascii=False))
write('api/manifest.json', json.dumps({'title': 'Realot Studio API catalog', 'engine': 'Realot Studio', 'files': {'catalog': 'api/index.json', 'searchIndex': 'search-index.json', 'llms': 'llms.txt', 'llmsFull': 'llms-full.txt'}, 'componentCount': len(COMP_NAMES), 'componentFieldCount': sum(len([f for f in FACTS['components'][c]['fields'] if not f['name'].startswith('_')]) for c in COMP_NAMES), 'scriptModuleCount': len(FACTS['api']), 'scriptMemberCount': sum(len({m for vals in a['member_sets'].values() for m in vals}) for a in FACTS['api'].values()), 'sharedRelayToolCount': len(FACTS.get('aiBridge', {}).get('sharedRelayTools', [])), 'localCompanionToolCount': len(FACTS.get('aiBridge', {}).get('localBridgeTools', [])), 'pageCount': len(RENDERED)}, indent=1))

# A lightweight human-facing search page. The same full-text index is also directly ingestible by AI agents.
search_page = r'''<!doctype html>
<html lang="en" data-theme="dark" data-root="./">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Search · Realot Studio Documentation</title><meta name="description" content="Search Realot Studio guides, editor controls, scripting APIs, components and export instructions."><meta name="robots" content="index,follow"><link rel="icon" href="favicon.svg" type="image/svg+xml"><link rel="icon" href="favicon.ico" sizes="any"><link rel="apple-touch-icon" href="icons/apple-touch-icon.png"><link rel="search" type="application/opensearchdescription+xml" title="Realot Studio Docs" href="opensearch.xml"><link rel="stylesheet" href="assets/site.css"><style>
.search-main{max-width:1000px;margin:0 auto;padding:54px 24px 90px}.search-hero{margin:14px 0 28px}.search-hero h1{font-size:clamp(32px,5vw,48px);letter-spacing:-.04em;margin:0 0 10px}.search-hero p{color:var(--text-3);max-width:680px;line-height:1.65}.search-form{display:flex;gap:10px;margin:24px 0 12px}.search-form input{flex:1;min-width:0;background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:15px 16px;color:var(--text);font:inherit}.search-form button{border:0;border-radius:12px;padding:0 22px;background:var(--accent);color:white;font-weight:700;cursor:pointer}.search-meta{font-size:13px;color:var(--text-3);margin:16px 0}.search-results{display:grid;gap:12px}.search-result{border:1px solid var(--border);border-radius:14px;padding:17px 18px;background:var(--surface)}.search-result h2{font-size:18px;margin:0 0 7px}.search-result h2 a{color:var(--text);text-decoration:none}.search-result h2 a:hover{color:var(--accent)}.search-result p{margin:6px 0;color:var(--text-3);line-height:1.55}.result-section{font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--accent)}.result-match{font-size:12px;color:var(--text-3)}.search-empty{padding:26px;border:1px dashed var(--border);border-radius:14px;color:var(--text-3)}.search-links{display:flex;flex-wrap:wrap;gap:10px;margin-top:22px}.search-links a{color:var(--accent)}@media(max-width:560px){.search-main{padding:32px 16px}.search-form{flex-direction:column}.search-form button{padding:14px}}
</style></head>
<body data-layout="static"><header class="topbar"><div class="topbar-inner"><a class="brand" href="index.html"><img class="brand-mark" src="favicon.svg" alt=""><span>Realot Studio</span><small>Docs</small></a><div class="top-spacer"></div><a class="search-btn" href="docs/index.html">Browse documentation</a></div></header>
<main class="search-main"><section class="search-hero"><div class="eyebrow">REALOT STUDIO DOCUMENTATION</div><h1>Find the answer.</h1><p>Search guides, editor controls, scripting APIs, components, project files and export workflows. You can describe what you are trying to do rather than knowing the exact page name.</p></section>
<form class="search-form" id="doc-search-form" action="search.html" method="get"><input id="doc-search-input" type="search" name="q" placeholder="Try “make an NPC follow the player” or “export Android APK”…" autocomplete="off"><button type="submit">Search</button></form>
<div class="search-meta" id="search-meta" aria-live="polite">Search by topic, feature, API name or the problem you are trying to solve. AI tools can use <code>/api/search?q=your-question</code> to retrieve the closest matching pages.</div><section class="search-results" id="search-results" aria-live="polite"></section>
<div class="search-links"><a href="llms.txt">AI retrieval guide</a><a href="search-index.json">Full search index (JSON)</a><a href="llms-full.txt">Full documentation text</a><a href="api/index.json">API catalog</a></div></main>
<script src="assets/search-page.js" defer></script></body></html>'''
write('search.html', search_page)
search_js = r'''(function(){
  const input=document.getElementById('doc-search-input'),form=document.getElementById('doc-search-form'),meta=document.getElementById('search-meta'),results=document.getElementById('search-results');
  if(!input||!form||!meta||!results)return;
  const aliases={
    apk:['android','application package','build service','mobile app'],android:['apk','mobile export','build service'],
    project:['realot','save file','load file','archive'],realot:['project','project file','.realot'],
    autosave:['save now','backup','persist','save project'],
    online:['browser','web','hosted','website'],update:['publish','reload','cache','refresh'],
    install:['pwa','progressive web app','add to home screen'],
    movement:['physics','rigidbody','character controller','velocity'],
    follow:['navigation','nav agent','pathfinding','steering'],
    collision:['collider','rigidbody','physics','trigger'],
    enemy:['npc','non-player character','ai','navigation'],
    icon:['favicon','launcher icon'],
    script:['javascript','gameplay code','api','lifecycle']
  };
  const tokenize=s=>(String(s||'').toLowerCase().match(/[a-z0-9_.$+-]{2,}/g)||[]).filter(w=>!['the','and','for','with','from','that','this','what','when','where','your','you','are','can','how','into','use','using','does','not','all','has','have','will','then','than','their','they','them','its','our','was','were','but','or','as','is','a','an','of','to','in','on','by','be'].includes(w));
  function expand(tokens){const out=new Set(tokens);tokens.forEach(t=>(aliases[t]||[]).forEach(a=>tokenize(a).forEach(x=>out.add(x))));return [...out]}
  function editSimilarity(a,b){if(a===b)return 1;if(!a||!b)return 0;if(Math.abs(a.length-b.length)>3)return 0;let prev=Array.from({length:b.length+1},(_,i)=>i);for(let i=1;i<=a.length;i++){let cur=[i];for(let j=1;j<=b.length;j++)cur[j]=Math.min(cur[j-1]+1,prev[j]+1,prev[j-1]+(a[i-1]===b[j-1]?0:1));prev=cur;}return 1-prev[b.length]/Math.max(a.length,b.length)}
  function score(doc,terms,phrase){const title=String(doc.title||doc.t||'').toLowerCase(),desc=String(doc.description||doc.d||'').toLowerCase(),section=String(doc.section||doc.s||'').toLowerCase(),keywords=(doc.keywords||[]).join(' ').toLowerCase(),heads=(doc.headings||[]).join(' ').toLowerCase(),content=String(doc.content||doc.x||'').toLowerCase();let s=0,matched=0;
    if(phrase&&title.includes(phrase))s+=18;if(phrase&&desc.includes(phrase))s+=8;
    terms.forEach(term=>{let weight=0;if(title.split(/[^a-z0-9_.$+-]+/).includes(term))weight=9;else if(title.includes(term))weight=6;else if(keywords.includes(term))weight=5;else if(heads.includes(term))weight=4;else if(desc.includes(term))weight=3;else if(section.includes(term))weight=2;else if(content.includes(term))weight=1;else {const near=(doc.keywords||[]).reduce((m,w)=>Math.max(m,editSimilarity(term,w)),0);if(near>.82)weight=1.5;}if(weight){s+=weight;matched++;}});
    const coverage=terms.length?matched/terms.length:0;s+=coverage*4;if(doc.f)s+=1.5;return s;
  }
  function esc(s){return String(s||'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
  function render(items,terms){if(!items.length){results.innerHTML='<div class="search-empty">No close matches yet. Try a broader phrase, a component name, or a related term. You can also browse the <a href="docs/index.html">documentation index</a>.</div>';return;}
    results.innerHTML=items.map(({doc,rank})=>{const title=doc.title||doc.t,description=doc.description||doc.d,url=doc.url||doc.u,content=doc.content||doc.x||'';let snippet=description||content.slice(0,220);let pos=-1;for(const t of terms){const i=content.toLowerCase().indexOf(t);if(i>=0&&(pos<0||i<pos))pos=i;}if(pos>=0)snippet='…'+content.slice(Math.max(0,pos-95),Math.min(content.length,pos+210))+'…';return '<article class="search-result"><div class="result-section">'+esc(doc.section||doc.s||'Documentation')+'</div><h2><a href="'+esc(url)+'">'+esc(title)+'</a></h2><p>'+esc(snippet)+'</p><div class="result-match">Related match · '+Math.round(rank)+' relevance points</div></article>';}).join('');}
  let records=[];fetch('search-index.json').then(r=>{if(!r.ok)throw Error('index unavailable');return r.json()}).then(j=>{records=j;run();}).catch(()=>{meta.textContent='The search index could not be loaded. Open the documentation index or the AI retrieval guide instead.';});
  let requestNumber=0;
  function run(){
    const q=input.value.trim(),raw=tokenize(q),terms=expand(raw),phrase=q.toLowerCase();
    if(!q){meta.textContent=records.length+' pages are ready to search. Enter a topic, API name or description of the task.';results.innerHTML='';return;}
    const current=++requestNumber;
    const endpoint=new URL('api/search',new URL(document.documentElement.dataset.root||'./',location.href));
    endpoint.searchParams.set('q',q); endpoint.searchParams.set('limit','12');
    fetch(endpoint.toString(),{headers:{Accept:'application/json'}}).then(r=>{if(!r.ok)throw Error('search endpoint unavailable');return r.json();}).then(data=>{
      if(current!==requestNumber)return;
      const ranked=(data.results||[]).map(item=>({doc:{title:item.title,description:item.description,section:item.section,url:item.url,content:item.snippet},rank:item.score||0}));
      meta.textContent=ranked.length+' closest matches for “'+q+'”';render(ranked,terms);
    }).catch(()=>{
      if(current!==requestNumber)return;
      const ranked=records.map(doc=>({doc,rank:score(doc,terms,phrase)})).filter(x=>x.rank>0).sort((a,b)=>b.rank-a.rank).slice(0,20);
      meta.textContent=ranked.length+' relevant results for “'+q+'” (local index)';render(ranked,terms);
    });
  }
  const q=new URLSearchParams(location.search).get('q')||'';input.value=q;form.addEventListener('submit',e=>{e.preventDefault();history.replaceState(null,'','search.html'+(input.value.trim()?'?q='+encodeURIComponent(input.value.trim()):''));run();});input.addEventListener('input',()=>{if(input.value.trim().length>=2)run();});if(q)setTimeout(run,0);
})();'''
write('assets/search-page.js', search_js)
write('opensearch.xml', '''<?xml version="1.0" encoding="UTF-8"?>\n<OpenSearchDescription xmlns="http://a9.com/-/spec/opensearch/1.1/">\n  <ShortName>Realot Studio Docs</ShortName>\n  <Description>Search Realot Studio documentation</Description>\n  <Url type="text/html" template="search.html?q={searchTerms}"/>\n  <InputEncoding>UTF-8</InputEncoding>\n</OpenSearchDescription>\n''')

# sitemap + robots
urls = sorted({r['url'] for r in RENDERED.values()} | {'index.html', 'search.html', 'sitemap.html', 'llms.txt', 'llms-full.txt', 'search-index.json', 'api/index.json'})
if ORIGIN:
    xml = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'] + [f'  <url><loc>{escape(ORIGIN + "/" + u)}</loc></url>' for u in urls] + ['</urlset>']
    write('sitemap.xml', '\n'.join(xml) + '\n')
else:
    write('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n<!-- Sitemaps require absolute URLs. Rebuild with: python3 build.py --origin https://your-domain.example -->\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"></urlset>\n')
write('robots.txt', 'User-agent: *\nAllow: /\n\n# AI search and training crawlers are intentionally allowed.\nUser-agent: OAI-SearchBot\nAllow: /\nUser-agent: GPTBot\nAllow: /\nUser-agent: ClaudeBot\nAllow: /\nUser-agent: PerplexityBot\nAllow: /\nUser-agent: Google-Extended\nAllow: /\n' + (f'\nSitemap: {ORIGIN}/sitemap.xml\n' if ORIGIN else '\n# Add "Sitemap: https://your-domain/sitemap.xml" after rebuilding with --origin.\n'))
write('.nojekyll', '')

Path(HERE / 'build.log').write_text('\n'.join(log) + '\n')
(OUT / '.nojekyll').write_text('')
print(f'built {len(RENDERED)} pages -> {OUT}; {len(log)} source-driven corrections')
