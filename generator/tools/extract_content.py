#!/usr/bin/env python3
"""One-time migration: pull each page's article body out of the legacy HTML site into
content/<path>.html fragments with a JSON front-matter header. After this, the fragments are the
editable source of truth and build.py renders them into the new design."""
import json, re, sys
from pathlib import Path
from bs4 import BeautifulSoup
old = Path(sys.argv[1]); out = Path(sys.argv[2])
base = old / 'docs' if (old / 'docs').is_dir() else old
n = 0
for f in sorted(base.rglob('*.html')):
    rel = f.relative_to(base).as_posix()
    s = BeautifulSoup(f.read_text(), 'lxml')
    art = s.select_one('article.doc-content')
    if not art: continue
    title = art.h1.get_text(strip=True)
    desc = (s.find('meta', attrs={'name': 'description'}) or {}).get('content', '')
    lede = art.select_one('p.lede'); lede_t = lede.get_text(' ', strip=True) if lede else desc
    for x in (art.select_one('.eyebrow'), art.h1, lede):
        if x: x.decompose()
    body = art.decode_contents().strip()
    # strip legacy inline behaviour
    body = body.replace(' style="padding-top:20px"', '')
    meta = {'title': title, 'description': desc or lede_t, 'lede': lede_t}
    dest = out / (rel[:-5] + '.html')
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text('<!--meta ' + json.dumps(meta, ensure_ascii=False) + ' -->\n' + body + '\n', encoding='utf-8')
    n += 1
print('extracted', n, 'pages')
