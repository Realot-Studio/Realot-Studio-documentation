# Tuning guide

> Practical “increase/decrease this” rules for movement, physics, navigation, lighting, UI and path authoring.

- Source: https://realot-studio.pages.dev/docs/reference/tuning-guide.html

## How to tune movement

| Goal | Raise | Lower |
| --- | --- | --- |
| More responsive character movement | acceleration, airControl | acceleration, airControl |
| Longer/faster jump | jumpForce, maxJumps if desired | gravityScale / jumpForce |
| More stable vehicle | turn/brake smoothing, recovery settings | overly aggressive steering values |
| Faster NavAgent | speed, acceleration | stoppingDistance if you want it closer before stopping |

## How to tune physics

| Goal | Typical setting | Direction |
| --- | --- | --- |
| Make dynamic body fall faster | Rigidbody2D.gravityScale | Increase above 1. |
| Make body coast longer | linearDamping | Decrease toward 0. |
| Make body stop rotating sooner | angularDamping | Increase. |
| Make contact bouncier | Collider2D.restitution | Increase. |
| Reduce sliding | Collider2D.friction | Increase. |
| Make a platform one-way | Collider2D.isOneWayPlatform | Enable; contact filtering then only allows landing from the supported side. |

## How to tune navigation

| Setting | Increase means | Decrease means |
| --- | --- | --- |
| NavWorld2D.cellSize | coarser/faster grid, less geometric detail | finer grid, narrower detail but more work |
| NavAgent2D.radius | larger clearance requirement | smaller agent clearance |
| NavAgent2D.repathInterval | less frequent replanning | more responsive replanning |
| NavWorld2D.areaCosts slot | more expensive path cost through that area | closer to the cheapest route |

## How to tune lighting

| Setting | Increase means | Decrease means |
| --- | --- | --- |
| Light.intensity | brighter/stronger contribution | dimmer |
| Light.radius | larger influence region | tighter/localized light |
| ShadowCaster.length | longer shadow reach | shorter/contact shadow |
| ShadowCaster.softness | softer/wider penumbra | crisper edge |
| LightingSettings.raymarchSteps | more samples/detail, more GPU work | less GPU work, potentially less detail |
| LightingSettings.ambientDarkness | darker unlit regions | brighter ambient base |

> **Rule for numeric documentation:** Realot Studio documentation should state not only what a field is, but what increasing and decreasing it does, its units, default, and whether the value is clamped/validated. The API catalog in api-options.json follows this model for option objects.
