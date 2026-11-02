# Components: complete workflow

> A complete guide to adding, configuring, testing, removing, and scripting components. This page complements each individual component reference; it does not replace the per-component settings tables.

- Source: https://realot-studio.pages.dev/docs/editor/component-workflows.html

## 1. Select the entity first

Click an entity in the **Hierarchy** on the left or select it in the Scene viewport. The selected entity's properties appear in the **Inspector** on the right.

## 2. Add a component

At the bottom of the Inspector click **Add Component**. A centered **Add Component** modal opens with a search field and a scrollable list. Type the component name, then click its row. The list excludes components the entity already has.

## 3. Configure the component

After adding it, scroll the Inspector to the new component section. Start with the component's mode/type field if it has one. Changing a mode can expose or hide related settings. Configure required references/assets before tuning numbers.

## 4. Understand values versus runtime state

Serialized authoring settings are saved with the scene. Runtime state fields can change while the game runs and are useful for debugging. Examples include Rigidbody2D velocity/ground state and CharacterController request/state values.

## 5. Test in Play mode

Run the game, observe the result, and inspect the component again when debugging. Change one setting at a time so you can identify which property caused the behavior.

## 6. Use the dedicated editor tools

| System | Where | What it does |
| --- | --- | --- |
| Sprite | Inspector SpriteRenderer section / asset picker | Assign the visual asset. |
| Animation | SpriteAnimation → Open Animation Window | Create and edit clips/frames. |
| Physics | Collider/Transform gizmos in Scene viewport | Visually inspect/edit geometry. |
| Navigation | NavWorld2D + navigation toolbar + Edit → Nav Areas… | Author areas, bake/debug navigation, then use NavAgent2D. |
| Tiles | Tileset/Tilemap panels | Create tile data and paint the map. |
| Stroke Path | Stroke Path viewport tool/gizmo | Edit path points and inspect serialized path settings. |
| Scripts | Script → Create New Script / Load Script… / Open Script Editor | Create, attach, edit, and enable scripts. |
| Lighting | Light/ShadowCaster gizmos + Inspector | Author light geometry and shadow participation. |

## 7. Component combinations that matter

- **Dynamic physics actor:** Rigidbody2D + Collider2D; add SpriteRenderer/ShapeRenderer for visuals.
- **Platformer controller:** Rigidbody2D + Collider2D + CharacterController; choose Platformer and configure its movement group.
- **Navigation agent:** NavWorld2D in the navigation world + NavAgent2D on the moving entity; bake/configure the world before testing agent movement.
- **Animated character:** SpriteRenderer + SpriteAnimation, optionally with Rigidbody2D/CharacterController.
- **Interactive UI:** the appropriate UI component (TextRenderer, TextInput, Joystick, SpeechBubble, ChatLog) plus Script when behavior is needed.

## 8. Where to go next

Use the component reference for the complete field table, defaults, API members, notes, and examples. Use [Navigation: Complete Setup](../scripting/navigation-complete.html) for multi-system navigation. Use [Script API Cookbook](../scripting/api-cookbook.html) for complete scripting recipes.
