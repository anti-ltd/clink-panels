#!/usr/bin/env python3
import hashlib, json, os, pathlib
root = pathlib.Path(__file__).resolve().parents[1]
repo = os.environ.get("GITHUB_REPOSITORY", "anti-ltd/clink-panels")
panels = []
# Each distinct set of bytes gets a permanent release URL. A cached manifest
# must never point at a newer file with a different checksum: a client that
# read the catalog before a release still installs the bytes it was promised.
version = "panels-" + hashlib.sha256(json.dumps(
    [(p.name, hashlib.sha256(p.read_bytes()).hexdigest())
     for p in sorted(((root / "Panels").glob("*.clinkpanel"))) if not p.name.startswith(".")],
    separators=(",", ":")).encode()).hexdigest()

for path in sorted((root / "Panels").glob("*.clinkpanel")):
    data = path.read_bytes(); panel = json.loads(data)
    panels.append({"id": path.stem, "name": panel["name"], "icon": panel.get("icon", ""), "summary": panel.get("summary", ""), "version": version, "asset": {"path": path.name, "url": f"https://github.com/{repo}/releases/download/{version}/{path.name}", "sha256": hashlib.sha256(data).hexdigest(), "byteCount": len(data)}})
(root / "manifest.json").write_text(json.dumps({"version": version, "panels": panels}, indent=2) + "\n")
