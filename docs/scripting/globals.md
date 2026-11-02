# Global scripting API

> Reference for every built-in global function and service object available inside Realot Studio scripts.

- Source: https://realot-studio.pages.dev/docs/scripting/globals.html

## Entity lookup

| Function | Returns / behavior |
| --- | --- |
| `findFirst(name)` | First entity with this name, or `null`. |
| `findAll(name)` | All entities with this name. |
| `findFirstWithTag(tag)` | First entity with this tag, or `null`. |
| `findAllWithTag(tag)` | All entities with this tag. |
| `findWithTag(tag)` | Alias for `findAllWithTag(tag)`. |
| `findById(id)` | Entity with this exact stable ID, or `null`. |
| `findInRadius(x, y, radius, opts?)` | Nearby entities, nearest first. Optional filters can narrow the search. |

## Scene (`scene`)

`scene` contains the same entity-lookup functions above, plus `load(sceneName)`, `restart()`, `pause()`, `resume()`, the read-only properties `current` and `isPaused`, and scene-wide `lighting`. `scene.pause()` freezes gameplay simulation while leaving the editor/Play window responsive; call `scene.resume()` to continue.

## Physics (`physics`)

`physics.raycast(x1, y1, x2, y2, opts?)` casts a ray against Rapier collider shapes and returns the closest hit or `null`. A hit contains the entity, world point, surface normal (when available) and distance. Pass `{ exclude: [this] }` to skip an entity, `{ debug: true }` to draw the ray for one frame, or `{ layerMask: physics.layer(0, 2) }` to filter by layer bits. `physics.layer(...indices)` creates the bitmask for slots 0–15.

```
function onUpdate() {
  var hit = physics.raycast(this.x, this.y, this.x + 200, this.y, {
    exclude: [this],
    debug: true
  });
  if (hit) debug.log("Ray hit", hit.entity.name);
}
```

## Navigation (`nav`)

| Member | Purpose |
| --- | --- |
| `findPath(x1, y1, x2, y2, opts?)` | Returns world-space waypoints or `null` when no route is available. |
| `isWalkable(x, y)` | Tests whether a world point falls on a walkable navigation cell. |
| `bake()` | Rebuilds the scene NavWorld2D from current colliders; returns walkable/blocked counts or `null`. |
| `areaIndex(name)` | Resolves an area name to a slot index, or `-1`. |
| `areaMask(...names)` | Builds a bitmask from named areas. |
| `areaCosts(costsByName)` | Builds a 16-entry cost array from area names and positive costs. |

For moving entities every frame, use `this.navMoveToward()` or (for a Car controller) `this.navDriveToward()`. See [Pathfinding](navigation.html).

## Keyboard (`input`)

`input.keyDown(key)` is true while a key is held. `input.keyPressed(key)` is true only on the frame it is first pressed. Both accept `"Any"` to test whether any key is held or was pressed that frame. Use the [Input guide](input.html) for key naming and patterns.

## Mouse and pointer (`mouse`)

`mouse.x` and `mouse.y` are world coordinates. `screenX` and `screenY` are canvas pixels. `over` reports whether the pointer is over the game canvas. `down(button?)`, `pressed(button?)` and `released(button?)` read mouse buttons (0 left, 1 middle, 2 right; omitted means left). `isOver(entityOrName, opts?)` tests hover and `clickedOn(entityOrName, opts?, button?)` tests a click on a specific entity.

## Touch (`touch`)

`touch` is a live array of active touches. Each touch exposes `id`, world-space `x/y`, canvas-pixel `screenX/screenY`, start coordinates, displacement (`dx/dy`), `distance`, and one-frame `justStarted/justEnded` flags. The array also exposes `count`, `first`, `anyJustStarted` and `anyJustEnded`. Gesture helpers are `swipe.active/direction/dx/dy/distance` and `pinch.active/scale/delta/distance`. `touch.isOver(entityOrName, opts?)` checks a finger over an entity; `touch.tappedOn(entityOrName, opts?)` detects the initial tap. See [Input guide](input.html).

## Time (`time`)

`time.deltaTime` is scaled frame time, `time.unscaledDeltaTime` is frame time before time scaling, `time.elapsed` is elapsed game time, and `time.scale` controls game speed. A scale of 0 pauses time-driven simulation; 1 is normal speed. See [Time scale & game speed](time-scale.html).

## Random and math helpers

`random.int(min, max)` returns an inclusive random integer. `random.float(min, max)` returns a random float in the half-open range [min, max). `mathx` provides `lerp`, `smoothstep`, `clamp`, `moveToward`, `remap` and `approximately`. A bare `smoothstep(a, b, value)` global is also available. Native JavaScript `Math` is available as well.

## Shared in-memory state (`global`)

`global` is a shared key/value object visible to all scripts in the current running game. Read and write named properties directly, for example `global.score = 10`. It is memory-only; it does not survive reloading the game page. Use `save` for persistent data.

## Persistent save data (`save`)

`save` stores JSON-safe values in IndexedDB, separated into named save slots. Its full 13-member API is listed in [SaveAPI](../api/script-modules.html#saveapi). Common calls are `get`, `set`, `has`, `delete`, `keys` and `clear`. Use `await save.load("slot2")` to change slots, `await save.listSlots()` to list them, `await save.deleteSlot("slot2")` to remove a slot, and `await save.flushNow()` to wait for pending writes. See [Persistence](persistence.html).

## Debug HUD (`debug`)

`debug.show()` enables the gameplay HUD and system timing display in the Play window; `debug.show(false)` turns it off. `debug.showFps(false)` hides only its FPS line. `debug.log(label, value)` adds or updates a custom line; `debug.clear(label)` removes one line; `debug.clearAll()` removes all custom lines. This is separate from the editor Console.

## Object pools (`pool`)

`pool.create(name, options)` creates a named pool using a source prefab, scene entity or EntityContext. `pool.find(name)` retrieves a named pool, `pool.get(name, x, y)` gets an active object, and `pool.release(entity)` returns it for reuse. A pooled entity can call `this.releaseToPool(delay?)`. Pooled scripts can use `onEnable` and `onDisable` for work that should run each time an object is borrowed or returned.

## Spawn, timers, messages and tweens

| Function | Behavior |
| --- | --- |
| `spawn(nameOrTag, opts?)` | Clones an entity found by name, or by tag when `opts.byTag` is true. Returns an EntityContext or `null`. |
| `wait(seconds, callback)` | Runs once after game time passes; returns a timer ID. |
| `repeat(seconds, callback)` | Runs repeatedly at the interval; returns a timer ID. |
| `cancelWait(id)` / `cancelRepeat(id)` | Cancel the matching timer. Entity-owned timers also stop when their owner is destroyed or the scene changes. |
| `sendMessage(tagOrEntity, message, data?)` | Sends to all scripts matching a tag, or one exact entity context. |
| `broadcastMessage(message, data?)` | Sends to every script in the current scene. |
| `tween(target, properties, duration, easing?, onComplete?)` | Animates numeric properties over game time; returns an ID. |
| `cancelTween(id)` | Cancels a running tween. |

Read [Timers, state & messaging](timers-state.html), [Finding and spawning](finding-entities.html) and [Tween API](tween.html) for complete examples and option details. The [script module index](../api/script-modules.html) contains all 24 component/global API module allow-lists.
