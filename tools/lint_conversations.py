#!/usr/bin/env python3
"""Lint conversations/*.md (and current-situation/scenes.md for rules 2-4).

Run from repo root:  python3 tools/lint_conversations.py
Exit code 1 if any problem is found.

Dialogue format: lines starting with `**S:**` (setter) and `**P:**` (prospect).
Annotations are blockquote lines starting with `> [TAG ...]`.
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BANNED = [
    r"show the gap", r"are you actually committed", r"committed to making",
    r"there'?s an investment", r"anywhere from \$", r"\$\d[\d,.]*k? to \$\d",
    r"how does that make you feel", r"why aren'?t you", r"why haven'?t you",
    r"i hear you", r"journey", r"unlock", r"transform",
]
SECTIONS = ["Depth scorecard", "What to notice", "If they had said X instead", "Worse version"]
ORDER = ["FRAME", "INTENT", "CURRENT", "RECAP", "TIMEFRAME", "WGW", "WHY NOW",
         "FIN", "PITCH", "LOCK", "SHOW UP"]
TAG_RE = re.compile(r"\[(FRAME|INTENT|EI|CURRENT|RECAP|TIMEFRAME|WGW|WHY NOW|FIN|PITCH|LOCK|SHOW UP|TEST [ABC]|WHY THIS LINE|RECOVERY)[^\]]*\]")
S_RE = re.compile(r"^\*\*S:\*\*\s*(.*)")
P_RE = re.compile(r"^\*\*P:\*\*\s*(.*)")
SCENE_S = re.compile(r"^S:\s*(.*)")
SCENE_P = re.compile(r"^P:\s*(.*)")
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")


def blocklist():
    p = os.path.join(ROOT, "tools", "pii_blocklist.txt")
    if not os.path.exists(p):
        return []
    return [l.strip().lower() for l in open(p, encoding="utf-8")
            if l.strip() and not l.startswith("#")]


def words(s):
    return len(re.findall(r"\S+", s))


def check_lines(path, text, s_re, p_re, problems, full):
    cur_tags = []
    p_turns = []
    test_a = False
    allowed_hear = 0
    for n, line in enumerate(text.splitlines(), 1):
        if line.startswith(">"):
            for m in TAG_RE.finditer(line):
                cur_tags.append(m.group(1))
                if m.group(1).startswith("TEST A"):
                    test_a = True
            if "TEST A" in line:
                test_a = True
            continue
        m = s_re.match(line)
        if m:
            s = m.group(1)
            low = s.lower()
            for b in BANNED:
                if re.search(b, low):
                    if b == r"why haven'?t you" and test_a:
                        continue
                    if b == r"i hear you":
                        allowed_hear += 1
                        if allowed_hear <= 1:
                            continue
                    problems.append(f"{path}:{n}: banned /{b}/ in: {s[:60]}")
            if s.count("?") >= 2:
                problems.append(f"{path}:{n}: stacked questions: {s[:60]}")
            last = cur_tags[-1] if cur_tags else ""
            if words(s) > 40 and last not in ("FRAME", "PITCH"):
                problems.append(f"{path}:{n}: setter turn {words(s)} words (>40)")
            continue
        m = p_re.match(line)
        if m:
            p_turns.append(words(m.group(1)))
    return p_turns, cur_tags


def lint_conversation(path, problems):
    text = open(path, encoding="utf-8").read()
    name = os.path.relpath(path, ROOT)
    p_turns, _ = check_lines(name, text, S_RE, P_RE, problems, True)

    for sec in SECTIONS:
        if sec.lower() not in text.lower():
            problems.append(f"{name}: missing section '{sec}'")

    head = text[:1500]
    outcome = re.search(r"\*\*Outcome:\*\*\s*([\w-]+)", head)
    outcome = outcome.group(1).lower() if outcome else ""
    tags = []
    for line in text.splitlines():
        if line.startswith(">"):
            tags += [m.group(1) for m in TAG_RE.finditer(line)]
    seq = [t for t in tags if t in ORDER]
    if "FRAME" not in seq or "INTENT" not in seq:
        problems.append(f"{name}: missing [FRAME] or [INTENT]")
    if outcome == "booked":
        want = [t for t in ORDER]
        # collapse repeated CURRENT tags
        collapsed = [t for i, t in enumerate(seq) if i == 0 or t != seq[i - 1]]
        missing = [t for t in want if t not in collapsed]
        if missing:
            problems.append(f"{name}: booked call missing tags {missing}")
        else:
            idx = [collapsed.index(t) for t in want]
            if idx != sorted(idx):
                problems.append(f"{name}: tags out of order: {collapsed}")
    elif outcome not in ("dq", "no-book", "nobook"):
        problems.append(f"{name}: unknown/missing Outcome '{outcome}'")

    first = p_turns[:12]
    if first and sum(first) / len(first) > 14:
        problems.append(f"{name}: prospect too cooperative (avg {sum(first)/len(first):.1f} words)")

    pii(name, text, problems)


def pii(name, text, problems):
    if EMAIL.search(text.replace("you@", "")):
        problems.append(f"{name}: email address found")
    if "fathom.video" in text.lower():
        problems.append(f"{name}: fathom link")
    low = text.lower()
    for b in blocklist():
        if b in low:
            problems.append(f"{name}: blocklisted name")


def main():
    problems = []
    files = sorted(f for f in glob.glob(os.path.join(ROOT, "conversations", "*.md"))
                   if os.path.basename(f) not in ("_TEMPLATE.md", "README.md"))
    for f in files:
        lint_conversation(f, problems)
    scenes = os.path.join(ROOT, "current-situation", "scenes.md")
    if os.path.exists(scenes):
        text = open(scenes, encoding="utf-8").read()
        check_lines("current-situation/scenes.md", text, SCENE_S, SCENE_P, problems, False)
        pii("current-situation/scenes.md", text, problems)
    for p in problems:
        print(p)
    print(f"{len(files)} conversations checked, {len(problems)} problems")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
