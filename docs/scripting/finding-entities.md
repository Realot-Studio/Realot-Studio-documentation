# Finding & spawning entities

> The find/findAll/findWithTag family, plus spawn() for runtime-instantiated clones.

- Source: https://realot-studio.pages.dev/docs/scripting/finding-entities.html

## Finding entities

| API | Returns |
| --- | --- |
| findFirst(name) | First entity with this exact name, or null. |
| findAll(name) | Every entity with this name, as an array. |
| findFirstWithTag(tag) / findAllWithTag(tag) | Same pair, keyed by tag instead of name. |
| findById(id) | Never ambiguous — use the id from an earlier spawn() or find() call. |
| findInRadius(x, y, radius, opts) | Entities within radius world units of a point, nearest first. |
| entity.distanceTo(x, y) | Instance method on any EntityContext: distance from that entity to a point. |

## Spawning

`spawn(nameOrTag, opts)` spawns a runtime clone of an existing entity. Looks the source up by name by default:

```
spawn("Bullet");
spawn("Bullet", { x: this.x, y: this.y });
spawn("Enemy", { byTag: true, x: 200, y: 100 }); // look up by tag, clone the first match
```

Optionally rename the clone with `opts.name`. Returns an EntityContext for the new entity (same shape as `this`), or null if no source entity matches. The clone’s own `onClone()` then `onStart()` fire automatically on the next frame, with `this.isClone === true` inside them. Also available as an instance method, `this.spawn(nameOrTagOrEntity, opts)` — pass an EntityContext directly (e.g. `this.spawn(this)`) to clone that exact entity with zero name/tag ambiguity.
