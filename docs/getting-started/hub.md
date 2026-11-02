# The Realot Hub

> Use Projects to create and reopen games, and Learn to open the built-in guide.

- Source: https://realot-studio.pages.dev/docs/getting-started/hub.html

## Overview

The Hub is the Realot Studio home screen. It is the starting point for opening projects, creating a new game from a template, and opening the built-in learning material. The current Hub has two views: **Projects** and **Learn**.

| View | What it does |
| --- | --- |
| Projects | Shows your saved project cards. Start with a template, create a blank project, search/sort your projects, switch between grid and list layouts, or reopen a recent project. |
| Learn | Opens the Hub's learning area. The built-in quick guide is part of the engine distribution and can be cached for offline access. |

## Starter templates

The current template gallery includes:

| Template | Starting point |
| --- | --- |
| Blank Canvas | An empty project for custom 2D scenes and logic. |
| Platformer Kit | A platformer starter with a kinematic character controller and one-way platforms. |
| Top-Down | A top-down starter with a player, NPCs, collectibles and a dungeon scene. |
| Flappy Bird | A flap-to-fly starter with scoring and a simple game-state flow. |
| Sky Jumper | An endless jumping starter with platforms, stars and a following camera. |
| Physics Sandbox | A scene for experimenting with Rapier2D bodies, colliders and joints. |

## Install the Hub as an app

Realot is a web application. On browsers and deployments that support installation, the title bar can show an **Install app** action when the browser confirms the site is installable. Installation creates an app-like shortcut; it does not download a separate engine release. The service worker can cache the Hub, editor and runtime for supported offline use.

Updates are published to the hosted site. When the browser is online, reload the site to receive the current published files. An installed PWA may continue using cached files while offline and will need to reconnect to refresh them.

## Project files

**File → Save Project** downloads your project as a `.realot` file. This is Realot Studio's portable project format and includes the scenes, assets, prefabs, tags, navigation-area names and scripts needed to continue editing the game.

**Open a project from your computer:** install Realot Hub as a PWA in a supported desktop browser. Then double-click a downloaded `.realot` file in your file manager. The operating system opens the installed Realot app, and Realot loads that project in the editor. When asked, you can allow Realot to keep saving changes back to that same file. This file-opening behavior requires an installed PWA and browser/operating-system support for web-app file handling; if that option is unavailable, open the editor and use **File → Load Project**.
