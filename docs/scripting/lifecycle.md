# Lifecycle

> Complete Realot Studio script lifecycle and callback reference.

- Source: https://realot-studio.pages.dev/docs/scripting/lifecycle.html

## Core lifecycle

| Callback | Semantics |
| --- | --- |
| onStart() | Once before first onUpdate(). |
| onClone() | Once for runtime clones, immediately before onStart(). |
| onUpdate(dt) | Every render frame. |
| onFixedUpdate(dt) | Fixed 60 Hz accumulator. |
| onDestroy() | Before entity removal / scene end. |

```
function onStart() {
  this.hp = 100; // custom fields on this persist across the entity’s lifetime
  debug.log("HP", this.hp);
}

function onUpdate() {
  this.x += 50 * time.deltaTime; // frame-rate independent movement
}

function onFixedUpdate(dt) {
  // runs at a fixed 60 Hz step — good for deterministic physics-adjacent logic
}

function onDestroy() {
  debug.clear("HP");
}
```

## Pointer callbacks

`onClick()` is a frame pulse for mouse/finger presses targeting an entity with Collider2D. For continuous polling, use `this.isPointerOver`, `this.isClicked`, `this.isTouchOver` or `this.isTapped` where appropriate.

```
function onClick() {
  this.destroy(); // pops this entity when clicked or tapped
}
```

## Collision callbacks

| Callback | Runs |
| --- | --- |
| onCollision(other) | Alias of collision-enter behavior. |
| onCollisionEnter(other) | Contact begins. |
| onCollisionStay(other) | Every physics step while still touching. |
| onCollisionExit(other) | Contact ends. |
| onTriggerEnter(other) | Trigger overlap begins. |
| onTriggerExit(other) | Trigger overlap ends. |

```
function onCollisionEnter(other) {
  if (other.name === "Ground") this.isGrounded = true;
}

function onTriggerEnter(other) {
  if (other.hasComponent("Rigidbody2D")) scene.load("Level2");
}
```

## State callbacks

When using `this.state.change(name)`, Realot Studio can call `onStateExit()`, `onStateEnter()` and `onStateUpdate(dt)` for state-specific logic.

```
function onUpdate() {
  if (this.hp <= 0 && this.state.current !== "dead") {
    this.state.change("dead");
  }
}

function onStateEnter() {
  if (this.state.current === "dead") this.sprite.opacity = 0.3;
}
```

## Error isolation

Lifecycle errors are caught and reported by the runtime. A one-time `onStart()` failure disables the script; recurring `onUpdate()` errors are isolated so the next frame can continue.
