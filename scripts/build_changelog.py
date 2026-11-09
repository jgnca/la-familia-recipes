#!/usr/bin/env python3
"""Rebuild CHANGELOG.md from changelog.json.

changelog.json is the source of truth (the website reads it too).
Run this after adding an entry:  python3 scripts/build_changelog.py
"""
import json
from datetime import date
from pathlib import Path

root = Path(__file__).resolve().parent.parent
log = json.loads((root / "changelog.json").read_text())
titles = {r["id"]: r["title"] for r in json.loads((root / "recipes.json").read_text())}
LABEL = {"added": "Added", "changed": "Changed", "removed": "Removed", "site": "Book"}

def nice(d):
    y, m, dd = map(int, d.split("-"))
    return date(y, m, dd).strftime("%B %-d, %Y")

lines = [
    "# Change log",
    "",
    "Every recipe added to La Familia Recipe Book and every correction made to one, newest first.",
    "This file is generated from `changelog.json` by `scripts/build_changelog.py`; edit the JSON, not this file.",
    "",
]
current = None
for e in sorted(enumerate(log), key=lambda p: (p[1]["date"], p[0]), reverse=True):
    e = e[1]
    if e["date"] != current:
        current = e["date"]
        lines += [f"## {nice(current)}", ""]
    who = titles.get(e.get("recipe"), e.get("recipe")) if e.get("recipe") else "Recipe book"
    lines.append(f"- **{LABEL.get(e['type'], e['type'].title())} · {who}:** {e['summary']}")
    if e.get("why"):
        lines.append(f"  - *Why:* {e['why']}")
lines.append("")
(root / "CHANGELOG.md").write_text("\n".join(lines))
print(f"Wrote CHANGELOG.md ({len(log)} entries)")
