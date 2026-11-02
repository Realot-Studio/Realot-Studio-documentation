# Runtime modules and global API

> Index of global functions and objects supplied to gameplay scripts in Realot Studio.

- Source: https://realot-studio.pages.dev/docs/api/runtime.html

## Entity lookup functions

`findFirst(name)`, `findAll(name)`, `findFirstWithTag(tag)`, `findAllWithTag(tag)`, `findWithTag(tag)`, `findById(id)` and `findInRadius(x, y, radius, opts?)` locate entities in the current scene.

## Scene, physics and navigation

| Object | Exposed surface |
| --- | --- |
| `scene` | Entity lookup; `load`, `restart`, `pause`, `resume`; read-only `current` and `isPaused`; scene-wide `lighting`. |
| `physics` | `raycast(x1, y1, x2, y2, opts?)`, `layer(...indices)`. |
| `nav` | `findPath`, `isWalkable`, `bake`, `areaIndex`, `areaMask`, `areaCosts`. |

## Input, time and math

| Object | Exposed surface |
| --- | --- |
| `input` | `keyDown(key)`, `keyPressed(key)`. |
| `mouse` | World/screen coordinates, cursor state, button state, `isOver`, `clickedOn`. |
| `touch` | Active touch list, per-touch positions and state, swipe/pinch helpers, `isOver`, `tappedOn`. |
| `time` | `deltaTime`, `unscaledDeltaTime`, `elapsed`, `scale`. |
| `random` | `int(min, max)`, `float(min, max)`. |
| `mathx` | `lerp`, `smoothstep`, `clamp`, `moveToward`, `remap`, `approximately`. |
| `smoothstep(a, b, value)` | Global smoothstep helper also available without `mathx.`. |

## Game services

| Object / function | Purpose |
| --- | --- |
| `global` | Shared in-memory key/value state between scripts during the running game. |
| `save` | Persistent key/value data and named save slots backed by IndexedDB; exact members are in [SaveAPI](script-modules.html#saveapi). |
| `debug` | Play-window diagnostic HUD, FPS line and custom values. |
| `pool` | Named object pools for reusing entities. |
| `spawn(nameOrTag, opts?)` | Creates a runtime clone. |
| `wait`, `repeat`, `cancelWait`, `cancelRepeat` | Entity-owned one-shot and repeating timers. |
| `sendMessage`, `broadcastMessage` | Targeted, tag-group or scene-wide script messaging. |
| `tween`, `cancelTween` | Property animation over game time. |

## Detailed global API guide

The [Global scripting API](../scripting/globals.html) explains each object with examples. Use [Input](../scripting/input.html), [Persistence](../scripting/persistence.html), [Pathfinding](../scripting/navigation.html) and [Tween API](../scripting/tween.html) for focused guides.

## Per-entity component modules

Component modules such as `this.rigidbody`, `this.sprite`, `this.camera` and `this.text` depend on the components attached to the entity. The [complete script module index](script-modules.html) lists every supported member from all 24 script API modules, its access type and required context. The [`this` reference](this.html) explains EntityContext shortcuts and prerequisites.

## Fixed update

`onFixedUpdate(dt)` runs on the fixed physics cadence (60 steps per second in the supplied runtime). Use it for logic that should follow fixed-step physics timing; use `onUpdate(dt)` for frame-based presentation and input handling.

## Coordinate spaces

Entity positions, `mouse.x/y`, touch `x/y`, raycast points and navigation waypoints use world-space coordinates. Mouse/touch `screenX/screenY` values are raw game-canvas pixels. Camera reference resolution and world units are separate concepts.
