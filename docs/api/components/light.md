# Light

> Realot Studio Light component reference: fields, script API, behavior and examples.

- Source: https://realot-studio.pages.dev/docs/api/components/light.html

> **Scope:** This page documents the Light component in Realot Studio. Runtime fields are serialized scene data; the Script API section lists only members intentionally exposed to game scripts.

> **Where to find it in the editor:** Top GameObject → Light → Directional/Point/Spot/Area/God Rays/Freeform. Existing lights expose their settings in the Inspector.

## What it does

2D light source supporting Directional, Point, Spot, Area, GodRays and Freeform light shapes.

> **Component setup & editor tools:** Light adds the engine’s 2D lighting source and exposes a viewport gizmo for spatial editing.

## How to add and use Light

**Editor path:** Select the target entity in the **Hierarchy** (left side) → look at the **Inspector** (right side) → click **Add Component** at the bottom of the Inspector → search for **Light** → click the component row. The Add Component picker is a centered modal with a search box; it only lists components not already attached.

For components with a dedicated editor tool, the tool is opened or activated from the location described below. Do not assume that adding the component alone activates its editor; some systems require a separate window, panel, or viewport tool.

## Component setup & editor tools

- Select entity → Inspector → Add Component → Light. The Light gizmo appears in the Scene viewport; use it to position/edit freeform geometry where supported.

### What you should see after adding it

The component appears as its own section in the Inspector. Its serialized settings are listed in the **Component data** table below. If a field is conditional, it appears only when the relevant mode/type is selected. If a field is a runtime state field (for example grounded or resolved velocity), treat it as read-only diagnostic state unless the API reference explicitly documents it as writable.

### How to read the settings

For every setting below, the documentation distinguishes **type**, **default**, **meaning**, and tuning direction where behavior is known. When a value represents a direction, use the engine's coordinate convention documented in [Coordinate system](../../reference/coordinate-system.html); do not substitute Unity/Godot conventions.

## Component data

| Field | Type | Purpose | Default |
| --- | --- | --- | --- |
| `type` | LightType enum: Directional | Point | Spot | Area | GodRays | Freeform | Directional | Point | Spot | Area | GodRays | Freeform. | `Point` |
| `color` | hex color string | Light color. | `#ffffff` |
| `intensity` | number | Light intensity. | `1` |
| `radius` | number | Reach for Point/Spot/GodRays. | `200` |
| `angle` | number | Cone angle for Spot/GodRays. | `45` |
| `width` | number | Area-light width. | `200` |
| `height` | number | Area-light height. | `200` |
| `castsOnWorld` | boolean | Light the world. | `true` |
| `castShadows` | boolean | Cast shadows. | `false` |
| `shadowColor` | hex color string | Shadow color. | `#000000` |
| `shadowStrength` | number | Shadow strength. | `1` |
| `flicker` | boolean | Flicker enabled. | `false` |
| `flickerSpeed` | number | Flicker speed. | `8` |
| `flickerDuration` | number | Flicker duration. | `0` |
| `coreSize` | number | Visible light-core size. | `0.22` |
| `coreVisible` | boolean | Show visible light core. | `true` |
| `points` | nullable value | Freeform local polygon points. | `null` |

## Tuning behavior

These are the practical direction-of-change rules for the most important controls on this component.

| Setting | What changing it does |
| --- | --- |
| `intensity` | 0 is off; 1 is the normal baseline; >1 produces stronger/brighter illumination. |
| `radius` | Larger values extend point/spot/area reach. Smaller values concentrate the light. |
| `angle` | For Spot/God Rays, larger values widen the cone; 0 is very narrow. |
| `shadowStrength` | 0 removes visible shadow contribution; 1 gives full light-side shadow strength. |
| `flickerSpeed` | Higher = faster flicker cycles. |
| `flickerDuration` | 0 = indefinite flicker when enabled; positive values stop the flicker after that many seconds. |

## Script API

| Member | Kind | Description |
| --- | --- | --- |
| `angle` | Property (read/write) | The `this.light` sub-object exposed to user scripts on any entity that has a Light component. |
| `castShadows` | Property (read/write) | The `this.light` sub-object exposed to user scripts on any entity that has a Light component. |
| `castsOnWorld` | Property (read/write) | The `this.light` sub-object exposed to user scripts on any entity that has a Light component. |
| `color` | Property (read/write) | The `this.light` sub-object exposed to user scripts on any entity that has a Light component. |
| `coreSize` | Property (read/write) | Light core size. |
| `coreVisible` | Property (read/write) | Show light core. |
| `flicker` | Property (read/write) | Flicker toggle. |
| `flickerDuration` | Property (read/write) | Flicker duration. |
| `flickerSpeed` | Property (read/write) | Flicker speed. |
| `height` | Property (read/write) | The `this.light` sub-object exposed to user scripts on any entity that has a Light component. |
| `intensity` | Property (read/write) | The `this.light` sub-object exposed to user scripts on any entity that has a Light component. |
| `radius` | Property (read/write) | The `this.light` sub-object exposed to user scripts on any entity that has a Light component. |
| `shadowColor` | Property (read/write) | The `this.light` sub-object exposed to user scripts on any entity that has a Light component. |
| `shadowStrength` | Property (read/write) | The `this.light` sub-object exposed to user scripts on any entity that has a Light component. |
| `type` | Property (read/write) | The `this.light` sub-object exposed to user scripts on any entity that has a Light component. |
| `width` | Property (read/write) | The `this.light` sub-object exposed to user scripts on any entity that has a Light component. |

## Examples

```
this.light.intensity = 1.5;
```

```
this.light.castShadows = true;
```

> **Need the full workflow?:** Components: complete workflow covers adding, configuring, testing, combining, and removing components.
