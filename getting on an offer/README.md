# GETTING ON AN OFFER

Everyone's said the same thing: stop roleplaying and get on an offer. This folder is for that.

| File | What it is |
|---|---|
| `01-your-calls-review.md` | Your setter roleplays (Kevin #1–8, Atefur #5) reviewed with timestamps: what you do well, the 10 habits to fix, drills, and a scorecard for every call from now on |
| `02-loom-scripts.md` | Scott's Loom rules from the Syndicate call, your draft rewritten, three scripts (general, trading, program offers), a 5-slide deck, the 3-takes rule, and a volume target |
| `03-interviews-and-vetting-offers.md` | Interview questions with strong answers, the live roleplay test, questions to ask *them* so you don't land on a dead offer, red flags, where to find offers, and a DM template |
| `04-first-two-weeks-on-an-offer.md` | Days 1–2 prep, a daily routine, US time zones from Moldova, the numbers to track and what they mean, a closer note template, and reminders that cut no-shows |
| `drills.html` | **The drill app.** 306 cards in 3 checks: **Check 1** core (65), **Check 2** one or more cards from every one of the 150 roleplays (153), **Check 3** new scenarios that aren't in any call yet: voicemails, gatekeepers, ready buyers, debt, crisis moments, interviews, life on an offer, and the habits from your own calls (88). Practice mode, plus a **20-card check** that scores you. Phone link: https://claude.ai/artifact/5rhnkhdNt3ys769LBP5FhJ |
| `drills-src/` | The cards as editable JSON files, plus `build.py`, which rebuilds `drills.html` |
| `applications-tracker.csv` | Open in Google Sheets or Excel. One row per application. |

**This week's plan**
1. Every morning: 15 minutes of `drills.html` (the Habits and Money categories first).
2. One roleplay a day with Kevin, scored with the card in `01`.
3. Record your Loom (Script A from `02`), three takes max. Send 5 applications a day.
4. Before every interview, reread `03`.

## Running the drills on your computer

**Easiest (no install):**
1. Go to https://github.com/StefanCasenco/Setting/blob/main/getting%20on%20an%20offer/drills.html
2. Click the **Download raw file** button (the down-arrow icon, top right of the file view).
3. Double-click the downloaded `drills.html`. It opens in your browser and works offline.

**Whole repo:** on https://github.com/StefanCasenco/Setting click **Code → Download ZIP**, unzip it, then open `getting on an offer/drills.html`.

**With git:**
```bash
git clone https://github.com/StefanCasenco/Setting.git
```
```bash
open "Setting/getting on an offer/drills.html"
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
Progress is saved in your browser (a reset button is in the app). Each browser and device keeps its own progress.

## How to use it

- **Every morning, 15 minutes:** practice mode on one check. Say every answer **out loud**.
- **Before going live, and every Sunday:** run a **20-card check** on Mix all. 85% or more means you're ready for that set. Below 65% means back to practice.
- Start with **Check 3 → You** and **Check 1 → Habits**. Those are your own patterns from the Kevin and Atefur calls.
