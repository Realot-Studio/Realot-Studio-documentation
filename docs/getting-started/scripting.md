# Scripting quickstart

> Learn the Realot Studio JavaScript scripting model in one page.

- Source: https://realot-studio.pages.dev/docs/getting-started/scripting.html

## Script shape

Realot Studio scripts are plain JavaScript functions executed by the ScriptSystem. You do not create a class instance yourself. The engine binds the entity context to `this`.

```
function onStart() {
  this.health = 100;
}

function onUpdate(dt) {
  this.x += 100 * dt;
}
```

## The two layers of the API

| Layer | Examples | Use when |
| --- | --- | --- |
| Entity context (`this`) | `this.x`, `this.sprite`, `this.rigidbody`, `this.destroy()` | You are acting on the current entity. |
| Globals | `findFirst()`, `scene.load()`, `physics.raycast()`, `input.keyDown()` | You need scene-wide services or another entity. |

## Common component shortcuts

When a component exists on the entity, the corresponding module is exposed on `this`: `this.sprite`, `this.shape`, `this.text`, `this.rigidbody`, `this.controller`, `this.animator`, `this.camera`, `this.audio`, `this.collider`, `this.joint`, `this.navAgent`, `this.light`, `this.shadowCaster`, `this.strokePath`, and more.

## Discoverability

The editor’s script autocomplete is sourced from the same public API lists documented here. A good rule for generated code is: use documented globals and component modules; do not reach into internal runtime systems or editor modules.
