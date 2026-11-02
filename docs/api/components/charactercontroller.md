# CharacterController

> Realot Studio CharacterController component reference: fields, script API, behavior and examples.

- Source: https://realot-studio.pages.dev/docs/api/components/charactercontroller.html

> **Scope:** This page documents the CharacterController component in Realot Studio. Runtime fields are serialized scene data; the Script API section lists only members intentionally exposed to game scripts.

> **Where to find it in the editor:** Inspector → Add Component → Movement Type. Pick Character Controller, Platformer, Top-Down, Car, Follow or Patrol; fields in the Inspector change with the selected mode.

## What it does

High-level movement modes: Character Controller, Platformer, Top-Down, Car, Follow, Patrol and Free.

> **Component setup & editor tools:** CharacterController provides the higher-level movement behaviors such as Platformer, Car, Follow, or Patrol when configured with the required physics components.

## How to add and use CharacterController

**Editor path:** Select the target entity in the **Hierarchy** (left side) → look at the **Inspector** (right side) → click **Add Component** at the bottom of the Inspector → search for **CharacterController** → click the component row. The Add Component picker is a centered modal with a search box; it only lists components not already attached.

For components with a dedicated editor tool, the tool is opened or activated from the location described below. Do not assume that adding the component alone activates its editor; some systems require a separate window, panel, or viewport tool.

## Component setup & editor tools

- Select entity → Inspector → Add Component → Movement Type (CharacterController). Choose the controller type first; the Inspector then exposes the relevant movement fields. Platformer/Car/Follow/Patrol fields are not interchangeable—configure only the group belonging to the selected controller type.

### What you should see after adding it

The component appears as its own section in the Inspector. Its serialized settings are listed in the **Component data** table below. If a field is conditional, it appears only when the relevant mode/type is selected. If a field is a runtime state field (for example grounded or resolved velocity), treat it as read-only diagnostic state unless the API reference explicitly documents it as writable.

### How to read the settings

For every setting below, the documentation distinguishes **type**, **default**, **meaning**, and tuning direction where behavior is known. When a value represents a direction, use the engine's coordinate convention documented in [Coordinate system](../../reference/coordinate-system.html); do not substitute Unity/Godot conventions.

## Component data

| Field | Type | Purpose | Default |
| --- | --- | --- | --- |
| `controllerType` | ControllerType enum: Character Controller | Platformer | Top-Down | Car | Follow | Patrol | Free | Character Controller | Platformer | Top-Down | Car | Follow | Patrol | Free. | `Character Controller` |
| `moveSpeed` | number | Movement (Character / Platformer / Top-Down) px/s | `200` |
| `acceleration` | number | how fast velocity approaches target (higher = snappier) | `20` |
| `airControl` | number | 0-1 multiplier on acceleration while airborne (Platformer only) | `0.5` |
| `canJump` | boolean | Jump (Character Controller + Platformer) | `true` |
| `jumpForce` | number | px/s upward velocity applied on jump | `420` |
| `maxJumps` | number | 1 = no double jump, 2 = double jump, etc. | `1` |
| `useGravity` | boolean | Gravity (Character Controller can toggle it off for e.g. | `true` |
| `gravityScale` | number | Multiplier on gravity's strength for Character Controller/Platformer (same name/semantics as Rigidbody2D.gravityScale on a Dynamic body — 1 = normal, 2 = falls twice as fast, 0.5 = floaty/moon-gravity, 0 = no downward pull at all while still respecting useGravity's on/off switch). | `1` |
| `useDefaultInput` | boolean | Input. For Character/Platformer/Top-Down and Car, this controls the built-in keyboard while script APIs can contribute in the same frame. | `true` |
| `maxSpeed` | number | Car-specific (Car controller only) top forward speed in px/s | `350` |
| `carAcceleration` | number | how fast the car speeds up (px/s^2) | `200` |
| `brakeForce` | number | how fast it brakes / goes into reverse (px/s^2) | `400` |
| `turnSpeed` | number | max turn rate in deg/s (at full speed; scales down at lower speeds) | `150` |
| `driftFactor` | number | 0-1: how much lateral velocity is retained (higher = more slide) | `0.92` |
| `driveTowardArriveDistance` | number | px from the target that counts as "arrived" for | `12` |
| `targetName` | string | Follow-specific (Follow controller only) name of the entity to pursue |  |
| `followSpeed` | number | pursuit speed in px/s | `150` |
| `followDistance` | number | stop when within this many pixels of the target | `5` |
| `patrolDistance` | number | Patrol-specific (Patrol controller only). | `150` |
| `patrolMode` | PatrolMode enum: Platformer | Top-Down | Patrol's own movement scheme — see PatrolMode above. | `Platformer` |
| `patrolAxis` | PatrolAxis enum: Horizontal | Vertical | Which axis a TopDown-mode Patrol walks along — see PatrolAxis above. | `Horizontal` |
| `requestJump` | boolean | Set (transiently, for one ControllerSystem update) by this.controller.simulateJump() (see scripting/components/ ControllerAPI.js) to trigger a jump from script logic — consumed and reset to false by ControllerSystem.js right after reading it, the same one-shot request pattern Rigidbody2D's pendingForceX/Y uses. | `false` |
| `requestMoveX` | nullable value | Set (transiently, for one ControllerSystem update) by this.controller.simulateMove(x, y) (see scripting/components/ ControllerAPI.js) as a script/joystick movement contribution. | `null` |
| `requestMoveY` | nullable value | Inspector field stored on this component. | `null` |
| `requestThrottle` | nullable value | Set (transiently, for one ControllerSystem update) by this.controller.simulateDrive(throttle, steer) (see scripting/ components/ControllerAPI.js), Car-only. | `null` |
| `requestSteer` | nullable value | Inspector field stored on this component. | `null` |
| `requestJoystickX` | nullable value | Set (transiently, for one ControllerSystem update) by this.controller.simulateDriveJoystick(x, y) (see scripting/ components/ControllerAPI.js), Car-only. | `null` |
| `requestJoystickY` | nullable value | Inspector field stored on this component. | `null` |
| `requestDriveTowardX` | nullable value | Set (transiently, for one ControllerSystem update) by this.controller.simulateDriveToward(x, y) (see scripting/ components/ControllerAPI.js), Car-only. | `null` |
| `requestDriveTowardY` | nullable value | Inspector field stored on this component. | `null` |
| `requestFlip` | boolean | Set (transiently, for one ControllerSystem update) by this.controller.flipDirection() (see scripting/components/ ControllerAPI.js), Patrol-only. | `false` |

## Tuning behavior

These are the practical direction-of-change rules for the most important controls on this component.

| Setting | What changing it does |
| --- | --- |
| `moveSpeed` | Higher = faster target movement. |
| `acceleration` | Higher = reaches the requested speed faster; lower = softer/slower ramp. |
| `airControl` | For Platformer, 0 removes horizontal air steering; 1 gives full ground-like acceleration in air. |
| `jumpForce` | Higher = stronger/faster upward launch; lower = shorter jump. |
| `gravityScale` | 1 = normal controller gravity, 0 = no controller gravity; higher magnifies the pull. |

## Script API

| Member | Kind | Description |
| --- | --- | --- |
| `acceleration` | Property (read/write) | Acceleration. |
| `airControl` | Property (read/write) | Air-control factor. |
| `brakeForce` | Property (read/write) | Car brake force. |
| `canJump` | Property (read/write) | Whether jumping is available. |
| `controllerType` | Property (read-only) | Read-only movement type. |
| `driftFactor` | Property (read/write) | Car drift factor. |
| `driveTowardArriveDistance` | Property (read/write) | Exposed by this script module. |
| `facingDirection` | Property (read-only) | Current patrol facing direction. |
| `flipDirection()` | Method | Reverse Patrol direction. |
| `followDistance` | Property (read/write) | Follow distance. |
| `followSpeed` | Property (read/write) | Follow speed. |
| `gravityScale` | Property (read/write) | Gravity scale. |
| `groundAngle` | Property (read-only) | Ground angle. |
| `isGrounded` | Property (read-only) | Ground state. |
| `isOnCeiling` | Property (read-only) | Ceiling contact. |
| `isOnSlope` | Property (read-only) | Slope contact. |
| `isOnWall` | Property (read-only) | Wall contact. |
| `jumpForce` | Property (read/write) | Jump force. |
| `maxJumps` | Property (read/write) | Maximum jumps. |
| `maxSpeed` | Property (read/write) | Car maximum speed. |
| `moveSpeed` | Property (read/write) | Movement speed. |
| `patrolAxis` | Property (read/write) | Horizontal | Vertical. |
| `patrolDistance` | Property (read/write) | Patrol distance. |
| `patrolMode` | Property (read/write) | Platformer | Top-Down. |
| `simulateDrive(throttle, steer)` | Method | Drive a Car controller by script. |
| `simulateDriveJoystick(x, y)` | Method | Drive using joystick-style vector input. |
| `simulateDriveToward(x, y)` | Method | Drive toward a world point. |
| `simulateJump()` | Method | Request a jump. |
| `simulateMove(x, y)` | Method | Drive movement by script. |
| `targetName` | Property (read/write) | Follow target name. |
| `turnSpeed` | Property (read/write) | Car turn speed. |
| `useDefaultInput` | Property (read/write) | Built-in input mapping. |
| `useGravity` | Property (read/write) | Gravity toggle. |

## Notes & behavior

- Car-only fields/actions are meaningful for the Car controller. Patrol has its own patrolMode and patrolAxis. Free is script-driven with no built-in input mapping.

## Examples

```
this.controller.simulateMove(input.keyDown("ArrowRight") ? 1 : 0, 0);
```

```
this.controller.simulateJump();
```

> **Need the full workflow?:** Components: complete workflow covers adding, configuring, testing, combining, and removing components.
