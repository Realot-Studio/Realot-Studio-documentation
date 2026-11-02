# Tween API

> Animate numeric properties smoothly with tween(), choose from 33 easing curves, and stop animations with cancelTween().

- Source: https://realot-studio.pages.dev/docs/scripting/tween.html

## Overview

`tween(target, properties, duration, easing, onComplete)` smoothly moves one or more numeric properties from their current value to a target value over a number of **game seconds**. It is a global function, available in every script with no import. It returns a numeric id you can pass to `cancelTween(id)`.

| Argument | Type | Meaning |
| --- | --- | --- |
| `target` | object | An entity context (`this`, or the result of `findFirst()` etc.) or a scripting component object such as `this.sprite`, `this.light` or `this.camera`. |
| `properties` | object | Map of property name to end value, for example `{ x: 420, y: 180 }`. Only finite numbers are accepted as end values. |
| `duration` | number | Length in game seconds. `0` (or an invalid value) completes on the next tween update. |
| `easing` | string | Optional. One of the [33 easing names](#easing-catalogue). Empty or omitted means `"linear"`. |
| `onComplete` | function | Optional. Called once when the tween finishes, with `this` bound to the entity that started the tween. |

```
function onStart() {
  // Move, spin and resize over 0.8 game seconds
  tween(this, { x: 420, y: 180, rotation: 90, scaleX: 1.2, scaleY: 1.2 }, 0.8, "easeOutCubic", function () {
    // "this" is still the entity that started the tween
    tween(this.sprite, { opacity: 0.25 }, 0.35, "easeInOutSine");
  });
}
```

## What can be tweened

A property is tweened only if it **already exists on the target and currently holds a finite number**. Properties that are missing, non-numeric (colours are hex strings, `position` and `scale` are objects) or non-finite are skipped.

| Target | Typical tweenable properties |
| --- | --- |
| `this` (entity) | `x`, `y`, `rotation`, `scaleX`, `scaleY` |
| `this.sprite` | `opacity` |
| `this.shape` | `width`, `height`, `radius`, `opacity`, `outlineWidth` |
| `this.text` | `fontSize`, `opacity` |
| `this.light` | `intensity`, `radius`, `angle`, `shadowStrength` |
| `this.audio` | `volume`, `pitch` |
| `this.camera` | `zoom`, `offsetX`, `offsetY` |
| `this.strokePath` | `thickness`, `opacity`, `textureOffset` |
| `scene.lighting` | `ambientDarkness`, `glowStrength` |

Any numeric member listed on a component's Script API table can be a tween target. Each tween writes through the normal script API, so setter rules (clamping, validation) still apply.

## Cancelling

```
var id = tween(this, { x: 700 }, 2, "easeOutBounce");
// later
var wasActive = cancelTween(id);   // true only if a tween with that id was still running
```

`cancelTween()` leaves the property at whatever value it had reached. `onComplete` is not called for a cancelled tween.

## Behavior and rules

- **Start tweens from lifecycle callbacks** such as `onStart()`, `onClick()` or a collision handler. Calling `tween()` outside script execution logs `[tween]` warning and returns `-1`. Avoid creating a new tween every frame in `onUpdate()`; start one and let it run.
- **Game time.** Tweens advance once per frame after `onUpdate` callbacks, using the scaled frame clock. [`time.scale`](time-scale.html) speeds them up or slows them down, and `scene.pause()` freezes them.
- **Exact finish.** When progress reaches 1 the property is set to the exact end value, so back/elastic overshoot never leaves a rounding error.
- **Several properties at once** in one call share the same duration and easing.
- **Automatic cleanup.** A tween ends silently if the entity that started it, or the entity it targets, is destroyed. Restarting or switching scenes clears all tweens.
- **Errors.** If an easing function or a property setter throws, that tween is removed and the error is reported in the Console with the owning entity name. A completion callback that throws is reported as `tween onComplete`.
- **Return value.** Invalid input (bad target, properties not an object, unknown easing, no numeric properties, non-function `onComplete`) returns `-1` and logs a `[tween]` warning that says what to fix. An unknown easing name is never silently treated as linear.
- **Easing names** are case-insensitive and ignore spaces, hyphens and underscores, so `"EASE-OUT-QUAD"` equals `"easeOutQuad"`.

> **Tweening physics bodies:** Assigning x or y on an entity that has a Dynamic or Kinematic Rigidbody2D teleports the body each frame. For moving physics objects use velocities or forces; use tween for transforms, opacity, UI, lights, cameras and Static or non-physics entities.

## Editor support

The Script Editor autocompletes `tween` and `cancelTween`, and offers the easing names inside the easing string (type `tween(this, { x: 100 }, 1, "easeOut` and the matching names appear). Both names are syntax-highlighted as engine globals.

## Easing catalogue

Every name below is a real engine easing. Each preview is drawn from the engine's own easing function: the horizontal axis is time (0 to 1) and the vertical axis is progress. The dashed lines mark the start value (bottom) and end value (top); curves that cross them overshoot on purpose. **In** starts slowly, **Out** ends slowly, **InOut** does both.

| Family | Names |
| --- | --- |
| Basic | `linear`, `smoothstep`, `smootherstep` |
| Quad | `easeInQuad`, `easeOutQuad`, `easeInOutQuad` |
| Cubic | `easeInCubic`, `easeOutCubic`, `easeInOutCubic` |
| Quart | `easeInQuart`, `easeOutQuart`, `easeInOutQuart` |
| Quint | `easeInQuint`, `easeOutQuint`, `easeInOutQuint` |
| Sine | `easeInSine`, `easeOutSine`, `easeInOutSine` |
| Expo | `easeInExpo`, `easeOutExpo`, `easeInOutExpo` |
| Circ | `easeInCirc`, `easeOutCirc`, `easeInOutCirc` |
| Back | `easeInBack`, `easeOutBack`, `easeInOutBack` |
| Elastic | `easeInElastic`, `easeOutElastic`, `easeInOutElastic` |
| Bounce | `easeInBounce`, `easeOutBounce`, `easeInOutBounce` |

### Basic

`linear`

`smoothstep`

`smootherstep`

### Quad

`easeInQuad`

`easeOutQuad`

`easeInOutQuad`

### Cubic

`easeInCubic`

`easeOutCubic`

`easeInOutCubic`

### Quart

`easeInQuart`

`easeOutQuart`

`easeInOutQuart`

### Quint

`easeInQuint`

`easeOutQuint`

`easeInOutQuint`

### Sine

`easeInSine`

`easeOutSine`

`easeInOutSine`

### Expo

`easeInExpo`

`easeOutExpo`

`easeInOutExpo`

### Circ

`easeInCirc`

`easeOutCirc`

`easeInOutCirc`

### Back

`easeInBack`

`easeOutBack`

`easeInOutBack`

### Elastic

`easeInElastic`

`easeOutElastic`

`easeInOutElastic`

### Bounce

`easeInBounce`

`easeOutBounce`

`easeInOutBounce`

## Recipes

### Fade out and destroy

```
function onClick() {
  tween(this.sprite, { opacity: 0 }, 0.4, "easeInQuad", function () {
    this.destroy();
  });
}
```

### Pop-in UI

```
function onStart() {
  this.scaleX = 0;
  this.scaleY = 0;
  tween(this, { scaleX: 1, scaleY: 1 }, 0.5, "easeOutBack");
}
```

### Light pulse that can be stopped

```
function onStart() {
  this._pulse = tween(this.light, { intensity: 2 }, 0.6, "easeInOutSine", function () {
    tween(this.light, { intensity: 0.5 }, 0.6, "easeInOutSine");
  });
}
function onDestroy() { cancelTween(this._pulse); }
```

### Slow-motion hit stop with a tween that ignores nothing

```
function onCollisionEnter(other) {
  time.scale = 0.2;                 // tweens and timers slow down too
  wait(0.3, function () { time.scale = 1; });
}
```
