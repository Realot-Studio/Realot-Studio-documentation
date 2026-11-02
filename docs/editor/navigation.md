# Navigation authoring

> Bake 2D navigation with NavWorld2D and configure NavAgent2D.

- Source: https://realot-studio.pages.dev/docs/editor/navigation.html

> **Exact control path:** Create the shared nav grid with GameObject → 2D Object → Nav World 2D . Then the top toolbar exposes U walkable, I blocked and O area paint tools. Brush −/+ controls sit directly beside those nav tools. Named areas are configured at Edit → Nav Areas… .

## NavWorld2D

A NavWorld2D defines world bounds, cell size and authored/baked cell data. It supports 16 navigation areas, per-area costs, optional diagonal traversal and optional dynamic rebuilding.

## Agents

NavAgent2D adds radius, speed, acceleration/deceleration, stopping distance, automatic repathing and avoidance. Vehicle-oriented settings are available for car-style navigation/steering.

## Script access

Scripts use the global `nav` module: `nav.findPath()`, `nav.isWalkable()` and `nav.bake()`. A NavAgent exposes its live `currentPath` and `currentPathIndex` as read-only script state.

## Pathfinding behavior

Path endpoints are snapped to the nearest walkable cell. Returned waypoints are world-space points with straight runs merged, but they are not geometrically smoothed.
