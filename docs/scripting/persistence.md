# Persistence

> Use transient global state and durable IndexedDB saves.

- Source: https://realot-studio.pages.dev/docs/scripting/persistence.html

## global vs save

| Surface | Lifetime |
| --- | --- |
| global | Transient cross-script state for the current play session/page. Refreshing the page clears it. |
| save | Persistent per-slot key/value storage backed by IndexedDB. Survives refresh/reopen when browser storage is available. |

## Basic save API

```
save.set("score", 1250);
const score = save.get("score");

if (!save.has("tutorialSeen")) {
  save.set("tutorialSeen", true);
}
```

## Multiple save slots

```
await save.load("slot2");
const hp = save.get("targetHp");

const slots = await save.listSlots();
```

## Flush before a transition

```
async function onGameComplete() {
  save.set("completed", true);
  await save.flushNow();
  scene.load("Credits");
}
```

## Storage errors

`save.set()` updates the in-memory value synchronously while IndexedDB writes happen in the background. Register `save.onError(fn)` to observe persistent-storage failures such as quota errors or unavailable IndexedDB implementations.
