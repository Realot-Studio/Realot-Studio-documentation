/* Realot Studio Docs — progressive enhancement. The site is fully usable (and fully crawlable) without this
   file: every page is complete static HTML. This adds client-side navigation, search, theme, copy. */
(function () {
  'use strict';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var root = document.documentElement;
  var ICON_CHECK = '<svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>';
  var ICON_COPY = '<svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>';

  /* ---------- theme ---------- */
  function setTheme(t) {
    root.setAttribute('data-theme', t);
    try { localStorage.setItem('realot-docs-theme', t); } catch (e) {}
  }
  document.addEventListener('click', function (e) {
    var b = e.target.closest('[data-theme-toggle]');
    if (b) { setTheme(root.getAttribute('data-theme') === 'light' ? 'dark' : 'light'); }
  });

  /* ---------- helpers ---------- */
  function siteRoot() { return new URL(root.getAttribute('data-root') || './', location.href); }
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function flash(btn, html, ms) { var old = btn.innerHTML; btn.innerHTML = html; btn.classList.add('done'); setTimeout(function () { btn.innerHTML = old; btn.classList.remove('done'); }, ms || 1400); }

  /* ---------- copy buttons (delegated: survives client navigation) ---------- */
  document.addEventListener('click', function (e) {
    var b = e.target.closest('.copy');
    if (b) {
      var pre = b.closest('.codeblock').querySelector('pre');
      var text = pre.innerText.replace(/\n$/, '');
      (navigator.clipboard ? navigator.clipboard.writeText(text) : Promise.reject()).then(function () { flash(b, ICON_CHECK + 'Copied'); }, function () { flash(b, 'Press Ctrl+C'); });
      return;
    }
    var m = e.target.closest('[data-copy-md]');
    if (m) {
      e.preventDefault();
      var link = $('link[rel=alternate][type="text/markdown"]');
      if (!link) return;
      fetch(link.href).then(function (r) { return r.text(); }).then(function (t) { return navigator.clipboard.writeText(t); })
        .then(function () { flash(m, ICON_CHECK + 'Copied Markdown'); }, function () { location.href = link.href; });
    }
  });

  /* ---------- sidebar drawer ---------- */
  document.addEventListener('click', function (e) {
    if (e.target.closest('[data-menu-toggle]')) { document.body.classList.toggle('drawer'); return; }
    if (document.body.classList.contains('drawer') && !e.target.closest('#sidebar')) document.body.classList.remove('drawer');
  });

  /* ---------- TOC scrollspy + heading anchors ---------- */
  var spy = null;
  function initSpy() {
    if (spy) spy.disconnect();
    var links = $$('.toc a');
    if (!links.length || !('IntersectionObserver' in window)) return;
    var map = {}; links.forEach(function (a) { map[a.getAttribute('href').slice(1)] = a; });
    var heads = $$('.doc h2[id], .doc h3[id]');
    spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { links.forEach(function (l) { l.classList.remove('on'); }); var a = map[en.target.id]; if (a) { a.classList.add('on'); a.scrollIntoView({ block: 'nearest' }); } }
      });
    }, { rootMargin: '-72px 0px -72% 0px', threshold: 0 });
    heads.forEach(function (h) { spy.observe(h); });
  }

  /* ---------- sidebar state ---------- */
  function syncSidebar(cur) {
    var sb = $('#sidebar'); if (!sb) return;
    var here = cur || location.pathname;
    var active = null;
    $$('a', sb).forEach(function (a) {
      var is = new URL(a.getAttribute('href'), location.href).pathname === here;
      if (is) { a.setAttribute('aria-current', 'page'); active = a; } else a.removeAttribute('aria-current');
    });
    if (active) { var g = active.closest('details'); if (g) g.open = true; active.scrollIntoView({ block: 'center' }); }
  }

  /* ---------- client-side navigation ---------- */
  var cache = new Map(), inflight = null;
  function fetchPage(url) {
    if (cache.has(url)) return Promise.resolve(cache.get(url));
    return fetch(url, { credentials: 'same-origin' }).then(function (r) {
      if (!r.ok || !/text\/html/.test(r.headers.get('content-type') || '')) throw new Error('bad response');
      return r.text();
    }).then(function (t) { cache.set(url, t); return t; });
  }
  function progress(p) { var b = $('#nav-progress'); if (!b) return; b.style.opacity = p === 1 ? 0 : 1; b.style.width = (p * 100) + '%'; if (p === 1) setTimeout(function () { b.style.width = '0'; }, 250); }
  function eligible(a, e) {
    if (!a || a.target || a.hasAttribute('download') || e.defaultPrevented || e.button || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return false;
    var u = new URL(a.href, location.href);
    if (u.origin !== location.origin || location.protocol === 'file:') return false;
    if (!/\.html$|\/$/.test(u.pathname)) return false;
    if (document.body.getAttribute('data-layout') !== 'docs') return false;
    return true;
  }
  function swap(html, url, push) {
    var doc = new DOMParser().parseFromString(html, 'text/html');
    if (doc.body.getAttribute('data-layout') !== 'docs' || !$('#main', doc)) { location.href = url; return; }
    document.title = doc.title;
    ['meta[name=description]', 'link[rel=canonical]', 'link[rel=alternate][type="text/markdown"]'].forEach(function (sel) {
      var n = $(sel), o = $(sel, doc);
      if (n && o) { n.replaceWith(o); } else if (o) document.head.appendChild(o); else if (n) n.remove();
    });
    root.setAttribute('data-root', doc.documentElement.getAttribute('data-root'));
    document.body.setAttribute('data-page', doc.body.getAttribute('data-page') || '');
    $('#main').innerHTML = $('#main', doc).innerHTML;
    // relative hrefs in chrome depend on the page's depth, so re-render them from the fetched page
    var tb = $('.topbar-inner'), tb2 = $('.topbar-inner', doc); if (tb && tb2) tb.innerHTML = tb2.innerHTML;
    var sb = $('#sidebar'), sb2 = $('#sidebar', doc); if (sb && sb2) { var st = sb.scrollTop; sb.innerHTML = sb2.innerHTML; sb.scrollTop = st; }
    $$('[data-mod]').forEach(function (k) { k.textContent = /Mac|iPhone|iPad/.test(navigator.platform || '') ? '⌘K' : 'Ctrl K'; });
    if (push) history.pushState({ v: 1 }, '', url);
    var u = new URL(url, location.href);
    syncSidebar(u.pathname);
    document.body.classList.remove('drawer');
    if (u.hash && $(decodeURIComponent(u.hash))) $(decodeURIComponent(u.hash)).scrollIntoView(); else window.scrollTo(0, 0);
    var h1 = $('#main h1'); if (h1) { h1.setAttribute('tabindex', '-1'); h1.focus({ preventScroll: true }); }
    initSpy();
  }
  function go(url, push) {
    var token = inflight = {}; progress(.3);
    fetchPage(url.split('#')[0]).then(function (html) {
      if (inflight !== token) return; progress(.9); swap(html, url, push); progress(1);
    }).catch(function () { location.href = url; });
  }
  document.addEventListener('click', function (e) {
    var a = e.target.closest('a[href]');
    if (!eligible(a, e)) return;
    var u = new URL(a.href, location.href);
    if (u.pathname === location.pathname && u.hash) return; // in-page anchor: native behaviour
    e.preventDefault(); go(a.href, true);
  });
  window.addEventListener('popstate', function () { if (document.body.getAttribute('data-layout') === 'docs') go(location.href, false); });
  function prefetch(e) { var a = e.target.closest && e.target.closest('a[href]'); if (a && eligible(a, { button: 0 })) fetchPage(new URL(a.href, location.href).href.split('#')[0]).catch(function () {}); }
  document.addEventListener('mouseover', prefetch, { passive: true });
  document.addEventListener('focusin', prefetch);
  document.addEventListener('touchstart', prefetch, { passive: true });

  /* ---------- search palette ---------- */
  var index = null, pal = null, sel = 0, shown = [];
  function loadIndex() {
    if (index) return Promise.resolve(index);
    return fetch(new URL('search-index.json', siteRoot())).then(function (r) { return r.json(); }).then(function (j) { index = j; return j; }).catch(function () { index = []; return index; });
  }
  function terms(q) { return q.toLowerCase().split(/[^a-z0-9_.$]+/).filter(Boolean); }
  function score(doc, ws) {
    var t = doc.t.toLowerCase(), d = (doc.d || '').toLowerCase(), k = (doc.k || '').toLowerCase(), x = (doc.x || '').toLowerCase(), c = ' ' + (doc.c || '').toLowerCase() + ' ';
    var total = 0, best = null;
    for (var i = 0; i < ws.length; i++) {
      var w = ws[i], s = 0;
      if (t === w) s += 30; else if (t.indexOf(w) === 0) s += 18; else if (t.indexOf(w) > -1) s += 12;
      if (k.indexOf(w) > -1) s += 7;
      if (d.indexOf(w) > -1) s += 4;
      for (var j = 0; j < (doc.h || []).length; j++) { if (doc.h[j][0].toLowerCase().indexOf(w) > -1) { s += 6; if (!best) best = doc.h[j]; break; } }
      if (c.indexOf(' ' + w + ' ') > -1) s += 14; else if (c.indexOf(w) > -1) s += 5;
      if (x.indexOf(w) > -1) s += 1.5;
      if (!s) return { s: 0 };
      total += s;
    }
    return { s: total + (doc.f ? 1 : 0), h: best };
  }
  function hl(text, ws) {
    var out = esc(text);
    ws.forEach(function (w) { if (w.length > 1) out = out.replace(new RegExp('(' + w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'ig'), '<mark>$1</mark>'); });
    return out;
  }
  function render(q) {
    var list = $('.pal-list', pal), ws = terms(q), items;
    if (!ws.length) {
      items = (index || []).filter(function (d) { return d.f; }).map(function (d) { return { d: d, g: 'Suggested' }; });
    } else {
      items = (index || []).map(function (d) { var r = score(d, ws); return r.s ? { d: d, s: r.s, h: r.h, g: d.s } : null; }).filter(Boolean).sort(function (a, b) { return b.s - a.s; }).slice(0, 40);
    }
    shown = items; sel = 0;
    if (!items.length) { list.innerHTML = '<div class="pal-empty">No results for “' + esc(q) + '”. Try a component name such as <b>Rigidbody2D</b> or an API like <b>findFirst</b>.</div>'; return; }
    var html = '', last = null;
    items.forEach(function (it, i) {
      if (it.g !== last) { html += '<div class="pal-group">' + esc(it.g) + '</div>'; last = it.g; }
      var href = new URL(it.d.u, siteRoot()).href + (it.h ? '#' + it.h[1] : '');
      var title = it.h ? it.d.t + ' › ' + it.h[0] : it.d.t;
      html += '<a class="pal-item" role="option" id="pal-' + i + '" data-i="' + i + '" href="' + esc(href) + '" aria-selected="' + (i === 0) + '"><b><span>' + hl(title, ws) + '</span><i>' + esc(it.d.s) + '</i></b><p>' + hl(it.d.d || '', ws) + '</p></a>';
    });
    list.innerHTML = html;
  }
  function mark(i) {
    if (!shown.length) return;
    sel = (i + shown.length) % shown.length;
    $$('.pal-item', pal).forEach(function (n) { n.setAttribute('aria-selected', String(+n.getAttribute('data-i') === sel)); });
    var n = $('#pal-' + sel, pal); if (n) n.scrollIntoView({ block: 'nearest' });
  }
  function ensurePalette() {
    if (pal) return pal;
    pal = document.createElement('div'); pal.className = 'palette'; pal.setAttribute('role', 'dialog'); pal.setAttribute('aria-modal', 'true'); pal.setAttribute('aria-label', 'Search documentation');
    pal.innerHTML = '<div class="pal-box"><div class="pal-head"><svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg><input type="search" autocomplete="off" spellcheck="false" placeholder="Search components, APIs and guides…" aria-label="Search" role="combobox" aria-expanded="true" aria-controls="pal-list"><kbd>Esc</kbd></div><div class="pal-list" id="pal-list" role="listbox"></div><div class="pal-foot"><span><kbd>↑</kbd><kbd>↓</kbd> navigate</span><span><kbd>↵</kbd> open</span><span><kbd>Esc</kbd> close</span></div></div>';
    document.body.appendChild(pal);
    var input = $('input', pal);
    input.addEventListener('input', function () { render(input.value); });
    pal.addEventListener('mousedown', function (e) { if (e.target === pal) closePal(); });
    pal.addEventListener('mousemove', function (e) { var n = e.target.closest('.pal-item'); if (n && +n.getAttribute('data-i') !== sel) mark(+n.getAttribute('data-i')); });
    pal.addEventListener('click', function (e) { var n = e.target.closest('.pal-item'); if (n) { closePal(); if (eligible(n, e)) { e.preventDefault(); go(n.href, true); } } });
    input.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowDown') { e.preventDefault(); mark(sel + 1); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); mark(sel - 1); }
      else if (e.key === 'Enter') { var n = $('#pal-' + sel, pal); if (n) { e.preventDefault(); n.click(); } }
    });
    return pal;
  }
  function openPal() { ensurePalette(); pal.classList.add('open'); var i = $('input', pal); i.value = ''; i.focus(); loadIndex().then(function () { render(i.value); }); }
  function closePal() { if (pal) pal.classList.remove('open'); }
  document.addEventListener('click', function (e) { if (e.target.closest('[data-search-open]')) openPal(); });
  document.addEventListener('keydown', function (e) {
    var typing = /^(input|textarea|select)$/i.test((e.target.tagName || '')) || e.target.isContentEditable;
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') { e.preventDefault(); openPal(); }
    else if (e.key === '/' && !typing) { e.preventDefault(); openPal(); }
    else if (e.key === 'Escape') { closePal(); document.body.classList.remove('drawer'); }
  });

  /* ---------- boot ---------- */
  syncSidebar(); initSpy();
  var isMac = /Mac|iPhone|iPad/.test(navigator.platform || '');
  $$('[data-mod]').forEach(function (k) { k.textContent = isMac ? '⌘K' : 'Ctrl K'; });
})();
