# Script

> Realot Studio Script component reference: fields, script API, behavior and examples.

- Source: https://realot-studio.pages.dev/docs/api/components/script.html

> **Scope:** This page documents the Script component in Realot Studio. Runtime fields are serialized scene data; the Script API section lists only members intentionally exposed to game scripts.

> **Where to find it in the editor:** Inspector → Add Component → Script, then use the script editor via the script asset/project item. IntelliSense completion is driven from the same runtime option metadata.

## What it does

Script component holding a script name, source and enabled state.

> **Component setup & editor tools:** Script attaches a JavaScript file to an entity. The Inspector provides Create New Script, Load Script…, and Open Script Editor controls.

## How to add and use Script

**Editor path:** Select the target entity in the **Hierarchy** (left side) → look at the **Inspector** (right side) → click **Add Component** at the bottom of the Inspector → search for **Script** → click the component row. The Add Component picker is a centered modal with a search box; it only lists components not already attached.

For components with a dedicated editor tool, the tool is opened or activated from the location described below. Do not assume that adding the component alone activates its editor; some systems require a separate window, panel, or viewport tool.

## Component setup & editor tools

- Select entity → Inspector → Script section → Create New Script, Load Script…, or Open Script Editor. After attachment, Enabled controls whether the script runs.

### What you should see after adding it

The component appears as its own section in the Inspector. Its serialized settings are listed in the **Component data** table below. If a field is conditional, it appears only when the relevant mode/type is selected. If a field is a runtime state field (for example grounded or resolved velocity), treat it as read-only diagnostic state unless the API reference explicitly documents it as writable.

### How to read the settings

For every setting below, the documentation distinguishes **type**, **default**, **meaning**, and tuning direction where behavior is known. When a value represents a direction, use the engine's coordinate convention documented in [Coordinate system](../../reference/coordinate-system.html); do not substitute Unity/Godot conventions.

## Component data

| Field | Type | Purpose | Default |
| --- | --- | --- | --- |
| `scriptName` | string | Script asset/name. | `NewScript` |
| `source` | string | Script source code. |  |
| `enabled` | boolean | Whether the script is enabled. | `true` |
| `inspectValues` | object | Inspector field stored on this component. | `{}` |

## Notes & behavior

- Scripts are executed by ScriptSystem and receive the lifecycle/globals documented under Scripting. Script components are scene data rather than a `this.script` runtime API.

> **Need the full workflow?:** Components: complete workflow covers adding, configuring, testing, combining, and removing components.
