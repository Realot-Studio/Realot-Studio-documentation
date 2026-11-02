# Rigidbody2D

> Realot Studio Rigidbody2D component reference: fields, script API, behavior and examples.

- Source: https://realot-studio.pages.dev/docs/api/components/rigidbody2d.html

> **Scope:** This page documents the Rigidbody2D component in Realot Studio. Runtime fields are serialized scene data; the Script API section lists only members intentionally exposed to game scripts.

> **Where to find it in the editor:** Inspector (right) → Add Component → Rigidbody 2D. Pair with Collider 2D for a colliding body. Edit → Physics Layers… controls named layer slots.

## What it does

2D physics body backed by the engine physics runtime. Dynamic, Kinematic and Static bodies have different script controls.

> **Component setup & editor tools:** Rigidbody2D gives an entity a Rapier 2D body. Collider2D is normally paired with it when physical contact is required.

## How to add and use Rigidbody2D

**Editor path:** Select the target entity in the **Hierarchy** (left side) → look at the **Inspector** (right side) → click **Add Component** at the bottom of the Inspector → search for **Rigidbody2D** → click the component row. The Add Component picker is a centered modal with a search box; it only lists components not already attached.

For components with a dedicated editor tool, the tool is opened or activated from the location described below. Do not assume that adding the component alone activates its editor; some systems require a separate window, panel, or viewport tool.

## Component setup & editor tools

- Select entity → Inspector → Add Component → Rigidbody 2D. After adding it, the Rigidbody2D section exposes body type, gravity/damping, velocity/drive values, rotation locking, and controller/ground state fields.

### What you should see after adding it

The component appears as its own section in the Inspector. Its serialized settings are listed in the **Component data** table below. If a field is conditional, it appears only when the relevant mode/type is selected. If a field is a runtime state field (for example grounded or resolved velocity), treat it as read-only diagnostic state unless the API reference explicitly documents it as writable.

### How to read the settings

For every setting below, the documentation distinguishes **type**, **default**, **meaning**, and tuning direction where behavior is known. When a value represents a direction, use the engine's coordinate convention documented in [Coordinate system](../../reference/coordinate-system.html); do not substitute Unity/Godot conventions.

## Component data

| Field | Type | Purpose | Default |
| --- | --- | --- | --- |
| `bodyType` | BodyType enum: Dynamic | Kinematic | Static | Dynamic | Kinematic | Static. | `Dynamic` |
| `simulated` | boolean | Whether the body participates in physics simulation. | `true` |
| `mass` | number | Dynamic-only | `1` |
| `autoMass` | boolean | Inspector field stored on this component. | `true` |
| `gravityScale` | number | Gravity multiplier. | `1` |
| `linearDamping` | number | Linear damping. | `0` |
| `angularDamping` | number | Angular damping. | `0` |
| `lockRotation` | boolean | Dynamic + Kinematic | `false` |
| `velocityX` | number | working velocity — for Dynamic this is read back FROM Rapier each frame (unless driveVelocityX below is set by a controller this same frame); for Kinematic this is the velocity the caller/script sets to drive the body (consumed by PhysicsWorld as a kinematic move). | `0` |
| `velocityY` | number | Y velocity. | `0` |
| `angularVelocity` | number | Angular velocity. | `0` |
| `driveVelocityX` | nullable value | Set (transiently, one frame at a time) by runtime/systems/ControllerSystem.js to drive a DYNAMIC body's horizontal speed via Rapier's setLinvel while leaving the Y axis (and therefore Rapier's own gravity/impulse integration) alone. | `null` |
| `driveVelocityY` | nullable value | Set (transiently, one frame) by ControllerSystem to override a DYNAMIC body's Y velocity this physics step — used both for a one-shot jump kick (Character Controller/Platformer) and for continuous Y drive (Top-Down, which has no gravity to preserve). | `null` |
| `driveAngularVelocity` | nullable value | Set (transiently, one frame) by ControllerSystem to drive a DYNAMIC body's angular velocity (e.g. | `null` |
| `grounded` | boolean | Read-only contact state: written every physics step from Rapier contact manifolds. | `false` |
| `resolvedVelocityX` | number | KINEMATIC-only, read-only: written every physics step with the ACTUAL movement that the kinematic target-motion query resolved after blocking/sliding against obstacles. | `0` |
| `resolvedVelocityY` | number | Inspector field stored on this component. | `0` |
| `pendingForceX` | number | DYNAMIC-only force/impulse queue: pushed by the scripting API's DynamicRigidbodyAPI (see scripting/components/RigidbodyAPI.js) via .addForce()/.addImpulse()/.addTorque() and drained by PhysicsWorld.\_syncEntity every physics step, exactly like driveVelocityX/Y above — plain, serializable data (RULES.txt section 4)… | `0` |
| `pendingForceY` | number | Inspector field stored on this component. | `0` |
| `pendingImpulseX` | number | Inspector field stored on this component. | `0` |
| `pendingImpulseY` | number | Inspector field stored on this component. | `0` |
| `pendingTorque` | number | Inspector field stored on this component. | `0` |
| `pendingAngularImpulse` | number | Inspector field stored on this component. | `0` |

## Tuning behavior

These are the practical direction-of-change rules for the most important controls on this component.

| Setting | What changing it does |
| --- | --- |
| `mass` | Higher mass makes the body harder to accelerate from the same force/impulse. It does not make gravity itself stronger. |
| `gravityScale` | 1 is the normal engine gravity response for Dynamic bodies; 2 doubles it; 0 disables gravity contribution. |
| `linearDamping` | Higher values remove linear velocity faster; 0 leaves the body with no linear damping. |
| `angularDamping` | Higher values remove rotational velocity faster. |

## Automatic mass and force at a point

- `autoMass` (default `true`): a Dynamic body computes its mass from the attached collider geometry and density. Uncheck it in the Inspector to use the `mass` value instead.
- `angularDamping`: resistance to spinning, separate from linear damping.
- `addForceAtPoint(...)` in the script API pushes the body at a world point, so it also creates torque.

## Script API

| Member | Kind | Description |
| --- | --- | --- |
| `addAngularImpulse(t)` | Method | The `this.rigidbody` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `addForce(x, y)` | Method | The `this.rigidbody` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `addForceAtPoint(x, y, pointX, pointY)` | Method | The `this.rigidbody` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `addImpulse(x, y)` | Method | The `this.rigidbody` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `addTorque(t)` | Method | The `this.rigidbody` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `angularDamping` | Property (read/write) | Angular damping. |
| `gravityScale` | Property (read/write) | Gravity multiplier. |
| `groundAngle` | Property (read-only) | The `this.rigidbody` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `groundAngleLimit` | Property (read/write) | The `this.rigidbody` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `grounded` | Property (read-only) | The `this.rigidbody` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `isGrounded` | Property (read-only) | The `this.rigidbody` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `isOnCeiling` | Property (read-only) | The `this.rigidbody` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `isOnSlope` | Property (read-only) | The `this.rigidbody` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `isOnWall` | Property (read-only) | The `this.rigidbody` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `linearDamping` | Property (read/write) | Linear damping. |
| `mass` | Property (read/write) | Dynamic mass. |
| `move(dx, dy)` | Method | The `this.rigidbody` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `resolvedVelocity` | Property (read-only) | The `this.rigidbody` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `slopeMinAngle` | Property (read/write) | The `this.rigidbody` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `type` | Property (read/write) | Dynamic | Kinematic | Static; switching type is supported at runtime. |
| `velocity` | Property (read/write) | {x,y} velocity. |
| `velocityX` | Property (read/write) | Horizontal velocity. |
| `velocityY` | Property (read/write) | Vertical velocity. |
| `wallAngleLimit` | Property (read/write) | The `this.rigidbody` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |

## Notes & behavior

- Kinematic-only methods are meaningful for Kinematic bodies; Dynamic-only force methods apply to Dynamic bodies.
- Position assignment through this.x/this.y is treated as a physics teleport target for non-static bodies.

## Examples

```
this.rigidbody.addImpulse(0, -350);
```

```
this.rigidbody.velocityX = 200;
```

```
this.rigidbody.move(100 * time.deltaTime, 0);
```

> **Need the full workflow?:** Components: complete workflow covers adding, configuring, testing, combining, and removing components.
