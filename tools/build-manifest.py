#!/usr/bin/env python3
import hashlib, json, os, pathlib

# BEGIN repository platform policy (Tools/sync_repository_platforms.py)
def apply_platforms(root, manifest):
    """Annotate every pack; absent policy preserves legacy cross-platform packs."""
    path = root / "platforms.json"
    policy = json.loads(path.read_text()) if path.exists() else {}
    if not isinstance(policy, dict) or set(policy) - {"default", "overrides"}:
        raise ValueError("platforms.json must contain default and overrides only")
    default = policy.get("default", "both")
    overrides = policy.get("overrides", {})
    allowed = ("ios", "android", "both")
    if default not in allowed or not isinstance(overrides, dict):
        raise ValueError("Invalid repository platform policy")
    if any(value not in allowed for value in overrides.values()):
        raise ValueError("Platforms must be ios, android or both")
    entries = [entry for key, value in manifest.items() if isinstance(value, list)
               for entry in value]
    identifiers = {entry.get("id", entry.get("code", entry.get("locale"))) for entry in entries}
    if set(overrides) - identifiers:
        raise ValueError("Platform overrides name missing packs: " + str(sorted(set(overrides) - identifiers)))
    for entry in entries:
        identifier = entry.get("id", entry.get("code", entry.get("locale")))
        entry["platform"] = overrides.get(identifier, default)
    return manifest
# END repository platform policy

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
(root / "manifest.json").write_text(json.dumps(apply_platforms(root, {"version": version, "panels": panels}), indent=2) + "\n")
