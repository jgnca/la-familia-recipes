# System changes (admin log)

Changes to how the recipe book works and looks (themes, icons, layout, features), newest first.
Recipe additions and corrections are in [CHANGELOG.md](CHANGELOG.md).

_Generated from `changelog.json` by `scripts/build_changelog.py`; edit the JSON, not this file._

## November 9, 2026

- Added a "Suggest a change" button at the bottom of every recipe. It opens John's Google Form (no sign-in needed) with the recipe name filled in. Requests are emailed to John and saved in the form's linked Google Sheet.
  - *Why:* Lets readers like John's wife request corrections, with a record of every request, including ones that aren't acted on.
  - *Files:* `index.html`, `README.md`
  - *Commit:* pending (filled in on the next update)
- Added recipe photos: one photo of the finished dish at the top of each recipe and as a thumbnail in the list, with a "No photo yet" placeholder until one is added. New script scripts/add_photo.py crops and resizes photos to 1200×900 and strips all metadata, including GPS location.
  - *Why:* John wants a photo of each finished dish, using his own photos rather than the creators' (which can't be republished in a public repo).
  - *Files:* `index.html`, `scripts/add_photo.py`, `README.md`
  - *Commit:* [f672e27](https://github.com/jgnca/la-familia-recipes/commit/f672e27)
- Replaced the Black & White theme with Slate, a calm blue-gray. Themes are now Sage, Dusty Rose, Terracotta and Slate. Anyone who had picked Black & White falls back to Sage.
  - *Why:* John preferred the blue-gray over plain black and white.
  - *Files:* `index.html`
  - *Commit:* [37682c9](https://github.com/jgnca/la-familia-recipes/commit/37682c9)
- Split the change log in two. The book's Change log page and CHANGELOG.md now show recipe changes only; system changes (themes, icons, layout, features) go to SYSTEM-CHANGES.md, with the files touched and a link to each commit.
  - *Why:* Cooks only need recipe history; system changes are for the admin.
  - *Files:* `changelog.json`, `scripts/build_changelog.py`, `CHANGELOG.md`, `SYSTEM-CHANGES.md`, `index.html`, `README.md`
  - *Commit:* [b3f6c2f](https://github.com/jgnca/la-familia-recipes/commit/b3f6c2f)
- Added four color themes, picked from the dots next to Change log: Sage (the original), Dusty Rose, Terracotta, and Black & White. Each one follows the device's light/dark setting, and the choice is saved per device.
  - *Why:* Lets each person pick the look they like while keeping the book simple.
  - *Files:* `index.html`
  - *Commit:* [b8c6a44](https://github.com/jgnca/la-familia-recipes/commit/b8c6a44)
- Added the change log: changelog.json as the source of truth, a Change log page and per-recipe History section in the book, and CHANGELOG.md generated for GitHub.
  - *Files:* `changelog.json`, `CHANGELOG.md`, `scripts/build_changelog.py`, `index.html`, `README.md`
  - *Commit:* [ae612f6](https://github.com/jgnca/la-familia-recipes/commit/ae612f6)

## November 8, 2026

- Added an A–Z / Newest sort toggle to the recipe list, defaulting to A–Z.
  - *Files:* `index.html`
  - *Commit:* [d325f16](https://github.com/jgnca/la-familia-recipes/commit/d325f16)
- Added the fork-and-spoon home screen icon (dusty rose).
  - *Files:* `icon.svg`, `icon-512.png`, `apple-touch-icon.png`, `index.html`
  - *Commit:* [231f8cf](https://github.com/jgnca/la-familia-recipes/commit/231f8cf)

## November 7, 2026

- Book description changed to "Recipes from the web, family, and friends."
  - *Files:* `index.html`
  - *Commit:* [c9cb5b5](https://github.com/jgnca/la-familia-recipes/commit/c9cb5b5)
- Moved the recipe book from a claude.ai artifact to GitHub Pages (static index.html + recipes.json), with search, tag filters, servings scaling and cooking mode with timers.
  - *Files:* `index.html`, `recipes.json`, `README.md`
  - *Commit:* [9aa1953](https://github.com/jgnca/la-familia-recipes/commit/9aa1953)
