# La Familia Recipe Book

Our family recipe book, published with GitHub Pages at https://jgnca.github.io/la-familia-recipes/

## How it works

- `index.html` is the whole site: search, tag filters, a servings dial that rescales amounts, and a step-by-step cooking mode with timers.
- `recipes.json` holds every recipe. Adding a recipe means adding one entry to this file and committing it; GitHub Pages republishes the site a minute or two later.

## Recipe format

Each entry in `recipes.json` looks like this:

```json
{
  "id": "boiled-chicken-breasts",
  "title": "Recipe name",
  "description": "One sentence",
  "source": {"type": "instagram | tiktok | web | question | other", "label": "Where it came from", "url": "optional link"},
  "servings": 4,
  "servingsLabel": "servings",
  "time": "About 30 min",
  "tags": ["chicken", "weeknight"],
  "addedAt": "ISO timestamp",
  "ingredients": [{"amount": 0.5, "unit": "cup", "name": "cooked lentils"}],
  "steps": [{"title": "Short step name", "text": "Cook {3} with {5}...", "minutes": 4}],
  "notes": "Paragraphs separated by newlines"
}
```

- `unit` is one of g, kg, ml, l, tsp, tbsp, cup, fl_oz, oz, lb, pinch, or left out for countable items.
- `{N}` in step text inserts ingredient N (counting from 0) with its scaled amount.
- Steps with `minutes` get a timer in cooking mode.

## Change log

Every recipe added and every correction made is recorded in `changelog.json`, with the date, the recipe, what changed and why. The site shows it on a Change log page and in a History section on each recipe. [CHANGELOG.md](CHANGELOG.md) is the readable version for GitHub.

To log a change, add an entry to `changelog.json` in the same commit as the edit, then run `python3 scripts/build_changelog.py` to rebuild CHANGELOG.md:

```json
{
  "date": "2026-11-09",
  "recipe": "crispy-smashed-potatoes-garlic-rosemary",
  "type": "changed",
  "summary": "What changed, including old and new values (e.g. oven 375°F → 425°F).",
  "why": "Why it changed."
}
```

- `type` is `added`, `changed`, `removed`, or `site` (a change to the book itself; leave out `recipe`).
- `why` is optional for `added` entries.
