# Editor settings and configuration

> Complete reference for the editor menus, panel visibility, physics layers, navigation areas, Inspector notes, saving preferences and performance defaults.

- Source: https://realot-studio.pages.dev/docs/editor/settings.html

## Where the settings are

Realot Studio does not currently have one large Settings window. Options are placed beside the editor feature they control: use **File** for project storage and export, **Edit** for physics and navigation labels, and **Window** for panel visibility. Component-specific settings live in the Inspector and are documented on each [component reference page](../api/index.html).

## File menu

| Menu item | What it does | Availability / notes |
| --- | --- | --- |
| **Save Now / Saved** | Immediately saves the open Hub project to its browser autosave storage. The label shows whether there are unsaved changes. | Shown when the project was opened with a Hub autosave slot. |
| **Save Project** | Downloads a portable `.realot` project archive. When editing a supported file handle, the label can become *Save to [filename]*. | Available for project export to a local file. |
| **Auto-update file: ON / OFF** | Controls whether changes are automatically written back to the opened project file. | Only shown when a supported file handle is active. This is local file writing, not cloud sync. |
| **Save as copy (download)** | Downloads a separate copy without replacing the current file. | Shown when a file handle exists or the browser supports the Save File Picker. |
| **Optimize Assets on Save: ON / OFF** | Arms an optimization pass for the next Save Project operation. When enabled, supported PNG images are losslessly optimized and WAV audio is repacked before the archive is written. | Toggle does not save immediately; the next Save Project action performs the work. |
| **Load Project…** | Opens a saved Realot project file. | Choose a `.realot` project. Loading a project containing scripts asks for confirmation because scripts execute as page code. Loading a project containing scripts asks for confirmation because scripts execute as page code. |
| **Export…** | Opens the standalone game export window. | See [Export window](../export/export-window.html) and [Android APK](../export/android.html). |
| **Enable Extra Backup Storage…** | Lets you select a local folder for mirrored project autosaves, outside the browser's normal storage quota. | Requires browser support for the File System Access API and user permission. |
| **Extra Backup Storage: ON** | Turns off future mirroring to the selected folder. | Does not delete files already written to that folder. |
| **Restore from Backup Folder…** | Restores the most recent project snapshot mirrored to the selected folder. | Only shown while extra backup storage is enabled for the project. |

## Edit menu

| Menu item | What it configures |
| --- | --- |
| **Physics Layers…** | Opens the 16-slot physics layer-name editor. Slot 0 starts as `Default` and cannot be cleared, though it can be renamed. Slots 1–15 can be named or left blank. These names are labels for the fixed runtime layer indices used by Collider2D layer/mask filtering and physics queries. |
| **Nav Areas…** | Opens the 16-slot navigation-area name editor. Slot 0 starts as `Ground` and cannot be cleared; slot 1 starts as `Water`; slots 2–15 are initially blank. Names can be changed or cleared except for slot 0. The slot indices are stored in navigation cells and NavAgent2D area masks. |

Physics-layer and navigation-area names are saved with project data. The indices—not the text labels—are what collision filtering and pathfinding use at runtime. Renaming an existing slot does not move its contents to another index.

## Project tags

Use the selected entity's **Tag** dropdown in the Inspector to assign a tag. The initial list contains `Untagged`, `Player` and `Enemy`. These are ordinary tag names supplied as starting defaults; `Player` and `Enemy` do not have automatic engine behavior just because of their names.

- Choose **Add Tag…** in the dropdown to create a project tag.
- Custom tags can be removed from the tag list. `Untagged` is protected and cannot be deleted.
- `Player` and `Enemy` are not protected; they can be removed like other tags.
- Removing a tag removes it from the dropdown. Entities that already carry that tag keep their current tag value until you change it.
- The available tag list is included in the saved project snapshot. An entity's assigned tag is stored with its scene data.

Tags are separate from physics layers and navigation areas. Use physics layers for collision filtering and navigation areas for pathfinding costs or masks; use tags to identify objects in editor workflows and scripts.

## GameObject and UI menus

**GameObject → Empty GameObject** creates an empty entity. **GameObject → Light** provides Directional, Point, Spot, Area, God Rays and Freeform lights. **GameObject → 2D Object** creates a Tileset, Tilemap, Nav World 2D or Stroke Path. **GameObject → Shape** creates Square, Circle, Capsule or Triangle shapes with a matching visible ShapeRenderer and collider.

The **UI** menu creates a Text object, Speech Bubble, Chat Log, Message Input (TextInput) or Joystick. These are shortcuts for creating an entity with the corresponding component; the full settings are on each component's reference page.

## Window menu and panel visibility

| Panel | What it contains | Default |
| --- | --- | --- |
| **Hierarchy** | Scene entities and their selection/order. | Visible |
| **Asset Panel** | Bottom editor area for assets and related project panels. | Visible |
| **Inspector** | Selected entity properties and component settings. | Visible |

Choose a panel name under **Window** to show or hide it. Hiding a panel gives more room to the Scene view. When one or more panels are hidden, **Show All Panels** restores them. Visibility is remembered in this browser, not stored as a project setting.

## Inspector component notes

The Inspector's information toggle controls optional explanatory notes below component settings. It is a display preference; actionable setup warnings remain visible independently. The default is off.

## Performance preferences and defaults

The current source defines the following stored preferences under the browser storage key `realot_engine_settings`. This is a reference to the shipped implementation—not a hidden user settings screen. Apart from the Inspector component-notes toggle described above, the current editor does not expose controls for these performance preferences in a general Settings dialog.

| Stored setting | Default | Meaning / supported values |
| --- | --- | --- |
| `editorFpsFocused` | `60` | Target rendering rate for the editor viewport while the editor window is focused. |
| `editorFpsUnfocused` | `24` | Target rendering rate for the editor viewport while unfocused. |
| `gameFps` | `60` | Play-window target: `30`, `60`, `120`, or `0` for unlimited (limited by the browser's animation-frame scheduling). |
| `backgroundRendering` | `true` | Allows throttled editor rendering to continue while the editor is unfocused rather than fully pausing. |
| `vsync` | `true` | Stored vertical-sync preference read by the rendering scheduler. |
| `showComponentNotes` | `false` | Whether optional Inspector component notes are displayed. This one is toggled by the Inspector UI. |

These values are implementation defaults and targets, not guarantees that a browser, device or display can maintain a particular frame rate. The editor viewport's focused/unfocused caps are separate from the runtime frame loop in an exported game.

## Console and diagnostics

The Console is part of the bottom editor area. It displays editor messages and script output; use its **Copy** control to copy visible logs and **Clear** to clear them. The gameplay debug HUD is separate: scripts can enable it with `debug.show()` in the Play window. See [Global API](../scripting/globals.html).

## Component settings

Component-specific options are not centralized in this page. The source-derived [component reference](../api/index.html) lists every public scene field, its data type, current default and script-facing API members for all 25 components. For navigation, physics and animation workflows, start with the corresponding [Physics](physics.html), [Navigation](navigation.html) and [Assets & animation](assets-animation.html) guides.
