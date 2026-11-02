# Tilemap

> Realot Studio Tilemap component reference: fields, script API, behavior and examples.

- Source: https://realot-studio.pages.dev/docs/api/components/tilemap.html

> **Scope:** This page documents the Tilemap component in Realot Studio. Runtime fields are serialized scene data; the Script API section lists only members intentionally exposed to game scripts.

> **Where to find it in the editor:** Top GameObject → 2D Object → Tilemap. Assign a Tileset entity in the Inspector; T and Y tools appear when a Tilemap/Tileset exists.

## What it does

Sparse painted tile grid that references a Tileset entity by ID.

> **Component setup & editor tools:** Tilemap paints a tile grid and exposes tilemap-specific viewport/panel tools.

## How to add and use Tilemap

**Editor path:** Select the target entity in the **Hierarchy** (left side) → look at the **Inspector** (right side) → click **Add Component** at the bottom of the Inspector → search for **Tilemap** → click the component row. The Add Component picker is a centered modal with a search box; it only lists components not already attached.

For components with a dedicated editor tool, the tool is opened or activated from the location described below. Do not assume that adding the component alone activates its editor; some systems require a separate window, panel, or viewport tool.

## Component setup & editor tools

- Select/create a Tilemap entity → Inspector → Add Component → Tilemap. Use the Tilemap viewport/panel tools to paint the configured Tileset.

### What you should see after adding it

The component appears as its own section in the Inspector. Its serialized settings are listed in the **Component data** table below. If a field is conditional, it appears only when the relevant mode/type is selected. If a field is a runtime state field (for example grounded or resolved velocity), treat it as read-only diagnostic state unless the API reference explicitly documents it as writable.

### How to read the settings

For every setting below, the documentation distinguishes **type**, **default**, **meaning**, and tuning direction where behavior is known. When a value represents a direction, use the engine's coordinate convention documented in [Coordinate system](../../reference/coordinate-system.html); do not substitute Unity/Godot conventions.

## Component data

| Field | Type | Purpose | Default |
| --- | --- | --- | --- |
| `tilesetEntityId` | nullable value | @type {string|null} entity id of the Tileset-holding entity this tilemap paints with. | `null` |
| `cells` | object | @type {Record<string, true>} sparse map of "col,row" -> true for every painted cell. | `{}` |

## Notes & behavior

- Tilemap has no dedicated `this.tilemap` script API in the current engine. It is edited as scene data by the editor and rendered by TilemapSystem.
- Cells may use negative coordinates. The key format is `col,row`.

> **Need the full workflow?:** Components: complete workflow covers adding, configuring, testing, combining, and removing components.
