# Entity context

> Reference the `this` object and entity-aware shortcuts available in Realot Studio scripts.

- Source: https://realot-studio.pages.dev/docs/scripting/entity-context.html

## Core members

| Member | Meaning |
| --- | --- |
| x, y | World position; writes to physics position targets when a non-static Rigidbody2D exists. |
| position | Read/assign {x,y}. |
| rotation | Degrees. |
| scaleX, scaleY | Scale. |
| translate(dx,dy) | Move by a delta. |
| distanceTo(x,y) | Distance to a world point. |
| name | Read-only entity name. |
| tag | Read/write tag. |
| id | Stable unique ID. |
| visible | Show/hide entity. |
| enabled | Enable/disable the current script. |
| destroy() | Queue entity destruction. |
| destroyed | Read-only destruction state. |
| isClone | True for runtime-spawned clones. |

```
function onUpdate() {
  this.translate(0, -50 * time.deltaTime); // move up
  var target = findFirst("Target");
  if (target && this.distanceTo(target.x, target.y) < 40) {
    this.destroy();
  }
}
```

## Component modules

Depending on attached components, `this` exposes modules including `transform`, `sprite`, `shape`, `text`, `speechBubble`, `chat`, `textInput`, `joystick`, `rigidbody`, `controller`, `animator`, `camera`, `audio`, `ear`, `collider`, `joint`, `navAgent`, `light`, `shadowCaster` and `strokePath`.

```
function onUpdate() {
  if (this.hasComponent("Rigidbody2D")) {
    this.rigidbody.addForce(0, -500);
  }
  this.sprite.opacity = this.isPointerOver ? 1 : 0.6;
}
```

## Timers belong to entities

Both `wait()` and `repeat()` are associated with the scheduling entity. When the entity is destroyed or a scene restarts/switches, its timers are automatically cancelled.

```
function onStart() {
  this.wait(1.5, function () {
    this.sprite.opacity = 1; // this is still the entity that scheduled the timer
  });
}
```

## Pointer helpers

> **Collider requirement:** isPointerOver , isClicked , isTouchOver , isTapped and myTouch require Collider2D because hit testing uses the real collider shape.
