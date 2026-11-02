# NavAgent2D

> Realot Studio NavAgent2D component reference: fields, script API, behavior and examples.

- Source: https://realot-studio.pages.dev/docs/api/components/navagent2d.html

> **Scope:** This page documents the NavAgent2D component in Realot Studio. Runtime fields are serialized scene data; the Script API section lists only members intentionally exposed to game scripts.

> **Where to find it in the editor:** Inspector → Add Component → Nav Agent 2D. For radius and area painting, use the Nav toolbar after a Nav World 2D exists; Match Collider is in the Nav Agent inspector section.

## What it does

Per-agent navigation settings and current path state for NavWorld2D pathfinding.

> **Component setup & editor tools:** NavAgent2D is the moving-agent side of Realot Studio navigation. It works with NavWorld2D and the navigation API.

## How to add and use NavAgent2D

**Editor path:** Select the target entity in the **Hierarchy** (left side) → look at the **Inspector** (right side) → click **Add Component** at the bottom of the Inspector → search for **NavAgent2D** → click the component row. The Add Component picker is a centered modal with a search box; it only lists components not already attached.

For components with a dedicated editor tool, the tool is opened or activated from the location described below. Do not assume that adding the component alone activates its editor; some systems require a separate window, panel, or viewport tool.

## Component setup & editor tools

- Select the agent → Inspector → Add Component → Nav Agent 2D. Configure agent parameters, then use the NavWorld2D + navigation workflow before expecting paths. Runtime movement is driven by the NavAgent2D API.

### What you should see after adding it

The component appears as its own section in the Inspector. Its serialized settings are listed in the **Component data** table below. If a field is conditional, it appears only when the relevant mode/type is selected. If a field is a runtime state field (for example grounded or resolved velocity), treat it as read-only diagnostic state unless the API reference explicitly documents it as writable.

### How to read the settings

For every setting below, the documentation distinguishes **type**, **default**, **meaning**, and tuning direction where behavior is known. When a value represents a direction, use the engine's coordinate convention documented in [Coordinate system](../../reference/coordinate-system.html); do not substitute Unity/Godot conventions.

## Component data

| Field | Type | Purpose | Default |
| --- | --- | --- | --- |
| `radius` | number | Agent px clearance this agent needs from obstacles/other geometry. | `16` |
| `speed` | number | Movement px/s top move speed | `120` |
| `acceleration` | number | px/s^2 — how fast the agent speeds up toward `speed` | `800` |
| `deceleration` | number | px/s^2 — how fast the agent slows when arriving/stopping | `1000` |
| `stoppingDistance` | number | px from the final target that counts as arrived | `1` |
| `autoRepath` | boolean | Pathfinding if true, the agent re-checks its path on a timer/on | `true` |
| `repathInterval` | number | target movement automatically (see repathInterval/ repathDistance below). | `0.35` |
| `repathDistance` | number | world units a moving target must shift before an | `4` |
| `avoidanceEnabled` | boolean | Avoidance — separate from pathfinding (see NavWorldSystem.js header: "Pathfinding answers how do I get there, avoidance answers how do I avoid this NPC directly in front of me"). | `true` |
| `avoidancePriority` | number | 0-100. Higher-priority agents yield less to | `50` |
| `collabEnabled` | boolean | Collaboration — separate from both pathfinding AND avoidance (see #5 above: "how do I get there" vs "how do I avoid the NPC in front of me"). | `false` |
| `collabGroupRadius` | number | scripts behave exactly as before. | `96` |
| `vehicleLookahead` | number | Car + NavAgent2D local vehicle planner. | `72` |
| `vehicleCornerLookahead` | number | Corner lookahead. | `110` |
| `vehicleObstacleLookahead` | number | Obstacle lookahead. | `120` |
| `vehicleObstacleWidth` | number | Obstacle width estimate. | `28` |
| `vehicleSteerSmoothing` | number | Steering smoothing. | `7` |
| `vehicleSpeedSmoothing` | number | Speed smoothing. | `5` |
| `vehicleCornerSlowdown` | number | Corner slowdown multiplier. | `0.72` |
| `vehicleObstacleBrake` | number | Obstacle braking factor. | `0.9` |
| `vehicleRecoveryTime` | number | seconds of being stuck (pushing into | `1.35` |
| `vehicleRecoveryReverseTime` | number | something with little progress, drifting off the planned lane, or on a collision course with something dead ahead) before the car commits to a recovery maneuver. | `0.9` |
| `area` | value | Navigation — same model as Unity's NavMeshAgent.areaMask: a bitmask of which NavWorld2D cell areas (Ground, Water, Mud, ...) this agent is ALLOWED to path through at all — a route can never cross a bit that's off here, no matter how short a shortcut it would be. | `0xffff` |
| `areaCosts` | nullable value | Per-agent override of NavWorld2D.areaCosts, index-aligned with the same 16 area slots (see editor/state/NavAreas.js for the name registry both arrays share). | `null` |
| `currentPath` | nullable value | Set (transiently, for one movement step) by NavWorldSystem/ScriptAPI path-following helpers to hand a fresh path to this agent without NavAgent2D reaching back into the system itself — plain data, one- shot per repath, same pattern as CharacterController's requestJump. | `null` |
| `currentPathIndex` | number | Inspector field stored on this component. | `0` |

## Tuning behavior

These are the practical direction-of-change rules for the most important controls on this component.

| Setting | What changing it does |
| --- | --- |
| `radius` | The clearance needed around this agent. Larger radius makes narrow passages become non-walkable for this agent. |
| `speed` | Top travel speed in world units/second. |
| `acceleration / deceleration` | Higher values make movement and stopping snappier; lower values make it softer. |
| `stoppingDistance` | Larger values let the agent stop farther from the final target. |
| `repathInterval` | Lower reacts faster to changing routes/targets but costs more path queries. |
| `area` | Hard allowed-area mask; excluding an area prevents the route from crossing it. |

## Script API

| Member | Kind | Description |
| --- | --- | --- |
| `acceleration` | Property (read/write) | Acceleration. |
| `area` | Property (read/write) | Allowed area mask. |
| `areaCosts` | Property (read/write) | 16-entry area cost overrides. |
| `autoRepath` | Property (read/write) | Auto-repath. |
| `avoidanceEnabled` | Property (read/write) | Avoidance toggle. |
| `avoidancePriority` | Property (read/write) | Avoidance priority. |
| `collabEnabled` | Property (read/write) | Collaborative vehicle avoidance. |
| `collabGroupRadius` | Property (read/write) | Group radius. |
| `currentPath` | Property (read-only) | Read-only world-space waypoint array or null. |
| `currentPathIndex` | Property (read-only) | Read-only current waypoint index. |
| `deceleration` | Property (read/write) | Deceleration. |
| `radius` | Property (read/write) | Agent radius. |
| `repathDistance` | Property (read/write) | Target-move repath threshold. |
| `repathInterval` | Property (read/write) | Repath interval. |
| `speed` | Property (read/write) | Preferred speed. |
| `stoppingDistance` | Property (read/write) | Stopping distance. |
| `vehicleCornerLookahead` | Property (read/write) | Corner lookahead. |
| `vehicleCornerSlowdown` | Property (read/write) | Corner slowdown. |
| `vehicleLookahead` | Property (read/write) | Vehicle lookahead. |
| `vehicleObstacleBrake` | Property (read/write) | Obstacle brake factor. |
| `vehicleObstacleLookahead` | Property (read/write) | Obstacle lookahead. |
| `vehicleObstacleWidth` | Property (read/write) | Obstacle width. |
| `vehicleRecoveryReverseTime` | Property (read/write) | Reverse recovery time. |
| `vehicleRecoveryTime` | Property (read/write) | Recovery time. |
| `vehicleSpeedSmoothing` | Property (read/write) | Speed smoothing. |
| `vehicleSteerSmoothing` | Property (read/write) | Steering smoothing. |

## Examples

```
this.navAgent.speed = 180;
```

```
this.navAgent.autoRepath = true;
```

> **Need the full workflow?:** Components: complete workflow covers adding, configuring, testing, combining, and removing components.
