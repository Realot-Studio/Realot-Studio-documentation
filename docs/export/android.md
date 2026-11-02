# Export an Android APK

> Build an Android APK directly from the Realot Studio Export window. The current editor allows three APK exports in a rolling 14-day period.

- Source: https://realot-studio.pages.dev/docs/export/android.html

> **One simple flow:** Click Export , choose Android APK , and let Realot build the file. There is no separate setup wizard or need to export HTML5 first.

## Steps

1. Open the game project in Realot Studio.
2. Click **Export** in the editor toolbar. You can also use **File → Export…**.
3. In the Export Game window, choose **Android APK**.
4. Wait for the build to finish. Realot downloads the finished `.apk` file to your device.

The game title is filled in from the project name and can be changed before exporting. Choosing a custom favicon is optional. Those are the only optional details shown in the export form; you do not need Android Studio, Gradle, the Android SDK or a separate web export.

## APK export limit

The current editor allows **3 APK exports in a rolling 14-day period**. The Export window shows how many of the three remain and explains when an export becomes available again. The window is rolling: an export becomes available again 14 days after the corresponding counted export, rather than all three resetting on one calendar date.

An export is counted after the build service accepts the job. A failed or cancelled build gives that export back. **HTML5 and PWA exports are not limited by the APK quota.**

> **Quota detail for support and AI tools:** The supplied browser client records the rolling quota in this browser's local storage. It is therefore a per-browser client allowance, not an account-based counter. The build service should enforce its own server-side usage limits; clearing browser data is not a supported way to manage exports.

## What the APK contains

The current Android option produces a **debug-signed APK** intended for testing and direct installation on an Android device. It is not a Play Store production-signed release. The Android build service is needed to create the APK; the downloaded game does not need to contact that service while it is running.

## When an export does not finish

Read the message shown in the Export window. If the service is waking up or temporarily unavailable, try again later. A failed or cancelled build returns the consumed export allowance. If the same error keeps happening, copy the message from the export window and include it when reporting the issue.

## Other export formats

- **HTML5:** creates a standalone web game you can host as a static site.
- **PWA:** creates the web game plus an installable manifest and service worker for offline use.
- **Desktop (Windows/Mac/Linux):** listed in the format picker as coming soon in the supplied engine build.

For the other formats, see [HTML5 and PWA export](web.html) or the [Export window reference](export-window.html).
