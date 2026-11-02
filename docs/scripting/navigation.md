# Pathfinding & NavWorld2D

> navMoveToward, nav.findPath, named areas and per-area cost, and multi-agent avoidance.

- Source: https://realot-studio.pages.dev/docs/scripting/navigation.html

## What navigation is in Realot Studio

Realot Studio navigation is a shared 2D grid system. A scene normally contains one NavWorld2D, while NavAgent2D components query that world using agent-specific radius, area restrictions, costs, path refresh timing, and avoidance settings.

> **Need the whole workflow?:** Read Navigation: complete setup for the complete editor + scripting + tuning flow.

## Quickest working path

```
function onUpdate(dt) {
  var target = findFirst("Target");
  if (target) this.navMoveToward(target.x, target.y, 120);
}
```

This requires a NavWorld2D in the scene and, for useful per-agent clearance/settings, a NavAgent2D on the moving entity.

## Manual path query

```
var path = nav.findPath(this.x, this.y, 800, 300, {
  radius: 16,
  area: nav.areaMask("Ground", "Road"),
  areaCosts: nav.areaCosts({ Mud: 4, Road: 1 }),
  debug: true
});
```

The result is an array of world-space `{x,y}` waypoints or `null` when no route is available.

## Cars

For a Car-type CharacterController with NavAgent2D, use `this.navDriveToward(targetX, targetY, speed, opts)`. It adds vehicle-oriented braking, steering, lookahead, and recovery behavior rather than pretending a car is a walking agent.

## Area rules worth remembering

| Tool | Use it for |
| --- | --- |
| `nav.areaMask("Road", "Ground")` | Hard permission: route may only cross named areas in the mask. |
| `nav.areaCosts({ Road: 1, Mud: 4 })` | Soft preference: both areas remain legal, but Mud becomes more expensive. |
| `NavAgent2D.radius` | Per-agent clearance; larger agents can be blocked by corridors smaller agents can use. |
