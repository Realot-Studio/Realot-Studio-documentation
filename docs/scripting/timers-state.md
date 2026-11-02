# Timers, state & messaging

> wait()/repeat() timers, the built-in this.state machine, and sendMessage/broadcastMessage.

- Source: https://realot-studio.pages.dev/docs/scripting/timers-state.html

## Timers

Timers run on game time, so [`time.scale`](time-scale.html) speeds them up, slows them down or freezes them. To animate a property over time use [`tween()`](tween.html) instead of hand-written timers.

| API | Meaning |
| --- | --- |
| wait(seconds, callback) | Runs callback once after seconds of game time. this inside the callback is the same entity that called wait(). Returns a timer id for cancelWait(id). Also available as this.wait(...). |
| repeat(seconds, callback) | Runs callback every seconds, forever, until cancelled, the entity is destroyed, or the scene restarts/switches. The first call happens seconds from now, then every seconds after. |
| cancelWait(id) / cancelRepeat(id) | Stop a pending timer before it fires. Safe to call with an id that already fired or was already cancelled. |

> **Timers are entity-owned:** Timers are automatically cancelled if their entity is destroyed, or if the scene restarts/switches before they fire — a wait() never fires "late" against a scene that’s already gone.

## State machine

`this.state` needs no component — it works on every entity automatically. `this.state.current`/`this.state.previous` give the current/previous state name (current defaults to `"default"`). `this.state.change(name)` fires `onStateExit()` for the outgoing state, then `onStateEnter()` for the new one.

```
function onUpdate() {
  if (this.isGrounded && this.state.current !== "idle") {
    this.state.change("idle");
  }
}

function onStateEnter() {
  if (this.state.current === "idle") this.animator.play("Idle");
  if (this.state.previous === "jump") debug.log("Landed!", "");
}
```

## Messaging

`sendMessage(tagOrEntity, message, data)` accepts either a tag string (messages every entity with that tag — a group broadcast) or an EntityContext directly (messages that one exact entity, unambiguous even if others share its name/tag). `broadcastMessage(message, data)` sends to every scene entity.

```
function onCollisionEnter(other) {
  sendMessage("Enemy", "targetNearby", { x: this.x, y: this.y });
}

function onMessage(message, sender, data) {
  if (message === "targetNearby") {
    this.navMoveToward(data.x, data.y, 80);
  }
}
```
