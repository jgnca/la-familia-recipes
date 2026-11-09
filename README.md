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

## Photos

Each recipe can have one photo of the finished dish, ideally your own, taken when you make it. Recipes without one show a "No photo yet" placeholder.

To add or replace a photo:

```
python3 scripts/add_photo.py <recipe-id> path/to/photo.jpg --alt "Short description"
```

The script turns the photo upright, crops it to 4:3, resizes it to 1200×900, saves it as `images/<recipe-id>.jpg` with all metadata removed (iPhone photos include GPS location, and this repo is public), and sets the recipe's `image` field. Then log it in `changelog.json` ("Added a photo") and rebuild the logs.

## Change log

Every change is recorded in `changelog.json`, with the date, what changed and why. It feeds two logs:

- **Recipe log:** recipes added, changed or removed. Shown in the book (the Change log page and a History section on each recipe) and in [CHANGELOG.md](CHANGELOG.md).
- **Admin log:** system changes such as themes, icons, layout and features. Kept out of the book and listed in [SYSTEM-CHANGES.md](SYSTEM-CHANGES.md), with the files touched and a link to each commit.

To log a change, add an entry to `changelog.json` in the same commit as the edit, then run `python3 scripts/build_changelog.py` to rebuild both Markdown files. Never edit the Markdown files by hand.

Recipe entry:

```json
{
  "date": "2026-11-09",
  "recipe": "crispy-smashed-potatoes-garlic-rosemary",
  "type": "changed",
  "summary": "What changed, including old and new values (e.g. oven 375°F → 425°F).",
  "why": "Why it changed."
}
```

System entry:

```json
{
  "date": "2026-11-09",
  "type": "system",
  "summary": "What changed.",
  "why": "Why it changed.",
  "files": ["index.html"]
}
```

- Recipe `type` is `added`, `changed` or `removed`; `why` is optional for `added`.
- System entries leave out `recipe`. Their `commit` is filled in automatically by the build script after the entry is committed.
