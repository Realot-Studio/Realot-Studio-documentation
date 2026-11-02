# Navigation: complete setup

> Build, paint, name, script, tune, debug, and ship a complete Realot Studio navigation setup without skipping the hard parts.

- Source: https://realot-studio.pages.dev/docs/scripting/navigation-complete.html

## The complete model: five pieces, one pipeline

Realot Studio navigation is easiest to understand as a pipeline rather than as one button. A scene normally has **one shared NavWorld2D**; the NavWorld stores the base walkability grid, each NavAgent2D supplies per-agent size/restrictions, and script movement consumes the resulting path.

Static Collider2D geometry→NavWorld2D bake / paint→Area mask + costs→Agent radius→A\* path→Agent steering / avoidance

> **Important distinction:** The navigation grid answers “which route is possible?” while avoidance answers “how should this agent steer around nearby agents/obstacles?” Do not try to solve both by constantly rebaking the world.

## End-to-end setup: from empty scene to moving NPC

### Goal: make one NPC walk around walls to the target

1

**Create the navigation world.** In the editor top menu, open GameObject → 2D Object → Nav World 2D. Select the new Nav World 2D entity in the Hierarchy; its fields appear in the right-side Inspector under **Nav World 2D**.

2

**Set the navigation rectangle.** In the Inspector, edit `Bounds X`, `Bounds Y`, `Bounds Width`, and `Bounds Height`. The bounds define the grid region; they do not move the entity's Transform by themselves.

3

**Choose Cell Size.** Smaller values give finer obstacle detail but create more cells. Start around `32` world units, then reduce it only when a corridor or obstacle genuinely needs more resolution.

4

**Make walls real navigation obstacles.** Give the walls a **Collider2D** and, for baked/static geometry, leave the Rigidbody absent or Static. Triggers and Dynamic/Kinematic rigidbodies are not treated as baked obstacles.

5

**Bake.** In the selected Nav World 2D Inspector use **Bake Nav World** after the static geometry is ready. The runtime API equivalent is `nav.bake()`. Most games bake in the editor once.

6

**Inspect the result.** When a Nav World exists, the top-center editor toolbar gains the navigation tools. Use the Bounds view to see the overall rectangle cheaply, then the Cells view for detailed walkability.

7

**Manually fix special cells.** Press U for the Walkable brush, I for the Blocked brush, and O for the Area brush. Normal click paints; **Alt+click** clears that override. The `−`/`+` brush buttons beside the nav display controls reduce/increase the brush radius.

8

**Add the agent.** Select the NPC in the Hierarchy and use Inspector → Add Component → Nav Agent 2D. Start with `Radius 16`, `Speed 120`, `Auto Repath ON`, and the default area mask.

9

**Attach the movement script.** On the NPC's Script component, use the following minimal loop:

```
function onUpdate(dt) {
  var target = findFirst("Target");
  if (!target) return;

  this.navMoveToward(target.x, target.y, 120, {
    repathInterval: 0.25,
    finalArriveDist: 12,
    debug: true
  });
}
```

> **What should happen:** The NPC requests a path, advances through the returned waypoints, periodically rechecks the target, and stops inside the final arrival radius. The green debug path appears for a frame when debug:true is used and the debug overlay is visible.

## Every navigation editor control, in context

| Control | Where it appears | What it does | Increase / decrease behavior |
| --- | --- | --- | --- |
| `Nav World 2D` | GameObject → 2D Object → Nav World 2D | Adds the shared navigation grid component/entity. | One shared world per scene is the normal design. |
| `Bounds X / Y` | Right Inspector → Nav World 2D | Moves the grid rectangle relative to the Nav World entity. | Larger positive/negative values shift the grid rectangle; they do not resize it. |
| `Bounds W / H` | Right Inspector → Nav World 2D | Controls navigation coverage. | Larger = larger navigable region and more cells; smaller = less coverage. |
| `Cell Size` | Right Inspector → Nav World 2D | Controls grid resolution. | Smaller = more precise/narrower features represented, more cells/work. Larger = cheaper, but narrow geometry may disappear into one cell. |
| `Bake Nav World` | Right Inspector → Nav World 2D | Reads eligible Collider2D geometry and produces the base walkability grid. | Run after changing static obstacles unless Dynamic mode is being used. |
| `Dynamic` | Right Inspector → Nav World 2D | Enables automatic rebaking when bake-relevant static geometry changes. | ON = convenience for runtime-changing static-like geometry; OFF = avoid rebake work for mostly-static levels. |
| `Allow Diagonal` | Right Inspector → Nav World 2D | Controls whether A\* may use diagonal grid neighbors. | OFF = 4-neighbor grid; ON = diagonals become valid route steps. |
| `U` Walkable | Top editor toolbar; only after Nav World 2D exists | Paints an explicit walkable override. | Brush size is controlled by the nearby `−`/`+` buttons. |
| `I` Blocked | Top editor toolbar; only after Nav World 2D exists | Paints an explicit blocked override. | Same brush-size controls and Alt+click erase behavior. |
| `O` Area | Top editor toolbar; only after Nav World 2D exists | Paints the selected navigation area onto cells. | Area choice appears beside the brush only while Area mode is active. |
| `Edit → Nav Areas…` | Top editor menu Edit | Names the 16 navigation area slots. | Names are used later by `nav.areaMask()` and `nav.areaCosts()`. |
| `Bounds / Cells` view buttons | Top toolbar beside nav tools | Switches between cheap bounds visualization and detailed cell visualization. | Cells view is the one to use when diagnosing exact painted/baked coverage. |

## Named areas: hard restrictions vs soft preferences

Realot Studio exposes 16 navigation-area slots. Name them with Edit → Nav Areas…, then use the names in script instead of memorizing bit positions.

### Hard restriction: Area Mask

```
var allowed = nav.areaMask("Ground", "Road");
var path = nav.findPath(this.x, this.y, 800, 300, {
  area: allowed,
  radius: 16
});
```

An area omitted from the mask is **impassable for that query**. This is different from cost.

### Soft preference: Area Cost

```
var path = nav.findPath(this.x, this.y, 800, 300, {
  area: nav.areaMask("Ground", "Road", "Mud"),
  areaCosts: nav.areaCosts({
    Road: 0.5,
    Mud: 4
  })
});
```

Cost changes route preference among allowed areas. A cost of `1` is neutral; a higher value makes that area more expensive; a lower positive value makes it more attractive. Cost does not turn an allowed area into a hard wall.

> **Common mistake:** Do not use areaCosts: { Water: 0 } to try to block water. Use nav.areaMask(...) and leave Water out of the mask.

## NavAgent2D tuning: what every major value actually changes

| Field | Increase it | Decrease it | Use it when… |
| --- | --- | --- | --- |
| `radius` | Agent needs wider clearance; narrow passages become unavailable sooner. | Agent can fit through tighter passages. | Different NPC sizes need to share the same NavWorld. |
| `speed` | Higher top movement speed. | Slower movement. | Simple traversal pacing. |
| `acceleration` | Reaches the requested speed faster. | Softer/slower speed changes. | Making movement feel snappy vs floaty. |
| `deceleration` | Stops more quickly. | Longer, softer stopping. | Preventing overshoot near goals. |
| `stoppingDistance` | Agent intentionally stops farther away. | Agent gets closer to target. | Enemies should keep melee/shooting distance. |
| `repathInterval` | Fewer route checks; cheaper. | More frequent route checks; more responsive and more expensive. | Balancing moving-target responsiveness vs CPU work. |
| `repathDistance` | Target must move farther before a re-path is triggered. | Target motion triggers re-path sooner. | Fast-moving targets. |
| `avoidancePriority` | Higher priority means the agent is treated as more important in avoidance decisions. | Lower priority makes it more willing to yield. | Mixed-priority crowds or special NPCs. |
| `area` | Add area bits to permit additional terrain categories. | Remove bits to forbid categories. | Making a route legally impossible through a terrain class. |

## Complete car / road navigation flow

Vehicle navigation is not simply “walk an NPC path with a car sprite.” Realot Studio exposes `this.navDriveToward()` specifically for Car-type CharacterController movement and the NavAgent2D vehicle tuning fields.

1

Make the road surface part of the NavWorld and name it, for example, `Road`. Use another area such as `Ground` for ordinary terrain.

2

Add **Nav Agent 2D** to the car. Set `collabEnabled` or avoidance only when you actually need those behaviors.

3

Use `nav.areaMask("Road")` when the car must stay on roads. Use a wider mask if road-only routing is too restrictive.

4

Drive toward the destination:

```
function onUpdate(dt) {
  var target = findFirst("Destination");
  if (!target) return;

  this.navDriveToward(target.x, target.y, 220, {
    repathInterval: 0.2,
    arriveDist: 8,
    finalArriveDist: 18,
    debug: true
  });
}
```

For road-vs-ground preference, allow both and use costs instead of a hard mask:

```
var path = nav.findPath(this.x, this.y, target.x, target.y, {
  area: nav.areaMask("Road", "Ground"),
  areaCosts: nav.areaCosts({ Ground: 3, Road: 1 })
});
```

> **Tuning order for vehicles:** First make the NavWorld route correct. Then tune agent radius. Then tune speed/acceleration/deceleration. Only after that adjust the vehicle lookahead/smoothing/braking fields. This separates route problems from steering problems.

## When to use Dynamic

Turn on **Dynamic** only when bake-relevant static geometry can actually change during play. The runtime checks a cheap collider signature and rebakes when the signature changes; it does not blindly rebake the entire world every frame. Dynamic navigation still has a real rebake cost when qualifying geometry changes.

```
// Procedural level example: after spawning a new static obstacle
var result = nav.bake();
if (result) debug.log("Nav rebuilt: " + result.walkable + " walkable, " + result.blocked + " blocked");
```

## Navigation debugging checklist

**1.** Is a Nav World 2D actually present in the scene?  
**2.** Are the walls using Collider2D and eligible for baking?  
**3.** Did you bake after editing static geometry?  
**4.** Does Cells view show the corridor as walkable?  
**5.** Is the agent radius too large for that corridor?  
**6.** Is the Area Mask accidentally excluding the only available route?  
**7.** Are you confusing area cost with a hard restriction?  
**8.** Is your target inside the NavWorld bounds or at least near a walkable cell?  
**9.** Is the script calling the correct method for the movement type (`navMoveToward` vs `navDriveToward`)?  
**10.** Turn on `debug:true` and make the debug overlay visible to inspect the actual route.

## LLM/code-generation rule

When generating navigation code, preserve this dependency order: **NavWorld2D → walkability/bake → named areas → NavAgent2D → script movement → tuning**. Do not invent properties such as `destination`, `setDestination`, or a Unity/Godot class when Realot Studio's documented API is `this.navMoveToward()`, `nav.findPath()`, and `this.navAgent.*`.
