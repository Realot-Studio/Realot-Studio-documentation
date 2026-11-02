# Collisions & triggers

> onCollisionEnter/Stay/Exit, onTriggerEnter/Exit, the other parameter, and physics layers from script.

- Source: https://realot-studio.pages.dev/docs/scripting/collisions.html

## Requirements

Collision and trigger callbacks need a Collider2D on the entity receiving the callback (a Rigidbody2D is not strictly required — a collider with no rigidbody is treated as static, matching how Unity handles a collider-only object).

## The other parameter

`other` in every collision/trigger callback is an EntityContext — the exact same shape as `this`. You can read `other.x`, `other.name`, call `other.hasComponent(...)`, or even `other.destroy()`.

## Enter vs. Stay vs. Exit

```
function onCollisionEnter(other) {
  if (other.name === "Ground") this.isGrounded = true;
}

function onCollisionExit(other) {
  if (other.name === "Ground") this.isGrounded = false;
}
```

`onCollisionStay(other)` fires every physics step the collider remains touching — from the step after Enter, up to (not including) the step Exit fires. Use Stay sparingly for continuous effects (e.g. damage-over-time while standing in a hazard); use Enter/Exit for one-shot state changes.

## Triggers

A collider with `isTrigger: true` detects overlap without physically blocking movement, and fires `onTriggerEnter`/`onTriggerExit` instead of the collision events:

```
function onTriggerEnter(other) {
  if (other.hasComponent("Rigidbody2D")) {
    scene.load("Level2");
  }
}
```

## Physics layers

Collider2D’s `layer`/`mask` fields (16 named layers, same slot-based model as Unity) control which pairs of colliders physically interact and receive callbacks at all. Two colliders only interact if each one’s membership layer is included in the other’s mask — see Collider2D for the full bitmask reference and `physics.layer(...)` for building a mask from script.
