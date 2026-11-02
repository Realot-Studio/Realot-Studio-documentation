# Script API cookbook

> Concrete Realot Studio script examples with setup, placement, required components, options, expected behavior, and common mistakes.

- Source: https://realot-studio.pages.dev/docs/scripting/api-cookbook.html

## How to use the cookbook

Every example assumes a **Script** component exists on the entity that owns the code. In the editor, select the entity in the left Hierarchy, then use the right Inspector to open its **Script** component. Paste the example into the script's lifecycle function or adapt it to your existing script.

> **Read API reference + recipe together:** The API reference tells you what a function/property means. The recipes show when to call it, what object should own the script, and what other setup the feature needs.

## 1. Find an entity and move toward it

### Setup

Create an entity named `Target`. Put this script on the enemy.

### Code

```
function onUpdate(dt) {
  var target = findFirst("Target");
  if (!target) return;
  this.navMoveToward(target.x, target.y, 140);
}
```

`findFirst(name)` returns one matching entity or `null`. `navMoveToward()` supplies the navigation movement behavior.

## 2. Spawn a runtime clone

Author a source entity in the scene first, for example an entity named `Bullet`. The script below can live on a target, weapon, or spawner.

```
var bullet = spawn("Bullet", {
  x: this.x + 24,
  y: this.y,
  name: "Bullet_Instance"
});
if (bullet) {
  bullet.velocityX = 500;
}
```

> **Why the source entity matters:** spawn() clones an existing authored entity. It is not a constructor that invents a new component set from scratch.

## 3. Raycast toward an entity

Put this on the entity performing the vision/sensor check.

```
function onUpdate(dt) {
  var target = findFirst("Target");
  if (!target) return;

  var hit = physics.raycast(this.x, this.y, target.x, target.y, {
    layerMask: 1 << 0,
    exclude: [this],
    debug: true
  });

  this.hasLineOfSight = !hit || hit.entity === target;
}
```

The result is either a hit object containing `entity`, `point`, `normal`, and `distance`, or a falsy result when nothing is hit.

## 4. Send an event without hard-coding the receiver's logic

```
// Sender
var enemy = findFirst("Enemy");
if (enemy) sendMessage(enemy, "takeDamage", { amount: 25 });

// Receiver
function onMessage(message, sender, data) {
  if (message === "takeDamage") {
    this.hp -= data.amount;
  }
}
```

Use an EntityContext when you need exactly one receiver. Use a tag string when you intentionally want a group to receive the same message.

## 5. Keyboard movement with frame-independent speed

```
function onUpdate(dt) {
  var dx = 0;
  var dy = 0;
  if (input.keyDown("ArrowLeft")) dx -= 1;
  if (input.keyDown("ArrowRight")) dx += 1;
  if (input.keyDown("ArrowUp")) dy -= 1;
  if (input.keyDown("ArrowDown")) dy += 1;

  var length = Math.hypot(dx, dy);
  if (length > 0) {
    dx /= length;
    dy /= length;
    this.x += dx * 220 * dt;
    this.y += dy * 220 * dt;
  }
}
```

This is useful for simple non-physics entities. Use Rigidbody2D/CharacterController APIs when movement is supposed to participate in physics/controller resolution.

## 6. Delay work without hand-written countdown variables

```
function onStart() {
  this.wait(1.5, function () {
    this.sprite.opacity = 0.4;
  });

  this.repeat(2, function () {
    debug.log("heartbeat");
  });
}
```

Entity-owned timers are automatically cancelled when the scheduling entity is destroyed or the scene changes.

## 7. Persistent save data

```
function onStart() {
  this.hp = save.get("targetHp") ?? 100;
}

function onCheckpointReached() {
  save.set("targetHp", this.hp);
  save.set("checkpoint", { x: this.x, y: this.y });
}

async function onGameComplete() {
  save.set("completed", true);
  await save.flushNow();
  scene.load("Credits");
}
```

> **Important:** save.set() updates the in-memory save immediately. Use await save.flushNow() when the next action must wait for durable storage before continuing.

## 8. Ask the navigation system for a path

```
var path = nav.findPath(this.x, this.y, goalX, goalY, {
  radius: this.navAgent.radius,
  area: nav.areaMask("Ground", "Road"),
  areaCosts: nav.areaCosts({ Road: 1, Mud: 4 }),
  debug: true
});

if (path) {
  debug.log("Waypoints: " + path.length);
}
```

This example demonstrates four separate concepts: agent clearance, hard area permission, soft area preference, and debug visualization.

## 9. Change a NavAgent2D at runtime

Select the moving entity and add **Nav Agent 2D** in Inspector → Add Component → Nav Agent 2D. The exposed script properties are read/write.

```
this.navAgent.speed = 180;
this.navAgent.radius = 12;
this.navAgent.avoidanceEnabled = true;
this.navAgent.repathInterval = 0.2;

// Read-only current route state:
var path = this.navAgent.currentPath;
var index = this.navAgent.currentPathIndex;
```

> **Read-only fields:** currentPath and currentPathIndex are managed by navMoveToward() . Do not assign to them; call this.navMoveToward(newX,newY,...) to change the destination.

## 10. Use named navigation areas instead of raw bitmasks

First name the slots in Edit → Nav Areas…. For example: `Ground`, `Road`, `Mud`, `Water`.

```
var roadOnly = nav.areaMask("Road");
var mixed = nav.areaMask("Road", "Ground");
var waterSlot = nav.areaIndex("Water");
```

This keeps scripts readable and means you do not have to remember which slot number was assigned to each named area.

## 11. Camera follow

```
function onUpdate(dt) {
  var target = findFirst("Target");
  if (target) {
    this.camera.follow(target, { smoothing: 0.1 });
  }
}
```

Put the script on the entity that has the Camera component. The engine template also demonstrates this pattern.

## 12. Switch animations from gameplay state

```
function onUpdate(dt) {
  if (!this.rigidbody) return;

  if (!this.rigidbody.grounded) {
    if (this.rigidbody.velocityY > 0) this.animator.play("fall");
    else this.animator.play("Jump");
  } else if (Math.abs(this.rigidbody.velocityX) > 5) {
    this.animator.play("Run");
  } else {
    this.animator.play("Idle");
  }
}
```

## 13. Touch / joystick control

For a Joystick component, select an entity, then use Inspector → Add Component → Joystick. The script can read normalized values:

```
function onUpdate(dt) {
  if (!this.joystick || !this.joystick.active) return;
  this.controller.simulateMove(this.joystick.x, this.joystick.y);
}
```

`x` and `y` are normalized joystick axes; `magnitude` tells you how far the thumb is displaced.

## 14. Trigger a scene change on overlap

Give the portal entity a **Collider2D** and enable its **Is Trigger** checkbox in the right Inspector.

```
function onTriggerEnter(other) {
  if (other.name === "Target") {
    scene.load("Level2");
  }
}
```

Trigger callbacks depend on Collider2D overlap. A trigger does not behave like a solid blocking collider.

## 15. Build your own tiny diagnostic HUD

```
function onUpdate(dt) {
  debug.log(
    "pos=" + Math.round(this.x) + "," + Math.round(this.y) +
    " speed=" + Math.round(this.navAgent ? this.navAgent.speed : 0)
  );
}
```

Use this while developing, then remove or gate noisy logging before a final release.

## Patterns that scale well

| Need | Prefer | Avoid |
| --- | --- | --- |
| Exact entity | `findById()` or a known EntityContext | Assuming a shared name is unique when it is not. |
| Group communication | Tag + `sendMessage()` | Duplicating the same lookup in every receiver. |
| Persistent data | `save.*` | Using `global.*` for data that must survive reload. |
| Pathfinding | One NavWorld2D + NavAgent2D per mover | Creating a navigation world per NPC. |
| Physics movement | Rigidbody2D / CharacterController APIs | Directly changing `x/y` when you need collision resolution. |
| Frame-independent custom movement | Multiply speed by `dt` | Using a raw pixels-per-frame constant. |

## Where to go next

### Complete Navigation

[Full editor-to-runtime navigation setup, areas, costs, vehicles and debugging.](./navigation-complete.html)

### Option schemas

[Exact `opts` objects, defaults, types and override rules.](../api/options.html)

### Component reference

[Every component and its editor/runtime contract.](../api/index.html)
