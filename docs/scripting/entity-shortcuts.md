# Entity shortcuts (this.x, this.transform)

> What this is inside a script, which properties are flat shortcuts, and which require a specific component.

- Source: https://realot-studio.pages.dev/docs/scripting/entity-shortcuts.html

## Flat shortcuts (always available)

Inside any lifecycle function, `this` is an EntityContext bound to the entity the script is attached to. A small set of properties are flat shortcuts directly onto the entity’s Transform, because Transform has only one shape. Everything else lives behind a sub-object gated by a specific component — see the full this reference for every sub-object.

| Shortcut | Meaning |
| --- | --- |
| this.x / this.y | Read/write live position. Writing immediately moves the entity, and correctly teleports the physics body too on a Dynamic or Kinematic Rigidbody2D rather than being silently overwritten by the next physics step. |
| this.position | {x, y}; assigning moves the entity. |
| this.translate(dx, dy) | Move by a delta this call. |
| this.rotation, this.scaleX, this.scaleY | Degrees and scale factors, matching the Inspector’s Transform fields. |
| this.visible, this.enabled | Show/hide and enable/disable the entity. |

```
function onUpdate() {
  this.rotation += 90 * time.deltaTime; // spin
  this.translate(0, -1); // drift upward one unit per frame
  if (this.y < -50) this.visible = false;
}
```

## Identity & lifecycle helpers

| Helper | Meaning |
| --- | --- |
| this.destroy() | Queues the entity for removal (deferred, not instant). this.destroyed becomes true immediately even though removal has not happened yet. |
| this.hasComponent(key) | True if the entity currently has the named component. "Transform" always returns true. Works on any EntityContext, including one from find() or a collision callback’s other. |
| this.name, this.tag, this.id | Read-only name; read/write tag; stable unique ID. |
| this.isClone | True inside onClone()/onStart() for a runtime-spawned clone. |

```
function onUpdate() {
  if (this.hp <= 0 && !this.destroyed) {
    this.destroy();
  }
}

function onStart() {
  if (this.isClone) this.tag = "spawned"; // mark runtime clones differently
}
```
