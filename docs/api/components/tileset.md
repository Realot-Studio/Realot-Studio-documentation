# Tileset

> Realot Studio Tileset component reference: fields, script API, behavior and examples.

- Source: https://realot-studio.pages.dev/docs/api/components/tileset.html

> **Scope:** This page documents the Tileset component in Realot Studio. Runtime fields are serialized scene data; the Script API section lists only members intentionally exposed to game scripts.

> **Where to find it in the editor:** Top GameObject → 2D Object → Tileset, then open the Tileset Editor window from the Inspector. Import one auto-sliced 4×4 sheet or 16 role images.

## What it does

Defines a reusable 16-role autotile set. The editor can auto-slice one image or accept separate role images.

> **Component setup & editor tools:** Tileset stores tile definitions used by Tilemap and is edited through the Tileset panel.

## How to add and use Tileset

**Editor path:** Select the target entity in the **Hierarchy** (left side) → look at the **Inspector** (right side) → click **Add Component** at the bottom of the Inspector → search for **Tileset** → click the component row. The Add Component picker is a centered modal with a search box; it only lists components not already attached.

For components with a dedicated editor tool, the tool is opened or activated from the location described below. Do not assume that adding the component alone activates its editor; some systems require a separate window, panel, or viewport tool.

## Component setup & editor tools

- Select/create a Tileset entity → Inspector → Add Component → Tileset → open the Tileset panel. Define tile data there, then assign/use the Tileset from a Tilemap.

### What you should see after adding it

The component appears as its own section in the Inspector. Its serialized settings are listed in the **Component data** table below. If a field is conditional, it appears only when the relevant mode/type is selected. If a field is a runtime state field (for example grounded or resolved velocity), treat it as read-only diagnostic state unless the API reference explicitly documents it as writable.

### How to read the settings

For every setting below, the documentation distinguishes **type**, **default**, **meaning**, and tuning direction where behavior is known. When a value represents a direction, use the engine's coordinate convention documented in [Coordinate system](../../reference/coordinate-system.html); do not substitute Unity/Godot conventions.

## Component data

| Field | Type | Purpose | Default |
| --- | --- | --- | --- |
| `name` | string | Tileset display name. | `New Tileset` |
| `tileWidth` | number | Tile width in pixels/world units. | `32` |
| `tileHeight` | number | Tile height. | `32` |
| `slots` | object | @type {Record<string, string|null>} role name -> spriteKey (or null if that slot hasn't been filled in yet). | `{}` |

## Autotile roles

| Slot | Role | Meaning |
| --- | --- | --- |
| 1 | `cornerTL` | Canonical role slot |
| 2 | `edgeT` | Canonical role slot |
| 3 | `cornerTR` | Canonical role slot |
| 4 | `stubT` | Canonical role slot |
| 5 | `edgeL` | Canonical role slot |
| 6 | `center` | Canonical role slot |
| 7 | `edgeR` | Canonical role slot |
| 8 | `lineV` | Canonical role slot |
| 9 | `cornerBL` | Canonical role slot |
| 10 | `edgeB` | Canonical role slot |
| 11 | `cornerBR` | Canonical role slot |
| 12 | `stubB` | Canonical role slot |
| 13 | `stubL` | Canonical role slot |
| 14 | `lineH` | Canonical role slot |
| 15 | `stubR` | Canonical role slot |
| 16 | `single` | Canonical role slot |

## Notes & behavior

- Autotile selection is computed from the four orthogonal neighbors; the stored Tilemap data is the filled-cell set, not a baked per-cell sprite choice.

> **Need the full workflow?:** Components: complete workflow covers adding, configuring, testing, combining, and removing components.
