# GETTING ON AN OFFER

Everyone's said the same thing: stop roleplaying and get on an offer. This folder is for that.

| File | What it is |
|---|---|
| `01-your-calls-review.md` | Your setter roleplays (Kevin #1–8, Atefur #5) reviewed with timestamps: what you do well, the 10 habits to fix, drills, and a scorecard for every call from now on |
| `02-loom-scripts.md` | Scott's Loom rules from the Syndicate call, your draft rewritten, three scripts (general, trading, program offers), a 5-slide deck, the 3-takes rule, and a volume target |
| `03-interviews-and-vetting-offers.md` | Interview questions with strong answers, the live roleplay test, questions to ask *them* so you don't land on a dead offer, red flags, where to find offers, and a DM template |
| `04-first-two-weeks-on-an-offer.md` | Days 1–2 prep, a daily routine, US time zones from Moldova, the numbers to track and what they mean, a closer note template, and reminders that cut no-shows |
| `drills.html` | **Setter Drills.** 603 cards in 3 checks: **Check 1** core (65), **Check 2** cards from all 150 roleplays (153), **Check 3** new scenarios (385): 175 hand-written situations, plus the 15 punches every setter takes played in all 14 niches. Practice mode, plus a **20-card check** that scores you. Phone: https://claude.ai/artifact/5rhnkhdNt3ys769LBP5FhJ |
| `fluency.html` | **Phone Fluency.** 2,200 examples of turning a bare question into one with context before it (Atefur: context before the question lowers resistance), each with **when to use it** and **when to skip it** (Scott: one beat, then the question). 145 hand-written patterns, from opening to booking, practised across 28 prospects in 14 niches. Filter by niche and stage, plus a 20-card check. Phone: https://claude.ai/artifact/BK6qBu5SyEqoCfnBvfaA5j |
| `drills-src/`, `fluency-src/` | The source data and `build.py` scripts that rebuild each app |
| `applications-tracker.csv` | Open in Google Sheets or Excel. One row per application. |

**This week's plan**
1. Every morning: 15 minutes of `drills.html` (the Habits and Money categories first).
2. One roleplay a day with Kevin, scored with the card in `01`.
3. Record your Loom (Script A from `02`), three takes max. Send 5 applications a day.
4. Before every interview, reread `03`.

## Running both apps on your computer

**Easiest (no install):**
1. Open each file on GitHub:
   - https://github.com/StefanCasenco/Setting/blob/main/getting%20on%20an%20offer/drills.html
   - https://github.com/StefanCasenco/Setting/blob/main/getting%20on%20an%20offer/fluency.html
2. Click **Download raw file** (the down-arrow icon, top right of the file view).
3. Double-click the downloaded file. It opens in your browser and works offline.

**Whole repo:** on https://github.com/StefanCasenco/Setting click **Code → Download ZIP**, unzip it, then open `getting on an offer/drills.html` and `getting on an offer/fluency.html`.

**With git:**
```bash
git clone https://github.com/StefanCasenco/Setting.git
```
```bash
open "Setting/getting on an offer/drills.html"
```
```bash
open "Setting/getting on an offer/fluency.html"
```
(On Windows use `start "" "Setting\getting on an offer\drills.html"`.)

**On your phone:** use the link above. Opening a downloaded HTML file on a phone is awkward.

## Adding your own cards

Each card in `drills-src/*.json` looks like this:
```
["Category", "STAGE", "Context", "What the prospect says", ["Good answer 1", "Good answer 2"], "Not this", "Why", "source"]
```
Add a line to any deck file, then rebuild:
```bash
python3 "getting on an offer/drills-src/build.py"
```
For Phone Fluency, add a pattern to `fluency-src/lines.py` (copy an `add(...)` line), then:
```bash
python3 "getting on an offer/fluency-src/build.py"
```
Progress is saved in your browser (a reset button is in the app). Each browser and device keeps its own progress.

## How to use it

- **Every morning, 15 minutes:** practice mode on one check. Say every answer **out loud**.
- **Before going live, and every Sunday:** run a **20-card check** on Mix all. 85% or more means you're ready for that set. Below 65% means back to practice.
- **Phone Fluency, 10 minutes a day:** pick your offer's niche and one stage (start with MONEY and WHY NOW). Say the fluent version out loud in your own words, then compare.
- Start with **Check 3 → You** and **Check 1 → Habits**. Those are your own patterns from the Kevin and Atefur calls.
