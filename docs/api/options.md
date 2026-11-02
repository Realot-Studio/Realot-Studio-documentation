# Option schemas & opts

> Exact option objects, types, defaults and semantics for the most important Realot Studio APIs, with machine-readable JSON for tooling and LLMs.

- Source: https://realot-studio.pages.dev/docs/api/options.html

> **Need to know what must exist first?:** Use the API requirements & complete usage map to see prerequisites for every global and component API.

> **Hands-on examples:** See the Script API cookbook for complete scripts showing where each API lives and how the pieces fit together.

> **Authoritative option metadata:** Navigation option names are defined once in runtime/scripting/NavAPI.js and consumed by both runtime behavior and editor IntelliSense. The machine-readable api-options.json mirrors the documented public option groups.

## nav.findPath

| Option | Type | Default | Effect |
| --- | --- | --- | --- |
| `debug` | boolean | False | Draw the current path as green debug segments for one frame. |
| `radius` | number | 0 | Agent clearance against the shared NavWorld2D. Larger radius can close narrow passages. |
| `area` | number | 65535 | 16-bit allowed-area mask. Default 0xffff allows every area. |
| `areaCosts` | number[]|null | None | Per-call 16-slot cost overrides; null entries use NavWorld2D defaults. |

## this.navMoveToward

| Option | Type | Default | Effect |
| --- | --- | --- | --- |
| `repathInterval` | number | 0.35 | Seconds between re-path checks when autoRepath is enabled. |
| `arriveDist` | number | 4 | Distance at which an intermediate waypoint is considered reached. |
| `finalArriveDist` | number | 1 | Distance from final target considered arrived. |
| `targetChangeDistance` | number | 4 | Target movement that forces an immediate re-path; effective default is max(4, arriveDist). |
| `debug` | boolean | False | Draw the current path as green debug segments for one frame. |

## this.navDriveToward

| Option | Type | Default | Effect |
| --- | --- | --- | --- |
| `repathInterval` | number | 0.35 | Seconds between re-path checks when autoRepath is enabled. |
| `arriveDist` | number | 4 | Distance at which an intermediate waypoint is considered reached. |
| `finalArriveDist` | number | 1 | Distance from final target considered arrived. |
| `targetChangeDistance` | number | 4 | Target movement that forces an immediate re-path; effective default is max(4, arriveDist). |
| `debug` | boolean | False | Draw the current path as green debug segments for one frame. |

## findInRadius

| Option | Type | Default | Effect |
| --- | --- | --- | --- |
| `name` | string|undefined | None | Only return entities with this exact name. |
| `tag` | string|undefined | None | Only return entities with this exact tag when name is not provided. |

## spawn

| Option | Type | Default | Effect |
| --- | --- | --- | --- |
| `x` | number|undefined | source x | Spawn position X override. |
| `y` | number|undefined | source y | Spawn position Y override. |
| `name` | string|undefined | source name | Rename the clone. |
| `byTag` | boolean | False | Interpret the first argument as a tag instead of a name. |

## physics.raycast

| Option | Type | Default | Effect |
| --- | --- | --- | --- |
| `layerMask` | number|undefined | engine default | Restrict ray hits to collider layers included in the mask. |
| `debug` | boolean | False | Draw the ray debug line for one frame. |
| `exclude` | array|undefined | None | Exclude listed entity/entity-context targets from hit testing. |

## mouse.isOver / clickedOn

| Option | Type | Default | Effect |
| --- | --- | --- | --- |
| `byTag` | boolean | False | Interpret the string target as a tag instead of an entity name. |

## touch.isOver / tappedOn

| Option | Type | Default | Effect |
| --- | --- | --- | --- |
| `byTag` | boolean | False | Interpret the string target as a tag instead of an entity name. |
| `justStarted` | boolean | False | Only match touches that began this frame. |

## Examples

```
this.navMoveToward(target.x, target.y, 160, {
  repathInterval: 0.2,
  arriveDist: 6,
  finalArriveDist: 12,
  debug: true,
});

const hits = physics.raycast(this.x, this.y, target.x, target.y, {
  layerMask: 1 << 0,
  exclude: [this],
  debug: true,
});
```

## How `opts` overrides work

Realot Studio uses options in a few different ways. An explicit option normally wins for that call; otherwise the method uses the component/default value. This matters most for navigation and raycasts.

| Pattern | What it means |
| --- | --- |
| `this.navMoveToward(x,y,160)` | Explicit speed is used for this call; other behavior can come from the NavAgent2D component. |
| `this.navMoveToward(x,y,160,{ finalArriveDist: 12 })` | Only `finalArriveDist` changes for this call; unrelated options keep their defaults/component behavior. |
| `nav.findPath(...,{ radius: 24 })` | Manual query uses the supplied radius instead of assuming the caller's component radius. |
| `physics.raycast(...,{ exclude:[this] })` | The current entity is removed from the query results, preventing self-hits. |

> **Do not invent option names.:** Realot Studio is not drop-in Unity/Unreal/Godot API compatibility. Use the exact option names documented here and in the editor's IntelliSense.

## Navigation option recipes

### Hard route restriction

```
var route = nav.findPath(this.x, this.y, goalX, goalY, {
  area: nav.areaMask("Road", "Ground")
});
```

Only named areas in the mask are legal. An omitted area is not a fallback route; it is forbidden.

### Soft route preference

```
var route = nav.findPath(this.x, this.y, goalX, goalY, {
  area: nav.areaMask("Road", "Ground", "Mud"),
  areaCosts: nav.areaCosts({ Road: 1, Ground: 2, Mud: 5 })
});
```

All three areas remain legal, but the pathfinder prefers cheaper traversals when route length is otherwise comparable.

### Per-agent runtime override

```
var costs = this.navAgent.areaCosts || [];
costs[2] = 4;
this.navAgent.areaCosts = costs;
```

`areaCosts` is an indexed 16-slot array on the component. Assign a new normalized array back to the property; mutating a previously-read temporary is not enough unless you reassign it.

## LLM usage rule

When generating Realot Studio code, prefer the documented option name and shape exactly as listed. Do not invent Unity/Unreal/Godot option names just because they sound familiar; Realot Studio’s runtime and IntelliSense contract is the authority.
