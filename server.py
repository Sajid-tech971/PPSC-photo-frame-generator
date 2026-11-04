#!/usr/bin/env python3
"""Local server for Pabna Photo Frame Generator with dynamic /frames discovery."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import json
import os
import re
import mimetypes

ROOT = Path(__file__).resolve().parent
FRAME_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg"}

def display_name(filename: str) -> str:
    known_names = {
        "frame01": "School Official",
        "frame02": "Science & Technology",
        "frame03": "Victory Day",
        "frame04": "Independence Day",
        "frame05": "Language Day",
        "frame06": "Sports Carnival",
        "frame07": "Cultural Festival",
        "frame08": "Graduation",
        "frame09": "Robotics & Coding",
        "frame10": "Alumni Reunion",
        "frame11": "Admission Season",
        "frame12": "Premium Dark",
    }
    stem = Path(filename).stem
    if stem.casefold() in known_names:
        return known_names[stem.casefold()]
    stem = re.sub(r"[_-]+", " ", stem)
    stem = re.sub(r"\s+", " ", stem).strip()
    return stem.title() or filename

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        if self.path.split("?", 1)[0] == "/api/frames":
            frames_dir = ROOT / "frames"
            frames_dir.mkdir(exist_ok=True)
            manifest_path = ROOT / "frames.json"
            items_by_path = {}
            if manifest_path.exists():
                try:
                    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                    for entry in manifest.get("frames", []):
                        if isinstance(entry, dict) and entry.get("path"):
                            items_by_path[entry["path"]] = entry
                except (OSError, ValueError, TypeError):
                    pass
            config_path = ROOT / "frame-config.json"
            configured = {}
            if config_path.exists():
                try:
                    config_data = json.loads(config_path.read_text(encoding="utf-8"))
                    configured = {item.get("filename"): item for item in config_data.get("frames", []) if item.get("filename")}
                except (OSError, ValueError, TypeError):
                    configured = {}
            for path in sorted(frames_dir.iterdir(), key=lambda p: p.name.casefold()):
                if path.is_file() and path.suffix.lower() in FRAME_EXTENSIONS and not path.name.startswith("."):
                    item = {
                        "filename": path.name,
                        "name": display_name(path.name),
                        "path": "frames/" + path.name
                    }
                    slot_config = configured.get(path.name, {}).get("photoSlots")
                    if isinstance(slot_config, list) and slot_config:
                        item["photoSlots"] = slot_config
                    items_by_path[item["path"]] = item
            items = sorted(items_by_path.values(), key=lambda item: (item.get("name", "").casefold(), item.get("path", "").casefold()))
            payload = json.dumps({"frames": items}, ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(payload)))
            self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
            self.end_headers()
            self.wfile.write(payload)
            return
        return super().do_GET()

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()

if __name__ == "__main__":
    os.chdir(ROOT)
    server = ThreadingHTTPServer(("127.0.0.1", 8000), Handler)
    print("Pabna Photo Frame Generator is running.")
    print("Open: http://127.0.0.1:8000")
    print("Drop PNG/JPG/WEBP/SVG files into the frames folder; the website rescans every 3 seconds.")
    print("Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\\nServer stopped.")
    finally:
        server.server_close()
