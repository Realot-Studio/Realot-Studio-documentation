# Assets & animation

> Use sprites, animation clips and audio assets from the editor.

- Source: https://realot-studio.pages.dev/docs/editor/assets-animation.html

> **Exact control path:** Imported sprites/audio/scripts/prefabs live in the bottom Project panel. Drag supported assets into the center Scene viewport. For animation, add Sprite Animation in the Inspector, then use the Animation editor window to create clips and import frames.

## Sprites

SpriteRenderer points at an asset key rather than embedding image data in the component. This keeps scene JSON lightweight and lets exported runtime assets remain separate.

## Animation

SpriteAnimation stores clips and current playback state. Scripts can call `this.animator.play("Run")`, stop playback and inspect current clip/frame information.

## Audio

AudioSource stores the asset key plus playback properties. 3D sources use `minDistance` for full volume and fade toward silence at `maxDistance`. AudioListener defines the hearing radius and sound enter/leave callbacks are available to scripts.
