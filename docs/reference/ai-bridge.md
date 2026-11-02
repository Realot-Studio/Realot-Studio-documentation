# AI Bridge: connect an AI assistant

> Connect an MCP-compatible AI app to the open Realot Studio editor using the built-in shared relay, with optional self-hosting, read-only mode and a complete source-derived tool catalog.

- Source: https://realot-studio.pages.dev/docs/reference/ai-bridge.html

> **Built in and ready to use:** Realot Studio includes a shared relay address. Most users do not need to install Node.js, configure a local server, create a Cloudflare account or deploy anything. Open AI Bridge, copy the private link into an AI app that supports remote MCP connectors, and press Connect in Realot.

## Connect your AI assistant

1. Open your project in Realot Studio and click **AI Bridge** in the editor.
2. Click **Copy link** in the panel.
3. In your AI app, open its connector or MCP-server settings. Add a **remote MCP server** or **custom connector**, paste the copied link, and name it **Realot**. The exact menu name depends on the AI app.
4. Return to Realot and click **Connect**. The panel should show **Connected**. Ask the AI to inspect the open project before asking it to make changes.

The copied link contains a private secret key. Treat it like a password: anyone who has the link may be able to use the tools exposed by your open editor. Do not post it in public messages or commit it to a project repository.

## AI Bridge panel options

| Option | What it does |
| --- | --- |
| **Copy link** | Copies the private remote MCP connector URL for this editor. |
| **Connect / Disconnect** | Starts or closes the editor's connection to the relay. The editor must remain open while the AI works on the live project. |
| **Read-only** | Blocks tools that change the project. The AI can inspect the editor but cannot perform supported edit operations while this is enabled. |
| **Connect automatically when the editor opens** | Remembers the preference and reconnects on a later editor launch when a private key is already configured. |
| **Make a new private link** | Creates a new secret key and invalidates the old link. Add the new link to your AI app; the old connector URL will no longer authenticate. |
| **Need more AI time? → click here to host it** | Opens Cloudflare's deployment flow for an optional personal copy of the relay. This is not needed for the built-in shared relay. |
| **Use it / Default** | *Use it* switches to the relay URL you supplied and refreshes the connector link. *Default* switches back to Realot's built-in shared relay. Re-copy the connector link after changing relay addresses. |

## Shared relay time allowance

The built-in shared relay includes **30 minutes of active AI work in each 24-hour usage window**. Time is counted while a tool call is running and for up to 20 seconds between calls. Being connected while the AI is idle does not use the allowance. The panel shows the remaining time and the reset countdown.

The usage record is kept in this browser's local storage. It is a client-side allowance display and should not be treated as an account-wide quota or a tamper-proof billing record. Hosting your own relay removes the shared-relay active-time limit; Cloudflare account usage and service terms may still apply.

## Optional: host a personal relay

Most users should stay on the built-in relay. Hosting your own is an advanced option for users who want to avoid the shared-relay time allowance or operate their own relay endpoint.

1. In the AI Bridge panel, select **click here to host it**. Realot opens the Cloudflare deployment page for the relay source repository.
2. Complete Cloudflare's deployment and copy the HTTPS address ending in `.workers.dev`.
3. Paste that address into the relay field in the AI Bridge panel and click **Use it**.
4. Click **Copy link** again and replace the old Realot connector URL in your AI app. Connect from the editor.

To return to the shared relay, click **Default**, copy the refreshed link, and update the connector in your AI app. A personal relay has no Realot active-AI-minutes cap, but you are responsible for its deployment, availability and Cloudflare account.

## What the AI can do

The built-in relay currently exposes **93 MCP tools**. They allow an AI app to inspect editor state, scenes and entities; create and modify entities and components; read, write and attach scripts; start or pause play mode; inspect the Console and capture a screenshot; manage assets and chunked uploads; edit animation clips and frames; manage tilesets and tilemaps; paint navigation cells and configure navigation and physics layers; manage tags, folders, prefabs and scenes; save or export project data; and control editor panels and tools.

The tables below list every hosted tool name and its input fields. Fields shown in bold are required. Full JSON input schemas—including exact types, constraints and additional properties—are published in the [machine-readable API catalog](../../api/index.json) under `aiBridge.sharedRelayTools`.

## Complete hosted MCP tool catalog

### Project and scene inspection

| Tool | What it does |
| --- | --- |
| `get_editor_state` Inputs: none | Overview of the open Realot editor: project name, whether the game is playing, selected entity ids, entity count, available component types. |
| `list_entities` Inputs: `limit`: integer | List every entity in the current scene (id, name, tag, active, component types, x/y position). |
| `get_entity` Inputs: **`id`: string (required)** | Full data of one entity: all components with every property. |
| `list_scenes` Inputs: none | List every scene in the project and which one is active. |

### Entities and components

| Tool | What it does |
| --- | --- |
| `create_entity` Inputs: **`name`: string (required)**; `x`: number; `y`: number; `tag`: string; `components`: object | Create an entity. 'components' maps a component type (e.g. SpriteRenderer, Collider2D, Rigidbody2D, Script) to its properties. A Transform is always added. Undoable with undo. Values are validated: wrong types, unknown properties, invalid enum values (e.g. Light.type), out-of-range numbers, bad hex colors and values the engine would silently clamp are rejected with a message listing every problem and the allowed values; nothing is changed on error. |
| `update_component` Inputs: **`id`: string (required)**; **`type`: string (required)**; **`props`: object (required)** | Change properties of an existing component on an entity (only properties the component already has). Use get\_entity first to see them. Values are validated: wrong types, unknown properties, invalid enum values (e.g. Light.type), out-of-range numbers, bad hex colors and values the engine would silently clamp are rejected with a message listing every problem and the allowed values; nothing is changed on error. |
| `add_component` Inputs: **`id`: string (required)**; **`type`: string (required)**; `props`: object | Add a component to an entity. Values are validated: wrong types, unknown properties, invalid enum values (e.g. Light.type), out-of-range numbers, bad hex colors and values the engine would silently clamp are rejected with a message listing every problem and the allowed values; nothing is changed on error. |
| `remove_component` Inputs: **`id`: string (required)**; **`type`: string (required)** | Remove a component (not Transform) from an entity. |
| `delete_entities` Inputs: **`ids`: array (required)** | Delete entities by id (same as pressing Delete in the editor). Undoable. |
| `select_entities` Inputs: **`ids`: array (required)** | Select entities in the editor so the user sees them in the Inspector. |
| `update_entity` Inputs: **`id`: string (required)**; **`patch`: object (required)** | Rename an entity or change its tag, active flag, or hierarchy folder. Use update\_component for Transform and other components. |
| `create_scene` Inputs: `name`: string; `switch`: boolean | Create a new scene (with a Main Camera). Switches to it unless switch=false. |
| `switch_scene` Inputs: **`scene_id`: string (required)** | Make another scene the active one in the editor. |
| `rename_scene` Inputs: **`scene_id`: string (required)**; **`name`: string (required)** | Rename a scene. |
| `delete_scene` Inputs: **`scene_id`: string (required)**; `confirm`: boolean | Delete a scene. Cannot be undone, so the first call only reports what would be deleted; repeat with confirm=true. A project must keep one scene. |
| `duplicate_scene` Inputs: **`scene_id`: string (required)** | Duplicate a scene (deep copy) and add it to the project. Does not switch to it. |

### Scripts, play mode and diagnostics

| Tool | What it does |
| --- | --- |
| `list_scripts` Inputs: none | Names of all scripts in the project. |
| `get_script` Inputs: **`name`: string (required)** | Source code of a script. |
| `write_script` Inputs: **`name`: string (required)**; **`source`: string (required)** | Create or overwrite a script's source code. Entities already using this script get the new code too. Reports syntax errors. |
| `attach_script` Inputs: **`id`: string (required)**; **`scriptName`: string (required)** | Attach an existing script to an entity (adds a Script component). |
| `set_playing` Inputs: **`playing`: boolean (required)** | Start or stop play mode (opens the game in the play window). |
| `get_console` Inputs: `limit`: integer | Recent editor/play console lines (logs, warnings, script errors). |
| `screenshot` Inputs: none | Image of the scene viewport as the user sees it. |
| `undo` Inputs: none | Undo the last editor change. |
| `redo` Inputs: none | Redo the last undone change. |
| `delete_script` Inputs: **`name`: string (required)**; `confirm`: boolean | Delete a script from the project and clear it from objects using it. Cannot be undone, so the first call reports usage; repeat with confirm=true. |
| `set_script_enabled` Inputs: **`id`: string (required)**; **`enabled`: boolean (required)** | Enable or disable the Script component on an entity without removing it. |
| `set_paused` Inputs: **`paused`: boolean (required)** | Pause or resume the running game. The game must be playing (see set\_playing). |

### Assets and uploads

| Tool | What it does |
| --- | --- |
| `list_assets` Inputs: `kind`: string [all, sprite, animation, frame, tile, audio]; `query`: string; `limit`: integer | List imported images and audio without returning binary data, grouped like the editor's Project folders: Sprites, Animation Clips (uploaded animation frames) and Tiles (tileset images), plus Audio. Use the keys in SpriteRenderer, AudioSource, animation clips, and tilesets. |
| `begin_asset_upload` Inputs: **`file_name`: string (required)**; **`mime_type`: string (required)**; **`size_bytes`: integer (required)**; **`purpose`: string [sprite, audio, animation-image, animation-zip, animation-gif, animation-sheet, tileset-sheet, tileset-tile, frame-asset, tile-asset, project-zip] (required)**; `entity_id`: string; `clip_id`: string; `tileset_entity_id`: string; `role`: string; `grid_cols`: integer; `grid_rows`: integer; `group`: string | Start uploading a custom asset: a sprite, audio file, animation source, tileset image, or a loose image for the Animation Clips folder (purpose 'frame-asset') or Tiles folder (purpose 'tile-asset'). Then send sequential base64 chunks with append\_asset\_upload\_chunk and finish with complete\_asset\_upload. The editor must be open and connected. Maximum 20 MiB per file. Purpose 'project-zip' (a .realot project, max 20 MiB) REPLACES the entire open project and asks the person at the editor to confirm. Animation uploads land in the Animation Clips folder; tileset uploads land in the Tiles folder. |
| `append_asset_upload_chunk` Inputs: **`upload_id`: string (required)**; **`chunk_index`: integer (required)**; **`chunk_base64`: string (required)** | Send one base64-encoded binary chunk for an active asset upload. Chunks must be independent base64 strings, sequential from index 0. Use the chunk size returned by begin\_asset\_upload; retrying the same index and data is safe. |
| `complete_asset_upload` Inputs: **`upload_id`: string (required)** | Validate and import all received bytes using the editor's native import pipeline. Call only after every chunk has been accepted. |
| `cancel_asset_upload` Inputs: **`upload_id`: string (required)** | Discard a staged upload before it is imported. |
| `rename_asset` Inputs: **`key`: string (required)**; **`kind`: string [sprite, frame, animation, tile, audio] (required)**; **`name`: string (required)** | Rename an imported sprite, animation frame, tile or audio asset while preserving its key and references. |
| `delete_asset` Inputs: **`key`: string (required)**; **`kind`: string [sprite, frame, animation, tile, audio] (required)**; `confirm`: boolean | Delete an imported asset. If the asset is referenced by scenes or prefabs, the first call reports those references; set confirm=true only when it is acceptable to leave them unresolved. |
| `slice_asset_into_tileset` Inputs: **`entity_id`: string (required)**; **`asset_key`: string (required)** | Cut one existing project image (for example an uploaded sprite) into a 4x4 grid and fill all 16 Tileset slots with the pieces. The pieces are saved in the Tiles folder under the tileset's name. Undoable. |

### Animation

| Tool | What it does |
| --- | --- |
| `list_animations` Inputs: none | List animation clips and ordered frame keys for every entity in the active scene. |
| `create_animation_clip` Inputs: **`entity_id`: string (required)**; `name`: string; `fps`: number; `loop`: boolean | Create an empty animation clip on an entity, adding SpriteAnimation if needed, and open it in the animation editor. |
| `update_animation_clip` Inputs: **`entity_id`: string (required)**; **`clip_id`: string (required)**; **`fields`: object (required)** | Change an animation clip name, frame rate, loop setting, or collider override. Set collider\_override to null to remove the override. |
| `delete_animation_clip` Inputs: **`entity_id`: string (required)**; **`clip_id`: string (required)** | Delete one animation clip from its entity. The remaining clips and frames are preserved. |
| `move_animation_frame` Inputs: **`entity_id`: string (required)**; **`clip_id`: string (required)**; **`from_index`: integer (required)**; **`to_index`: integer (required)** | Reorder an animation frame by moving it from one zero-based position to another. |
| `delete_animation_frame` Inputs: **`entity_id`: string (required)**; **`clip_id`: string (required)**; **`frame_index`: integer (required)** | Remove one zero-based frame position from an animation clip without deleting the underlying imported asset. |
| `add_animation_frames` Inputs: **`entity_id`: string (required)**; **`clip_id`: string (required)**; **`asset_keys`: array (required)**; `index`: integer | Add images that are already in the project (sprites, Animation Clips frames, or Tiles) to an animation clip as frames. Use list\_assets for keys and list\_animations for entity/clip ids. Optional index inserts at that position instead of appending. Undoable. |

### Tilesets and tilemaps

| Tool | What it does |
| --- | --- |
| `list_tilesets` Inputs: none | List tilesets, tile dimensions, and sprite keys assigned to each role. |
| `update_tileset` Inputs: **`entity_id`: string (required)**; **`patch`: object (required)** | Edit a tileset name, tile dimensions, or selected role-to-sprite assignments. Set a slot to null to clear it. |
| `set_tileset_slot` Inputs: **`entity_id`: string (required)**; **`role`: string (required)**; **`asset_key`: string|null (required)** | Put an existing project image (sprite, animation frame or tile) in one slot of a Tileset, or clear the slot with asset\_key null. Roles come from list\_tilesets. |
| `list_tilemaps` Inputs: none | List Tilemap entities, their assigned tileset entity, painted cell count, and up to 500 grid coordinates. |
| `paint_tilemap` Inputs: **`entity_id`: string (required)**; **`mode`: string [paint, erase] (required)**; **`cells`: array (required)** | Paint or erase grid cells on a Tilemap. Coordinates are integer cell columns and rows, not world coordinates. Undoable. |

### Navigation and physics

| Tool | What it does |
| --- | --- |
| `list_navigation_worlds` Inputs: none | List NavWorld2D entities with bounds, cell size, painted cell counts, and navigation settings. |
| `paint_navigation_cells` Inputs: **`entity_id`: string (required)**; **`mode`: string [walkable, blocked, erase\_walkability, area, clear\_area] (required)**; `area_index`: integer; **`cells`: array (required)** | Paint walkable or blocked navigation cells, restore baked walkability, or set/clear navigation area indices. Coordinates are integer grid columns and rows. Undoable. |
| `update_navigation_world` Inputs: **`entity_id`: string (required)**; **`patch`: object (required)** | Edit NavWorld2D bounds, cell size, obstacle threshold, diagonal movement, dynamic mode, or all 16 area costs. Cell changes invalidate the baked runtime cache. |
| `list_navigation_areas` Inputs: none | List the 16 named navigation area slots and their indices. |
| `set_navigation_area_name` Inputs: **`index`: integer (required)**; **`name`: string (required)** | Rename one navigation area slot. Slot 0 is the default Ground area and cannot be cleared. |
| `list_physics_layers` Inputs: none | List all 16 named physics layers and their indices. |
| `set_physics_layer_name` Inputs: **`index`: integer (required)**; **`name`: string (required)** | Rename one of the 16 physics layer slots. Slot 0 is the default layer and cannot be cleared. |
| `set_collider_layer_filter` Inputs: **`entity_id`: string (required)**; **`layer`: integer (required)**; **`collides_with`: array (required)** | Set a Collider2D's physics layer and the layer indices it collides with. Use list\_physics\_layers to map names to indices. |
| `bake_navworld` Inputs: **`id`: string (required)** | Bake a NavWorld2D from the scene's colliders (the editor's Bake button). Reports walkable and blocked cell counts. |

### Tags, folders and prefabs

| Tool | What it does |
| --- | --- |
| `list_tags` Inputs: none | List the project tag registry. |
| `add_tag` Inputs: **`tag`: string (required)** | Add a tag to the registry. |
| `delete_tag` Inputs: **`tag`: string (required)** | Remove a tag from the registry (Untagged cannot be removed). |
| `list_prefabs` Inputs: none | List prefabs in the project. |
| `create_prefab` Inputs: **`id`: string (required)**; `name`: string | Create a prefab from an entity and link that entity to it. |
| `instantiate_prefab` Inputs: **`prefab_id`: string (required)**; `name`: string; `x`: number; `y`: number | Place a new instance of a prefab in the active scene. |
| `rename_prefab` Inputs: **`prefab_id`: string (required)**; **`name`: string (required)** | Rename a prefab. |
| `delete_prefab` Inputs: **`prefab_id`: string (required)**; `confirm`: boolean | Delete a prefab from the catalogue; existing instances become unlinked. First call reports impact; repeat with confirm=true. |
| `list_folders` Inputs: none | List Hierarchy folders in the active scene (id, name, parentId). |
| `create_folder` Inputs: **`name`: string (required)**; `parent_id`: string | Create a Hierarchy folder, optionally nested in another. Put entities in it with update\_entity folderId. |
| `rename_folder` Inputs: **`folder_id`: string (required)**; **`name`: string (required)** | Rename a Hierarchy folder. |
| `move_folder` Inputs: **`folder_id`: string (required)**; `parent_id`: string | Nest a folder inside another folder, or move it to the top level (omit parent\_id). Cycles are refused. |
| `delete_folder` Inputs: **`folder_id`: string (required)** | Delete a folder. Its entities and sub-folders move up one level; nothing inside is deleted. |
| `update_prefab` Inputs: **`id`: string (required)**; `apply_position`: boolean; `apply_rotation`: boolean; `apply_scale`: boolean | Push an instance's current data to its prefab and to every non-overridden instance across all scenes (the editor's Update Prefab). |
| `revert_prefab` Inputs: **`id`: string (required)** | Reset a prefab instance to its prefab's data, discarding overrides. |
| `unpack_prefab` Inputs: **`id`: string (required)** | Unlink an instance from its prefab, keeping its current data. |

### Export and project files

| Tool | What it does |
| --- | --- |
| `save_project` Inputs: none | Save now (browser autosave slot, and the .realot file if one is being kept up to date). |
| `export_game` Inputs: **`format`: string [html, pwa] (required)**; `title`: string; `download`: boolean | Build the game as a standalone HTML5 or PWA ZIP. By default it also downloads the ZIP in the editor's browser; read the bytes with read\_export\_chunk. APK builds are not supported through MCP. |
| `read_export_chunk` Inputs: **`export_id`: string (required)**; **`chunk_index`: integer (required)** | Read one base64 chunk of the last export\_game ZIP. |
| `release_export` Inputs: **`export_id`: string (required)** | Free the memory held by the last export\_game result. |
| `download_project_zip` Inputs: `name`: string; `optimize_assets`: boolean | Save the whole project as a .realot ZIP, downloaded in the editor's browser (File > Save Project without a file handle). |

### Editor controls

| Tool | What it does |
| --- | --- |
| `open_editor_panel` Inputs: **`panel`: string [animation, tileset, physics\_layers, navigation\_areas] (required)**; `entity_id`: string; `clip_id`: string | Open the animation editor, tileset editor, physics-layer panel, or navigation-area panel. Animation and tileset panels need the matching entity\_id. |
| `set_editor_tool` Inputs: **`tool`: string [select, translate, rotate, scale, pan, tile, erase, nav, nav-block, nav-area, path] (required)**; `entity_id`: string | Choose a viewport tool and optionally select its Tilemap, NavWorld2D, or StrokePath entity so the user can continue painting in the editor. |

## Safe and reliable use

- Start with project inspection. Ask the AI to identify the active scene, selected objects and relevant components before it edits anything.
- Use **Read-only** when you only want explanations or an audit.
- Ask the AI to make a small change first, then inspect the result in the editor and test it in Play mode.
- Use undo for supported scene edits. Do not assume every operation—especially script writes, project-file operations or scene-list changes—can be reversed in the same way. Save a project backup before large edits.
- Review generated JavaScript. Project scripts execute as browser page code and are not an isolated security sandbox. Do not run untrusted scripts or import project archives from sources you do not trust.
- Tool results may contain project names, scenes, scripts, assets and Console output. These are sent to the connected AI app; use an AI provider you trust and avoid connecting projects containing secrets or private data.
- Disconnect when finished and keep the private connector URL secret. Use **Make a new private link** if you think the link has been exposed.

## About the included local MCP companion source

The engine archive also contains a Node.js stdio companion under `mcp-bridge/` and an editor integration module under `project/editor/mcp/EditorBridge.js`. In this supplied build, that editor integration's installer is not called by the editor startup path. The local companion is therefore not a supported, ready-to-connect alternative in the packaged editor. Use the built-in shared relay described above. Developers who want a local stdio integration must first wire and test the companion against the editor; its 23 local tool definitions are not the same interface as the 80 tools exposed by the live shared relay.

> **For AI clients and coding agents:** Start with For AI assistants & LLMs , then read the script-module reference and global runtime API when generating game scripts. AI Bridge tools edit the editor; script APIs run inside the game. They are different interfaces.


## Playtesting and discovery tools

The AI can play and test the game it builds: `play_restart`, `play_input` (keys, clicks, taps, drags, waits, `assert`, `screenshot`), `play_step`, `play_screenshot`, `play_get_state`, `play_get_entity`, `play_eval`, `play_get_errors`. Tests run on a fixed 60 fps step. `get_engine_guide`, `describe_component`, `check_project`, `duplicate_entities`, `clear_console` help it build correctly. Each tool call has a 25 second limit.
