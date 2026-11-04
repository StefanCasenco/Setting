#!/usr/bin/env python3
"""Builds ../fluency.html: Phone Fluency, the 'say it with context' drill.

Usage (from anywhere):
    python3 "getting on an offer/fluency-src/build.py"

How it works: lines.py holds the hand-written patterns (bare question, the fluent version,
when to use it, when not to). Each pattern is filled in for every niche's prospects
(drills-src/niches.py and personas2.py), so you practise the same skill in many real
situations. Patterns with no niche details are included once.
"""
import json
import pathlib
import sys

here = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent / "drills-src"))
sys.path.insert(0, str(here))
from niches import NICHES  # noqa: E402
from lines import L  # noqa: E402
from personas2 import P2  # noqa: E402

people = []
for n in NICHES:
    people.append(dict(n))
    alt = dict(n)
    alt.update(P2[n["key"]])
    people.append(alt)

items, seen = [], set()
for ln in L:
    for p in people:
        if ln["modes"] and p["mode"] not in ln["modes"]:
            continue
        try:
            say = ln["say"].format(**p)
            bare = ln["bare"].format(**p)
        except KeyError as e:
            raise SystemExit(f"missing field {e} in: {ln['say']}")
        if "{}" in say or say.count("  "):
            continue
        if p["key"] == "tech" and "side thing" in say:
            continue
        if say[:1].islower():
            say = say[0].upper() + say[1:]
        universal = say == ln["say"]
        key = say
        if key in seen:
            continue
        seen.add(key)
        items.append([ln["stage"], "All niches" if universal else p["label"],
                      "" if universal else p["persona"], bare, say, ln["tool"], ln["use"], ln["skip"]])

html = (here / "template.html").read_text(encoding="utf-8")
html = html.replace("/*__DATA__*/", json.dumps(items, ensure_ascii=False))
(here.parent / "fluency.html").write_text(html, encoding="utf-8")
print(f"Built fluency.html: {len(items)} unique examples from {len(L)} patterns x {len(people)} prospects")
