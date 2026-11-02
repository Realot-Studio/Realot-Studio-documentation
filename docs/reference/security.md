# Security and play origin

> Understand the script trust boundary and why shared projects should run on a separate origin.

- Source: https://realot-studio.pages.dev/docs/reference/security.html

> **Game scripts are not a security sandbox:** Project scripts execute as ordinary JavaScript in the game page. Treat scripts inside imported projects as code from another person, not as inert project data.

## Script execution

Realot shadows selected browser globals inside its script environment as a guardrail against accidental access. This is not a hardened security boundary: scripts are compiled and run as page code. Do not open a project containing scripts unless you trust its source.

## Use a separate play origin for shared projects

For a deployment where people can open projects from others, configure the editor to launch Play on a separate hostname that serves the same Realot files. In `project/editor/index.html`, set the `realot-play-origin` meta tag to that HTTPS origin:

```
<meta name="realot-play-origin" content="https://play.example.com" />
```

The editor sends the scene to the play page using `postMessage`. Because the two hostnames are different origins, browser same-origin policy keeps the play page's localStorage, IndexedDB and DOM separate from the editor's. Leave the meta content empty and Play uses the same origin; that is less isolated and is not recommended for untrusted projects.

## Offline behavior

If the configured play origin cannot be reached, such as while offline, the editor can fall back to same-origin Play and logs a warning. Data saved by the game on the play origin is separate from the editor origin's storage.

## Other protections

- Messages are accepted only from the corresponding editor/play window and expected origin.
- Console output and project-controlled names are escaped before display in the editor UI.
- Loading a project containing scripts asks for confirmation first.
- Exported games run on the origin where the developer hosts them; they are separate from the editor's Play-origin setting.

## APK build credentials

The APK service URL is public configuration. Permanent service credentials must not be placed in the static editor source because all shipped JavaScript can be inspected by visitors. The editor's intended managed flow requests a short-lived token from the service and renews it when needed. The service must still enforce appropriate quotas and access controls; a public token-issuance endpoint alone does not identify an approved user.
