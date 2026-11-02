# State & messaging

> Build lightweight state machines and decoupled entity communication.

- Source: https://realot-studio.pages.dev/docs/scripting/state-messaging.html

## State machine

Every entity gets `this.state` without a dedicated component. `current` starts as `"default"`; `previous` is the state before the last transition. `change(name)` is a no-op when the name is already current.

## State callbacks

```
function onStateEnter() {
  if (this.state.current === "chasing") {
    this.animator.play("Run");
  }
}

function onStateUpdate(dt) {
  if (this.state.current === "chasing") {
    // chase logic
  }
}
```

## Messages

```
function onStart() {
  sendMessage("Enemy", "takeDamage", { amount: 10 });
}

function onMessage(message, data) {
  if (message === "takeDamage") {
    this.hp -= data.amount;
  }
}
```

## When to use messages

Messaging is useful when entities should react to an event without knowing another entity’s exact implementation. Use `findById`/`sendMessage(entity,...)` when you need one exact target; use a tag when you intentionally want a group.
