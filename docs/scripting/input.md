# Input

> Keyboard, mouse, touch, gestures and virtual joystick input in Realot Studio.

- Source: https://realot-studio.pages.dev/docs/scripting/input.html

## Keyboard

`input.keyDown(code)` is true while a key is held. `input.keyPressed(code)` is a one-frame pulse. Browser-style codes include `ArrowLeft`, `ArrowRight`, `KeyA`, `Space` and the special code `Any`.

```
function onUpdate() {
  var speed = 200 * time.deltaTime;
  if (input.keyDown("ArrowRight") || input.keyDown("KeyD")) this.x += speed;
  if (input.keyDown("ArrowLeft")  || input.keyDown("KeyA")) this.x -= speed;

  if (input.keyPressed("Space")) {
    this.controller.simulateJump(); // one-frame pulse — fires once per press, not every frame held
  }
}
```

## Mouse

| API | Semantics |
| --- | --- |
| mouse.x / mouse.y | World-space cursor position. |
| mouse.screenX / mouse.screenY | Raw canvas-pixel cursor position. |
| mouse.down(button) | Held button; 0 left, 1 middle, 2 right. |
| mouse.pressed(button) | Pressed this frame. |
| mouse.released(button) | Released this frame. |
| mouse.isOver(target) | Shape-accurate entity hit test. |
| mouse.clickedOn(target) | Hit test + pressed pulse. |

```
function onUpdate() {
  if (mouse.clickedOn(this.name)) {
    this.destroy(); // click this entity to pop it
  }
  // or, from inside the entity’s own script:
  if (this.isClicked) {
    this.sprite.opacity = 0.5;
  }
}
```

## Touch

The global `touch` surface is array-like. Each active touch has `id`, world/screen coordinates, start coordinates, `dx`, `dy`, `distance`, `justStarted` and `justEnded`.

```
function onUpdate() {
  for (var t of touch) {
    if (t.justStarted) {
      debug.log("Touch " + t.id, t.x + ", " + t.y);
    }
  }
  if (touch.tappedOn(this.name)) {
    this.spawn("Explosion", { x: this.x, y: this.y });
  }
}
```

## Gestures

| Gesture | Properties |
| --- | --- |
| touch.swipe | active, direction, dx, dy, distance; active after >40 px movement. |
| touch.pinch | active, scale, delta, distance for two-finger gestures. |

```
function onUpdate() {
  if (touch.swipe.active && touch.swipe.direction === "left") {
    scene.load("NextLevel");
  }
  if (touch.pinch.active) {
    this.camera.zoom *= touch.pinch.scale; // pinch-to-zoom
  }
}
```

## Virtual joysticks

The Joystick component exposes normalized read-only `x`, `y`, `magnitude`, `angle` and `active` values. This works well with Car controllers and custom movement scripts.

```
// Script attached to an entity with a Joystick component:
function onUpdate() {
  if (this.joystick.active) {
    this.controller.simulateMove(this.joystick.x, this.joystick.y);
  }
}
```
