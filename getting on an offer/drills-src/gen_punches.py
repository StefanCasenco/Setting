"""Generates deck3c-niche-punches.json: the 15 punches every setter takes, played in all 14 niches.

Each card keeps the niche's own prospect, wording and the right money logic for that offer type.
Run by build.py automatically.
"""
import json
import pathlib
from niches import NICHES, BIZOPP

here = pathlib.Path(__file__).resolve().parent


def money_reason(n):
    m = n["mode"]
    if m == "capital":
        return (f"Fair question. I'm sure you know in {n['topic']} it takes money to make money. "
                f"So I want to know what's realistic before I put you in front of {n['closer']}. Just a rough figure, what are you working with?")
    if m == "program":
        return (f"Fair question. It's so {n['closer']} can put a plan together that's actually realistic for where you're at. "
                f"There's no point building a plan around money you don't have. Rough figure is fine.")
    if m == "credit":
        return (f"Fair question. Proper help with credit is usually monthly, so I want to make sure it's realistic, "
                f"and that it doesn't come out of money you need for the {n['goal'].replace('approved for a ', '')}.")
    return (f"Fair question. It's so {n['closer']} can suggest something that fits your budget. "
            f"I'd rather know now than book you into something that doesn't make sense.")


def price_answer(n):
    return (f"Honestly, it depends on what you need, and I don't know that yet. That's exactly what {n['closer']}'s call is for. "
            f"If it's clearly not a fit, I'll tell you in five minutes.")


def vague_answer(n):
    m = n["mode"]
    if m in BIZOPP:
        return [f"Sure. What's {n['work']} bringing in for you right now, roughly?",
                "And how much would you need for this to actually be worth it? … What would that change for you?"]
    if m == "health":
        return ["What does that look like for you? Like, picture it's worked. What's different?",
                "And has someone said something, or is it more how you feel in the mirror?"]
    if m == "credit":
        return ["Better for what, specifically? What's the thing you want to be able to do?",
                "And has something happened recently that's made it matter?"]
    return ["When was the last time you really felt that? Like, a specific moment.",
            "What would be different for you if it changed?"]


def build():
    out = []
    for n in NICHES:
        L, P = n["label"], n["persona"]
        ctx = lambda s: f"{L} · {P}. {s}"
        out += [
            ["Niche punches", "WHY NOW", ctx("You asked what made them reach out now."),
             "Honestly? I just saw the ad.",
             [f"Fair. And you said you've been dealing with {n['pain']} for {n['time']}. So what's different now compared to back then?",
              "When you saw it, what was it that actually clicked?"],
             "Okay, cool. So what's your goal?",
             "Don't accept it, and don't fish for a trigger. Pin the timeframe, then ask what's different now (Scott, Atefur #5).", "new"],
            ["Niche punches", "MONEY", ctx("Money section, after urgency."),
             "Why do you need to know how much I make?",
             [money_reason(n)],
             "Um, sorry, it's just something we have to ask.",
             "A calm reason, no stutter. Atefur: not 'like a cute girl at the bar'." + (" For a capital offer, 'it takes money to make money' is your line." if n["mode"] == "capital" else " There's no capital here, so don't use the 'takes money to make money' line."), "new"],
            ["Niche punches", "OPEN", ctx("First minute."),
             "Before anything, how much is it?",
             [price_answer(n)],
             "It's about five thousand.",
             "Never quote a price. If they ask three times, name it: 'I can tell this is really bugging you.'", "new"],
            ["Niche punches", "BOOK", ctx("You just offered two times for the call."),
             "Let me think about it and get back to you.",
             [f"Totally fair. What's the part you want to think about? … The call with {n['closer']} is where you get the full picture, so you can think with real information. Tomorrow at 6, or Thursday?"],
             "Okay, no problem, call me when you're ready.",
             "'Think about it' at the booking is usually one specific worry. Find it, then book.", "new"],
            ["Niche punches", "OPEN", ctx("Early in the call."),
             "Can you just send me some info?",
             [f"For sure. Honestly though, info without knowing where you're at is just a brochure. Give me five minutes and I'll know if it's even worth sending. If it's not for you, I'll tell you."],
             "Sure, what's your email? (call ends)",
             "Agree, give a reason, box the time, offer an exit.", "new"],
            ["Niche punches", "BOOK", ctx("At the money section."),
             "I'd have to talk to my partner first.",
             [f"That makes total sense. Then honestly, they should be on the call with {n['closer']} too, so they hear it straight and can ask their own questions. When are you both home?"],
             "Okay, talk to them and let me know.",
             "Get the decision maker on the call. Never accept 'I'll let you know'.", "new"],
            ["Niche punches", "TIMEFRAME", ctx("You asked what they've tried."),
             f"I tried {n['tried']}. It didn't really work.",
             [f"Okay. Walk me through it. What happened with {n['tried']}?", "And what do you think went wrong?"],
             "Yeah, that stuff never works. Ours is different.",
             "Never trash what they tried. Their answer shows the roadblock, and whether they've been burnt.", "new"],
            ["Niche punches", "ROADBLOCK", ctx("Roadblock."),
             "Honestly, I just don't have the time.",
             [f"That's fair. And if it's just a time thing, why not just keep going on your own, instead of getting help from someone like us? … So what were you hoping we could do for you?"],
             "It only takes an hour a day!",
             "Atefur #4: the time move makes them say the real roadblock. Leave time commitments to the closer (Scott).", "new"],
            ["Niche punches", "URGENCY", ctx("Temp check, what's holding it back."),
             "I'm not sure it works for someone like me.",
             ["'Someone like you.' What do you mean by that?", "(after they answer) What makes you say that?"],
             "Of course it works for you! Everyone can do it.",
             "That's a limiting belief. Get it said out loud, and flag it for the closer. Don't argue it away.", "new"],
            ["Niche punches", "OPEN", ctx("First minute."),
             "Is this legit? There's so much fake stuff out there.",
             [f"Honestly, that's a smart question. There's a lot of fake stuff. I'm not selling you anything on this call, I'm just seeing if it makes sense. If it doesn't, I'll tell you. And ask {n['closer']} everything on the next call."],
             f"Totally legit, {n['owner']} has helped thousands of people!",
             "Agree with the worry. Defending makes you sound less legit.", "new"],
            ["Niche punches", "ROADBLOCK", ctx("They push back on needing help."),
             "I could probably figure it out on my own.",
             [f"You might. So what's stopped it from working so far, in the last {n['time']}?", "What do you think it'd take for you to actually get there?"],
             "Most people who try alone fail.",
             "Let them argue with their own timeline, not with you.", "new"],
            ["Niche punches", "OPEN", ctx("Early in the call."),
             "I'm already doing another program.",
             ["Nice, good for you for jumping in. How's it going so far?", "(later) I'm not here to trash anybody's program. What made you look at us as well?"],
             "Oh. Well, ours is better.",
             "Curiosity, not competition. They'll tell you the gap themselves.", "new"],
            ["Niche punches", "CURRENT", ctx("Intent question."),
             f"I just want {n['vague']}.",
             vague_answer(n),
             f"Why do you want {n['vague']}? … But why?",
             "Change the angle. Don't ask the same why again (Scott, Syndicate call).", "new"],
            ["Niche punches", "CURRENT", ctx(f"You asked about {n['work']}."),
             "It's fine, I guess.",
             ["(two seconds of silence)", "…Fine?"],
             "Okay, cool. And how long have you been looking at this?",
             "Silence gets more than another question. Then repeat their word as a question (Atefur).", "new"],
            ["Niche punches", "URGENCY", ctx("Temp check."),
             "Like a five, I guess.",
             ["How come only a five?", f"…Is this something you actually want to change now, or something you'll keep kicking down the road?"],
             "Five's not bad! Let's book you in.",
             "Six or below: ask why, then a binary challenge. Then either disqualify or get a real number.", "new"],
        ]
    return out


if __name__ == "__main__":
    cards = build()
    (here / "deck3c-niche-punches.json").write_text(json.dumps(cards, ensure_ascii=False, indent=0), encoding="utf-8")
    print(len(cards), "cards")
