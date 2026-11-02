# Coordinate system & conventions

> The signs, units, axes, rotation conventions and reference-resolution rules that prevent common Realot Studio scripting mistakes.

- Source: https://realot-studio.pages.dev/docs/reference/coordinate-system.html

> **Core convention:** Realot Studio is a 2D screen-style coordinate system: +X is right and +Y is down. Treat Y signs accordingly when writing movement, offsets, camera/UI positioning, and physics examples.

## Transform axes

| Value | Positive direction | Common use |
| --- | --- | --- |
| `x` | Right | Horizontal world movement and placement. |
| `y` | Down | Vertical placement; jumping/falling code should use negative/positive signs according to the movement system being used. |
| `z` | Depth layer / pseudo-3D input | Affects pseudo-3D rendering only when the camera’s pseudo-3D behavior is enabled. |
| `rotation` | Degrees around Z | Used by sprites, lights and directional orientation; 0 points along +X for directional/spot style aiming. |
| `scaleX` / `scaleY` | 1 = native size | Values above 1 enlarge; values below 1 shrink; negative values mirror the axis. |

## UI coordinates

Screen-space Text, TextInput, ChatLog and Joystick components use the reference-resolution pixel convention supplied by the Camera/device-fit pipeline. This is why HUD coordinates remain stable when the physical device resolution changes.

## Angles and vectors

Vector-like APIs use ordinary JavaScript objects such as `{x, y}`. When converting a direction to an angle, remember that the canvas/world Y axis points downward, so visually “up” is negative Y.

## Timing

| Concept | Meaning |
| --- | --- |
| `time.deltaTime` | Seconds since the previous script update; multiply speeds expressed per second by deltaTime. |
| `wait(seconds,...)` | Wall-clock game/script timer in seconds. |
| `repathInterval` | Navigation re-plan period in seconds. |
