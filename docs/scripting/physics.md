# Physics & navigation scripting

> Use Rigidbody2D, Collider2D, raycasts and NavWorld2D from game scripts.

- Source: https://realot-studio.pages.dev/docs/scripting/physics.html

## Physics raycasts

```
const hit = physics.raycast(this.x, this.y, target.x, target.y, {
  exclude: [this],
  layerMask: physics.layer(2, 3),
  debug: true
});

if (hit) {
  debug.log("Hit", hit.entity.name);
}
```

## Raycast results

A hit returns `{ entity, point, normal, distance }`. The entity is a live script context; point and normal are world-space vectors. Triggers are skipped by raycasts.

## Navigation

```
const path = nav.findPath(this.x, this.y, target.x, target.y, {
  radius: this.navAgent.radius,
  debug: true
});
```

## One-line agent steering

Entities with NavAgent2D gain `navMoveToward(targetX,targetY,speed,opts)`. Car + NavAgent entities additionally gain `navDriveToward()` for path-following, avoidance and car steering/drift behavior.

## Physics body choice

Choose the body type based on ownership of movement: Dynamic for solver-driven motion, Kinematic for script/controller-driven collision-resolved movement, Static for fixed geometry.
