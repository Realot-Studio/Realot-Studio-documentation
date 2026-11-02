# Errors & debugging

> How script errors are classified and reported, and the on-screen debug HUD.

- Source: https://realot-studio.pages.dev/docs/scripting/errors.html

## How errors are reported

A thrown error inside one lifecycle call is caught right there and reported to the editor Console — it does not disable the whole script (except `onStart`, which only ever runs once). Identical errors repeating every frame are throttled: reported immediately once, then suppressed and periodically summarized with a repeat count, so a bug in `onUpdate` doesn’t spam the console 60 times a second.

## Error kinds

Errors thrown by the scripting API are tagged with a machine-readable `kind` so the Console can show a specific, actionable message instead of a generic "X is not a function":

| Kind | Meaning | Example |
| --- | --- | --- |
| missing-component | Accessed this.rigidbody/.sprite/etc. but the entity does not have that component at all. | this.sprite.opacity on an entity with no Sprite Renderer |
| unsupported-body-type | Called a member that does not apply to this entity’s current body/controller type. | this.rigidbody.addForce() on a Kinematic or Static body |
| unknown-api | A property or method that does not exist at all — almost always a typo. | this.rigidbody.addFrce() |
| script-error | Anything without a kind — a plain script bug (null dereference, bad logic, etc). | — |

Every `unknown-api` error also lists the valid member names for that sub-object, so a typo is a one-line fix rather than a trip back to this documentation.

## The on-screen debug HUD

```
debug.show(); // turn the HUD on (visible in the Play window, not the editor console)
debug.showFps(false); // keep the HUD on but hide just the FPS line
debug.log("Target HP", this.hp);
debug.clear("Target HP");
debug.clearAll();
```
