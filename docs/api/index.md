# API reference

> Complete Realot Studio component, script-module and runtime API reference.

- Source: https://realot-studio.pages.dev/docs/api/index.html

> **Start with prerequisites:** The API requirements & complete usage map shows which components or scene systems must exist before an API can be used.

## Components

The editor's component system contains 25 documented component types. Each component page lists its public scene fields, defaults, field descriptions, and the script API members exposed when that component is attached.

[**Transform**Position, rotation and scale.](components/transform.html)
[**SpriteRenderer**Texture, color, flips and opacity.](components/spriterenderer.html)
[**ShapeRenderer**Procedural square, circle, capsule and triangle shapes.](components/shaperenderer.html)
[**TextRenderer**World-space and screen-space text.](components/textrenderer.html)
[**StrokePath**Editable variable-width lines and textured paths.](components/strokepath.html)
[**SpeechBubble**Entity-attached dialogue bubble.](components/speechbubble.html)
[**ChatLog**Scrollable message history.](components/chatlog.html)
[**TextInput**Interactive text entry.](components/textinput.html)
[**Joystick**Virtual touch joystick.](components/joystick.html)
[**Rigidbody2D**Static, Dynamic and Kinematic physics body.](components/rigidbody2d.html)
[**Collider2D**Collision shape, triggers and layer filters.](components/collider2d.html)
[**Joint2D**Fixed, Revolute, Prismatic, Rope and Spring joints.](components/joint2d.html)
[**CharacterController**Character, Platformer, Top-Down, Car, Follow, Patrol and Free movement modes.](components/charactercontroller.html)
[**SpriteAnimation**Sprite-sheet clips and animation state.](components/spriteanimation.html)
[**Camera**Reference resolution, scaling, follow, shake and pseudo-3D.](components/camera.html)
[**AudioSource**Playback, pitch, volume and spatial attenuation.](components/audiosource.html)
[**AudioListener**Hearing radius and audio detection.](components/audiolistener.html)
[**Light**Six 2D light modes.](components/light.html)
[**ShadowCaster**Shadow occlusion geometry and softness.](components/shadowcaster.html)
[**LightingSettings**Scene-wide ambient and shadow quality settings.](components/lightingsettings.html)
[**NavAgent2D**Pathfinding, area filters, avoidance and vehicle tuning.](components/navagent2d.html)
[**NavWorld2D**Shared painted or baked navigation grid.](components/navworld2d.html)
[**Tileset**Reusable 16-role autotile setup.](components/tileset.html)
[**Tilemap**Painted tile grid linked to a Tileset.](components/tilemap.html)
[**Script**Script name, source and enabled state.](components/script.html)

## Complete script-module index

The [Script module member index](script-modules.html) is generated from the engine's supported-member sets. It covers every member exposed by the `this.*` component modules, plus `this.state`, `this.myTouch`, `scene.lighting` and the global `save` API. Each entry includes its access type, context and source file.

## Global runtime API

Scripts also receive global functions and objects such as `findFirst()`, `scene`, `physics`, `nav`, `input`, `mouse`, `touch`, `time`, `random`, `mathx`, `save`, `debug` and `pool`. See [Runtime modules](runtime.html) and the practical [Global API guide](../scripting/globals.html).

## Option shapes and requirements

Optional arguments for raycasts, spawning, navigation, camera follow and other script calls are documented in [Option schemas (opts)](options.html). The [requirements map](requirements.html) identifies component prerequisites and always-available APIs.

## Machine-readable catalog

For code tools and AI assistants, fetch [`api/index.json`](../../api/index.json). It contains component field/default metadata, lifecycle callbacks, enum values, global API groups, all 24 script API modules and their supported member lists. The full manual is available from [`llms-full.txt`](../../llms-full.txt); the search index is [`search-index.json`](../../search-index.json).
