# Editor overview

> Navigate the Realot Studio editor and understand the main development surfaces.

- Source: https://realot-studio.pages.dev/docs/editor/overview.html

## Main surfaces

| Area | Purpose |
| --- | --- |
| Hierarchy | Shows entities in the current scene, including hierarchy folders. |
| Inspector | Edits entity metadata and component properties. |
| Viewport | Scene/game editing and gizmos. |
| Script editor | Edit JavaScript with engine-aware autocomplete. |
| Bottom panels | Animation, tileset, navigation, status and related workflows. |
| Toolbar / menus | Save, project I/O, physics layers, navigation areas, entity creation and export. |

## Entity creation

The Add Component workflow exposes the engine’s authoring components, including Rigidbody2D, Collider2D, Joint2D, CharacterController, SpriteRenderer, SpriteAnimation, ShapeRenderer, StrokePath, Light, AudioSource, AudioListener, ShadowCaster, LightingSettings, Tileset, Tilemap, NavWorld2D, NavAgent2D, TextRenderer, SpeechBubble, ChatLog, TextInput and Joystick.

## Editor principle

The editor writes serializable scene/project data. Runtime systems consume that data. Private helper modules under `project/editor/` should be treated as implementation details, not game scripting APIs.
