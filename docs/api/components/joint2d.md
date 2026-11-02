# Joint2D

> Realot Studio Joint2D component reference: fields, script API, behavior and examples.

- Source: https://realot-studio.pages.dev/docs/api/components/joint2d.html

> **Scope:** This page documents the Joint2D component in Realot Studio. Runtime fields are serialized scene data; the Script API section lists only members intentionally exposed to game scripts.

> **Where to find it in the editor:** Inspector → Add Component → Joint 2D; choose Fixed/Revolute/Prismatic/Rope/Spring and configure anchors/limits/motor.

## What it does

Connect physics bodies with Fixed, Revolute, Prismatic, Rope or Spring constraints.

> **Component setup & editor tools:** Joint2D constrains one physics body relative to another and requires compatible Rigidbody2D setup.

## How to add and use Joint2D

**Editor path:** Select the target entity in the **Hierarchy** (left side) → look at the **Inspector** (right side) → click **Add Component** at the bottom of the Inspector → search for **Joint2D** → click the component row. The Add Component picker is a centered modal with a search box; it only lists components not already attached.

For components with a dedicated editor tool, the tool is opened or activated from the location described below. Do not assume that adding the component alone activates its editor; some systems require a separate window, panel, or viewport tool.

## Component setup & editor tools

- Select entity → Inspector → Add Component → Joint 2D. Configure the joint from its Inspector section and make sure the connected physics bodies satisfy the joint’s requirements.

### What you should see after adding it

The component appears as its own section in the Inspector. Its serialized settings are listed in the **Component data** table below. If a field is conditional, it appears only when the relevant mode/type is selected. If a field is a runtime state field (for example grounded or resolved velocity), treat it as read-only diagnostic state unless the API reference explicitly documents it as writable.

### How to read the settings

For every setting below, the documentation distinguishes **type**, **default**, **meaning**, and tuning direction where behavior is known. When a value represents a direction, use the engine's coordinate convention documented in [Coordinate system](../../reference/coordinate-system.html); do not substitute Unity/Godot conventions.

## Component data

| Field | Type | Purpose | Default |
| --- | --- | --- | --- |
| `jointType` | JointType2D enum: Fixed | Revolute | Prismatic | Rope | Spring | Fixed | Revolute | Prismatic | Rope | Spring. | `Revolute` |
| `connectedEntityId` | nullable value | null = jointed to a fixed point in the world instead of another body. | `null` |
| `anchor1X` | number | Local-space anchor points, in pixels — see class doc comment. | `0` |
| `anchor1Y` | number | Local anchor Y on this entity. | `0` |
| `anchor2X` | number | Local anchor X on the connected body/world anchor. | `0` |
| `anchor2Y` | number | Local anchor Y on the connected body/world anchor. | `0` |
| `axisX` | number | Prismatic only: slide axis, local to body1. | `1` |
| `axisY` | number | Prismatic axis Y. | `0` |
| `length` | number | Rope: total physical link-path length of the rope. | `100` |
| `stiffness` | number | Spring only. Note these are NOT the small "intuitive" values a spring might use in an SI/meters engine — Rapier computes spring force from anchor distance in METERS (via World.lengthUnit, see PhysicsWorld.js's LENGTH\_UNIT\_PX\_PER\_METER = 100), so at this engine's pixel scale a rest-length-50px displacement is only… | `6000` |
| `damping` | number | Spring damping. | `18` |
| `flexibility` | number | Revolute only: how freely the connected body may rotate. | `100` |
| `segmentCount` | number | Flexible Rope/Spring physical structure. | `18` |
| `ropeMass` | number | Mass per rope/spring segment. | `0.5` |
| `visualEnabled` | boolean | Runtime rope/string visualization. | `true` |
| `visualColor` | hex color string | Joint/rope visual color. | `#c8a66a` |
| `visualThickness` | number | Visual thickness. | `3` |
| `useTexture` | boolean | Optional image texture running along the rope/string instead of a flat color line — same texture/mode vocabulary as StrokePath (see runtime/components/StrokePath.js), so anyone who has textured a StrokePath already recognizes these fields. | `false` |
| `textureKey` | nullable value | Texture asset key. | `null` |
| `textureMode` | string | "stretch": the whole image is squeezed/stretched to fit the rope's current length end-to-end — warps as the rope swings and its chord length changes. | `stretch` |
| `textureTiling` | number | Tiling length. | `32` |
| `textureScale` | number | Texture scale. | `1` |
| `textureOffset` | number | Texture offset. | `0` |
| `textureFlip` | boolean | Flip texture. | `false` |
| `limitsEnabled` | boolean | Revolute + Prismatic: optional min/max limit on the joint's one free coordinate (degrees for Revolute, pixels for Prismatic). | `false` |
| `limitMin` | number | Minimum limit. | `-45` |
| `limitMax` | number | Maximum limit. | `45` |
| `motorEnabled` | boolean | Revolute + Prismatic: optional motor driving that same free coordinate. | `false` |
| `motorSpeed` | number | Motor target speed. | `0` |
| `motorMaxForce` | number | Maximum motor force. | `0` |
| `jointDrag` | number | Revolute-only passive rotational response. | `0` |
| `restStiffness` | number | Inspector field stored on this component. | `0` |
| `breakable` | boolean | Revolute-only structural failure. | `false` |
| `breakForce` | number | Inspector field stored on this component. | `10000` |
| `disableConnectedCollision` | boolean | When enabled, only this joint's two connected entities stop generating contact pairs with one another. | `false` |
| `collideConnected` | value | Legacy scene/script field. | `undefined` |
| `enabled` | boolean | Editor/gizmo convenience only — never read by PhysicsWorld. | `true` |

## Tuning behavior

These are the practical direction-of-change rules for the most important controls on this component.

| Setting | What changing it does |
| --- | --- |
| `length` | For Rope/Spring, higher length increases the rest/maximum link distance depending on the joint type. |
| `stiffness` | For Spring, higher values pull toward the rest length more strongly. |
| `damping` | Higher damping reduces oscillation faster. |
| `segmentCount` | Rope visual/solver subdivision count; higher can look smoother but costs more. |

## Breakable joints and drag

- `breakable` / `breakForce` (Revolute only): when the joint load exceeds `breakForce` the joint snaps apart. Script `joint.breakable` and `joint.breakForce`.
- `jointDrag` and `restStiffness` (Revolute only): drag/damping and the springiness that pulls the joint back to its rest pose.
- `disableConnectedCollision`: stop the two connected bodies from colliding with each other. It replaces the old `collideConnected` field, which is kept only for loading older projects.

> **Script API note::** JointAPI currently lists flexibility in its proxy allow-list, but the script object has no getter or setter for it. Reading it returns undefined , and writing it does not change the component. Set Flexibility (%) in the Inspector.

## Script API

| Member | Kind | Description |
| --- | --- | --- |
| `anchor1` | Property (read/write) | {x,y} local anchor on this body. |
| `anchor2` | Property (read/write) | {x,y} local anchor on connected body/world anchor. |
| `axis` | Property (read/write) | The `this.joint` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `breakForce` | Property (read/write) | Exposed by this script module. |
| `breakable` | Property (read/write) | The `this.joint` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `collideConnected` | Property (read/write) | Collision between connected bodies. |
| `connectedEntity` | Property (read/write) | Connected entity context, when one exists. |
| `damping` | Property (read/write) | Spring damping. |
| `disableConnectedCollision` | Property (read/write) | Exposed by this script module. |
| `enabled` | Property (read/write) | The `this.joint` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `flexibility` | Allow-listed but not implemented | The JointAPI allow-list contains this name, but no getter or setter is implemented. Reads return undefined and writes do not update Joint2D.flexibility. Set Flexibility (%) in the Inspector instead. |
| `jointDrag` | Property (read/write) | The `this.joint` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `jointType` | Property (read/write) | Joint type. |
| `length` | Property (read/write) | The `this.joint` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `limitMax` | Property (read/write) | Maximum limit. |
| `limitMin` | Property (read/write) | Minimum limit. |
| `limitsEnabled` | Property (read/write) | The `this.joint` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `motorEnabled` | Property (read/write) | The `this.joint` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `motorMaxForce` | Property (read/write) | Maximum motor force. |
| `motorSpeed` | Property (read/write) | Motor speed. |
| `restStiffness` | Property (read/write) | The `this.joint` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `ropeMass` | Property (read/write) | Rope/spring segment mass. |
| `segmentCount` | Property (read/write) | The `this.joint` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `stiffness` | Property (read/write) | The `this.joint` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `textureFlip` | Property (read/write) | The `this.joint` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `textureKey` | Property (read/write) | The `this.joint` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `textureMode` | Property (read/write) | The `this.joint` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `textureOffset` | Property (read/write) | The `this.joint` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `textureScale` | Property (read/write) | The `this.joint` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `textureTiling` | Property (read/write) | The `this.joint` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `useTexture` | Property (read/write) | The `this.joint` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `visualColor` | Property (read/write) | Visual color. |
| `visualEnabled` | Property (read/write) | Visual enabled. |
| `visualThickness` | Property (read/write) | Visual thickness. |

## Examples

```
this.joint.connectedEntity = findFirst("Target");
```

```
this.joint.jointType = "Spring";
```

> **Need the full workflow?:** Components: complete workflow covers adding, configuring, testing, combining, and removing components.
