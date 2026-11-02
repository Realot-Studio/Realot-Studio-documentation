# Source map & verification

> A source-grounded map of where Realot Studio’s public behavior and editor controls are actually implemented.

- Source: https://realot-studio.pages.dev/docs/reference/source-map.html

> **Verified source:** This documentation pass was checked against the supplied Realot Studio engine source, including runtime components, scripting API modules, editor panels/state, navigation, physics, scene serialization, and export code.

## Engine architecture map

| Area | Primary source locations | Purpose |
| --- | --- | --- |
| Public runtime entry | `project/runtime/index.js` | Wires World + systems + scripting and exposes createGame(). |
| Components | `project/runtime/components/` | Serializable component data used by scene entities. |
| Systems | `project/runtime/systems/` | Runtime behavior such as physics, rendering, animation, lighting, audio, navigation and scripting. |
| Scripting | `project/runtime/scripting/` | User-facing script surface, EntityContext and option metadata. |
| Physics | `project/runtime/physics/` | Rapier-backed collider/body/joint queries and contact behavior. |
| Navigation | `project/runtime/pathfinding/` | A\* grid bake, dynamic bake, area masks/costs and navigation support. |
| Editor UI | `project/editor/panels/` | Toolbar, Hierarchy, Inspector, Project/Console, animation, tileset, export and settings windows. |
| Editor state/events | `project/editor/state/` | Persistence, dirty state, layer/area registries and DOM event handling. |
| Scene serialization | `project/runtime/scene/SceneSerializer.js` | Serialized scene/entity component format. |

## Important source files for documentation truth

| Question | Verify here |
| --- | --- |
| What components exist? | `project/runtime/components/*.js` |
| What script members exist? | `project/runtime/scripting/components/*API.js` + `ScriptAPI.js` |
| What opts are accepted? | `project/runtime/scripting/NavAPI.js` and the relevant ScriptAPI doc comments |
| Where is a button? | `project/editor/panels/*.js` |
| What appears only conditionally? | `project/editor/panels/Toolbar.js` + `editor/state/EditorEvents.js` |
| How does an interaction actually behave? | Relevant runtime system + component + tests in the same area. |
