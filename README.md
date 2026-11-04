# PPSC Photo Frame Generator — upgraded editor

A static, browser-based photo composition editor for Pabna Pilot School & College. The original project, teacher records, image assets, welcome modal, developer information, language toggle, local Python server, and GitHub Pages workflow are retained.

## Run locally (Windows)

1. Extract the complete ZIP.
2. Install Python 3 if it is not already installed.
3. Double-click `run_local_server.bat`, or run `python server.py` in this folder.
4. Open `http://127.0.0.1:8000`.

The Python server scans `frames/` and returns the current project-owned frame list. Add your own frame assets to `frames/`; the website rescans the library while running locally. End users are not given a frame-upload feature.

## GitHub Pages deployment

1. Upload the contents of this folder to the repository root (so `index.html` and `.github/workflows/deploy.yml` are at the root / workflow path).
2. Commit and push to `main` or `master`.
3. In **Settings → Pages**, choose **GitHub Actions** as the source.
4. Open **Actions** and wait for **Deploy Photo Frame Website to GitHub Pages** to complete successfully.
5. Open the URL shown in **Settings → Pages**.

The workflow generates `frames.json` from the committed `frames/` directory. GitHub Pages is static hosting, so it cannot dynamically list a folder at runtime; a new frame becomes available after the file is committed and the workflow redeploys.

## Adding project-owned frames

Put PNG, JPG, JPEG, WEBP, or SVG assets in `frames/`, then commit and push. Use transparent PNG/SVG overlays for the best frame result. Do not add end-user frame upload controls.

## Defining photo slots

Edit `frame-config.json`. Coordinates use the editor's 1080×1080 canvas coordinate system. Example:

```json
{
  "frames": [
    {
      "filename": "collage-frame.png",
      "photoSlots": [
        {"id":"left", "x":80, "y":180, "width":420, "height":620},
        {"id":"right", "x":580, "y":180, "width":420, "height":620}
      ]
    }
  ]
}
```

Each queue photo maps to the corresponding slot in queue order. For a single-slot frame, choose the queue photo you want to use. If a frame has no slot definition, the editor uses one full-canvas slot. Extra photos remain in the queue and are not deleted. The supplied poster has a configured photo opening (approximately x=75, y=209, width=490, height=528 in the 1080×1080 editor coordinate space). Adjust `frame-config.json` if you change the artwork or need finer alignment.

## Editor features in this build

- Responsive dark editor layout.
- Project-owned frame library; no end-user frame upload.
- Up to five photos, multiple selection, drag-and-drop file intake, thumbnail queue, replace/remove, and reorder controls.
- Photo selection, zoom, rotation, pointer dragging, reset, and horizontal/vertical flip.
- Configuration-based one-to-five photo slots.
- Editable text layers with Bangla/English text input, font family, size, color, bold, italic, and drag positioning.
- PNG and JPG export.
- IndexedDB local autosave/restore, clear project, and basic undo/redo history.
- Preserved teacher profiles and existing contact links.

## Storage and privacy

Autosave is stored only in the current browser profile using IndexedDB. It is not a server backup and does not automatically synchronize between devices. Clearing browser site data may remove the saved project. Large photo sets can exceed browser storage quotas; the UI reports when autosave cannot complete.

## Verification performed

- Python syntax compilation for `server.py`.
- JavaScript syntax validation with `node --check`.
- JSON parsing for frame manifest and frame configuration.
- GitHub Actions embedded Python manifest generator syntax check.
- Local HTTP smoke test for the frame manifest endpoint.
- File integrity comparison for original teacher/image assets against the source ZIP.

## Known limitations / not claimed as tested

- No real-device Android/iPhone/tablet or cross-browser visual QA was available in this environment.
- No automated pointer/touch browser interaction test was run. Desktop HTML drag-and-drop and touch-friendly arrow reordering are provided; touch drag-reordering is not implemented.
- The text tool supports editable text, drag positioning, font, size, color, bold and italic. Dedicated text resize handles, rotation, letter spacing, alignment controls, opacity controls, shadow controls, duplicate-text, and a full layer panel are not included in this build.
- Undo/redo covers recorded editing actions but is not a full professional-grade per-keystroke history engine.
- The editor uses the configured photo-slot rectangles and frame overlay order. The supplied existing poster does not include slot metadata, so its default slot is full-canvas until configured.
- Bengali font loading uses Google Fonts when the visitor is online; local system fallback may be used offline.
- Frame assets must be served from the same project origin for reliable canvas export (avoids cross-origin canvas restrictions).

## Original project backup

`_original_backup/index.html` and `_original_backup/original-project.zip` preserve the unmodified original project source.
