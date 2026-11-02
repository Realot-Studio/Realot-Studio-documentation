# Architecture

> How Realot Studio separates runtime, editor, standalone runtime, components and systems.

- Source: https://realot-studio.pages.dev/docs/concepts/architecture.html

## Runtime / editor / target

The distribution follows a hard separation: `project/runtime/` is the engine shipped with games; `project/editor/` is the development tool; `project/player/` is the standalone runtime shell. Runtime must not import editor code; editor may import runtime code.

## Components are data

Components are plain data objects. Rendering, physics, lighting, audio and other behavior live in systems. This keeps scene serialization straightforward and makes the same scene data usable by the editor and standalone runtime.

## Systems run in an explicit order

| Order | System |
| --- | --- |
| 1 | ControllerSystem |
| 2 | PhysicsSystem |
| 3 | AnimationSystem |
| 4 | SpeechBubbleSystem |
| 5 | TextInputSystem |
| 6 | JoystickSystem |
| 7 | AudioSystem |
| 8 | AudioListenerSystem |
| 9 | ScriptSystem |
| 10 | Late controller work |
| 11 | RenderSystem |
| 12 | TilemapSystem |
| 13 | NavWorldSystem |
| 14 | LightingSystem |
| 15 | CameraRenderSystem |

## Rendering containers

The runtime separates game-content rendering, screen-space UI and late letterbox/pillarbox bars. Debug lines render in the world container. This separation explains why screen-space UI components such as TextRenderer can remain fixed while the world camera moves.
