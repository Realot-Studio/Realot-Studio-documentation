# Camera

> Realot Studio Camera component reference: fields, script API, behavior and examples.

- Source: https://realot-studio.pages.dev/docs/api/components/camera.html

> **Scope:** This page documents the Camera component in Realot Studio. Runtime fields are serialized scene data; the Script API section lists only members intentionally exposed to game scripts.

> **Where to find it in the editor:** Inspector → Add Component → Camera. Main camera and scaling/presentation settings are edited in the Inspector; Play/Export use the same runtime camera path.

## What it does

Orthographic 2D camera with reference resolutions, responsive scaling, follow, shake and optional pseudo-3D sprite depth scaling.

> **Component setup & editor tools:** Camera controls the 2D view and rendering/scaling behavior. The Scene viewport exposes a camera gizmo when a Camera entity is selected.

## How to add and use Camera

**Editor path:** Select the target entity in the **Hierarchy** (left side) → look at the **Inspector** (right side) → click **Add Component** at the bottom of the Inspector → search for **Camera** → click the component row. The Add Component picker is a centered modal with a search box; it only lists components not already attached.

For components with a dedicated editor tool, the tool is opened or activated from the location described below. Do not assume that adding the component alone activates its editor; some systems require a separate window, panel, or viewport tool.

## Component setup & editor tools

- Select the Camera entity → Inspector → Camera. The Camera gizmo appears in the Scene viewport. Mark the intended camera as Main and configure projection/scaling/aspect settings in the Inspector.

### What you should see after adding it

The component appears as its own section in the Inspector. Its serialized settings are listed in the **Component data** table below. If a field is conditional, it appears only when the relevant mode/type is selected. If a field is a runtime state field (for example grounded or resolved velocity), treat it as read-only diagnostic state unless the API reference explicitly documents it as writable.

### How to read the settings

For every setting below, the documentation distinguishes **type**, **default**, **meaning**, and tuning direction where behavior is known. When a value represents a direction, use the engine's coordinate convention documented in [Coordinate system](../../reference/coordinate-system.html); do not substitute Unity/Godot conventions.

## Component data

| Field | Type | Purpose | Default |
| --- | --- | --- | --- |
| `backgroundColor` | hex color string | Background color. | `#314D79` |
| `projection` | string | Projection mode. | `Orthographic` |
| `size` | number | Orthographic camera size. | `5` |
| `nearClip` | number | Near clip. | `0.3` |
| `farClip` | number | Far clip. | `1000` |
| `isMain` | boolean | Whether this is the main camera. | `false` |
| `aspectMode` | CameraAspectMode enum: Landscape | Portrait | Square | Custom | Landscape | Portrait | Square | Custom. | `Landscape` |
| `landscapeWidth` | number | Landscape reference width. | `960` |
| `landscapeHeight` | number | Landscape reference height. | `540` |
| `portraitWidth` | number | Portrait reference width. | `540` |
| `portraitHeight` | number | Portrait reference height. | `960` |
| `squareSize` | number | Square reference size. | `720` |
| `customWidth` | number | Custom width. | `800` |
| `customHeight` | number | Custom height. | `600` |
| `enablePseudo3D` | boolean | Use Transform.z for sprite depth scaling. | `false` |
| `renderToSpriteEntityId` | nullable value | Inspector field stored on this component. | `null` |
| `scalingMode` | ScalingMode enum: Expand | Fit | Fill | Stretch | ── Screen scaling (device-fit) settings ────────────────────── See the ScalingMode doc comment above and computeScreenFit() in CameraUtils.js for the full picture. | `Fit` |
| `keepHeight` | boolean | EXPAND-only. true = the reference HEIGHT is what's kept exact (matches Unity's Canvas Scaler "Match: Height" — width is the axis that expands/contracts to reveal more or less of the world). | `true` |
| `aspectRatioLock` | boolean | Safety override for EXPAND specifically: Expand's whole purpose is to let the effective aspect ratio drift to match the device (showing more/less world). | `true` |
| `allowStretching` | boolean | Safety override for STRETCH specifically: false (default) downgrades Stretch to behave like Fit instead, so a scalingMode accidentally left on "Stretch" can never actually distort the picture. | `false` |
| `letterboxing` | string | Horizontal bars (top/bottom) — shown when Fit (or a mode downgraded to Fit above) leaves vertical space unused. | `Auto` |
| `pillarboxing` | string | Same as letterboxing but for vertical bars (left/right), shown when horizontal space is left over. | `Auto` |
| `barColor` | hex color string | Color painted into letterbox/pillarbox bars when they're shown. | `#000000` |
| `integerScaling` | boolean | Rounds the computed scale down to the nearest whole integer (never below 1x) before applying it — keeps pixel-art crisp instead of blurry/uneven at fractional scales. | `false` |

## Tuning behavior

These are the practical direction-of-change rules for the most important controls on this component.

| Setting | What changing it does |
| --- | --- |
| `size / zoom` | For this 2D camera, larger effective view size shows more world; increasing zoom makes the scene appear smaller/farther, while reducing it magnifies the world. |
| `scalingMode` | FIT preserves the reference aspect and uses bars when necessary; FILL crops to fill; STRETCH changes aspect; EXPAND keeps the reference height and reveals more/less horizontal world. |
| `integerScaling` | When enabled, device-fit scale is constrained toward integer multiples to keep pixel-art rendering crisp. |

## Script API

| Member | Kind | Description |
| --- | --- | --- |
| `allowStretching` | Property (read/write) | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `aspectMode` | Property (read/write) | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `aspectRatioLock` | Property (read/write) | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `backgroundColor` | Property (read/write) | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `barColor` | Property (read/write) | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `customHeight` | Property (read/write) | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `customWidth` | Property (read/write) | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `enablePseudo3D` | Property (read/write) | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `follow(entityTarget, opts)` | Method | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `integerScaling` | Property (read/write) | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `keepHeight` | Property (read/write) | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `landscapeHeight` | Property (read/write) | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `landscapeWidth` | Property (read/write) | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `letterboxing` | Property (read/write) | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `offsetX` | Property (read/write) | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `offsetY` | Property (read/write) | Follow/render Y offset. |
| `pillarboxing` | Property (read/write) | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `portraitHeight` | Property (read/write) | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `portraitWidth` | Property (read/write) | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `renderToSprite(spriteEntity)` | Method | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `scalingMode` | Property (read/write) | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `shake(intensity, duration)` | Method | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `squareSize` | Property (read/write) | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `stopFollow()` | Method | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `x` | Property (read/write) | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `y` | Property (read/write) | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `zoom` | Property (read/write) | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |

## Examples

```
var cam = findFirst("Main Camera");
```

```
cam.camera.follow(findFirst("Target"), { smoothing: 0.1 });
```

> **Need the full workflow?:** Components: complete workflow covers adding, configuring, testing, combining, and removing components.
