"""Post-process legacy/authored page fragments into the new design's markup.
Everything here is deterministic and produces plain static HTML (no client rendering)."""
import json, re
from bs4 import BeautifulSoup, NavigableString, Tag
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import JavascriptLexer, JsonLexer, BashLexer, TextLexer, HtmlLexer, CssLexer
from .icons import svg

_FMT = HtmlFormatter(nowrap=True, classprefix='t-')

def slugify(s):
    s = re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')
    return s or 'section'

def guess_lang(text, classes):
    for c in classes or []:
        if c.startswith('language-'):
            return c[9:]
    t = text.strip()
    if re.match(r'^(python3?|pip|npm|npx|node|curl|git|cd|\$)\s', t): return 'bash'
    if re.match(r'^(POST|GET|PUT)\s+/', t): return 'http'
    if t[:1] in '{[' and re.search(r'"\s*:', t): return 'json'
    if t.startswith('<') and t.endswith('>'): return 'html'
    if re.search(r'^[\w./-]+/\s*$', t.split('\n')[0]) and not re.search(r'[;{}()=]', t) : return 'text'
    if not re.search(r'[;{}()=]', t) and '\n' in t and re.search(r'^\s*[\w./-]+\s*(#|—|-).*$', t, re.M): return 'text'
    return 'javascript'

LEXERS = {'javascript': JavascriptLexer, 'js': JavascriptLexer, 'json': JsonLexer, 'bash': BashLexer, 'sh': BashLexer,
          'html': HtmlLexer, 'css': CssLexer, 'text': TextLexer, 'http': TextLexer, 'txt': TextLexer}

def code_block(text, lang, soup):
    text = text.rstrip('\n')
    lex = LEXERS.get(lang, TextLexer)()
    inner = highlight(text, lex, _FMT).rstrip('\n')
    label = {'javascript': 'js', 'bash': 'shell', 'text': 'text'}.get(lang, lang)
    html = (f'<div class="codeblock" data-lang="{lang}"><header><span>{label}</span>'
            f'<button class="copy" type="button" aria-label="Copy code">{svg("copy")}Copy</button></header>'
            f'<pre tabindex="0"><code class="language-{lang}">{inner}</code></pre></div>')
    return BeautifulSoup(html, 'html.parser')

CALLOUT_ICON = {'info': 'info', 'warn': 'alert', 'warning': 'alert', 'success': 'checkc', 'danger': 'octx'}

def _callout(div, soup):
    kinds = [c for c in div.get('class', []) if c in CALLOUT_ICON]
    kind = kinds[0] if kinds else 'info'
    if kind == 'warning': kind = 'warn'
    children = [c for c in div.children if not (isinstance(c, NavigableString) and not c.strip())]
    title = None
    if children and isinstance(children[0], Tag) and children[0].name == 'strong':
        title = children[0].get_text(' ', strip=True); children = children[1:]
    if len(children) == 1 and isinstance(children[0], Tag) and children[0].name == 'div':
        children = list(children[0].children)
    new = soup.new_tag('div'); new['class'] = ['callout', kind]; new['role'] = 'note'
    new.append(BeautifulSoup(svg(CALLOUT_ICON[kind]), 'html.parser'))
    body = soup.new_tag('div'); body['class'] = ['cbody']
    if title:
        t = soup.new_tag('span'); t['class'] = ['ctitle']; t.string = title; body.append(t)
    # loose inline content should read as a paragraph
    inline_only = all(isinstance(c, NavigableString) or c.name in ('code', 'a', 'strong', 'em', 'b', 'span', 'br', 'kbd') for c in children)
    if inline_only and children:
        p = soup.new_tag('span')
        for c in children: p.append(c.extract() if hasattr(c, 'extract') else c)
        body.append(p)
    else:
        for c in children: body.append(c.extract() if hasattr(c, 'extract') else c)
    new.append(body)
    div.replace_with(new)

def _type_chip(text, soup):
    t = text.strip(); low = t.lower()
    cls = 'ty'
    if 'enum' in low or '|' in low and not low.startswith(('array', 'object')): cls += ' ty-enum'
    elif low.startswith(('number', 'integer', 'float')): cls += ' ty-num'
    elif low.startswith('boolean'): cls += ' ty-bool'
    elif low.startswith(('string', 'hex')): cls += ' ty-str'
    elif low.startswith(('array', 'object', 'sparse', '{')): cls += ' ty-obj'
    s = soup.new_tag('span'); s['class'] = cls.split(); s.string = t
    return s

def process(html, page_path, root_prefix=''):
    """Returns (processed_html, headings[list of (level, text, id)])."""
    soup = BeautifulSoup(html, 'html.parser')
    # strip inline styles from legacy content (design system owns layout)
    for el in soup.find_all(style=True): del el['style']
    # callouts (innermost first)
    for div in list(soup.select('div.callout, section.callout, aside.callout, p.callout')): _callout(div, soup)
    # tables
    for tb in soup.find_all('table'):
        if not (tb.parent and 'table-wrap' in (tb.parent.get('class') or [])):
            w = soup.new_tag('div'); w['class'] = ['table-wrap']; tb.wrap(w)
        # accessible scroll region
        tb.parent['tabindex'] = '0'; tb.parent['role'] = 'region'
    # re-do type chips properly (need original text)
    for tb in soup.find_all('table'):
        ths = [th.get_text(strip=True).lower() for th in tb.find_all('th')]
        if 'type' in ths:
            ix = ths.index('type')
            for tr in tb.find_all('tr'):
                tds = tr.find_all('td')
                if len(tds) > ix:
                    txt = tds[ix].get_text(strip=True)
                    if txt and not tds[ix].find('span', class_='ty'):
                        tds[ix].clear(); tds[ix].append(_type_chip(txt, soup))
    # code blocks
    for pre in list(soup.find_all('pre')):
        if pre.find_parent(class_='codeblock'): continue
        code = pre.find('code')
        text = (code or pre).get_text()
        lang = guess_lang(text, (code.get('class') if code else None))
        pre.replace_with(code_block(text, lang, soup))
    # headings: unique ids + anchors
    used = set(); heads = []
    for h in soup.find_all(['h2', 'h3', 'h4']):
        if h.find_parent(class_=['callout', 'codeblock']): continue
        text = h.get_text(' ', strip=True)
        base = h.get('id') or slugify(text); i = base; n = 2
        while i in used: i = f'{base}-{n}'; n += 1
        used.add(i); h['id'] = i
        a = soup.new_tag('a'); a['class'] = ['anchor']; a['href'] = '#' + i; a['aria-label'] = 'Link to this section'; a.string = '#'
        h.insert(0, a)
        if h.name in ('h2', 'h3'): heads.append((int(h.name[1]), text, i))
    # external links: safe rel
    for a in soup.find_all('a', href=True):
        if re.match(r'^https?://', a['href']): a['rel'] = 'noopener'
    out = str(soup)
    out = re.sub(r'<span class="t-w">(.*?)</span>', r'\1', out, flags=re.S)
    out = out.replace('viewbox=', 'viewBox=')
    return out, heads
