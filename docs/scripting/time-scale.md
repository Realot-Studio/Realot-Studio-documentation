# Time scale & game speed

> Slow motion, speed-up and freeze with time.scale, plus time.deltaTime, time.unscaledDeltaTime and time.elapsed.

- Source: https://realot-studio.pages.dev/docs/scripting/time-scale.html

## The time object

| Member | Type | Meaning |
| --- | --- | --- |
| `time.deltaTime` | number | Game seconds since the previous frame. Follows `time.scale`. |
| `time.unscaledDeltaTime` | number | Real seconds since the previous frame, ignoring `time.scale`. Use it for menus and UI that must keep animating while the game is slowed or frozen. |
| `time.elapsed` | number | Game seconds since the game started. Follows `time.scale`. |
| `time.scale` | number | Read/write game speed multiplier, from 0 to 100. Default `1`. |

## Using time.scale

`time.scale` changes how fast the whole game runs, like Unity's `Time.timeScale`.

```
function onClick() {
  time.scale = 0.3;              // slow motion
  wait(1.5, function () {        // 1.5 GAME seconds = 5 real seconds at 0.3
    time.scale = 1;
  });
}
```

| Value | Effect |
| --- | --- |
| `1` | Normal speed. |
| `0.5` | Slow motion (half speed). |
| `2` | Double speed. |
| `0` | Frozen. The world still updates with `dt = 0`, rendering continues, and scripts keep running so you can read input and show a pause menu. |

## What is and is not affected

- **Affected:** physics, animation, [`tween()`](tween.html), `wait()` and `repeat()`, `onFixedUpdate`, `time.deltaTime` and `time.elapsed`.
- **Not affected:** input, rendering and `time.unscaledDeltaTime`.

## Limits and gotchas

- Values must be numbers from 0 to 100. Anything else (negative, NaN, text) is ignored and a console warning says the previous value was kept. Values above 100 are clamped to 100.
- Each frame simulates at most half a second of game time, so on a 60 FPS screen speeds above roughly 30x will not go faster.
- A tab-out or long frame spike is clamped to 0.1 real seconds before the scale is applied.
- **It stays set** when you load or restart a scene. Set `time.scale = 1` yourself if the next scene should run at normal speed.
- Physics catch-up steps are capped, so extreme speeds trade accuracy for stability.

## Pause menu pattern

```
function onUpdate() {
  if (input.keyPressed("Escape")) {
    time.scale = time.scale === 0 ? 1 : 0;
  }
  // Menu animation that keeps running while frozen:
  this.rotation += 90 * time.unscaledDeltaTime;
}
```

`scene.pause()` and `scene.resume()` are the other way to freeze gameplay; see [Global API](globals.html). Unlike `time.scale = 0` (where scripts keep running with `deltaTime = 0`), `scene.pause()` stops scripts including `onUpdate`, physics, animation and audio from the next frame until `scene.resume()`.
