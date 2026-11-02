# API requirements & complete usage map

> Complete prerequisites and usage map for Realot Studio scripting APIs.

- Source: https://realot-studio.pages.dev/docs/api/requirements.html

> **Prerequisites matter.:** Realot Studio does not expose every component API on every entity. this.sprite , this.rigidbody , this.navAgent , and the other component sub-objects are created only when the corresponding component exists on that same entity. If the component is absent, the sub-object is undefined . Use this.hasComponent("...") when you need to guard optional behavior.

## Universal component-API workflow

1. Select the entity in the **Hierarchy**.
2. In the **Inspector** on the right, click **Add Component**.
3. Search for the required component and click it.
4. Configure its Inspector properties and any component-specific editor tool that appears.
5. Add a **Script** component to the same entity and open/edit its script.
6. Inside the script, access the matching sub-object, for example `this.rigidbody` or `this.sprite`.
7. Play the scene and inspect the Console if the component is missing or an API call is invalid.

```
// Example: Rigidbody2D is required for this API.
function onStart() {
  if (!this.rigidbody) return;
  this.rigidbody.velocity = { x: 100, y: 0 };
}
```

## Global APIs — no component required

These are injected into every running game script. They are not added through **Add Component**.

- `enabled`
- `showFps`
- `stats`
- `debugLines`
- `entity`
- `point`
- `normal`
- `distance`
- `findWithTag`
- `findFirst`
- `findAll`
- `findFirstWithTag`
- `findAllWithTag`
- `findById`
- `findInRadius`
- `scene`
- `physics`
- `nav`
- `sendMessage`
- `broadcastMessage`
- `spawn`
- `wait`
- `cancelWait`
- `repeat`
- `cancelRepeat`
- `input`
- `mouse`
- `touch`
- `time`
- `random`
- `smoothstep`
- `mathx`
- `global`
- `save`
- `debug`

| Global family | Required setup | Typical use |
| --- | --- | --- |
| `scene` | A running scene. | Load/restart/pause/resume scenes and access scene-level services. |
| `physics` | Physics runtime for physics queries. | Raycasts and collision-layer/mask operations. |
| `nav` | Configured Nav World 2D for meaningful pathfinding. | Find paths, test walkability, use named navigation areas/costs. |
| `input`, `mouse`, `touch` | Running game input; touch requires a touch-capable device for actual touch events. | Keyboard, mouse, touch, swipe and pinch controls. |
| `time`, `random`, `mathx` | None. | Frame timing, randomness and gameplay math. |
| `save` | Browser storage available to the deployment. | Persistent save slots. |
| `debug` | Running game/editor debug surface. | Debug messages and visual diagnostics. |
| `spawn`, `wait`, `repeat` | Running entity script/runtime. | Runtime clones and entity-owned timers. |
| `sendMessage`, `broadcastMessage` | Running scene with target entities when targeting by name/tag. | Script-to-script communication. |

## Component APIs — prerequisites and members

| API | Required setup | Public members found in the runtime API module |
| --- | --- | --- |
| `SpriteAnimation` | Add a Sprite Animation component to the same entity before using this.animator. | `reset, playing, currentClip, currentFrame, totalFrames, speed, it, trap, property, directly` |
| `AudioSource` | Add an Audio Source component to the same entity before using this.audio. | `volume, pitch, playing, to, trap, directly` |
| `AudioListener` | Add an Audio Listener component to the same entity before using this.ear. | `radius, enabled, sourcesInRange, check` |
| `Camera` | Add a Camera component to the same entity before using this.camera. | `zoom, backgroundColor, aspectMode, landscapeWidth, landscapeHeight, portraitWidth, portraitHeight, squareSize, customWidth, customHeight, enablePseudo3D, scalingMode, keepHeight, aspectRatioLock, allowStretching, letterboxing, pillarboxing, barColor, integerScaling, x, y, entity, center, each, offsetX, offsetY, applies, is, that, by, from, the, of` |
| `ChatLog` | Add a Chat Log component to the same entity before using this.chat. | `messages, maxMessages, visibleCount, width, lineHeight, fontSize, fontFamily, messageColor, senderColor, backgroundColor, backgroundOpacity, padding, showSender, screenSpace, visible, directly` |
| `Collider2D` | Add a Collider 2D component to the same entity before using this.collider. | `shape, width, height, radius, capsuleHalfHeight, capsuleRadius, offset, isTrigger, isOneWayPlatform, friction, restitution, density, layer, mask, isColliding, get, set` |
| `CharacterController` | Add a Character Controller component to the same entity before using this.controller. | `heading, directional, it, controllerType, moveSpeed, acceleration, airControl, useGravity, gravityScale, useDefaultInput, maxSpeed, brakeForce, turnSpeed, driftFactor, driveTowardArriveDistance, patrolDistance, patrolMode, patrolAxis, targetName, followSpeed, followDistance, of, every, directly, if` |
| `Joint2D` | Add a Joint 2D component to the same entity before using this.joint. | `jointType, connectedEntity, anchor1, anchor2, axis, length, stiffness, damping, segmentCount, ropeMass, visualEnabled, visualColor, visualThickness, useTexture, textureKey, textureMode, textureTiling, textureScale, textureOffset, textureFlip, limitsEnabled, limitMin, limitMax, motorEnabled, motorSpeed, motorMaxForce, collideConnected, enabled, key, get, set` |
| `Joystick` | Add a Joystick component to the same entity before using this.joystick. | `x, y, magnitude, angle, active, positionMode, regionX, regionY, regionWidth, regionHeight, baseRadius, knobRadius, baseColor, baseOpacity, knobColor, knobOpacity, outlineColor, outlineWidth, deadZone, returnToCenter, hideWhenIdle, idleOpacityMultiplier, directly` |
| `Light` | Add a Light component to the same entity before using this.light. | `type, color, intensity, radius, angle, width, height, castsOnWorld, castShadows, shadowColor, shadowStrength, flicker, flickerSpeed, flickerDuration, coreSize, coreVisible, for, on` |
| `LightingSettings` | Use the global <code>scene.lighting</code> surface; it is not an ordinary entity component API. | `shadowMode, raymarchSteps, ambientDarkness, glowStrength` |
| `NavAgent2D` | Add a Nav Agent 2D component to the same entity for this.navAgent. A Nav World 2D must also be configured for actual pathfinding. | `radius, speed, acceleration, deceleration, stoppingDistance, autoRepath, repathInterval, repathDistance, avoidanceEnabled, avoidancePriority, collabEnabled, collabGroupRadius, vehicleLookahead, vehicleCornerLookahead, vehicleObstacleLookahead, vehicleObstacleWidth, vehicleSteerSmoothing, vehicleSpeedSmoothing, vehicleCornerSlowdown, vehicleObstacleBrake, vehicleRecoveryTime, vehicleRecoveryReverseTime, area, areaCosts, currentPath, currentPathIndex, here, get, set` |
| `Rigidbody2D` | Add a Rigidbody 2D component to the same entity before using this.rigidbody. | `x, type, silently, velocity, velocityX, velocityY, mass, gravityScale, linearDamping, angularDamping, isGrounded, grounded, isOnCeiling, isOnWall, isOnSlope, groundAngle, resolvedVelocity, groundAngleLimit, wallAngleLimit, slopeMinAngle, it, property, directly, for, if` |
| `ShadowCaster` | Add a Shadow Caster component to the same entity before using this.shadowCaster. | `enabled, width, height, offsetX, offsetY, opacity, length, softness, its, from` |
| `ShapeRenderer` | Add a Shape Renderer component to the same entity before using this.shape. | `shapeType, width, height, radius, capsuleHalfHeight, capsuleRadius, fillColor, opacity, outlineEnabled, outlineColor, outlineWidth, trap, directly` |
| `SpeechBubble` | Add a Speech Bubble component to the same entity before using this.speechBubble. | `text, visible, backgroundColor, textColor, borderColor, borderWidth, fontSize, fontFamily, padding, cornerRadius, maxWidth, offsetX, offsetY, tailDirection, tailSize, from, directly` |
| `SpriteRenderer` | Add a Sprite Renderer component to the same entity before using this.sprite. | `texture, color, flipX, flipY, opacity, directly` |
| `State` | See complete reference. | `current, previous, to, at` |
| `StrokePath` | Add a Stroke Path component to the same entity before using this.strokePath. | `points, thickness, color, opacity, useTexture, textureKey, textureMode, textureTiling, textureScale, textureOffset, textureFlip, textureRotation, jointMode, capMode, pointCount, firstPoint, lastPoint, for, by, to, key, getLength, getPoint, setPoint, addPoint, insertPoint, removePoint, worldToLocal, localToWorld` |
| `TextRenderer` | Add a Text Renderer component to the same entity before using this.text. | `value, fontSize, color, fontFamily, bold, italic, align, anchorX, anchorY, opacity, screenSpace, wordWrap, wrapWidth, directly` |
| `TextInput` | Add a Text Input component to the same entity before using this.textInput. | `value, placeholder, maxLength, fontSize, fontFamily, textColor, placeholderColor, backgroundColor, borderColor, borderWidth, cornerRadius, width, height, padding, clearOnSubmit, focused, justSubmitted, directly` |
| `Transform` | Every entity has a Transform; this.transform is therefore available on normal entity scripts. | `position, doc, rotation, scale, trap` |
| `StateAPI` | Available as `this.state` on entity scripts; no separate component is required. | `current, previous` plus state-transition behavior documented in State & messaging. |
| `TouchTrackAPI` | Available as `this.myTouch` for the scripted entity; touch input must be enabled/available in the runtime. | `active, enabled, x, y` |
| `SaveAPI` | Available as global `save`; no entity component is required. Persistent storage depends on the browser/deployment environment. | `isReady, slot` |

## Entity context APIs

Inside lifecycle functions such as `onStart()` and `onUpdate(dt)`, `this` is the current entity context. Core transform shortcuts such as `this.x`, `this.y`, `this.position`, `this.rotation`, `this.scaleX` and `this.scaleY` are available without adding a separate Transform component.

Other capabilities are deliberately grouped under their component sub-object: `this.rigidbody`, `this.collider`, `this.joint`, `this.controller`, `this.sprite`, `this.animator`, `this.camera`, `this.audio`, `this.ear`, `this.navAgent`, `this.light`, `this.shadowCaster`, `this.strokePath`, and the UI APIs documented above.

## Guarding optional components

```
function onUpdate(dt) {{
  if (this.hasComponent("Rigidbody2D")) {{
    // Safe to use this.rigidbody here.
    this.rigidbody.velocityX = 100;
  }}
}}
```

Use the exact component name expected by the engine. For systems with additional world-level prerequisites—especially navigation—having the entity component is necessary but not sufficient.

## How to read opts

Whenever a function accepts an `opts` object, the reference must be read as a contract: each property has a type, default, allowed/meaningful range, and effect. Omitted properties use the documented default. Options that are explicitly per-call do not permanently rewrite the component or world setting unless the API says they do.

```
const path = nav.findPath(startX, startY, goalX, goalY, {{
  radius: 18,
  area: nav.areaMask("Ground", "Road"),
  areaCosts: nav.areaCosts({{ Mud: 4 }}),
  debug: true
}});
```

For navigation, configure the world and areas in the editor first, then use script options to select/override behavior for the particular query. See [Navigation: complete setup](../scripting/navigation-complete.html) for the complete editor-to-script workflow.

## Source-of-truth rule

This page and the individual API references describe the public game-script contract implemented by the supplied runtime source. Internal editor classes, renderer internals, and private helper functions are not presented as supported game APIs simply because they exist in the source tree.
