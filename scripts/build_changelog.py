#!/usr/bin/env python3
"""Rebuild CHANGELOG.md and SYSTEM-CHANGES.md from changelog.json.

changelog.json is the source of truth (the website reads it too).
Run this after adding an entry:  python3 scripts/build_changelog.py

- Recipe entries (added / changed / removed) go to CHANGELOG.md and the book's
  Change log page.
- System entries (themes, icons, layout, features) go to SYSTEM-CHANGES.md only.
  Their commit link is filled in automatically from git history once the entry
  has been committed; until then it shows as pending.
"""
import json
import subprocess
from datetime import date
from pathlib import Path

REPO_URL = "https://github.com/jgnca/la-familia-recipes"
root = Path(__file__).resolve().parent.parent
log_path = root / "changelog.json"
log = json.loads(log_path.read_text())
titles = {r["id"]: r["title"] for r in json.loads((root / "recipes.json").read_text())}
LABEL = {"added": "Added", "changed": "Changed", "removed": "Removed"}


def nice(d):
    y, m, dd = map(int, d.split("-"))
    return date(y, m, dd).strftime("%B %-d, %Y")


def first_commit_with(text):
    """Short hash of the oldest commit whose changelog.json gained this text."""
    try:
        out = subprocess.run(
            ["git", "log", "--reverse", "--format=%h", "-S", text, "--", "changelog.json"],
            cwd=root, capture_output=True, text=True, check=True,
        ).stdout.split()
        return out[0] if out else None
    except Exception:
        return None


# Fill in commit hashes for system entries that have since been committed.
filled = 0
for e in log:
    if e.get("type") == "system" and not e.get("commit"):
        # Search for the summary exactly as it's stored in the JSON (quotes escaped).
        c = first_commit_with(json.dumps(e["summary"], ensure_ascii=False)[1:-1])
        if c:
            e["commit"] = c
            filled += 1
if filled:
    log_path.write_text(json.dumps(log, indent=2, ensure_ascii=False) + "\n")


def newest_first(entries):
    return [e for _, e in sorted(enumerate(entries), key=lambda p: (p[1]["date"], p[0]), reverse=True)]


def by_day(entries, render):
    lines, current = [], None
    for e in newest_first(entries):
        if e["date"] != current:
            current = e["date"]
            lines += ["", f"## {nice(current)}", ""]
        lines += render(e)
    return lines


def recipe_line(e):
    who = titles.get(e.get("recipe"), e.get("recipe"))
    out = [f"- **{LABEL.get(e['type'], e['type'].title())} · {who}:** {e['summary']}"]
    if e.get("why"):
        out.append(f"  - *Why:* {e['why']}")
    return out


def system_line(e):
    out = [f"- {e['summary']}"]
    if e.get("why"):
        out.append(f"  - *Why:* {e['why']}")
    if e.get("files"):
        out.append("  - *Files:* " + ", ".join(f"`{f}`" for f in e["files"]))
    c = e.get("commit")
    out.append(f"  - *Commit:* [{c}]({REPO_URL}/commit/{c})" if c else "  - *Commit:* pending (filled in on the next update)")
    return out


recipes_log = [e for e in log if e.get("type") != "system"]
system_log = [e for e in log if e.get("type") == "system"]

(root / "CHANGELOG.md").write_text("\n".join([
    "# Change log",
    "",
    "Every recipe added to La Familia Recipe Book and every correction made to one, newest first.",
    "Changes to the book itself are in [SYSTEM-CHANGES.md](SYSTEM-CHANGES.md).",
    "",
    "_Generated from `changelog.json` by `scripts/build_changelog.py`; edit the JSON, not this file._",
    *by_day(recipes_log, recipe_line),
    "",
]))

(root / "SYSTEM-CHANGES.md").write_text("\n".join([
    "# System changes (admin log)",
    "",
    "Changes to how the recipe book works and looks (themes, icons, layout, features), newest first.",
    "Recipe additions and corrections are in [CHANGELOG.md](CHANGELOG.md).",
    "",
    "_Generated from `changelog.json` by `scripts/build_changelog.py`; edit the JSON, not this file._",
    *by_day(system_log, system_line),
    "",
]))

print(f"Wrote CHANGELOG.md ({len(recipes_log)} entries) and SYSTEM-CHANGES.md ({len(system_log)} entries)"
      + (f"; filled {filled} commit link(s)" if filled else ""))
