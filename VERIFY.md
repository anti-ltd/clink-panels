# Verify this Clink panels repository

Read `README.md`, `PROMPT.md`, each `Panels/*.clinkpanel`, and `tools/build-manifest.py`. Audit without changing files unless asked to remediate a finding.

Parse every panel JSON, then run:

```sh
python3 tools/build-manifest.py
```

Verify each panel has a unique stable id, visible name, valid SF Symbol icon, concise summary, placement, enabled state, and a `source` string defining `view(state)`. Inspect source against existing approved patterns. It must be small, offline, deterministic, Unicode-safe, and useful from the keyboard; it must not import modules or use networking, file access, randomness, time, or unsupported APIs. Consider empty, long, and Unicode user text.

Confirm the regenerated `manifest.json` represents exactly the panel files and check that release workflows and source-policy protections have not been weakened. Report commands, pass/fail status for every panel, manifest status, and exact paths plus fixes for any finding. Never claim runtime testing unless it was actually done in Clink.
