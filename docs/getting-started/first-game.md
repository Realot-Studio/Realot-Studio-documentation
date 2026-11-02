# Build your first game

> A practical first-game path using entities, components and a simple script.

- Source: https://realot-studio.pages.dev/docs/getting-started/first-game.html

## 1. Start with a scene

Create a scene and add an entity. The editor stores scene state as JSON-compatible data: entities have IDs, names, tags, active state, optional hierarchy folders/prefab metadata, and a component map.

## 2. Add a visual

Attach a `SpriteRenderer` and assign a sprite asset, or use a `ShapeRenderer` when you want a procedural primitive. Add a `Camera` and mark one camera as the main camera.

## 3. Add physics when you need it

A typical physics actor uses a `Rigidbody2D` plus a `Collider2D`. Choose Dynamic, Kinematic or Static based on who is responsible for movement.

## 4. Add a Script component

Put a script on the entity and define lifecycle functions. Realot Studio calls `onStart()` once and `onUpdate(dt)` every render frame.

```
function onStart() {
  this.speed = 220;
}

function onUpdate(dt) {
  if (input.keyDown("ArrowRight")) {
    this.x += this.speed * dt;
  }
  if (input.keyDown("ArrowLeft")) {
    this.x -= this.speed * dt;
  }
}
```

## 5. Prefer frame-rate-independent movement

Use `time.deltaTime` (or the `dt` lifecycle argument) when movement is expressed in units per second. Keep physics-step work in `onFixedUpdate(dt)` when the logic should track the fixed simulation cadence.

## 6. Run, iterate, export

Use the editor’s Play flow to test, inspect the Debug HUD when diagnosing runtime behavior, then use **Export** for HTML5, PWA or Android APK.
