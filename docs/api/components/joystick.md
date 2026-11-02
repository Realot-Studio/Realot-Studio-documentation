# Joystick

> Realot Studio Joystick component reference: fields, script API, behavior and examples.

- Source: https://realot-studio.pages.dev/docs/api/components/joystick.html

> **Scope:** This page documents the Joystick component in Realot Studio. Runtime fields are serialized scene data; the Script API section lists only members intentionally exposed to game scripts.

> **Where to find it in the editor:** Top UI → Joystick, or Inspector → Add Component → Joystick.

## What it does

Virtual touch joystick for mobile and pointer-driven control schemes.

> **Component setup & editor tools:** Joystick provides a touch/drag virtual control for mobile-oriented input.

## How to add and use Joystick

**Editor path:** Select the target entity in the **Hierarchy** (left side) → look at the **Inspector** (right side) → click **Add Component** at the bottom of the Inspector → search for **Joystick** → click the component row. The Add Component picker is a centered modal with a search box; it only lists components not already attached.

For components with a dedicated editor tool, the tool is opened or activated from the location described below. Do not assume that adding the component alone activates its editor; some systems require a separate window, panel, or viewport tool.

## Component setup & editor tools

- GameObject → UI → Joystick creates a joystick entity. You can also select an entity → Inspector → Add Component → Joystick.

### What you should see after adding it

The component appears as its own section in the Inspector. Its serialized settings are listed in the **Component data** table below. If a field is conditional, it appears only when the relevant mode/type is selected. If a field is a runtime state field (for example grounded or resolved velocity), treat it as read-only diagnostic state unless the API reference explicitly documents it as writable.

### How to read the settings

For every setting below, the documentation distinguishes **type**, **default**, **meaning**, and tuning direction where behavior is known. When a value represents a direction, use the engine's coordinate convention documented in [Coordinate system](../../reference/coordinate-system.html); do not substitute Unity/Godot conventions.

## Component data

| Field | Type | Purpose | Default |
| --- | --- | --- | --- |
| `positionMode` | JoystickPositionMode enum: Fixed | Dynamic | Fixed or pointer-positioned joystick. | `Fixed` |
| `regionX` | number | Dynamic-mode touch region — the screen-space rectangle (in the same pixel convention Transform.x/y already use for screen-space UI, see TextInput.js's file header) that a press must land inside to claim this joystick. | `0` |
| `regionY` | number | Region Y. | `0` |
| `regionWidth` | number | Region width. | `640` |
| `regionHeight` | number | Region height. | `720` |
| `baseRadius` | number | Visuals | `60` |
| `knobRadius` | number | Knob radius. | `28` |
| `baseColor` | hex color string | Base color. | `#ffffff` |
| `baseOpacity` | number | Base opacity. | `0.25` |
| `knobColor` | hex color string | Knob color. | `#ffffff` |
| `knobOpacity` | number | Knob opacity. | `0.6` |
| `outlineColor` | hex color string | Outline color. | `#ffffff` |
| `outlineWidth` | number | Outline width. | `2` |
| `deadZone` | number | Behavior 0-1: fraction of baseRadius the knob must move before x/y leaves 0 | `0.1` |
| `returnToCenter` | boolean | true = knob snaps back to center on release; false = holds last position | `true` |
| `hideWhenIdle` | boolean | true = invisible until actively being dragged (works in both position modes) | `false` |
| `idleOpacityMultiplier` | number | when hideWhenIdle is false, how much to dim the whole stick while not in use (1 = no dimming) | `0.35` |
| `x` | number | Live state — see the file header for why these live here rather than in JoystickSystem's private state. | `0` |
| `y` | number | -1..1, vertical knob offset (down = positive), after dead zone | `0` |
| `magnitude` | number | 0..1, distance of the knob from center after dead zone | `0` |
| `angle` | number | degrees, 0 = right, 90 = down (screen-space convention, matches Transform.rotation's clockwise-positive sense) | `0` |
| `active` | boolean | true while a finger/pointer is currently dragging this joystick | `false` |
| `baseScreenX` | number | current drawn base center, in screen px — equals Transform.x/y in Fixed mode, or the recentered touch point in Dynamic mode | `0` |
| `baseScreenY` | number | Inspector field stored on this component. | `0` |

## Tuning behavior

These are the practical direction-of-change rules for the most important controls on this component.

| Setting | What changing it does |
| --- | --- |
| `deadZone` | 0 means even tiny stick displacement is reported; increasing it keeps small movements at zero until the knob moves farther. |
| `baseRadius / knobRadius` | Larger values make the on-screen joystick physically larger. |
| `idleOpacityMultiplier` | Lower makes an idle joystick more transparent when hideWhenIdle is false. |
| `returnToCenter` | True snaps back on release; false preserves the last knob position. |

## Script API

| Member | Kind | Description |
| --- | --- | --- |
| `active` | Property (read-only) | The `this.joystick` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `angle` | Property (read-only) | The `this.joystick` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `baseColor` | Property (read/write) | Exposed by this script module. |
| `baseOpacity` | Property (read/write) | Exposed by this script module. |
| `baseRadius` | Property (read/write) | Base radius. |
| `deadZone` | Property (read/write) | The `this.joystick` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `hideWhenIdle` | Property (read/write) | The `this.joystick` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `idleOpacityMultiplier` | Property (read/write) | Exposed by this script module. |
| `knobColor` | Property (read/write) | Exposed by this script module. |
| `knobOpacity` | Property (read/write) | Exposed by this script module. |
| `knobRadius` | Property (read/write) | Knob radius. |
| `magnitude` | Property (read-only) | The `this.joystick` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `outlineColor` | Property (read/write) | Exposed by this script module. |
| `outlineWidth` | Property (read/write) | Exposed by this script module. |
| `positionMode` | Property (read/write) | Joystick positioning mode. |
| `regionHeight` | Property (read/write) | Region height. |
| `regionWidth` | Property (read/write) | Region width. |
| `regionX` | Property (read/write) | The `this.joystick` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `regionY` | Property (read/write) | Touch/pointer region Y. |
| `returnToCenter` | Property (read/write) | The `this.joystick` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `x` | Property (read-only) | The `this.joystick` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `y` | Property (read-only) | The `this.joystick` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |

## Examples

```
this.rigidbody.velocityX = this.joystick.x * 250;
```

> **Need the full workflow?:** Components: complete workflow covers adding, configuring, testing, combining, and removing components.
