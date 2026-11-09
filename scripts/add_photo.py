#!/usr/bin/env python3
"""Add (or replace) the photo for a recipe.

Usage:  python3 scripts/add_photo.py <recipe-id> <photo-file> [--alt "description"]

- Rotates the photo upright, center-crops it to 4:3 and resizes it to 1200x900.
- Saves it as images/<recipe-id>.jpg with ALL metadata removed (iPhone photos
  carry GPS location and device info; this repo is public).
- Sets the recipe's "image" (and optional "imageAlt") in recipes.json.

Remember to add a changelog.json entry ("Added a photo" / "Replaced the photo")
and run scripts/build_changelog.py before committing.
"""
import argparse
import json
from pathlib import Path

from PIL import Image, ImageOps

W, H = 1200, 900
root = Path(__file__).resolve().parent.parent

ap = argparse.ArgumentParser()
ap.add_argument("recipe_id")
ap.add_argument("photo")
ap.add_argument("--alt")
args = ap.parse_args()

recipes_path = root / "recipes.json"
recipes = json.loads(recipes_path.read_text())
recipe = next((r for r in recipes if r["id"] == args.recipe_id), None)
if recipe is None:
    raise SystemExit(f"No recipe with id {args.recipe_id!r}")

try:  # iPhone HEIC support, if available
    from pillow_heif import register_heif_opener
    register_heif_opener()
except ImportError:
    pass

img = ImageOps.exif_transpose(Image.open(args.photo)).convert("RGB")
img = ImageOps.fit(img, (W, H), Image.LANCZOS, centering=(0.5, 0.5))

out_dir = root / "images"
out_dir.mkdir(exist_ok=True)
out = out_dir / f"{args.recipe_id}.jpg"
clean = Image.new("RGB", img.size)  # fresh image = no EXIF/GPS carried over
clean.paste(img)
clean.save(out, "JPEG", quality=82, optimize=True, progressive=True)

recipe["image"] = f"images/{args.recipe_id}.jpg"
if args.alt:
    recipe["imageAlt"] = args.alt
recipes_path.write_text(json.dumps(recipes, indent=2, ensure_ascii=False) + "\n")
print(f"Saved {out.relative_to(root)} ({out.stat().st_size // 1024} KB) and updated recipes.json")
