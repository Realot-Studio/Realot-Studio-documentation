# Editor controls & exact locations

> Exact Realot Studio UI paths, panel positions, keyboard shortcuts, conditional tools, and where feature-specific buttons live.

- Source: https://realot-studio.pages.dev/docs/editor/controls.html

> **Navigation rule:** This page is an index, not a substitute for feature docs. Each feature page also states the exact control path needed to perform its workflow.

## Editor layout

| Region | Location | What it contains |
| --- | --- | --- |
| Top toolbar | Across the top | File, Edit, GameObject, UI, Window; transform/navigation tools; Play/Pause; Export; Hub. |
| Hierarchy | Left, fixed-width column (~213px) | Current scene entity tree, search, folders, selection and add shortcuts. |
| Viewport | Center | Scene/Game tabs, viewport toolbar, canvas and editor gizmos. |
| Inspector | Right, fixed-width column (~255px) | Selected entity name/tag, components, property fields, Add Component and feature-specific buttons. |
| Bottom panel | Bottom edge | Project and Console tabs; scenes, sprites, audio, scripts, prefabs and runtime/editor logs. |

## Top menu paths

| Path | Open by clicking | Available commands |
| --- | --- | --- |
| File | File | Save Now / Saved, Save Project, Optimize Assets on Save, Load Project…, Export…, Extra Backup Storage, Restore from Backup Folder. |
| Edit | Edit | Physics Layers… and Nav Areas…. |
| Window | Window | Hierarchy, Asset Panel and Inspector show/hide checkboxes; Show All Panels while any panel is hidden. See [Editor settings & performance](settings.html). |
| GameObject | GameObject | Empty GameObject, Light, 2D Object, Shape. |
| UI | UI | Text, Speech Bubble, Chat Log, Message Input, Joystick. |
| GameObject → Light | GameObject → Light | Directional Light, Point Light, Spot Light, Area Light, God Rays, Freeform Light. |
| GameObject → 2D Object | GameObject → 2D Object | Tileset, Tilemap, Nav World 2D, Stroke Path. |
| GameObject → Shape | GameObject → Shape | Square, Circle, Capsule, Triangle. |

## Toolbar tools and shortcuts

| Key | Tool | When visible | Exact behavior |
| --- | --- | --- | --- |
| Q | Hand / Pan | Always | Drag to pan; scroll to zoom. |
| W | Translate | Always | Move selected entity with transform gizmo. |
| E | Rotate | Always | Rotate selected entity. |
| R | Scale | Always | Scale selected entity. |
| T | Tile | When a Tilemap or Tileset exists | Paint tile cells. |
| Y | Erase | When a Tilemap or a Nav World 2D exists | Erase tiles / relevant paint data. |
| P | Path | When a Stroke Path exists | Append/move/insert path points. |
| U | Nav paint walkable | When a Nav World 2D exists | Click = walkable; Alt-click = clear override. |
| I | Nav paint blocked | When a Nav World 2D exists | Click = blocked; Alt-click = clear override. |
| O | Nav area paint | When a Nav World 2D exists | Click = assign selected area; Alt-click = clear area. |

## Selection, history and playback shortcuts

These global shortcuts are ignored while you type in a text field, while the Script Editor is open, and while the Export window is open. Ctrl is Cmd on macOS.

| Shortcut | Action | Notes |
| --- | --- | --- |
| Delete / Backspace | Delete the selected entities | Requires a selection. |
| Ctrl+C | Copy selection | Yields to normal text copy when text is selected on the page. |
| Ctrl+V | Paste |  |
| Ctrl+D | Duplicate selection | Copy + paste in one step. |
| Ctrl+Z | Undo | Scene edits and Animation-editor edits keep separate histories; undo acts on whichever editor is active. Up to 100 steps. |
| Ctrl+Shift+Z or Ctrl+Y | Redo |  |
| Space | Toggle Play | Opens or closes the Play window. |

## Conditional controls

Some controls intentionally do not exist until the related scene object exists. This is important when documenting or generating instructions: do not tell users to click a hidden tool before creating the required object.

| Control | Condition |
| --- | --- |
| Tile (T) | A Tilemap or Tileset exists in the current world. |
| Erase (Y) | A Tilemap or a Nav World 2D exists (a Tileset alone does not enable it). |
| Path (P) | A Stroke Path exists. |
| U / I / O Nav brushes | A Nav World 2D exists. |
| Nav bounds/cells view | A Nav World 2D exists. |
| Paint Area selector | Nav Area tool O is active and named areas exist. |
