# Project format

> Understand the portable .realot archive and the difference between editable projects and standalone game exports.

- Source: https://realot-studio.pages.dev/docs/reference/project-format.html

## Current project file

**Save Project** downloads a `.realot` file. The extension identifies Realot's portable project file, which the editor reads as a complete project package.

## Archive contents

| Entry | Purpose |
| --- | --- |
| `manifest.json` | Project name, engine compatibility metadata and save information. |
| `scenes/index.json` | Scene list and active scene information. |
| `scenes/*.json` | Serialized scene entities and component data. |
| `assets/sprites.json`, `frames.json`, `audio.json` | Asset catalogues and references to binary asset files. |
| `assets/bin/` | Binary image/audio data referenced by the asset catalogues. |
| `scripts.json` | User-authored JavaScript source. |
| `prefabs.json` | Saved prefab definitions. |
| `layers.json`, `navAreas.json`, `tags.json` | Project-wide layer, navigation-area and tag names. |

## Open a project

Use the editor's **File → Load Project** command to open a saved `.realot` project. On a desktop browser that supports PWA file handling, you can also install Realot Hub and double-click a downloaded `.realot` file to open it in the editor.

## Project archive versus game export

A `.realot` archive is an editable project that can be loaded back into the editor. An HTML5/PWA export is a separate standalone game package with `index.html` at its root, containing the runtime and files needed to run the game. The Android build service consumes the standalone game export, not the editable project file.

## Compatibility metadata

The project manifest includes engine compatibility metadata. The loader compares it with the engine build and can warn when a project was saved by a newer engine. This metadata belongs to the project format; it is not a documentation version or a user-facing engine download version.
