# Tilemaps & tilesets

> Author sparse tile grids and 16-role autotile tilesets.

- Source: https://realot-studio.pages.dev/docs/editor/tilemaps.html

> **Exact control path:** Create a reusable tileset via GameObject → 2D Object → Tileset and the tile grid via GameObject → 2D Object → Tilemap . Once present, T selects tile painting and Y selects erase. The Tileset Editor exposes the 4×4 role grid and import actions.

## Tileset authoring

The editor can take one image and auto-slice it into a 4×4 role grid, or accept up to 16 separate role images. The stored result is sixteen role-to-sprite-key mappings.

## The 16 roles

The canonical order is `cornerTL, edgeT, cornerTR, stubT, edgeL, center, edgeR, lineV, cornerBL, edgeB, cornerBR, stubB, stubL, lineH, stubR, single`.

## Tilemap data

A Tilemap references a Tileset by entity ID and stores a sparse set of filled cells keyed as `col,row`. The runtime computes the visual tile role from orthogonal neighbors; it does not store the final role per cell.

## Scripting

> **No direct Tilemap script module:** Tilemap/Tileset are editor/scene-data components. There is currently no documented this.tilemap runtime API.
