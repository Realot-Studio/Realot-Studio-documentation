# Prefab workflow

> Create, place, edit, update, revert and unpack Realot Studio prefabs with the exact editor controls involved.

- Source: https://realot-studio.pages.dev/docs/editor/prefabs.html

> **What a prefab is:** In Realot Studio a prefab is a reusable one-entity template. Instances keep a prefabId and track field-level overrides. Updating a prefab can propagate the canonical data to other instances.

## Create a prefab

Select an entity in the Scene viewport or Hierarchy. In the right Inspector, use the small prefab/box action next to the entity name. The engine creates a prefab from that entity and links the source entity to it.

## Place an instance

Use the bottom Project panel → Prefabs folder. Drag a prefab asset into the center Scene viewport. The editor instantiates the template and places the new instance in the scene.

## Edit an instance

Change component values normally in the Inspector. Realot Studio records changed fields as prefab overrides for that instance.

## Update the prefab

When an instance is selected, the Inspector shows a blue Prefab strip. Optional Update Transform checkboxes control whether Position, Rotation, and Scale should also propagate to other instances. Click Update Prefab to make this instance the new canonical template.

## Revert / Unpack

| Inspector control | Effect |
| --- | --- |
| `Revert Prefab` | Discard the instance’s overrides and re-sync its values from the prefab. |
| `Unpack Prefab` | Detach this instance while keeping its current values. Future prefab updates no longer reach it. |

## Delete a prefab asset

Bottom Project → Prefabs. Use the asset delete control. Existing objects keep their current data but are no longer linked to the deleted prefab.

## Important implementation fact

Prefab data is stored in the project’s `prefabs.json` catalogue and is included by Save Project/import/export flows.
