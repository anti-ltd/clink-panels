# Create a Clink panel

You are contributing one focused custom keyboard panel. Read `README.md`, inspect the existing `Panels/*.clinkpanel` files, and inspect `tools/build-manifest.py` before editing. Create or update exactly one panel file in `Panels/`.

A panel is JSON with a stable id, visible name, SF Symbol icon, concise summary, placement, enabled state, and a `source` string defining `view(state)`. Begin with the closest existing panel and use only the constrained panel helpers and patterns it demonstrates. Keep the panel small, offline, deterministic, and immediately useful from the keyboard. It must not use imports, networking, file access, randomness, time, or unsupported APIs. Treat all inserted text as user-facing content and preserve Unicode correctly.

Use a unique id and descriptive kebab-case filename. Check that the JSON parses and review the source for useful empty, long-text, and Unicode cases. Then run:

```sh
python3 tools/build-manifest.py
```

Include the regenerated `manifest.json` if changed. Do not alter the release workflow or security policy. Finish by explaining the panel’s interaction, the constrained APIs used, and the checks performed.
