# Entities & components

> Understand Realot Studio scene entities, IDs, tags, component composition and runtime cloning.

- Source: https://realot-studio.pages.dev/docs/concepts/entities-components.html

## Entity identity

An entity has a unique stable ID such as `e12`, a human-facing name, a tag, active state, optional hierarchy folder, prefab metadata and a component map. Names and tags are not unique; IDs are.

## Why IDs matter

Use `findById(id)` when you mean one exact entity. Use name/tag queries when you intentionally want one or many matches. Runtime clones keep unique IDs and expose `isClone`.

## Component composition

A gameplay actor can combine Transform + SpriteRenderer + Collider2D + Rigidbody2D + Script. A UI button might combine Transform + TextRenderer + Collider2D + Script. There is no requirement that every entity have every component.

## Runtime cloning

Use `spawn()` or `this.spawn()` to clone an authored entity. The returned context is the new live entity; `onClone()` runs for runtime clones before `onStart()`.

```
function onUpdate() {
  if (input.keyPressed("Space")) {
    var bullet = spawn("Bullet", { x: this.x, y: this.y });
    bullet.rotation = this.rotation; // configure the clone right after spawning
  }
}

// Inside Bullet’s own script:
function onClone() {
  this.tag = "projectile"; // runs once, before this clone’s onStart()
}
```

## Destroying entities

`this.destroy()` queues destruction for the end of the frame. `onDestroy()` runs before removal. Waiting/repeating timers owned by the entity are automatically cancelled when the entity is destroyed.
