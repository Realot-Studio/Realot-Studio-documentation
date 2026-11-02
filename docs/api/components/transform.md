# Transform

> Realot Studio Transform component reference: fields, script API, behavior and examples.

- Source: https://realot-studio.pages.dev/docs/api/components/transform.html

> **Scope:** This page documents the Transform component in Realot Studio. Runtime fields are serialized scene data; the Script API section lists only members intentionally exposed to game scripts.

> **Where to find it in the editor:** Inspector (right side) → Transform component, automatically present on every GameObject. Use W/E/R toolbar tools for scene manipulation.

## What it does

Position, rotation and scale. Every spatial entity uses a Transform.

> **Component setup & editor tools:** Transform is automatically present on entities. Select an entity in the Hierarchy; its Transform section appears in the Inspector.

## How to add and use Transform

**Editor path:** Select the target entity in the **Hierarchy** (left side) → look at the **Inspector** (right side) → click **Add Component** at the bottom of the Inspector → search for **Transform** → click the component row. The Add Component picker is a centered modal with a search box; it only lists components not already attached.

For components with a dedicated editor tool, the tool is opened or activated from the location described below. Do not assume that adding the component alone activates its editor; some systems require a separate window, panel, or viewport tool.

## Component setup & editor tools

- Select an entity in the Hierarchy; edit Transform fields in the Inspector. Use the Scene viewport transform gizmo to move/rotate/scale visually.

### What you should see after adding it

The component appears as its own section in the Inspector. Its serialized settings are listed in the **Component data** table below. If a field is conditional, it appears only when the relevant mode/type is selected. If a field is a runtime state field (for example grounded or resolved velocity), treat it as read-only diagnostic state unless the API reference explicitly documents it as writable.

### How to read the settings

For every setting below, the documentation distinguishes **type**, **default**, **meaning**, and tuning direction where behavior is known. When a value represents a direction, use the engine's coordinate convention documented in [Coordinate system](../../reference/coordinate-system.html); do not substitute Unity/Godot conventions.

## Component data

| Field | Type | Purpose | Default |
| --- | --- | --- | --- |
| `x` | number | World position X. | `0` |
| `y` | number | World position Y. | `0` |
| `z` | number | Pseudo-3D depth; affects sprite scale only when Camera.enablePseudo3D is enabled. | `0` |
| `rotation` | number | Rotation in degrees around Z. | `0` |
| `scaleX` | number | Horizontal scale multiplier. | `1` |
| `scaleY` | number | Vertical scale multiplier. | `1` |

## Tuning behavior

These are the practical direction-of-change rules for the most important controls on this component.

| Setting | What changing it does |
| --- | --- |
| `x / y` | World position. Increasing X moves right; increasing Y moves down in the engine’s 2D world convention. |
| `rotation` | Degrees clockwise visually in the screen coordinate convention; 0 points along +X for directional/spot light orientation. |
| `scaleX / scaleY` | 1 is native scale; >1 enlarges; 0.5 halves size; negative values mirror the corresponding axis. |

## Script API

| Member | Kind | Description |
| --- | --- | --- |
| `lookAt(x, y)` | Method | Point the entity toward a world-space point. |
| `position` | Property (read/write) | { x, y } world-space position; read or assign. |
| `rotation` | Property (read/write) | Rotation in degrees. |
| `scale` | Property (read/write) | Exposed by this script module. |
| `translate(dx, dy)` | Method | Move by a delta amount. |

## Examples

```
this.position = { x: 200, y: 120 };
```

```
this.rotation = 45;
```

```
this.translate(50 * time.deltaTime, 0);
```

> **Need the full workflow?:** Components: complete workflow covers adding, configuring, testing, combining, and removing components.
