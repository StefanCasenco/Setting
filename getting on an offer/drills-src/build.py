#!/usr/bin/env python3
"""Builds ../drills.html from the deck JSON files and template.html.

Usage (from anywhere):
    python3 "getting on an offer/drills-src/build.py"

Each card is a JSON array:
    [category, stage, context, prospect line, [good answers...], "not this", "why", source]
Add cards to any deck file, run this script, and open drills.html.
"""
import json
import pathlib

here = pathlib.Path(__file__).resolve().parent
decks = [
    ["deck1-core.json"],
    ["deck2a-phone-calls-1-50.json", "deck2b-phone-calls-2-001-050.json", "deck2c-phone-calls-2-051-100.json"],
    ["deck3-new-scenarios.json"],
]

data = []
for files in decks:
    cards = []
    for f in files:
        part = json.loads((here / f).read_text(encoding="utf-8"))
        for c in part:
            assert len(c) in (7, 8) and isinstance(c[4], list), f"bad card in {f}: {c[:4]}"
        cards += part
    data.append(cards)

html = (here / "template.html").read_text(encoding="utf-8")
html = html.replace("/*__DATA__*/", json.dumps(data, ensure_ascii=False))
out = here.parent / "drills.html"
out.write_text(html, encoding="utf-8")
print(f"Built {out.name}: " + ", ".join(f"check {k+1} = {len(d)} cards" for k, d in enumerate(data)) + f", total {sum(map(len, data))}")
