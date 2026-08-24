#!/usr/bin/env python3
import hashlib, json, os, pathlib
root = pathlib.Path(__file__).resolve().parents[1]
repo = os.environ.get("GITHUB_REPOSITORY", "anti-ltd/clink-panels")
panels = []
for path in sorted((root / "Panels").glob("*.clinkpanel")):
    data = path.read_bytes(); panel = json.loads(data)
    panels.append({"id": path.stem, "name": panel["name"], "version": "latest", "asset": {"path": path.name, "url": f"https://github.com/{repo}/releases/download/latest/{path.name}", "sha256": hashlib.sha256(data).hexdigest(), "byteCount": len(data)}})
(root / "manifest.json").write_text(json.dumps({"version": "latest", "panels": panels}, indent=2) + "\n")
