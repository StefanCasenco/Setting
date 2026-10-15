# CLAUDE CODE BRIEF: Rebuild the Appointment-Setting repo around Script v2

> **You are Claude Code in a cloud session with access to `StefanCasenco/Appointment-Setting`.**
> Read this whole file before touching anything. It is the spec. When it conflicts with the existing repo, **this file wins**. When it conflicts with your instincts about sales, **this file still wins**. The reasons are all in Section 3.

---

## 0. Mission in five lines

1. The repo documents an **old setting script** (guide-download lead, Show the Gap, "are you committed?", a price range on the call). It's obsolete. Ștefan has a **new script** (Appendix A) after ~5 hours of coaching from a more experienced closer, Atefur.
2. Rewrite the repo around the new script: the SOP, the README, and the example calls.
3. Add the two things Ștefan asked for that don't exist yet: a **CURRENT SITUATION toolkit** (examples, every question he can ask there, ladders by what the prospect says first) and a **library of full conversations**, organised by *what the prospect gives first* (vague, open, closed, specific, loaded, guarded...), so he can feel how a setting call goes.
4. Goal of everything: make setting calls feel like **a conversation, not a form he walks people through**. Qualification still happens, but invisibly.
5. Credits expire **Nov 5, 2026**. Work in the phase order below, commit after each phase, and keep `PROGRESS.md` current so a new session can resume.

---

## 1. Read first: hard constraints

| # | Constraint |
|---|---|
| C1 | **The repo is public.** Never commit raw transcripts, emails, Fathom links, or full names of real people (Atefur's last name, Ștefan's email). Use the evidence digest in Appendix B instead. Prospect names in example calls must be invented. |
| C2 | **Tag the old state first:** `git tag v1-old-script` on current main, before any change. Work on branch `script-v2`. Commit per phase. Open a PR at the end. Never push to main. |
| C3 | **Don't invent facts about the offer.** Price, program names, closer names, call length, minimum savings, financing: use placeholders (`$CLOSER`, `$MIN_SAVINGS`, `$COMPANY`). If a spec says FLAG, use the default and list it in `PROGRESS.md` under "Needs Ștefan". |
| C4 | **Honesty guardrails stay.** No income or outcome claims, no guarantees, never help anyone borrow or risk money they can't spare (credit cards, loans, retirement, emergency funds), never say the offer is free, never deny a cost if asked directly. Keep the SOP's Safety section (Section 11) intact. |
| C5 | **Do not encode manipulation.** Atefur said things like "tell them what they want to hear" and "emotionally manipulate them enough" (O10 1:18:46, O14 37:07). Those are not adopted. The method here is *curiosity and honest qualification*. Don't write calls where the setter flatters, invents claims ("you're a perfect replica of our top students"), or manufactures pressure. |
| C6 | **Don't touch** `.git` history. Don't delete anything: **move** it to `archive/`. |
| C7 | **Language:** plain, native, casual English. No consultant-speak. See Section 7.3 (voice). |

---

## 2. Who and what

- **Ștefan** is learning high-ticket sales (B2C). Currently setting for **trading (futures/prop firms)** and **ecom**. Eastern-European, calm, logical, introverted by nature. His tonality improved (Atefur, O10 24:24 → O14 45:56) but his bottleneck is **CURRENT SITUATION**: listening, staying on a thread, and digging for pain without making it a form (his own diagnosis, O14 25:46).
- **Setter's job:** sell the *meeting*, not the product (O10 1:09:45). Bank four things for the closer: **real pain, real urgency (why now), real money, actually serious.** Then book.
- **Homework he's doing:** write the script out and read it aloud 10 times a day (O11 58:05). So the **fixed parts must be short, stable, and easy to say.** Everything you generate must preserve the exact wording in Appendix A.
- **What he wants from you:** examples and full calls he can read to absorb the *feel*. He wants to see what the prospect gives first and how the setter reads it, and he wants a big bank of natural CURRENT questions so he doesn't default to reading.

---

## 3. What changed and why (read the reasons, then obey)

Every decision below is backed by evidence in Appendix B (IDs like E14).

| # | Decision | Why |
|---|---|---|
| D1 | **Fixed spine; only CURRENT is freestyle.** | Atefur: structure should be "like iron", same every call (E23); stick to your process (E27). The old SOP's *free-order buckets* contradict this. Replace them. Keep one idea from the old SOP: if the prospect already answered a node, **confirm and skip it**, never reorder. |
| D2 | **Removed: Show the Gap, Want to Change / Commitment.** | Closer-level moves; "are you actually committed?" is a conviction test, not a setter move. The Recap + Why Now cover it. |
| D3 | **Added: RECAP (deep goal) and WHY NOW.** | Atefur endorsed "why now" (E28). Recap must restate the *deep* goal, not the tactical one (E30). |
| D4 | **Financial qualification = a ladder; the setter never says a price, range, or "there's an investment".** | Atefur O14 34:09-37:07, 38:09-39:13 (E29). If asked "how much?", give a taster only (see script). **Conflict:** a course video (Appendix B, V3) says the opposite: give a range and ask "doable?". Ștefan chose Atefur's version. Don't mix them. |
| D5 | **Pitch no longer ends with a price question.** | Same as D4. |
| D6 | **CURRENT is about emotion, not job facts.** Don't default to "what do you do, how do you feel about the job, how long...". | That chain assumes the job is the problem (E30). Prospects may love their job. Ask the real motivation instead. |
| D7 | **Layers, not interrogation.** Echo their word → "what do you mean?" → a scene → personal impact → cost. | E3, E11, E12, E21. |
| D8 | **No "why aren't you / why haven't you" in CURRENT.** | Defensive answers (E20). One line in TIMEFRAME is kept as an explicit A/B **TEST** (see script). |
| D9 | **Don't ask why they're still stuck (limiting belief).** | That's the closer's job (E22). |
| D10 | **Prospects in examples must be realistic, not cooperative.** | Atefur called the prospect in a roleplay "the most OP prospect in the world", and said real ones are harder (E9). The old repo's calls are probably too smooth. Fix that (Section 7.2). |
| D11 | **Depth over speed in *training*; shorter live.** | Atefur: "better too deep than shallow" (E14), real calls may go less deep (E24). Default target is 8-12 min live, CURRENT ≈ 4-6. FLAG. |
| D12 | **Move the old 50 roleplays to `archive/`; build a new library.** | They encode the old script. Patching 50 files half-way is worse than a clean library. Reuse their *lead profiles and hidden truths* as seeds where useful. |

---

## 4. Target repo structure

```
/
├── README.md                    (NEW: 1-page map of the repo; links everything)
├── SETTING-SCRIPT.md            (NEW: Appendix A, verbatim. The single source of truth.)
├── SETTING-SOP.md               (REWRITE: shorter; see Phase 2)
├── PROGRESS.md                  (NEW: phase checklist, "Needs Ștefan" list, open flags)
├── current-situation/
│   ├── README.md                (the playbook: layers, techniques, exit test, don'ts)
│   ├── question-bank.md         (≥150 tagged questions: the big one)
│   ├── by-first-answer.md       (table + mini-ladders for every common first answer)
│   ├── mistakes-and-fixes.md    (real bad lines → better lines, from Appendix C)
│   └── scenes.md                (30+ 6-12 line CURRENT excerpts; copy-paste practice)
├── conversations/
│   ├── README.md                (index + the first-answer matrix + how to use)
│   ├── 01-… .md … NN-… .md      (full calls; see Phase 4/5)
│   └── _TEMPLATE.md
├── drills/
│   ├── READ-ALOUD.md            (only the fixed SAY lines: the daily 10x sheet)
│   ├── self-play.md             (play prospect against yourself; Atefur O11 1:08:39)
│   ├── review-your-calls.md     (the pause-and-ask drill; O14 45:17)
│   ├── prospect-simulator.md    (system prompt to roleplay with an AI; see Appendix D)
│   └── call-log-template.md     (post-call log + A/B tally for the TEST line)
├── tools/
│   └── lint_conversations.py    (checks structure + banned strings; Section 9)
└── archive/
    ├── v1-setting-framework.pdf (moved from `setting framework:script.pdf`; rename: no colon)
    ├── v1-SOP.md                (copy of the old SOP)
    └── v1-roleplays/            (the old `roleplays/` folder, moved intact)
```

---

## 5. Phase plan (do in order; commit after each; update PROGRESS.md)

**Phase 0: Prep (≤10 min)**
- `git tag v1-old-script`; create branch `script-v2`.
- Create `PROGRESS.md` with every phase as a checkbox and a "Needs Ștefan" section.
- Move old material to `archive/` (Section 4). Rename the PDF without the colon.
- *Done when:* the tree matches Section 4 (empty files OK), nothing was deleted, tag exists.

**Phase 1: The script (≤15 min)**
- Write Appendix A **verbatim** to `SETTING-SCRIPT.md`.
- Write `drills/READ-ALOUD.md`: only the SAY lines, in spine order, no commentary, one screen.
- *Done when:* `diff` of the SAY lines between the two files shows no differences.

**Phase 2: Rewrite the SOP (shorter)**
Rewrite `SETTING-SOP.md`. Keep what's good, cut what contradicts Section 3.
- **Keep (reword to fit):** the "checklist not a script" idea; follow-don't-read (but see D1); go in when it's loaded (inside CURRENT only); classify answers (vague / loaded / specific); bridge, don't jump; confirm back out loud (now = the Recap); honest beats booked; never promise results; know your role; silence is a tool; curiosity over persuasion; the whole Safety section; the Attitude table; the Disqualification table; the Curveball library; handoff notes; Part 2 (offer adaptation worksheet); Part 3 modules A and B (Trading, Ecom).
- **Replace:** the spine (Section 3 D1-D5), the "router" and "default orders by stage" tables (order is now fixed; keep them only as a table of *what to emphasise inside CURRENT* per stage/driver), the Bridge bank (rewrite for the new nodes: INTENT→EARLY IMPACT→CURRENT→RECAP→TIMEFRAME→WGW→WHY NOW→FIN→PITCH), the "How much is it?" curveball (use the script's taster), the Qualification step (ladder; no price on the call).
- **Delete the stage × bucket order tables** that say e.g. "S3 Stuck: PE → G → TL → WGW → CS".
- Modules C (Airbnb), D (credit repair), E (template): keep but add a banner "Not updated for Script v2. Needs the same treatment as A and B." (Don't rewrite them. No budget for it.)
- Add a short section "Why this method" with 8 bullets from Appendix B.
- *Done when:* no occurrence of the banned strings in Section 9; SOP is under ~60% of its old length.

**Phase 3: CURRENT SITUATION toolkit** (see Section 6.1 for the exact spec)
- *Done when:* all five files exist and meet the counts in the spec.

**Phase 4: Conversations, Tier 1 (the core library: 16 calls)** (spec in Section 6.2 and 7)
- Write `conversations/_TEMPLATE.md` and `conversations/README.md` (with the matrix) first.
- Then write Tier 1 calls.
- Run `tools/lint_conversations.py` after each batch.

**Phase 5: Conversations, Tier 2 (12 more calls)** (same spec)

**Phase 6: Drills**
- `self-play.md`, `review-your-calls.md`, `call-log-template.md`, `prospect-simulator.md` (Appendix D).

**Phase 7: Root README + QA + PR**
- Root `README.md`: 1-page map: "start here → script → current toolkit → conversations → drills".
- Run lint, fix everything. Do a read-through of 3 random conversations against Section 7.2.
- Move `CLAUDE-CODE-BRIEF.md` to `archive/brief-v2.md` (it documents decisions; it shouldn't sit in the root).
- Open a PR from `script-v2` with a summary and the "Needs Ștefan" list.

**If credits run low:** finish phases in this order of value: 0, 1, 3, 4 (calls 01-08 first), 2, 6, 4 (rest), 5, then always a minimal 7 (root README + PR). Never leave the repo half-migrated: if you can't finish, commit what's done and mark the rest `TODO` in `PROGRESS.md`.

---

## 6. Content specs

### 6.1 CURRENT SITUATION toolkit

**`current-situation/README.md`: the playbook**
Sections: (1) what CURRENT is for, in plain words (pain + feeling + cost; tactical vs deep); (2) the layers L1-L5 with an example of each from a single imagined prospect; (3) **twelve techniques**, each with *when to use, why it works, 3 example lines, a failure mode*: echo a word; "what do you mean?"; scene ("walk me through a normal week"); the motivation question; guess out loud; two-option question; "what's the hardest part of that?"; the reason line when they resist; tactical-to-emotional analogy (the overweight/diabetes example: pain drives change, O14 13:20-13:41); silence; softened "as you want to be" (E20); stop-and-move-on when they stall; (4) the **exit test**; (5) the **Don'ts** from the script; (6) a one-page "if you only remember five things" box.

**`current-situation/question-bank.md`: ≥150 lines, each tagged**
Format per line: `- "line" · L2 · use: they said a vivid word · [echo]`.
Groups (≥12 lines each):
1. Openers right after INTENT/EARLY IMPACT, by what the prospect said (money / time / freedom / escape / "stuck" / tactical / curious).
2. Echo-and-ask templates.
3. "What do you mean?" family (and natural variants).
4. Scene-asking ("walk me through…", "what does a Sunday look like…").
5. Emotion without therapy-speak ("what's the hardest part of that?" vs "how does that make you feel", which is banned).
6. Impact on people (partner, kids, friends, parents).
7. Cost of staying here (light; never full-strength closer pressure).
8. Time and money facts, asked casually *inside* the story, not as a list.
9. Moves for one-liners / closed answers (guess out loud, two-option).
10. Moves for talkers (warm interruption, "back up", find the one real sentence).
11. Reason lines for resistance ("why are you asking?").
12. Pivot lines when stuck, and lines to leave CURRENT (into RECAP).
13. Ecom-specific versions (store, product, ads, suppliers, cash flow).
14. Trading-specific versions (prop firms, blown accounts, psychology, strategy, screen time, funded accounts).
**Quality rule:** every line must sound like something a person would say out loud, ≤ 2 short sentences, one question. No stacking. No "I'd like to understand…" corporate phrasing. Mark the 20 best "starter lines" with ⭐.

**`current-situation/by-first-answer.md`**
A table + mini-ladders. Rows = what the prospect gives first (at least 16): vague money · vague freedom · "get out of my 9-5" · "I'm stuck/plateaued" · "I blew accounts" · only tactical (psychology/strategy) · "just curious" · one word · closed yes/no · talker who dumps everything · loaded drop (divorce/debt) · numbers guy · happy with job · ego/"I know all this" · skeptic · price-first · time-pressed · family provider · student/young. Columns: *what they give · what it tells you · your first move · layer ladder (L1→L4 in 4-6 lines of example dialogue) · pitfall*.

**`current-situation/mistakes-and-fixes.md`**
From Appendix C. Each: the bad line · why it fails (one sentence) · the fix · source tag. Add ≥10 more in the same spirit, clearly marked `(constructed)`.

**`current-situation/scenes.md`**
≥30 short excerpts (6-12 lines), each a different prospect/situation, each ending at the exit test or a deliberate stall. Annotate layers `[L1]…[L4]`. These are the "feel" for CURRENT specifically. Spread across trading (≥18) and ecom (≥12).

### 6.2 The conversation library

**Axis A: what the prospect gives first** (the organising idea). Each Tier 1 call is one of these, from opener to lock:

| # | First-answer type | What it sounds like |
|---|---|---|
| 01 | Vague money | "I just want to make more money." |
| 02 | Vague freedom | "Freedom, I guess. Not being stuck." |
| 03 | Guarded one-word | "Yeah." "Idk." "Money." |
| 04 | Open talker | Tells his life story in the first answer |
| 05 | Loaded drop early | Divorce / debt / a death mentioned in passing |
| 06 | Specific numbers | "I make 2k, I want 10k." No feeling |
| 07 | Tactical only | Talks setups, psychology, prop firms. No personal life |
| 08 | Happy with job | "My job is fine, I just want more." |
| 09 | Already trading, stuck | Blown accounts, self-blame |
| 10 | Curious / low intent | "Just looking, saw an ad." |
| 11 | Ego / "I know all this" | Dismissive |
| 12 | Skeptic | "Is this a scam?" |
| 13 | Price-first | "How much is it?" (twice) |
| 14 | Time-pressed | "I've got two minutes" |
| 15 | No money (DQ at the ladder) | Honest and broke |
| 16 | Not sure / partial money + partner mention | Has some savings, hesitates |

**Tier 2 (12):** ecom: vague money; burned by a course; sales but no profit; student with no capital (DQ). Then: over-eager "sign me up"; hostile/venting about past sellers; emotionally heavy (setter stops the framework); underage (DQ); unsupported region (DQ); wants a guarantee (DQ-ish); forgot they booked; call that ends early (they hang up).

**Outcome mix across all 28:** ~55% booked, ~25% DQ (money, age, region, guarantee), ~20% ends without booking (tire-kicker, hang-up, "I'll think about it" before the pitch). Do **not** make every call a win.

**Each call file** follows `_TEMPLATE.md`:
```
# NN · Title
**First answer type:** … · **Offer:** trading|ecom · **Outcome:** booked | DQ | no-book
**Lead:** invented name, age, job, country · **Surface story:** … · **Hidden truth:** … · **Savings truth:** …
**Resistance style:** … · **Depth target:** L? · **Approx. duration:** ~N min
**Setter focus:** one skill to notice

## The call
(full dialogue, opener → lock/DQ/exit. Annotations in blockquotes:)
> [FRAME] / [INTENT] / [EI] / [CURRENT L1…L5] / [RECAP] / [TIMEFRAME] / [WGW] / [WHY NOW] / [FIN] / [PITCH] / [LOCK] / [SHOW UP]
> [WHY THIS LINE] one-sentence reason for a setter choice that isn't obvious
> [RECOVERY] when the setter slips and fixes it (include in ≥ 1 of every 3 calls)

## Depth scorecard
Layers reached · exit test met? · echoes used (count) · questions that assumed something (count) · minutes in CURRENT

## What to notice (3 bullets)
## If they had said X instead (2-3 mini-branches, 3-6 lines each)
## Worse version (one exchange: a typical bad setter line, why it fails, and the fix)
```
Length target: **1,400-2,200 words per call**, 60-120 dialogue lines. CURRENT should be the longest section (≈ 35-45% of the dialogue) in every booked call.

---

## 7. Writing rules for all generated dialogue

### 7.1 The setter's script is fixed
Use **exactly** the SAY lines from Appendix A for FRAME, INTENT, RECAP, TIMEFRAME, PITCH, SCHEDULE & LOCK, SHOW UP (placeholders filled). FIN may vary only in *which* ladder questions are skipped because the prospect already answered (e.g., he volunteered his income). The TEST line (TIMEFRAME) appears in A form in about a third of calls, B or C in the rest. Mark which with `[TEST A|B|C]` so the tally is possible.

### 7.2 Realism rules for prospects (this matters most)
1. Average prospect turn is **3-12 words** in the first half of the call. One 30-50 word burst is allowed only *after* a good echo/"what do you mean?".
2. **They don't hand over breadcrumbs.** The emotional truth appears only after ≥ 2 well-aimed layer questions, and sometimes never (some calls stall at L2, and the setter accepts it and moves on).
3. Prospects **deflect** with humour, jargon, "it's fine", or by asking a question back. They answer a different question. They contradict themselves. They go quiet ("…" is allowed). They ask "why are you asking?" in ≥ 4 calls.
4. Speech, not essays. Natural fillers ("I guess", "to be honest", "like") in moderation, not every line.
5. At least 6 calls have a prospect who is **wrong about something** (hours, numbers, who to blame). The setter doesn't argue.
6. Money answers are fuzzy ("couple grand?", "depends") before they become numbers.
7. Vary country, age (18-55), job, tone. No stereotypes. Use $ mostly; a few £ / AED / €.
8. Names and companies are invented. Use `$COMPANY`/`$CLOSER` placeholders in the setter's lines.

### 7.3 Voice: the setter (Ștefan)
- Warm, calm, curious, a bit flat. Not hype, not therapist. Eastern-European directness softened by a "man" now and then (max ~4 "man/bro" per call).
- **One question per turn. ≤ 2 short sentences.** Echo-then-ask. Never stack ("what do you do and how long and do you like it").
- Use the prospect's own words back to them.
- No "I hear you" on repeat, no "that's a great question", no "how does that make you feel", no "I'd love to understand", no "journey", no "unlock", no "transform".
- The setter never agrees to a claim he can't back ("we get results for everyone").
- Use "Sounds good?" / "Cool?" as the small-yes ending after frame and pitch (that's Ștefan's own habit).

### 7.4 Don't contradict the method (see lint, Section 9)
In every call: no Show the Gap, no "are you committed?", no price/range/"there's an investment" from the setter (the taster is allowed *only* if the prospect asks "how much is it?"), no "why aren't you / why haven't you" in CURRENT, no "what would that look like" (desire) before the pain has landed, no digging after the exit test is met, no "why are you still stuck".

---

## 8. Open decisions (defaults used if Ștefan doesn't answer)

| # | Decision | Default |
|---|---|---|
| Q1 | Fixed order vs flexible | **Fixed** (D1) |
| Q2 | Live call length | 8-12 min, CURRENT 4-6 |
| Q3 | "How much is it?" reply | Atefur's taster (script OPTION 1) |
| Q4 | Savings question wording | Generic ("saved") plus both numbers in the handoff |
| Q5 | Pitch mentions cost? | No (Atefur's version) |
| Q6 | Show-up reschedule line | Keep Ștefan's wording; add the safer alt in the script FLAG |
| Q7 | Lead source in examples | 70% "booked from an ad", 30% "downloaded a guide" |
| Q8 | `$MIN_SAVINGS` | Placeholder; DQ examples use "a couple hundred" (clearly too low) and "~$1,500, hesitant" (ambiguous) |
| Q9 | Ecom frame/intent wording | Mirror the trading lines with "ecom" |
| Q10 | Other offers (Airbnb, credit repair) | Out of scope; banner only |

Record every default you used in `PROGRESS.md`.

---

## 9. QA: the lint (build `tools/lint_conversations.py`)

The linter reads `conversations/*.md` (not `_TEMPLATE.md`) and fails if:

1. **Required tags missing or out of order** in booked calls: `[FRAME] → [INTENT] → [CURRENT L…] → [RECAP] → [TIMEFRAME] → [WGW] → [WHY NOW] → [FIN] → [PITCH] → [LOCK] → [SHOW UP]` (`[EI]` optional; DQ and no-book calls stop where they stop, but must show `[FRAME]` and `[INTENT]`).
2. **Banned strings** appear in the setter's lines (case-insensitive): `show the gap`, `are you actually committed`, `committed to making`, `there's an investment`, `anywhere from \$`, `\$\d+ to \$\d+` (price ranges), `how does that make you feel`, `why aren't you`, `why haven't you` (allowed only in a `[TEST A]` line), `I hear you` (allowed once), `journey`, `unlock`, `transform`.
3. **Stacked questions:** a setter turn with ≥ 2 question marks.
4. **Turn length:** a setter turn > 40 words (except `[FRAME]` and `[PITCH]`).
5. **Prospect too cooperative:** the first 12 prospect turns average > 14 words.
6. **Missing sections:** Depth scorecard, What to notice, If they had said X instead, Worse version.
7. **PII patterns:** any email address, `fathom.video`, or any name listed in `tools/pii_blocklist.txt` (gitignored; Ștefan adds real surnames locally; create the file with a comment line only).

Also run the linter over `current-situation/scenes.md` for rules 2-4. Fix, don't suppress. Add one line to the root README: how to run it.

---

## 10. Working method (to spend credits well)

- Do Phases 0-3 yourself (small, high-leverage, must be consistent).
- For Phases 4-5, spawn **parallel subagents**, 3-4 at a time, 3-4 calls each. Give each subagent: Appendix A, Section 7 (all), the `_TEMPLATE.md`, the lead sketches for its calls, and this instruction: "read two finished calls first so the voice matches." Run the linter after each batch. Don't let two subagents write the same file.
- Write **Call 01, 07 and 09 yourself first**: they set the quality bar (and 07/09 teach the hardest CURRENT moves). Show them to subagents as the reference.
- Before finishing: read **three random calls end-to-end**. Ask: does the prospect sound like a person? Does the setter sound like Ștefan? Is CURRENT the longest part? Would the *worse version* really be what a nervous setter would say? Fix if not.
- Keep every file skimmable: short paragraphs, tables where they help, no walls of text.

---

## 11. Suggestions for Ștefan (include in the PR description)

1. **These are for feel, not a substitute for reps.** Atefur's advice: get on a live offer; roleplays plateau (O14 46:23-48:35). Use the library, then talk to real people.
2. **Use `drills/prospect-simulator.md`** with Claude for realistic, harder prospects than a friendly peer. Run the same persona 3 times and watch your layers count go up.
3. **Record your calls** and use the pause drill (O14 45:17): after each prospect sentence, "how could I have gotten deeper?"
4. **Tally the TEST line** (A/B/C) in the call log for 20 calls, then keep the winner.
5. **Ask Atefur to review** the new script and 3 of the conversations. Free expert feedback.
6. **Consider making the repo private**: it's derived from mentorship material, and it quotes coaching sessions.

---

# APPENDIX A: THE SCRIPT (write verbatim to `SETTING-SCRIPT.md`)

Copy everything between the two markers into `SETTING-SCRIPT.md` exactly, without the markers. Make the first line a top-level `#` heading (here it is `##` only so this brief's outline stays clean). Heading numbers inside the script (1-12) are the script's own and unrelated to this brief's sections.

<!-- BEGIN SETTING-SCRIPT.md -->

## Setting Script v2: Trading / Ecom (B2C)

**Status:** first live version. Fixed spine, freestyle inside CURRENT.
**Updated:** 2026-10-15
**Rule:** don't edit for ~2 weeks / ~20 calls. Atefur: the structure should be "like iron", same every call (O11 55:01). Log what breaks, edit after.

**Legend**
- **SAY** = your wording, chosen. Read these aloud daily (5-10x, O11 58:05).
- **OPTION** = alternatives. Pick one per call, never stack.
- **TEST** = running as an A/B test. Tally results.
- **CUE** = not a line. A reminder for freestyle.
- **FLAG** = open decision. Default is written next to it.
- Source tags: `O10` / `O11` / `O14` = Atefur roleplay transcripts, with timestamps.

---

## The spine (fixed order)

**FRAME → INTENT → EARLY IMPACT → CURRENT (freestyle) → RECAP → TIMEFRAME → WHAT GOT IN THE WAY → WHY NOW → FINANCIAL QUALIFICATION → PITCH → SCHEDULE & LOCK → SHOW UP**

Only CURRENT is freestyle. If the prospect already answered a node, confirm it and skip it. Never reorder.

**Removed from v1:** Show the Gap, Want to Change / Commitment, the "would you be ready to invest" + price range line, a separate Past Experience node, a separate Goal question, the job-question chain as the default.

**Call length:** FLAG. Default is 8-12 minutes live (CURRENT alone is 4-6). Atefur's pace is current/pain 5-7 min (O11 26:41).

---

## 1. FRAME

**SAY**
> Heeey… $NAME?
> This is Ștefan from $COMPANY, it looks like you've booked from an ad, about possible help with trading, is that right?

**YES →**
> Cool, just to give you some insight into our application process, it's two steps.
> The first step is this call. My goal here is to get an understanding of where you're at, some of your goals and see if we can actually help you. If by the end of the call I feel like that's the case, I'll walk you through the next stage, cool?

**Rules:** say your name and company before the frame (O14 26:53). Same frame every call (O11 32:50). The frame changes only by lead source, not by mood.

**Variants by lead source** (FLAG: confirm which are live)
- Downloaded a guide: "it looks like you've downloaded our guide about possible help with trading, is that right?"
- Forgot / doesn't remember: "No worries man, it was an ad about possible help with trading. Is that something you're still looking into?"

**If they ask how long, or sound rushed**
> I've got about five minutes.

**If it's a bad time** (adapted from the course video)
> No stress. Is it the worst time to talk for five minutes, or can you do a quick one? / When's better, today or tomorrow?

---

## 2. INTENT

**SAY**
> Okay, so tell me man, like… out of all the ways to make money, what had you interested in trading in the first place?

**Listen for a tangible answer:** MONEY // TIME // FREEDOM.
This one question gives you their goal. Don't ask the goal a second time (O11 56:11).

**Ecom variant** (FLAG: confirm wording)
> Okay, so tell me man, like… out of all the ways to make money, what had you interested in ecom in the first place?

---

## 3. EARLY IMPACT (only if it fits the conversation)

**OPTION**
> Well, what makes you feel like you don't have $TANGIBLE right now?
> Well, what makes you feel like you're not as $TANGIBLE as you want to be right now?

Why the second one works: it uses their word, and "as you want to be" is softer than "why aren't you" (O11 44:46-45:30).

---

## 4. CURRENT (freestyle: this is where the call is won)

**Goal:** leave with their pain in their own words, plus **one feeling** and **one cost**, ideally one real scene from their week. You're not collecting job facts. You're finding the emotion under the tactical problem.

**Tactical vs deep** (O14 2:53): "I keep blowing prop accounts" is tactical. Under it is the real thing: freedom, time, family, feeling behind. Get to the real thing.

### Topics (CUE, not questions)
work and what they do · time and hours · people who depend on them · money · what's missing · what it looks like in a normal day or week · how long it's been like this

Take one or two and follow them to the feeling. You don't need all of them.

### Layers (CUE)
- **L1** surface answer ("stuck", "need money")
- **L2** what that means to them ("what do you mean?")
- **L3** a scene ("walk me through a normal week")
- **L4** the personal impact (how it hits them, their relationships, their sense of self)
- **L5** what it's costing them / what they'd lose by staying here

Atefur's example: more money → quit job → job takes all my time → no time with family or friends → the impact (O10 1:12:37). Aim for L3-L4 on most calls. Stop earlier if they genuinely don't open up. Surface answers are normal (O11 1:07:16).

### Moves by what they say (CUE)

| They say | You do |
|---|---|
| A vivid or emotional word ("stuck", "cycle", "empty", "behind") | Repeat the word, then "what do you mean?" (O14 1:02, O11 29:07) |
| "I want more money" / vague | "Sure man, most people want more money. What's the real reason behind it for you?" (shape from O14 44:49, wording mine) |
| Only tactical ("psychology", "my strategy") | **SAY:** "I know you want to get better at trading, but what's the real motivation for even trying it?" (O14 44:35) |
| "I like my job" / nothing wrong | Don't dig the job. Ask the motivation question above (O14 43:55) |
| One-liner or closed answer | Guess out loud, or give two options (mine) |
| Big or status goal | "What makes you feel like you're not as $X as you want to be right now?" (O11 43:00, 45:30) |
| They get emotional | Slow down. Don't fill the silence. "What's the hardest part of that?" (mine) |
| "Why are you asking me this?" | **SAY:** "I'm not asking just for the sake of asking. The better I understand you, the better I can help, like a personal trainer would." (O14 12:08) |
| They stall at the surface after 2 tries | Stop digging. Move on and let the rest of the call fill it in (mine) |

### Don'ts
- Don't ask "why aren't you / why haven't you" here (defensive answer, O11 44:46-45:30).
- Don't assume the job is the problem (O14 43:55).
- Don't jump to "what would that look like" (desire) before the pain has landed (O14 29:58).
- Don't re-dig current once you have the pain (O11 24:35).
- Don't ask why they're *still* stuck. That's the limiting belief, and it's the closer's job (O11 52:10).
- Don't ask "can you give me an example" (logical answer). Ask "what do you mean?" (O11 47:44-48:40).
- Don't copy Atefur's lines word for word. Keep the principle, say it your way (O11 39:15-40:13).

### Exit test
You can say their pain in their words, with one feeling and one cost. Example: "stuck in the cycle, drained, no time with my daughter." Then move on.

---

## 5. RECAP

**SAY**
> Okay so basically your main goal is to $REAL GOAL, correct?

**Rule:** recap the **deep** goal (time, freedom, family), not the tactical one ("get my psychology in place"). If you only have the tactical one, you're not out of CURRENT yet (O14 41:49-42:53).

---

## 6. TIMEFRAME

**SAY**
> Got it. Give me the bigger picture, like how long have you been looking into trading?
> Okay and within the last $TIMEFRAME… what have you tried in trading?

If they already trade, say "how long have you been trading?"

**TEST** (running as A/B; tally which pulls "I need guidance" more often than self-blame)
> A. Why haven't you been able to see success within trading over $TIMEFRAME?
> B. What do you feel has been missing to get you there?
> C. What do you think would make the difference?

Reason for the test: A can produce self-blame ("I guess I'm just not good enough, man", O11 6:18), not "I need help".

---

## 7. WHAT GOT IN THE WAY (one pass)

**OPTION**
> What actually got in the way, in terms of actually starting?
> What do you feel stopped you in terms of actually taking the real step?

**If they already started / tried** (use this, not the above)
> What happened with that?

**Rules:** one pass. Write down what they say. Don't challenge it and don't ask why they're still stuck.

---

## 8. WHY NOW

**OPTION**
> What's different now compared to six months ago?
> What made you start looking now?

Atefur called "why now" a good question (O14 31:51). Skip it if they already told you.

---

## 9. FINANCIAL QUALIFICATION (new: no price, no range)

Atefur (O14 34:09-37:07, 38:09-39:13): financial qualification is finding out how much money they have, not telling them the price. Price is the closer's job.

**SAY**
> What would you want to be making every month from trading, to make it worth your time?
> How much are you making right now? (just so I can understand how far away you are from that)
> How much of that are you able to save?
> I'm sure you know it takes money to make money. How much would you say you have saved up for your trading account?

**Ecom:** "...How much would you say you have saved up for investing into ecom?"

**FLAG:** this asks about trading / ecom capital, not about the mentorship. Atefur's own wording was generic: "You've got to invest money to make money. How much money do you have actually saved?" (O14 38:28). Default: use the generic wording and note both numbers for the closer.

**Rules**
- **Don't mention the investment or any number.**
- If they have the money → PITCH.
- If they don't → DQ.
- Threshold: `$MIN_SAVINGS` (FLAG: ask the company).
- Never help anyone borrow or risk money they can't spare (credit cards, loans, retirement, emergency funds).

**If they ask "how much is it?"** (FLAG: pick one)
> OPTION 1 (Atefur, O14 38:44): "It's a four-figure investment, depending on the program, but we can't even know if we can help you yet. That's what the call with $CLOSER is for."
> OPTION 2 (v1 line): "I wasn't trained on pricing, we have different programs and quoting the wrong one would be a disservice."

**DQ line** (O14 35:00: DQ and follow up in a month or two)
> Got it man. Right now it wouldn't make sense to book you. I'll send you some resources and we pick this up in a month or two.

**Honesty:** never say it's free, never deny there's a cost if asked directly.

---

## 10. PITCH

**SAY**
> Alright $NAME… based on everything you've told me, I genuinely believe we can help you.
> The next step would be connecting you with one of our senior advisors, $CLOSER, he can get more in-depth, and build a roadmap on how we can get you to $GOAL. Sounds good?

*(wait for the answer before moving on)*

**FLAG:** Atefur's version doesn't mention cost at all. A middle option is "…and walk you through what it looks like and what it costs", with no number. Default is Atefur's.

---

## 11. SCHEDULE & LOCK

**SAY**
> What time zone are you in?
> Great, let me check the calendar and see what slots are still available, what would work best tomorrow or $2DAYS FROM NOW?
> What works best, in the morning, afternoon or evening?
> $TIME #1 or $TIME #2, which works best?
> Okay $TIME & DATE.
> What's your best email for the call details?
> Is this number good for a reminder text?
> I've sent the invitation, I'll give you a moment to check your email right now, make sure you got it and accepted it.

**FLAG:** the "tomorrow or $2DAYS" line is clunky. Option: "Does tomorrow or $DAY work better?"

---

## 12. SHOW UP

**SAY**
> Okay, you're locked in. Just to double check, are you 100% sure $TIME & DATE works and there is nothing coming up that could clash?
> Great, if for some reason life gets in the way, just message me and we can reschedule.
> For the call, find a quiet space, be at your computer, $CLOSER will break it all down on the call aaand you two figure out if it's a fit. Cool?
> Amazing brother, stay blessed and take care!

**FLAG:** "just message me and we can reschedule" hands them an out right after you closed the exit. Option: "If something does come up, message me as early as you can."

---

## Handoff note (after every call)

- Name · offer · lead source
- Goal in their words + the number
- The pain: scene, feeling, cost (their words)
- Timeframe · what they tried · what got in the way · why now
- Income · monthly savings · amount saved (and what it's saved for)
- Flags: tight money, partner, ghost risk, skepticism
- Time zone + booked slot

---

## Curveballs (short)

| They say | You do |
|---|---|
| "Is this a scam?" | "Fair worry. This call is just to see where you're at, nothing more. $CLOSER answers the detailed stuff." |
| "Just looking / curious" | "Just to make sure, is this something you're still looking into, or not really?" (course video) |
| "I need to ask my wife / partner" | Note it for the closer. Don't push. (B2C: the closer handles it) |
| "Send me the info" | "Of course. So I send the right thing, what's the main thing you're trying to fix?" |
| Emotionally heavy (loss, crisis) | Stop the framework. One human sentence. Wait. |

---

## Source notes
- `O10` = Oct 10 roleplay, `O11` = Oct 11, `O14` = Oct 14 (file header says Oct 13).
- Fathom speaker labels are unreliable, especially around coach/prospect switches. Cite by content, not label.


<!-- END SETTING-SCRIPT.md -->

---

# APPENDIX B: EVIDENCE DIGEST (paraphrased; no raw transcripts in the repo)

Tags: `O10` / `O11` / `O14` = three roleplay sessions with Atefur (a closer with ~20 months' experience and limited setting experience; he said so, O10 15:28). `V3` = a course video on setting. Speaker labels in the original transcripts are unreliable, so these are cited by content.

**O10 (Oct 10)**
- E1 · 24:24-25:10. Setter sounded like a robot reading a script. Fix: tonality, more upbeat, real conversation.
- E2 · 1:06:44-1:09:45. Asking "what stopped you from taking action" (accountability) was the wrong place to dig. It's the closer's job. "You're selling the meeting."
- E3 · 1:10:02-1:12:37. Listen to the pain, repeat the same words, keep building. Layers example: more money → quit job → job is time-consuming → no time with family/friends → the negative impact.
- E4 · 1:13:47-1:16:46. His self-roleplay (warehouse, six days a week, "cycle", "hamster wheel"). When the prospect said "it can get a bit personal", he answered with a reason: "can we help if we don't know your story?"
- E5 · 1:16:55-1:17:21. The setter's goal is to establish the problem. How long / what done / why now is only context.
- E6 · 1:17:54. The bridge to the pitch: recap the pain, name the closer, frame the call as a roadmap that's valuable either way.
- E7 · 1:18:46. "Tell them what they want to hear / hype B2C": **not adopted** (see C5).
- E8 · 22:02-22:20. In the first run the prospect said he could do "a couple hundred" and called the $4-8k range expensive. Ștefan didn't DQ. (This is why the DQ line now exists.)
- E9 · 42:37 / 48:21. The prospect in a roleplay was "the most OP prospect in the world"; real calls are harder: smokescreens, hidden objections.

**O11 (Oct 11)**
- E10 · 3:58. Keep it simple: intent → current problem → go deeper in the layers.
- E11 · 6:38-8:56. Link their real-life emotion to trading ("what are you trying to get out of trading?"). Ask what's more painful, human to human.
- E12 · 11:05-12:46. Depth is "good enough" when there's a named problem with an emotion (e.g., no freedom of choice → unfulfilled).
- E13 · 14:01-16:48. People decide on emotion. Focus on their life, not on trading tactics.
- E14 · 21:52-22:04. Pattern recognition: better too deep (some sales resistance) than always shallow.
- E15 · 24:15-26:00. Don't redo current once you have the pain. Current = pain, desire = goals.
- E16 · 26:24-27:32. Flow: intro → current/pain (the most important part, 5-7 min) → surface overview of the past (how long, what done, what held you back) → quick future pace (optional) → financial qualification → pitch.
- E17 · 28:17-29:10. Money ladder example: goal → current income → what they keep → what they have saved.
- E18 · 32:50-37:13. Same frame every call. Formula: who I am, the goal of the call, "by the end I'll walk you to the next stage."
- E19 · 39:15-40:13. Don't copy his lines. Keep the principle, use your own words.
- E20 · 43:00-45:30. "Magic question": what makes you feel like you're not as $X as you want to be right now? Uses their words; softer than "why aren't you $X".
- E21 · 46:39-48:40. "What do you mean?" beats "can you give me an example?" (the second gets a logical answer).
- E22 · 49:32-52:47. The problem and the limiting belief behind it are separate. Asking why they're still stuck is the closer's territory.
- E23 · 54:46-56:50, 58:40. Trim the script: remove Past Experience and the separate Goal question. Structure "like iron", less is better.
- E24 · 58:05-58:37, 1:07:16, 1:08:39. Read the script aloud 5-10x/day. Leads give surface answers: go deeper. Today's depth was extra to build the muscle. Play prospect against yourself (or an AI).
- E25 · 1:09:42. Setting is about efficiency. Don't ask big open "tell me about yourself" questions.

**O14 (Oct 14; file header says Oct 13)**
- E26 · 2:53, 12:08, 13:20-13:41. Tactical vs deep. Reason line: "I'm not asking just for the sake of asking; the better I understand you, the better I can help, like a personal trainer." Analogy: pain drives change.
- E27 · 29:46-30:12. Setter jumped to "what would that look like" (desire) before pain had landed. Coach: stick to your process.
- E28 · 31:51. "Why now?" is a good question.
- E29 · 34:09-37:07, 38:09-39:13, 35:00. Financial qualification = how much money they have. Don't mention the investment or price; if they don't have it, DQ and follow up in a month or two. Ladder: monthly goal → current income ("so I can understand how far away") → savings per month → "you've got to invest money to make money, how much do you have saved?" If they push on price: a taster ("a four-figure investment, but we can't even know if we help you yet"). Summary: understanding of where at / where want to be / a bit of what stops them / do you have the money / book / show up.
- E30 · 41:49-44:35. Recapped the tactical goal (psychology) instead of the deep one. Job-question chain assumes the job is the problem. Better: "I know you want to get better at trading, but what's the real motivation for even trying it?"
- E31 · 45:08-45:37. Keep digging. Review calls: after each prospect sentence, "how could I have gotten deeper?"
- E32 · 46:23-48:35. Get on an offer; live reps beat more roleplays.
- E33 · 25:46. Stefan's own diagnosis: CURRENT is the bottleneck (you must freestyle, listen, dig).

**V3: course video on setting (a different coach)**
- Calls should be ~8-10 minutes. Who/why in the opener. "Is it the worst time to talk for two minutes?" for busy leads. Tire-kicker probe: "is this something you're still looking into, or not really?" Pick off three boxes: why change, why now, why this vehicle. Trust move at the pitch: "we've only been talking five minutes." Double-check the slot.
- **Not adopted:** the direct price range with "is that doable or out of the question?" (conflicts with E29), and the decision-maker check (B2C: the closer handles it).

---

# APPENDIX C: MISTAKES CATALOG (real lines, for `mistakes-and-fixes.md`)

| Bad line (Ștefan, real) | Why it fails | Fix | Source |
|---|---|---|---|
| "Do you trade full time or do you work?" (right after the prospect gave emotion) | Fact question that breaks the thread; assumes | Go to the emotion: "what are you trying to get out of trading?" | O11 8:09 |
| "Most people work 9-5. Why is that a problem?" | Challenges; gets defended | "What do you mean by the routine?" / "What's the hardest part of it?" | O11 20:30 |
| "If you're ambitious, why do you still stay in the job?" | Limiting-belief question, closer's job | Stay on the problem: "what's the hardest part of being there?" | O11 50:59 |
| "Can you give me an example of that?" | Logical answer, not emotional | "What do you mean?" | O11 46:39 |
| "Everyone wants to make more money…" (copied) | Sounds copied | Own words: "Sure, what's the real reason behind it?" | O11 39:03 |
| "What would that freedom look like day to day?" (too early) | Desire before pain landed | Stay on the pain one more layer | O14 29:46 |
| "How do you feel about the job? How long? What makes you want out?" | Assumes the job is the problem | "What's the real motivation for even trying it?" | O14 43:29-44:35 |
| "So your main goal is to get the psychology part in place, right?" | Recaps the tactical goal | Recap the deep goal: time / freedom / family | O14 41:49 |
| "…there's an investment, $3k to $7k. Doable?" | Setter quoting price (Atefur: closer's job) | The ladder; no number | O14 33:35 |
| "What stopped you from taking the real step?" asked of someone already trading | Doesn't fit; sounds scripted | "What happened with that?" | O14 31:12 |
| "What do you feel stopped you from trading with your own money?" (twice) | Accountability, closer's job | One pass, fact only, or skip | O10 20:41, 53:43 |
| "You must like the job then" (generic reaction to "it's fine") | Hands them a hook | "If you could change one thing about it, what?" | constructed |

---

# APPENDIX D: THE PROSPECT-SIMULATOR PROMPT (spec for `drills/prospect-simulator.md`)

Write a ready-to-paste system prompt that makes an AI play a prospect for a setter. It must contain:
1. Role: "You are a lead who booked a call from an ad about {trading|ecom}. You are not helpful by default."
2. A **persona card** the user fills in: name, age, job, country, first-answer type (from the 16), surface story, hidden truth, savings truth, resistance style, what makes them open up, what makes them shut down.
3. Rules: answer in 3-12 words at first; reveal the hidden truth only after the setter has used an echo or "what do you mean?" at least twice; get defensive on "why aren't you / why haven't you"; ask "why are you asking?" at some point; never volunteer money numbers before the ladder; if asked the price, ask "how much?" again once; end the call if the setter is boring or rude.
4. Don't coach during the call. After the setter types `END`, give a debrief: layers reached (L1-L5), echoes used, assumptions made, stacked questions, minutes in CURRENT, whether the exit test was met, and the three best and three worst lines, each with a rewrite.
5. 10 ready persona cards (copied from the first 10 first-answer types).

---

# APPENDIX E: THE LAUNCH PROMPT (for Ștefan to paste into Claude Code)

> Read `CLAUDE-CODE-BRIEF.md` in the repo root, end to end. Then follow its Phase plan from Phase 0. Work on branch `script-v2`. Don't ask me questions. Use the defaults in Section 8 and record them in `PROGRESS.md`. Commit after each phase. Use parallel subagents for Phases 4-5 as described. Stop at Phase 7 with a PR.
