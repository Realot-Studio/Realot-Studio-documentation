# Scenes & projects

> Save, load, switch, duplicate and serialize Realot Studio scenes and project manifests.

- Source: https://realot-studio.pages.dev/docs/editor/scenes-projects.html

> **Exact control path:** Project-level scene/file operations are in the bottom Project panel. Scene creation uses Project → Scenes → New Scene ; Save Project and Load Project are in the top File menu. The autosave indicator/action is also exposed through File → Save Now / Saved .

## Scene workflow

The Scene Manager supports creating, saving, switching, renaming, duplicating and deleting scenes. The last remaining scene cannot be deleted.

## Project compatibility

The project manifest stores compatibility metadata. When a project created by a newer engine build is opened in an older build, the editor can show a compatibility warning. This information belongs to the saved project and does not create versioned documentation pages or download releases.

## Recommended practice

Keep source projects with explicit scene names, tags and stable IDs. Keep backups of important project archives before opening them in a different engine build, especially when compatibility warnings appear.

## Save and reopen a project

Choose **File → Save Project** in the editor to download a `.realot` project file. To reopen it by double-clicking, install Realot Hub as a PWA in a desktop browser that supports file handling. Double-click the `.realot` file in your file manager; the installed Realot app opens the project in the editor. Realot can ask permission to save future changes back to the same file. If your browser does not support PWA file handling, use **File → Load Project** inside the editor.
