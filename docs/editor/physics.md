# Physics authoring

> Configure rigid bodies, colliders, joints, layers and one-way platforms.

- Source: https://realot-studio.pages.dev/docs/editor/physics.html

> **Exact control path:** Physics components are added from Inspector → Add Component (Rigidbody 2D, Collider 2D, Joint 2D, Movement Type). Global named physics layer slots are edited at Edit → Physics Layers… .

## Rigid bodies

| Body type | Typical responsibility |
| --- | --- |
| Dynamic | Physics solver controls movement; scripts apply forces/impulses or read/write velocity. |
| Kinematic | Scripts/controllers request movement; collision resolution produces contact state. |
| Static | Fixed world geometry; no dynamic motion. |

## Colliders

Collider2D supports Box, Circle, Capsule and Triangle shapes. You can enable triggers, one-way platforms, friction/restitution, density, offsets and 16-layer collision filtering.

## Collision layers

Each collider belongs to one layer (0-15) and exposes a 16-bit mask of layers it can interact with. A raycast can use `physics.layer(…)` to build the same mask model for query filtering.

## Joints

Joint2D supports Fixed, Revolute, Prismatic, Rope and Spring. Rope and Spring use multi-segment chains for visual/physical behavior and expose anchors, length, stiffness/damping and optional motors/limits.

## One-way platforms

> **Direction matters:** A one-way platform is a Collider2D with isOneWayPlatform = true . The physics system distinguishes pass-through movement from the blocking direction, so the behavior should be tested with the body moving from both sides.
