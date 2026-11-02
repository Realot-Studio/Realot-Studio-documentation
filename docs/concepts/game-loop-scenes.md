# Game loop & scenes

> Understand frame updates, fixed physics updates and scene transitions.

- Source: https://realot-studio.pages.dev/docs/concepts/game-loop-scenes.html

## Render-frame lifecycle

| Hook | When it runs |
| --- | --- |
| onStart() | Once before the first onUpdate(). |
| onClone() | Once for runtime clones, immediately before onStart(). |
| onUpdate(dt) | Every render frame. |
| onClick() | On the frame a mouse/finger press targets an entity with a collider. |
| onFixedUpdate(dt) | Fixed 60 Hz simulation cadence. |
| onDestroy() | Before the entity is removed or the scene ends. |

## Collision & trigger lifecycle

Use `onCollisionEnter(other)`, `onCollisionStay(other)` and `onCollisionExit(other)` for physical contacts. `onCollision(other)` remains an alias for collision-enter behavior. Trigger-only callbacks are `onTriggerEnter(other)` and `onTriggerExit(other)`.

## Scene controls

Use `scene.current` to read the current scene name, `scene.load(name)` to switch scenes, `scene.restart()` to restart, and `scene.pause()`/`scene.resume()` to freeze gameplay while leaving rendering responsive.

```
function onTriggerEnter(other) {
  if (other.name === "Target") scene.load("Level2");
}

function onUpdate() {
  if (input.keyPressed("Escape")) {
    scene.isPaused ? scene.resume() : scene.pause();
  }
}
```

## Pause semantics

During `scene.pause()`, physics, scripts, animation and audio stop advancing until resume. Rendering stays responsive, which is useful for pause menus and debugging UI.
