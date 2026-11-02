# Save data

> The save global: get/set/delete, save slots, and flushing writes.

- Source: https://realot-studio.pages.dev/docs/scripting/saving.html

## Overview

`save` is a global backed by IndexedDB — the way to make a game remember things across page refreshes and browser restarts, unlike `global` (see Timers, state & messaging), which resets on every reload.

## Basic reads and writes

```
save.set("highScore", 4200);
var best = save.get("highScore") ?? 0;
save.has("checkpoint");
save.delete("temporaryBuff");
save.keys(); // every key currently stored
save.clear(); // wipe the current slot
```

## Save slots

```
await save.load("slot2"); // switch to a different save file
save.slot; // the currently active slot name
save.listSlots();
save.deleteSlot("slot3");
```

## Flushing & readiness

`save.isReady` reflects whether the store has finished its initial load from IndexedDB. Writes are coalesced and flushed asynchronously; call `save.flushNow()` if you need a write to be durably committed before doing something else (e.g. right before `scene.load()` on a level transition). `save.onError(callback)` registers a handler for storage failures (e.g. a full or blocked IndexedDB).

## Example: persistent high score

```
function onDestroy() {
  var best = save.get("highScore") ?? 0;
  if (global.score > best) save.set("highScore", global.score);
}
```
