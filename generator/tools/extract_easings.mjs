// Extract the tween easing catalogue straight from the engine source.
// Usage: node tools/extract_easings.mjs <engine_root> easings.json
// Samples every easing from the real functions so the documentation gallery can never drift from the engine.
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';
import { writeFileSync } from 'node:fs';
const root = resolve(process.argv[2] || '.');
const out = process.argv[3] || 'easings.json';
const { TWEEN_EASING_NAMES, resolveTweenEasing } = await import(pathToFileURL(root + '/project/runtime/scripting/TweenEasing.js').href);
const N = 48;
const list = TWEEN_EASING_NAMES.map(({ label, detail }) => {
  const f = resolveTweenEasing(label);
  const samples = Array.from({ length: N + 1 }, (_, i) => +f(i / N).toFixed(5));
  return { label, detail, samples, min: Math.min(...samples), max: Math.max(...samples) };
});
writeFileSync(out, JSON.stringify({ count: list.length, easings: list }, null, 1));
console.log('easings:', list.length);
