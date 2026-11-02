# Lighting, audio & UI

> Build atmospheric scenes, sound behavior and responsive UI with Realot Studio components.

- Source: https://realot-studio.pages.dev/docs/editor/lighting-audio-ui.html

> **Exact control path:** Create lights from GameObject → Light or add Light/Audio/UI components through Inspector → Add Component . Screen-space UI entities can also be created directly from the top UI menu.

## Lighting

Lights support Directional, Point, Spot, Area, GodRays and Freeform types. LightingSettings controls scene-wide shadow quality, ambient darkness and visible glow strength. ShadowCaster controls per-entity shadow geometry and softness.

## Shadow quality

ShadowMode `quad` is the cheaper analytic mode. `raymarch` enables per-pixel ray-marched occlusion; `raymarchSteps` controls accuracy/cost and is clamped to 1-200.

## UI

TextRenderer can be screen-space, while SpeechBubble, ChatLog, TextInput and Joystick provide higher-level UI behaviors. TextInput exposes `justSubmitted`; Joystick exposes normalized x/y input and engagement state.

## Audio listeners

AudioSource can be 3D distance-attenuated. AudioListener receives hearing-area transitions that map to `onHearSound(source)` and `onLoseSound(source)`.
