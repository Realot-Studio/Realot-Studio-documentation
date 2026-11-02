# this (EntityContext) reference

> Complete reference for the current entity context, all flat shortcuts, pointer/touch helpers, navigation methods and per-entity script modules.

- Source: https://realot-studio.pages.dev/docs/api/this.html

## Transform shortcuts

Every entity has a Transform. These members read or write its live data; position values use world-space coordinates and rotation is in degrees.

| Member | Access | Meaning |
| --- | --- | --- |
| `x`, `y` | Read/write | World position coordinates. Writes also update the physics body's position target when a Rigidbody2D is attached. |
| `position` | Read/write | Gets or assigns an `{x, y}` object. |
| `rotation` | Read/write | Rotation in degrees. Kinematic bodies receive the script-set rotation target. |
| `scaleX`, `scaleY` | Read/write | Transform scale factors. |
| `translate(dx, dy)` | Method | Moves the entity by a relative world-space offset and synchronizes physics position targeting. |
| `distanceTo(x, y)` | Method | Returns straight-line distance from the entity to a world-space point. |
| `transform` | Sub-object | Always available; see [TransformAPI](script-modules.html#transformapi). |

## Identity, visibility and lifecycle members

| Member | Access | Meaning |
| --- | --- | --- |
| `name` | Read-only | Entity name. |
| `tag` | Read/write | Entity tag; can be changed while the game runs. |
| `id` | Read-only | Stable unique entity ID. Prefer this when you need to refer to one exact spawned instance. |
| `visible` | Read/write | Gets or sets the entity's active/visible state. |
| `enabled` | Read/write | Gets or sets the enabled state of the Script component attached to this entity. Without a Script component, reads as enabled. |
| `destroy()` | Method | Queues this entity for removal at the end of the current frame; it is not torn down in the middle of the callback. |
| `destroyed` | Read-only | True after destroy() is queued and before the entity is removed. |
| `hasComponent(componentKey)` | Method | Tests whether the entity currently has a component, for example `hasComponent("Rigidbody2D")`. Every entity has Transform. |
| `isClone` | Read-only | True for the context used by a script on an entity created by runtime `spawn()`. |
| `spawn(nameOrTagOrEntity, opts)` | Method | Creates a runtime clone. Accepts a name/tag lookup or an EntityContext. See [Finding and spawning](../scripting/finding-entities.html). |
| `wait(seconds, callback)`, `cancelWait(timerId)` | Methods | Start and cancel an entity-owned one-shot timer. |
| `repeat(seconds, callback)`, `cancelRepeat(timerId)` | Methods | Start and cancel an entity-owned repeating timer. |
| `releaseToPool(delay?)` | Method | Returns a pooled entity to its pool immediately or after an optional delay. |
| `isPooled` | Read-only | True when the entity was created and is managed by an object pool. |

## Pointer and touch helpers

These helpers test the current entity's actual Collider2D shape, not only its bounding rectangle. A **Collider2D is required**; without one these hit tests cannot match the pointer or a finger.

| Member | Meaning | Input |
| --- | --- | --- |
| `isPointerOver` | True while the mouse cursor is over this entity. | Mouse hover. |
| `isClicked` | True for the frame the left mouse button is pressed over this entity. | Mouse click. |
| `isTouchOver` | True while any active finger is over this entity. | Touch hover. |
| `isTapped` | True for the frame a finger first touches down over this entity. | Touch tap. |
| `myTouch` | Per-entity tracking for claiming and following one finger. The sub-object exists on every entity, but hit detection requires Collider2D. | See [TouchTrackAPI](script-modules.html#touchtrackapi). |

## Navigation movement methods

| Method | Requirements | Behavior |
| --- | --- | --- |
| `navMoveToward(targetX, targetY, speed?, opts?)` | NavWorld2D for pathfinding. NavAgent2D is optional but supplies radius, speed, repath, area and avoidance defaults. | Finds a path and advances the entity along it. It does not fall back to straight-line movement when no path exists. |
| `navDriveToward(targetX, targetY, speed?, opts?)` | Car-type CharacterController, NavWorld2D and NavAgent2D for the full vehicle tuning/agent behavior. | Follows a path using vehicle steering, lookahead, braking and recovery behavior. |

Use [Pathfinding](../scripting/navigation.html) and [Navigation: complete setup](../scripting/navigation-complete.html) for setup, options and examples.

## Component sub-objects

These modules are available only when the named component is attached to the same entity. Accessing a missing component module or misspelling a member produces a clear runtime API error. The generated [complete script-module index](script-modules.html) lists every exposed member and its read/write or method status.

| Script access | Required component | Reference |
| --- | --- | --- |
| `this.sprite` | SpriteRenderer | [SpriteRenderer](components/spriterenderer.html) |
| `this.shape` | ShapeRenderer | [ShapeRenderer](components/shaperenderer.html) |
| `this.text` | TextRenderer | [TextRenderer](components/textrenderer.html) |
| `this.strokePath` | StrokePath | [StrokePath](components/strokepath.html) |
| `this.speechBubble` | SpeechBubble | [SpeechBubble](components/speechbubble.html) |
| `this.chat` | ChatLog | [ChatLog](components/chatlog.html) |
| `this.textInput` | TextInput | [TextInput](components/textinput.html) |
| `this.joystick` | Joystick | [Joystick](components/joystick.html) |
| `this.rigidbody` | Rigidbody2D | [Rigidbody2D](components/rigidbody2d.html) |
| `this.collider` | Collider2D | [Collider2D](components/collider2d.html) |
| `this.joint` | Joint2D | [Joint2D](components/joint2d.html) |
| `this.controller` | CharacterController | [CharacterController](components/charactercontroller.html) |
| `this.animator` | SpriteAnimation | [SpriteAnimation](components/spriteanimation.html) |
| `this.camera` | Camera | [Camera](components/camera.html) |
| `this.audio` | AudioSource | [AudioSource](components/audiosource.html) |
| `this.ear` | AudioListener | [AudioListener](components/audiolistener.html) |
| `this.light` | Light | [Light](components/light.html) |
| `this.shadowCaster` | ShadowCaster | [ShadowCaster](components/shadowcaster.html) |
| `this.navAgent` | NavAgent2D | [NavAgent2D](components/navagent2d.html) |

## Always-available sub-objects

| Access | Availability | Reference |
| --- | --- | --- |
| `this.transform` | Every entity has Transform. | [TransformAPI](script-modules.html#transformapi) |
| `this.state` | Every entity; no Inspector component. Starts at state `default`. | [StateAPI](script-modules.html#stateapi) and [State & messaging](../scripting/state-messaging.html) |
| `this.myTouch` | Every entity; collider is needed for pointer/finger hit detection. | [TouchTrackAPI](script-modules.html#touchtrackapi) |

## Scene-level module

`scene.lighting` is not attached to `this`. It exposes scene-wide LightingSettings through the global `scene` object. When there is no LightingSettings component in the scene, reads use renderer defaults and writes have no effect. See [LightingSettingsAPI](script-modules.html#lightingsettingsapi) and [LightingSettings](components/lightingsettings.html).
