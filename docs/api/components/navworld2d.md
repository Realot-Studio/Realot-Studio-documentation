# NavWorld2D

> Realot Studio NavWorld2D component reference: fields, script API, behavior and examples.

- Source: https://realot-studio.pages.dev/docs/api/components/navworld2d.html

> **Scope:** This page documents the NavWorld2D component in Realot Studio. Runtime fields are serialized scene data; the Script API section lists only members intentionally exposed to game scripts.

> **Where to find it in the editor:** Top GameObject → 2D Object → Nav World 2D. Once present, toolbar U/I/O brushes and Bounds/Cells view controls appear. Configure named areas with Edit → Nav Areas….

## What it does

Shared navigation world for baked or dynamic 2D pathfinding, with 16 navigation areas.

> **Component setup & editor tools:** NavWorld2D owns the navigation world/bake configuration used by NavAgent2D and the navigation API.

## How to add and use NavWorld2D

**Editor path:** Select the target entity in the **Hierarchy** (left side) → look at the **Inspector** (right side) → click **Add Component** at the bottom of the Inspector → search for **NavWorld2D** → click the component row. The Add Component picker is a centered modal with a search box; it only lists components not already attached.

For components with a dedicated editor tool, the tool is opened or activated from the location described below. Do not assume that adding the component alone activates its editor; some systems require a separate window, panel, or viewport tool.

## Component setup & editor tools

- Select/create an entity → Inspector → Add Component → Nav World 2D. Use the Navigation toolbar and Edit → Nav Areas… controls to define/bake the navigation world; then connect agents to it through the documented navigation workflow.

### What you should see after adding it

The component appears as its own section in the Inspector. Its serialized settings are listed in the **Component data** table below. If a field is conditional, it appears only when the relevant mode/type is selected. If a field is a runtime state field (for example grounded or resolved velocity), treat it as read-only diagnostic state unless the API reference explicitly documents it as writable.

### How to read the settings

For every setting below, the documentation distinguishes **type**, **default**, **meaning**, and tuning direction where behavior is known. When a value represents a direction, use the engine's coordinate convention documented in [Coordinate system](../../reference/coordinate-system.html); do not substitute Unity/Godot conventions.

## Component data

| Field | Type | Purpose | Default |
| --- | --- | --- | --- |
| `boundsX` | number | World-space bounds X. | `-400` |
| `boundsY` | number | World-space bounds Y. | `-400` |
| `boundsWidth` | number | Bounds width. | `800` |
| `boundsHeight` | number | Bounds height. | `800` |
| `cellSize` | number | Navigation cell size. | `32` |
| `cells` | object | Authored filled cells. | `{}` |
| `bakedCells` | nullable value | Derived baked representation. | `null` |
| `paintOverrides` | object | Explicit walkability overrides. | `{}` |
| `cellAreas` | object | Per-cell navigation area bitmask (one bit per NAV\_AREA\_COUNT slot). | `{}` |
| `areaCosts` | nullable value | Per-area traversal cost multiplier, index-aligned with the 16 area slots (see editor/state/NavAreas.js) — same role as Unity's NavMeshAgent.SetAreaCost(): a SOFT preference, not a hard block. | `null` |
| `allowDiagonal` | boolean | Allow diagonal A\* connections. | `false` |
| `dynamic` | boolean | Rebuild from dynamic scene obstacles. | `false` |
| `minObstacleFootprint` | number | Smallest obstacle footprint (world units, along its narrower axis) that is still allowed to block a cell during bakeNavWorld(). | `0` |

## Tuning behavior

These are the practical direction-of-change rules for the most important controls on this component.

| Setting | What changing it does |
| --- | --- |
| `cellSize` | Smaller cells give a finer grid and can represent narrower corridors, but increase navigation work/memory. |
| `allowDiagonal` | Off means 4-neighbor movement; on adds diagonal connections. |
| `dynamic` | When enabled, navigation can be rebuilt dynamically from current geometry; use only when runtime rebaking is actually needed. |
| `areaCosts` | 1 means neutral cost; 3 makes an allowed area approximately three times as expensive to traverse. Cost is preference, not a hard exclusion. |

## Script API

| Member | Kind | Description |
| --- | --- | --- |
| `nav.findPath()` | Global | Find world-space path through a NavWorld2D. |
| `nav.isWalkable()` | Global | Check a world-space point. |
| `nav.bake()` | Global | Bake navigation data after authored changes. |
| `nav.areaIndex` | Property | Current/selected navigation area index surface. |
| `nav.areaMask` | Property | Navigation area mask. |
| `nav.areaCosts` | Property | Navigation area costs. |

## Notes & behavior

- NavWorld2D is a scene component; there is no `this.navWorld` object. Scripts use the global `nav` module.

> **Need the full workflow?:** Components: complete workflow covers adding, configuring, testing, combining, and removing components.
