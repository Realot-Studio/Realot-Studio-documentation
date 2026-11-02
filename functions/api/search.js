const STOP = new Set("the and for with from that this what when where your you are can how into does not all has have will then than their they them its our was were but or as is a an of to in on by be please help make create build use using want need show me my it i a the".split(" "));
const ALIASES = {
  enemy: ["npc", "non player character", "navigation", "follow"],
  follow: ["navigation", "nav agent", "pathfinding", "steering", "chase"],
  chase: ["follow", "navigation", "nav agent", "pathfinding"],
  movement: ["character controller", "rigidbody", "velocity", "physics"],
  collision: ["collider", "rigidbody", "physics", "trigger"],
  save: ["project file", "realot", "autosave", "backup", "load"],
  open: ["load", "project", "realot", "file handler"],
  android: ["apk", "mobile", "export", "build"],
  apk: ["android", "export", "build service"],
  mobile: ["android", "apk", "touch", "joystick"],
  camera: ["viewport", "follow", "zoom", "projection"],
  light: ["lighting", "shadow", "illumination"],
  sound: ["audio", "listener", "source"],
  ui: ["user interface", "button", "text input", "chat log"],
  lag: ["performance", "fps", "frame rate", "optimization"],
  slow: ["performance", "fps", "time scale", "delta time"],
  platformer: ["character controller", "jump", "grounded", "slope"],
  tile: ["tilemap", "tileset", "autotile"],
  script: ["javascript", "lifecycle", "api", "callback"]
};
const tokenize = (s) => (String(s || "").toLowerCase().match(/[a-z0-9_.$+-]{2,}/g) || []).filter(w => !STOP.has(w));
function editSimilarity(a, b) {
  if (a === b) return 1;
  if (!a || !b || Math.abs(a.length - b.length) > 2) return 0;
  let prev = Array.from({ length: b.length + 1 }, (_, i) => i);
  for (let i = 1; i <= a.length; i++) {
    const cur = [i];
    for (let j = 1; j <= b.length; j++) cur[j] = Math.min(cur[j - 1] + 1, prev[j] + 1, prev[j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1));
    prev = cur;
  }
  return 1 - prev[b.length] / Math.max(a.length, b.length);
}
function expand(words) {
  const out = new Set(words);
  for (const word of words) for (const alias of ALIASES[word] || []) for (const t of tokenize(alias)) out.add(t);
  return [...out];
}
function rank(doc, terms, phrase) {
  const title = String(doc.title || "").toLowerCase();
  const description = String(doc.description || "").toLowerCase();
  const section = String(doc.section || "").toLowerCase();
  const keywords = (doc.keywords || []).join(" ").toLowerCase();
  const headings = (doc.headings || []).join(" ").toLowerCase();
  const content = String(doc.content || "").toLowerCase();
  let score = 0, matched = 0;
  if (phrase && title.includes(phrase)) score += 22;
  if (phrase && description.includes(phrase)) score += 9;
  for (const term of terms) {
    let weight = 0;
    if (title.split(/[^a-z0-9_.$+-]+/).includes(term)) weight = 12;
    else if (title.includes(term)) weight = 8;
    else if (keywords.includes(term)) weight = 6;
    else if (headings.includes(term)) weight = 5;
    else if (description.includes(term)) weight = 4;
    else if (section.includes(term)) weight = 2;
    else if (content.includes(term)) weight = 1;
    else {
      const near = (doc.keywords || []).reduce((best, word) => Math.max(best, editSimilarity(term, String(word).toLowerCase())), 0);
      if (near >= 0.82) weight = 1.25;
    }
    if (weight) { score += weight; matched++; }
  }
  score += terms.length ? 6 * matched / terms.length : 0;
  return { score, matched };
}
function snippet(doc, terms) {
  const text = String(doc.content || doc.description || "").replace(/\s+/g, " ").trim();
  const lower = text.toLowerCase();
  let at = -1;
  for (const term of terms) { const i = lower.indexOf(term); if (i >= 0 && (at < 0 || i < at)) at = i; }
  if (at < 0) return text.slice(0, 260);
  return (at > 90 ? "…" : "") + text.slice(Math.max(0, at - 90), Math.min(text.length, at + 240)) + (at + 240 < text.length ? "…" : "");
}
export async function onRequest({ request, env }) {
  const url = new URL(request.url);
  if (request.method !== "GET" && request.method !== "HEAD") return new Response("Method not allowed", { status: 405, headers: { Allow: "GET, HEAD" } });
  const query = (url.searchParams.get("q") || "").trim();
  if (!query) return Response.json({ engine: "Realot Studio", usage: "GET /api/search?q=describe%20what%20you%20need", results: [] });
  if (query.length > 500) return Response.json({ error: "Query must be 500 characters or fewer." }, { status: 400 });
  const indexUrl = new URL("/search-index.json", url.origin);
  const indexResponse = await env.ASSETS.fetch(new Request(indexUrl.toString(), { headers: { Accept: "application/json" } }));
  if (!indexResponse.ok) return Response.json({ error: "The documentation search index is temporarily unavailable." }, { status: 503 });
  const records = await indexResponse.json();
  const rawTerms = tokenize(query);
  const terms = expand(rawTerms);
  const phrase = query.toLowerCase();
  const limit = Math.min(20, Math.max(1, Number.parseInt(url.searchParams.get("limit") || "8", 10) || 8));
  const results = records.map(doc => {
    const r = rank(doc, terms, phrase);
    return { doc, score: r.score, matchedTerms: r.matched };
  }).filter(x => x.score > 0).sort((a, b) => b.score - a.score).slice(0, limit).map(({ doc, score, matchedTerms }) => ({
    title: doc.title,
    description: doc.description,
    section: doc.section,
    url: doc.url,
    score: Math.round(score * 100) / 100,
    matchedTerms,
    snippet: snippet(doc, rawTerms)
  }));
  return Response.json({ engine: "Realot Studio", query, resultCount: results.length, results }, {
    headers: { "Cache-Control": "public, max-age=60, s-maxage=300", "Access-Control-Allow-Origin": "*" }
  });
}
