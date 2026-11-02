# Complete script module member index

> Complete source-verified member list for every script API module exposed by Realot Studio, including global utility modules and entity component APIs.

- Source: https://realot-studio.pages.dev/docs/api/script-modules.html

This is the complete member-name index for the script modules exposed by the supplied engine source. The allow-list in each module is the authority: entries not listed here are not part of that module’s supported script surface. Use the matching component page for full field meanings and examples.

## AnimatorAPI

**Access:** `this.animator`. **Requirement:** SpriteAnimation component. **Source:** `project/runtime/scripting/components/AnimatorAPI.js`.

| Member | Access | Purpose |
| --- | --- | --- |
| `currentClip` | Read-only property | The `this.animator` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `currentFrame` | Read/write property | The `this.animator` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `play(clipName)` | Method | The `this.animator` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `playing` | Read-only property | The `this.animator` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `speed` | Read/write property | The `this.animator` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `stop()` | Method | The `this.animator` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `totalFrames` | Read-only property | The `this.animator` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |

## AudioAPI

**Access:** `this.audio`. **Requirement:** AudioSource component. **Source:** `project/runtime/scripting/components/AudioAPI.js`.

| Member | Access | Purpose |
| --- | --- | --- |
| `pitch` | Read/write property | The `this.audio` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `play()` | Method | The `this.audio` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `playOnce()` | Method | The `this.audio` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `playing` | Read-only property | The `this.audio` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `stop()` | Method | The `this.audio` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `volume` | Read/write property | The `this.audio` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |

## AudioListenerAPI

**Access:** `this.ear`. **Requirement:** AudioListener component. **Source:** `project/runtime/scripting/components/AudioListenerAPI.js`.

| Member | Access | Purpose |
| --- | --- | --- |
| `canHear(nameOrTag, opts)` | Method | The `this.ear` sub-object exposed to user scripts (see scripting/ScriptAPI.js) — the query surface for the AudioListener component (see components/AudioListener.js). |
| `enabled` | Read/write property | The `this.ear` sub-object exposed to user scripts (see scripting/ScriptAPI.js) — the query surface for the AudioListener component (see components/AudioListener.js). |
| `radius` | Read/write property | The `this.ear` sub-object exposed to user scripts (see scripting/ScriptAPI.js) — the query surface for the AudioListener component (see components/AudioListener.js). |
| `sourcesInRange` | Read-only property | The `this.ear` sub-object exposed to user scripts (see scripting/ScriptAPI.js) — the query surface for the AudioListener component (see components/AudioListener.js). |

## CameraAPI

**Access:** `this.camera`. **Requirement:** Camera component. **Source:** `project/runtime/scripting/components/CameraAPI.js`.

| Member | Access | Purpose |
| --- | --- | --- |
| `allowStretching` | Read/write property | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `aspectMode` | Read/write property | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `aspectRatioLock` | Read/write property | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `backgroundColor` | Read/write property | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `barColor` | Read/write property | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `customHeight` | Read/write property | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `customWidth` | Read/write property | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `enablePseudo3D` | Read/write property | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `follow(entityTarget, opts)` | Method | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `integerScaling` | Read/write property | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `keepHeight` | Read/write property | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `landscapeHeight` | Read/write property | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `landscapeWidth` | Read/write property | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `letterboxing` | Read/write property | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `offsetX` | Read/write property | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `offsetY` | Read/write property | Follow/render Y offset. |
| `pillarboxing` | Read/write property | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `portraitHeight` | Read/write property | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `portraitWidth` | Read/write property | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `renderToSprite(spriteEntity)` | Method | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `scalingMode` | Read/write property | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `shake(intensity, duration)` | Method | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `squareSize` | Read/write property | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `stopFollow()` | Method | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `x` | Read/write property | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `y` | Read/write property | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `zoom` | Read/write property | The `this.camera` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |

## ChatLogAPI

**Access:** `this.chat`. **Requirement:** ChatLog component. **Source:** `project/runtime/scripting/components/ChatLogAPI.js`.

| Member | Access | Purpose |
| --- | --- | --- |
| `backgroundColor` | Read/write property | Background color. |
| `backgroundOpacity` | Read/write property | Background opacity. |
| `clear()` | Method | The `this.chat` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `fontFamily` | Read/write property | Font family. |
| `fontSize` | Read/write property | Font size. |
| `lineHeight` | Read/write property | Line height. |
| `maxMessages` | Read/write property | Maximum retained messages. |
| `messageColor` | Read/write property | Message color. |
| `messages` | Read-only property | The `this.chat` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `padding` | Read/write property | Padding. |
| `screenSpace` | Read/write property | Screen-space mode. |
| `send(sender, text, color)` | Method | The `this.chat` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `senderColor` | Read/write property | The `this.chat` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `showSender` | Read/write property | The `this.chat` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `visible` | Read/write property | Visibility. |
| `visibleCount` | Read/write property | Number of visible rows. |
| `width` | Read/write property | Panel width. |

## ColliderAPI

**Access:** `this.collider`. **Requirement:** Collider2D component. **Source:** `project/runtime/scripting/components/ColliderAPI.js`.

| Member | Access | Purpose |
| --- | --- | --- |
| `capsuleHalfHeight` | Read-only property | Capsule half-height. |
| `capsuleRadius` | Read-only property | Capsule radius. |
| `density` | Read-only property | Density. |
| `friction` | Read-only property | Friction. |
| `height` | Read-only property | Box height. |
| `isColliding(other)` | Method | The `this.collider` sub-object exposed to user scripts. |
| `isOneWayPlatform` | Read-only property | One-way platform flag. |
| `isTrigger` | Read/write property | Trigger-only collider. |
| `layer` | Read-only property | Layer index 0-15. |
| `mask` | Read-only property | 16-bit interaction mask. |
| `offset` | Read-only property | {x,y} collider offset. |
| `oneWayDirection` | Read/write property | The `this.collider` sub-object exposed to user scripts. |
| `radius` | Read-only property | Circle radius. |
| `restitution` | Read-only property | Restitution. |
| `rotation` | Read/write property | The `this.collider` sub-object exposed to user scripts. |
| `shape` | Read-only property | Box | Circle | Capsule | Triangle. |
| `width` | Read-only property | Box width. |

## ControllerAPI

**Access:** `this.controller`. **Requirement:** CharacterController component. This module combines members for several movement types; a member is available only when the component is set to a compatible type (Character, Platformer, Top-Down, Car, Follow or Patrol). Free mode exposes only its small common surface.. **Source:** `project/runtime/scripting/components/ControllerAPI.js`.

| Member | Access | Purpose |
| --- | --- | --- |
| `acceleration` | Read/write property | Acceleration. |
| `airControl` | Read/write property | Air-control factor. |
| `brakeForce` | Read/write property | Car brake force. |
| `canJump` | Read/write property | Whether jumping is available. |
| `controllerType` | Read-only property | Read-only movement type. |
| `driftFactor` | Read/write property | Car drift factor. |
| `driveTowardArriveDistance` | Read/write property | Member name confirmed by the module allow-list. See the corresponding component or scripting guide for usage details. |
| `facingDirection` | Read-only property | Current patrol facing direction. |
| `flipDirection()` | Method | Reverse Patrol direction. |
| `followDistance` | Read/write property | Follow distance. |
| `followSpeed` | Read/write property | Follow speed. |
| `gravityScale` | Read/write property | Gravity scale. |
| `groundAngle` | Read-only property | Ground angle. |
| `isGrounded` | Read-only property | Ground state. |
| `isOnCeiling` | Read-only property | Ceiling contact. |
| `isOnSlope` | Read-only property | Slope contact. |
| `isOnWall` | Read-only property | Wall contact. |
| `jumpForce` | Read/write property | Jump force. |
| `maxJumps` | Read/write property | Maximum jumps. |
| `maxSpeed` | Read/write property | Car maximum speed. |
| `moveSpeed` | Read/write property | Movement speed. |
| `patrolAxis` | Read/write property | Horizontal | Vertical. |
| `patrolDistance` | Read/write property | Patrol distance. |
| `patrolMode` | Read/write property | Platformer | Top-Down. |
| `simulateDrive(throttle, steer)` | Method | Drive a Car controller by script. |
| `simulateDriveJoystick(x, y)` | Method | Drive using joystick-style vector input. |
| `simulateDriveToward(x, y)` | Method | Drive toward a world point. |
| `simulateJump()` | Method | Request a jump. |
| `simulateMove(x, y)` | Method | Drive movement by script. |
| `targetName` | Read/write property | Follow target name. |
| `turnSpeed` | Read/write property | Car turn speed. |
| `useDefaultInput` | Read/write property | Built-in input mapping. |
| `useGravity` | Read/write property | Gravity toggle. |

## JointAPI

**Access:** `this.joint`. **Requirement:** Joint2D component. **Source:** `project/runtime/scripting/components/JointAPI.js`.

| Member | Access | Purpose |
| --- | --- | --- |
| `anchor1` | Read/write property | {x,y} local anchor on this body. |
| `anchor2` | Read/write property | {x,y} local anchor on connected body/world anchor. |
| `axis` | Read/write property | The `this.joint` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `breakForce` | Read/write property | Member name confirmed by the module allow-list. See the corresponding component or scripting guide for usage details. |
| `breakable` | Read/write property | The `this.joint` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `collideConnected` | Read/write property | Collision between connected bodies. |
| `connectedEntity` | Read/write property | Connected entity context, when one exists. |
| `damping` | Read/write property | Spring damping. |
| `disableConnectedCollision` | Read/write property | Member name confirmed by the module allow-list. See the corresponding component or scripting guide for usage details. |
| `enabled` | Read/write property | The `this.joint` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `flexibility` | Allow-listed but not implemented | The proxy allow-list contains this name, but the current JointAPI target has no getter or setter for it. Reads return undefined and writes do not update Joint2D.flexibility. Set Flexibility (%) in the Inspector instead. |
| `jointDrag` | Read/write property | The `this.joint` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `jointType` | Read/write property | Joint type. |
| `length` | Read/write property | The `this.joint` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `limitMax` | Read/write property | Maximum limit. |
| `limitMin` | Read/write property | Minimum limit. |
| `limitsEnabled` | Read/write property | The `this.joint` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `motorEnabled` | Read/write property | The `this.joint` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `motorMaxForce` | Read/write property | Maximum motor force. |
| `motorSpeed` | Read/write property | Motor speed. |
| `restStiffness` | Read/write property | The `this.joint` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `ropeMass` | Read/write property | Rope/spring segment mass. |
| `segmentCount` | Read/write property | The `this.joint` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `stiffness` | Read/write property | The `this.joint` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `textureFlip` | Read/write property | The `this.joint` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `textureKey` | Read/write property | The `this.joint` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `textureMode` | Read/write property | The `this.joint` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `textureOffset` | Read/write property | The `this.joint` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `textureScale` | Read/write property | The `this.joint` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `textureTiling` | Read/write property | The `this.joint` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `useTexture` | Read/write property | The `this.joint` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `visualColor` | Read/write property | Visual color. |
| `visualEnabled` | Read/write property | Visual enabled. |
| `visualThickness` | Read/write property | Visual thickness. |

## JoystickAPI

**Access:** `this.joystick`. **Requirement:** Joystick component. **Source:** `project/runtime/scripting/components/JoystickAPI.js`.

| Member | Access | Purpose |
| --- | --- | --- |
| `active` | Read-only property | The `this.joystick` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `angle` | Read-only property | The `this.joystick` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `baseColor` | Read/write property | Member name confirmed by the module allow-list. See the corresponding component or scripting guide for usage details. |
| `baseOpacity` | Read/write property | Member name confirmed by the module allow-list. See the corresponding component or scripting guide for usage details. |
| `baseRadius` | Read/write property | Base radius. |
| `deadZone` | Read/write property | The `this.joystick` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `hideWhenIdle` | Read/write property | The `this.joystick` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `idleOpacityMultiplier` | Read/write property | Member name confirmed by the module allow-list. See the corresponding component or scripting guide for usage details. |
| `knobColor` | Read/write property | Member name confirmed by the module allow-list. See the corresponding component or scripting guide for usage details. |
| `knobOpacity` | Read/write property | Member name confirmed by the module allow-list. See the corresponding component or scripting guide for usage details. |
| `knobRadius` | Read/write property | Knob radius. |
| `magnitude` | Read-only property | The `this.joystick` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `outlineColor` | Read/write property | Member name confirmed by the module allow-list. See the corresponding component or scripting guide for usage details. |
| `outlineWidth` | Read/write property | Member name confirmed by the module allow-list. See the corresponding component or scripting guide for usage details. |
| `positionMode` | Read/write property | Joystick positioning mode. |
| `regionHeight` | Read/write property | Region height. |
| `regionWidth` | Read/write property | Region width. |
| `regionX` | Read/write property | The `this.joystick` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `regionY` | Read/write property | Touch/pointer region Y. |
| `returnToCenter` | Read/write property | The `this.joystick` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `x` | Read-only property | The `this.joystick` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `y` | Read-only property | The `this.joystick` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |

## LightAPI

**Access:** `this.light`. **Requirement:** Light component. **Source:** `project/runtime/scripting/components/LightAPI.js`.

| Member | Access | Purpose |
| --- | --- | --- |
| `angle` | Read/write property | The `this.light` sub-object exposed to user scripts on any entity that has a Light component. |
| `castShadows` | Read/write property | The `this.light` sub-object exposed to user scripts on any entity that has a Light component. |
| `castsOnWorld` | Read/write property | The `this.light` sub-object exposed to user scripts on any entity that has a Light component. |
| `color` | Read/write property | The `this.light` sub-object exposed to user scripts on any entity that has a Light component. |
| `coreSize` | Read/write property | Light core size. |
| `coreVisible` | Read/write property | Show light core. |
| `flicker` | Read/write property | Flicker toggle. |
| `flickerDuration` | Read/write property | Flicker duration. |
| `flickerSpeed` | Read/write property | Flicker speed. |
| `height` | Read/write property | The `this.light` sub-object exposed to user scripts on any entity that has a Light component. |
| `intensity` | Read/write property | The `this.light` sub-object exposed to user scripts on any entity that has a Light component. |
| `radius` | Read/write property | The `this.light` sub-object exposed to user scripts on any entity that has a Light component. |
| `shadowColor` | Read/write property | The `this.light` sub-object exposed to user scripts on any entity that has a Light component. |
| `shadowStrength` | Read/write property | The `this.light` sub-object exposed to user scripts on any entity that has a Light component. |
| `type` | Read/write property | The `this.light` sub-object exposed to user scripts on any entity that has a Light component. |
| `width` | Read/write property | The `this.light` sub-object exposed to user scripts on any entity that has a Light component. |

## LightingSettingsAPI

**Access:** `scene.lighting`. **Requirement:** Scene lighting settings; exposed through the scene global. **Source:** `project/runtime/scripting/components/LightingSettingsAPI.js`.

| Member | Access | Purpose |
| --- | --- | --- |
| `ambientDarkness` | Read/write property | The `scene.lighting` sub-object exposed to user scripts (see scripting/ScriptAPI.js's getGlobals()) — lets scripts tune scene-wide lighting/shadow realism settings at runtime (see components/LightingSettings.js for the full field guide), e.g. |
| `glowStrength` | Read/write property | The `scene.lighting` sub-object exposed to user scripts (see scripting/ScriptAPI.js's getGlobals()) — lets scripts tune scene-wide lighting/shadow realism settings at runtime (see components/LightingSettings.js for the full field guide), e.g. |
| `raymarchSteps` | Read/write property | The `scene.lighting` sub-object exposed to user scripts (see scripting/ScriptAPI.js's getGlobals()) — lets scripts tune scene-wide lighting/shadow realism settings at runtime (see components/LightingSettings.js for the full field guide), e.g. |
| `shadowMode` | Read/write property | The `scene.lighting` sub-object exposed to user scripts (see scripting/ScriptAPI.js's getGlobals()) — lets scripts tune scene-wide lighting/shadow realism settings at runtime (see components/LightingSettings.js for the full field guide), e.g. |

## NavAgentAPI

**Access:** `this.navAgent`. **Requirement:** NavAgent2D component. **Source:** `project/runtime/scripting/components/NavAgentAPI.js`.

| Member | Access | Purpose |
| --- | --- | --- |
| `acceleration` | Read/write property | Acceleration. |
| `area` | Read/write property | Allowed area mask. |
| `areaCosts` | Read/write property | 16-entry area cost overrides. |
| `autoRepath` | Read/write property | Auto-repath. |
| `avoidanceEnabled` | Read/write property | Avoidance toggle. |
| `avoidancePriority` | Read/write property | Avoidance priority. |
| `collabEnabled` | Read/write property | Collaborative vehicle avoidance. |
| `collabGroupRadius` | Read/write property | Group radius. |
| `currentPath` | Read-only property | Read-only world-space waypoint array or null. |
| `currentPathIndex` | Read-only property | Read-only current waypoint index. |
| `deceleration` | Read/write property | Deceleration. |
| `radius` | Read/write property | Agent radius. |
| `repathDistance` | Read/write property | Target-move repath threshold. |
| `repathInterval` | Read/write property | Repath interval. |
| `speed` | Read/write property | Preferred speed. |
| `stoppingDistance` | Read/write property | Stopping distance. |
| `vehicleCornerLookahead` | Read/write property | Corner lookahead. |
| `vehicleCornerSlowdown` | Read/write property | Corner slowdown. |
| `vehicleLookahead` | Read/write property | Vehicle lookahead. |
| `vehicleObstacleBrake` | Read/write property | Obstacle brake factor. |
| `vehicleObstacleLookahead` | Read/write property | Obstacle lookahead. |
| `vehicleObstacleWidth` | Read/write property | Obstacle width. |
| `vehicleRecoveryReverseTime` | Read/write property | Reverse recovery time. |
| `vehicleRecoveryTime` | Read/write property | Recovery time. |
| `vehicleSpeedSmoothing` | Read/write property | Speed smoothing. |
| `vehicleSteerSmoothing` | Read/write property | Steering smoothing. |

## RigidbodyAPI

**Access:** `this.rigidbody`. **Requirement:** Rigidbody2D component. **Source:** `project/runtime/scripting/components/RigidbodyAPI.js`.

| Member | Access | Purpose |
| --- | --- | --- |
| `addAngularImpulse(t)` | Method | The `this.rigidbody` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `addForce(x, y)` | Method | The `this.rigidbody` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `addForceAtPoint(x, y, pointX, pointY)` | Method | The `this.rigidbody` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `addImpulse(x, y)` | Method | The `this.rigidbody` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `addTorque(t)` | Method | The `this.rigidbody` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `angularDamping` | Read/write property | Angular damping. |
| `gravityScale` | Read/write property | Gravity multiplier. |
| `groundAngle` | Read-only property | The `this.rigidbody` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `groundAngleLimit` | Read/write property | The `this.rigidbody` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `grounded` | Read-only property | The `this.rigidbody` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `isGrounded` | Read-only property | The `this.rigidbody` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `isOnCeiling` | Read-only property | The `this.rigidbody` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `isOnSlope` | Read-only property | The `this.rigidbody` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `isOnWall` | Read-only property | The `this.rigidbody` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `linearDamping` | Read/write property | Linear damping. |
| `mass` | Read/write property | Dynamic mass. |
| `move(dx, dy)` | Method | The `this.rigidbody` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `resolvedVelocity` | Read-only property | The `this.rigidbody` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `slopeMinAngle` | Read/write property | The `this.rigidbody` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `type` | Read/write property | Dynamic | Kinematic | Static; switching type is supported at runtime. |
| `velocity` | Read/write property | {x,y} velocity. |
| `velocityX` | Read/write property | Horizontal velocity. |
| `velocityY` | Read/write property | Vertical velocity. |
| `wallAngleLimit` | Read/write property | The `this.rigidbody` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |

## SaveAPI

**Access:** `save`. **Requirement:** Global save store; no entity component required. **Source:** `project/runtime/scripting/components/SaveAPI.js`.

| Member | Access | Purpose |
| --- | --- | --- |
| `clear()` | Method | The `save` global exposed to user scripts (see scripting/ScriptAPI.js getGlobals()). |
| `delete(key)` | Method | The `save` global exposed to user scripts (see scripting/ScriptAPI.js getGlobals()). |
| `deleteSlot(slotName)` | Method | The `save` global exposed to user scripts (see scripting/ScriptAPI.js getGlobals()). |
| `flushNow()` | Method | The `save` global exposed to user scripts (see scripting/ScriptAPI.js getGlobals()). |
| `get(key)` | Method | The `save` global exposed to user scripts (see scripting/ScriptAPI.js getGlobals()). |
| `has(key)` | Method | The `save` global exposed to user scripts (see scripting/ScriptAPI.js getGlobals()). |
| `isReady` | Read-only property | The `save` global exposed to user scripts (see scripting/ScriptAPI.js getGlobals()). |
| `keys()` | Method | The `save` global exposed to user scripts (see scripting/ScriptAPI.js getGlobals()). |
| `listSlots()` | Method | The `save` global exposed to user scripts (see scripting/ScriptAPI.js getGlobals()). |
| `load(slotName)` | Method | The `save` global exposed to user scripts (see scripting/ScriptAPI.js getGlobals()). |
| `onError(callback)` | Method | The `save` global exposed to user scripts (see scripting/ScriptAPI.js getGlobals()). |
| `set(key, value)` | Method | The `save` global exposed to user scripts (see scripting/ScriptAPI.js getGlobals()). |
| `slot` | Read-only property | The `save` global exposed to user scripts (see scripting/ScriptAPI.js getGlobals()). |

## ShadowCasterAPI

**Access:** `this.shadowCaster`. **Requirement:** ShadowCaster component. **Source:** `project/runtime/scripting/components/ShadowCasterAPI.js`.

| Member | Access | Purpose |
| --- | --- | --- |
| `enabled` | Read/write property | The `this.shadowCaster` sub-object exposed to user scripts on any entity that has a ShadowCaster component (see components/ShadowCaster.js). |
| `height` | Read/write property | The `this.shadowCaster` sub-object exposed to user scripts on any entity that has a ShadowCaster component (see components/ShadowCaster.js). |
| `length` | Read/write property | The `this.shadowCaster` sub-object exposed to user scripts on any entity that has a ShadowCaster component (see components/ShadowCaster.js). |
| `offsetX` | Read/write property | The `this.shadowCaster` sub-object exposed to user scripts on any entity that has a ShadowCaster component (see components/ShadowCaster.js). |
| `offsetY` | Read/write property | The `this.shadowCaster` sub-object exposed to user scripts on any entity that has a ShadowCaster component (see components/ShadowCaster.js). |
| `opacity` | Read/write property | The `this.shadowCaster` sub-object exposed to user scripts on any entity that has a ShadowCaster component (see components/ShadowCaster.js). |
| `softness` | Read/write property | The `this.shadowCaster` sub-object exposed to user scripts on any entity that has a ShadowCaster component (see components/ShadowCaster.js). |
| `width` | Read/write property | The `this.shadowCaster` sub-object exposed to user scripts on any entity that has a ShadowCaster component (see components/ShadowCaster.js). |

## ShapeAPI

**Access:** `this.shape`. **Requirement:** ShapeRenderer component. **Source:** `project/runtime/scripting/components/ShapeAPI.js`.

| Member | Access | Purpose |
| --- | --- | --- |
| `capsuleHalfHeight` | Read/write property | The `this.shape` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `capsuleRadius` | Read/write property | The `this.shape` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `fillColor` | Read/write property | The `this.shape` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `height` | Read/write property | The `this.shape` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `opacity` | Read/write property | The `this.shape` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `outlineColor` | Read/write property | The `this.shape` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `outlineEnabled` | Read/write property | The `this.shape` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `outlineWidth` | Read/write property | The `this.shape` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `radius` | Read/write property | The `this.shape` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `shapeType` | Read/write property | The `this.shape` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `visualRotation` | Read/write property | The `this.shape` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `width` | Read/write property | The `this.shape` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |

## SpeechBubbleAPI

**Access:** `this.speechBubble`. **Requirement:** SpeechBubble component. **Source:** `project/runtime/scripting/components/SpeechBubbleAPI.js`.

| Member | Access | Purpose |
| --- | --- | --- |
| `backgroundColor` | Read/write property | Background color. |
| `borderColor` | Read/write property | Border color. |
| `borderWidth` | Read/write property | Border width. |
| `cornerRadius` | Read/write property | Corner radius. |
| `fontFamily` | Read/write property | Font family. |
| `fontSize` | Read/write property | Font size. |
| `hide()` | Method | The `this.speechBubble` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `maxWidth` | Read/write property | The `this.speechBubble` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `offsetX` | Read/write property | The `this.speechBubble` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `offsetY` | Read/write property | Vertical offset. |
| `padding` | Read/write property | Padding. |
| `show(text, duration)` | Method | The `this.speechBubble` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `tailDirection` | Read/write property | The `this.speechBubble` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `tailSize` | Read/write property | Tail size. |
| `text` | Read/write property | The `this.speechBubble` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `textColor` | Read/write property | Text color. |
| `visible` | Read/write property | The `this.speechBubble` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |

## SpriteAPI

**Access:** `this.sprite`. **Requirement:** SpriteRenderer component. **Source:** `project/runtime/scripting/components/SpriteAPI.js`.

| Member | Access | Purpose |
| --- | --- | --- |
| `color` | Read/write property | Hex tint color. |
| `flipX` | Read/write property | Horizontal mirror. |
| `flipY` | Read/write property | Vertical mirror. |
| `opacity` | Read/write property | The `this.sprite` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `texture` | Read/write property | Sprite asset key. |
| `visualRotation` | Read/write property | The `this.sprite` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |

## StateAPI

**Access:** `this.state`. **Requirement:** Available on every entity; no component required. **Source:** `project/runtime/scripting/components/StateAPI.js`.

| Member | Access | Purpose |
| --- | --- | --- |
| `change(name)` | Method | The `this.state` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `current` | Read-only property | The `this.state` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `previous` | Read-only property | The `this.state` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |

## StrokePathAPI

**Access:** `this.strokePath`. **Requirement:** StrokePath component. **Source:** `project/runtime/scripting/components/StrokePathAPI.js`.

| Member | Access | Purpose |
| --- | --- | --- |
| `addPoint(x, y)` | Method | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `capMode` | Read/write property | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `color` | Read/write property | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `firstPoint` | Read-only property | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `getLength()` | Method | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `getPoint(index)` | Method | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `insertPoint(index, x, y)` | Method | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `jointMode` | Read/write property | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `lastPoint` | Read-only property | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `localToWorld(localX, localY)` | Method | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `opacity` | Read/write property | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `pointCount` | Read-only property | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `points` | Read/write property | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `removePoint(index)` | Method | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `setPoint(index, x, y)` | Method | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `textureFlip` | Read/write property | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `textureKey` | Read/write property | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `textureMode` | Read/write property | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `textureOffset` | Read/write property | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `textureRotation` | Read/write property | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `textureScale` | Read/write property | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `textureTiling` | Read/write property | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `thickness` | Read/write property | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `useTexture` | Read/write property | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `worldToLocal(worldX, worldY)` | Method | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |

## TextAPI

**Access:** `this.text`. **Requirement:** TextRenderer component. **Source:** `project/runtime/scripting/components/TextAPI.js`.

| Member | Access | Purpose |
| --- | --- | --- |
| `align` | Read/write property | The `this.text` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `anchorX` | Read/write property | The `this.text` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `anchorY` | Read/write property | Vertical anchor. |
| `bold` | Read/write property | Bold toggle. |
| `color` | Read/write property | Hex text color. |
| `fontFamily` | Read/write property | Font family. |
| `fontSize` | Read/write property | Font size. |
| `italic` | Read/write property | Italic toggle. |
| `opacity` | Read/write property | The `this.text` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `screenSpace` | Read/write property | The `this.text` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `value` | Read/write property | The `this.text` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `wordWrap` | Read/write property | Enable word wrapping. |
| `wrapWidth` | Read/write property | The `this.text` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |

## TextInputAPI

**Access:** `this.textInput`. **Requirement:** TextInput component. **Source:** `project/runtime/scripting/components/TextInputAPI.js`.

| Member | Access | Purpose |
| --- | --- | --- |
| `backgroundColor` | Read/write property | Background color. |
| `borderColor` | Read/write property | Border color. |
| `borderWidth` | Read/write property | Border width. |
| `clear()` | Method | The `this.textInput` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `clearOnSubmit` | Read/write property | The `this.textInput` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `cornerRadius` | Read/write property | Corner radius. |
| `focused` | Read-only property | The `this.textInput` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `fontFamily` | Read/write property | Font family. |
| `fontSize` | Read/write property | Font size. |
| `height` | Read/write property | Control height. |
| `justSubmitted` | Read-only property | The `this.textInput` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `maxLength` | Read/write property | Character cap. |
| `padding` | Read/write property | Padding. |
| `placeholder` | Read/write property | Placeholder. |
| `placeholderColor` | Read/write property | Placeholder color. |
| `textColor` | Read/write property | Text color. |
| `value` | Read/write property | The `this.textInput` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `width` | Read/write property | Control width. |

## TouchTrackAPI

**Access:** `this.myTouch`. **Requirement:** Available on every entity; no component required. **Source:** `project/runtime/scripting/components/TouchTrackAPI.js`.

| Member | Access | Purpose |
| --- | --- | --- |
| `active` | Read-only property | The `this.myTouch` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `disable()` | Method | The `this.myTouch` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `enable()` | Method | The `this.myTouch` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `enabled` | Read-only property | The `this.myTouch` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `startTracking()` | Method | The `this.myTouch` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `stopTracking()` | Method | The `this.myTouch` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `x` | Read-only property | The `this.myTouch` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `y` | Read-only property | The `this.myTouch` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |

## TransformAPI

**Access:** `this.transform`. **Requirement:** Available on every entity; no component required. **Source:** `project/runtime/scripting/components/TransformAPI.js`.

| Member | Access | Purpose |
| --- | --- | --- |
| `lookAt(x, y)` | Method | Point the entity toward a world-space point. |
| `position` | Read/write property | { x, y } world-space position; read or assign. |
| `rotation` | Read/write property | Rotation in degrees. |
| `scale` | Read/write property | Member name confirmed by the module allow-list. See the corresponding component or scripting guide for usage details. |
| `translate(dx, dy)` | Method | Move by a delta amount. |

## Global runtime objects and functions

The global runtime API is separate from per-entity component modules. The exact global members and common option shapes are described in [Runtime modules](runtime.html), [Global API](../scripting/globals.html), [Input](../scripting/input.html), and [Persistence](../scripting/persistence.html).

### Entity lookup functions

- `findFirst(name)`
- `findAll(name)`
- `findFirstWithTag(tag)`
- `findAllWithTag(tag)`
- `findWithTag(tag)`
- `findById(id)`
- `findInRadius(x, y, radius, opts)`

### Scene (`scene`)

- `findFirst(name)`
- `findAll(name)`
- `findFirstWithTag(tag)`
- `findAllWithTag(tag)`
- `findWithTag(tag)`
- `findById(id)`
- `load(sceneName)`
- `restart()`
- `pause()`
- `resume()`
- `isPaused (read-only)`
- `current (read-only)`
- `lighting`

### Physics (`physics`)

- `raycast(x1, y1, x2, y2, opts)`
- `layer(...indices)`

### Navigation (`nav`)

- `findPath(x1, y1, x2, y2, opts)`
- `isWalkable(x, y)`
- `bake()`
- `areaIndex(name)`
- `areaMask(...names)`
- `areaCosts(costsByName)`

### Input (`input`)

- `keyDown(key)`
- `keyPressed(key)`

### Mouse (`mouse`)

- `x, y (world-space)`
- `screenX, screenY (canvas pixels)`
- `over (read-only)`
- `down(button?)`
- `pressed(button?)`
- `released(button?)`
- `isOver(entityOrName, opts)`
- `clickedOn(entityOrName, opts, button?)`

### Touch (`touch`)

- `count, first, anyJustStarted, anyJustEnded`
- `per-touch: id, x, y, screenX, screenY, startX, startY, dx, dy, distance, justStarted, justEnded`
- `swipe: active, direction, dx, dy, distance`
- `pinch: active, scale, delta, distance`
- `isOver(entityOrName, opts)`
- `tappedOn(entityOrName, opts)`

### Time (`time`)

- `deltaTime`
- `unscaledDeltaTime`
- `elapsed`
- `scale`

### Random (`random`)

- `int(min, max)`
- `float(min, max)`

### Math helpers (`mathx`)

- `lerp(a, b, t)`
- `smoothstep(a, b, value)`
- `clamp(value, min, max)`
- `moveToward(current, target, maxDelta)`
- `remap(value, inMin, inMax, outMin, outMax)`
- `approximately(a, b, epsilon?)`

### Global state (`global`)

- `Read, write and test arbitrary named in-memory values shared by scripts; resets when the game page is reloaded.`

### Debug HUD (`debug`)

- `show(on?)`
- `showFps(on?)`
- `log(label, value)`
- `clear(label)`
- `clearAll()`

### Object pools (`pool`)

- `create(name, options)`
- `find(name)`
- `get(name, x, y)`
- `release(entity)`

### Global functions

- `spawn(nameOrTag, opts)`
- `wait(seconds, callback)`
- `cancelWait(timerId)`
- `repeat(seconds, callback)`
- `cancelRepeat(timerId)`
- `sendMessage(tagOrEntity, message, data)`
- `broadcastMessage(message, data)`
- `tween(target, properties, duration, easing?, onComplete?)`
- `cancelTween(tweenId)`
- `smoothstep(a, b, value)`
