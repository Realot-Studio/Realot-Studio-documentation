# Hierarchy & Inspector

> Organize the current scene and edit entities/components with stable serialized data.

- Source: https://realot-studio.pages.dev/docs/editor/hierarchy-inspector.html

> **Exact control path:** Select the entity in the left Hierarchy panel or click it in the center Scene view. Its properties appear immediately in the right Inspector . The Add Component button is at the bottom of the Inspector’s component list; use its search field to find a component by name.

## Hierarchy

The Hierarchy shows only entities that belong to the active scene. Entities can also belong to hierarchy folders. The saved scene stores folders separately so folder IDs remain stable across save/load.

## Inspector

The Inspector edits the entity name, tag, active state, component properties and component-specific authoring fields. For many components, the Inspector exposes more authoring fields than the runtime script API intentionally does.

## Gizmos and shapes

Spatial editing uses scene-view gizmos for things such as triangle collider/shape points and other editable geometry. Treat these as authoring controls; scripts should use the documented component APIs instead of manipulating editor gizmo state.
