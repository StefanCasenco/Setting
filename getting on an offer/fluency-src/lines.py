"""Phone Fluency: the hand-written lead-in patterns.

Each pattern turns a bare question into one with context ("lubricant") before it, Atefur's way:
a bit of context before the question lowers sales resistance, because the prospect hears WHY
you're asking. Scott's limit: one beat of context, then the question, clean. Over-talking takes
the edge off it.

Fields: stage, bare (what most setters say), say (the fluent version, with {niche} fields),
tool (the kind of lead-in), use (when it fits), skip (when NOT to use it), modes (None = all niches).
Niche fields come from drills-src/niches.py.
"""

B = ("capital", "program")          # bizopp
CAP = ("capital",)
PROG = ("program",)
NONBIZ = ("health", "credit", "personal")
HEALTH = ("health",)
CREDIT = ("credit",)
PERS = ("personal",)

L = []
def add(stage, bare, say, tool, use, skip, modes=None):
    L.append(dict(stage=stage, bare=bare, say=say, tool=tool, use=use, skip=skip, modes=modes))

# ---------------------------------------------------------------- OPENING
add("OPEN", "Hi, is this Marcus?",
    "Hey [name], how you doing? It's Stefan from {owner}'s team. I've got you down for 3 o'clock about {topic}, so perfect timing. What got you booking in?",
    "Context", "They booked a slot (a triage call).", "They called you, or it's an old lead.")
add("OPEN", "Are you free for a quick 5–10 minute chat?",
    "Hey, it's Stefan from {owner}'s team. You literally just put your info in about {topic}. What made you fill it out?",
    "Context", "Speed to lead: called within minutes of the form.", "Older leads. They won't remember 'just'.")
add("OPEN", "What made you download the guide?",
    "Hey, it's Stefan from {owner}'s team. You grabbed our free guide on {topic} a few days ago. Just so I don't waste your time, is this something you're actually looking to work on, or more just having a look around right now?",
    "Reason", "Lead magnet or free guide leads. They're colder.", "They applied or booked. They've already shown intent.")
add("OPEN", "Are you still interested?",
    "This is a bit of a random one. You reached out back in [month] about {topic} and never got a proper call. Where are you at with it now?",
    "Normalise", "Old leads, 1–12 months.", "Anyone who opted in this week.")
add("OPEN", "Did you like the webinar?",
    "You were on {owner}'s webinar last night. What stood out to you?",
    "Their words", "Webinar attendees. They just watched something, so they have an answer ready.", "They registered but didn't attend.")
add("OPEN", "You missed the webinar.",
    "You signed up for {owner}'s webinar on Tuesday, and I didn't see you on. (laugh) What happened?",
    "Normalise", "Webinar no-shows. It's light, with no guilt.", "If they sound stressed. Go gentler.")
add("OPEN", "Why did you call me back?",
    "Hey, yeah, it's Stefan from {owner}'s team. I tried you earlier about {topic}. Thanks for calling back. What made you fill out the form?",
    "Context", "They're calling back a missed call. Re-establish who you are fast.", "")
add("OPEN", "Is now a good time?",
    "Sounds like you're out. It's Stefan, about {topic}. Did I catch you at an okay time, or are you driving?",
    "Real life", "Background noise, or they sound busy. Check after they've said who they are.", "As your first line. It invites a quick 'no'.")
add("OPEN", "Let me explain how this works.",
    "My goal here is just to see where you're at with {topic}, where you want to be, and if we can actually help. If we can, I'll walk you through the next step.",
    "Reason", "After their first answer, if they seem unsure why you're calling.", "As a speech before you've asked anything. Scott: get them talking first.")

# ---------------------------------------------------------------- INTENT
add("INTENT", "Why {topic}?",
    "Everyone gets into {topic} for a different reason, so I always like to ask: what had you looking at it in the first place?",
    "Normalise", "Most intent questions. It shows there's no wrong answer.", "They've already told you why in the opener.")
add("INTENT", "Why do you want to make money online?",
    "Out of all the ways to make money online, what had you looking at {topic}?",
    "Contrast", "Bizopp offers. It makes them defend their choice.", "Health or personal offers.", B)
add("INTENT", "What made you interested?",
    "You mentioned you've been watching {owner}'s stuff. What was it that got you to actually reach out?",
    "Their words", "They mention the owner or their content.", "They haven't mentioned the owner.")
add("INTENT", "Why do you want help?",
    "What's going on right now that's made you want to {getinto}?",
    "Clean", "They're already warm and talking. No lead-in needed.", "Cold or one-word leads. Give them a beat of context first.")
add("INTENT", "What do you want?",
    "And what are you hoping {topic} will give you that you don't have right now?",
    "Contrast", "After a vague first answer (Atefur).", "As the very first question. It's too deep too soon.")

# ---------------------------------------------------------------- SOFT QUAL
add("SOFT QUAL", "What do you do for work?",
    "And {topic} is usually a side thing for most people at the start, so what's paying the bills right now?",
    "Normalise", "Bizopp leads. It explains why you're asking about work.", "They've already told you their job.", B)
add("SOFT QUAL", "What's your job?",
    "Just so I get a picture of your week, what are you doing for work at the moment?",
    "Reason", "Any niche. A soft way in.", "They're mid-story. Follow the story instead.")
add("SOFT QUAL", "Where do you work?",
    "You mentioned {work}. How long have you been doing that?",
    "Their words", "They hinted at it already.", "They haven't mentioned work yet.")
add("SOFT QUAL", "Have you done this before?",
    "Is {topic} something you're completely new to, or have you already had a go at it?",
    "Clean", "Early, to gauge how sophisticated they are (Scott's soft qual).", "They've told you what they've tried.")
add("SOFT QUAL", "Is this full time or part time?",
    "And would you be looking to do this alongside {work}, or is it something you'd want to go all in on eventually?",
    "Their words", "Bizopp. It shows how serious they are.", "Health, credit or personal offers.", B)
add("SOFT QUAL", "Are you a student?",
    "Just to get a better understanding of your situation, where are you based, and what are you doing right now, work or study?",
    "Reason", "Every lead, early. It catches students and the unemployed.", "")

# ---------------------------------------------------------------- CURRENT SITUATION
add("CURRENT", "How do you feel about your job?",
    "{work} for {time}. How's that actually been for you?",
    "Their words", "They've given the job and how long.", "It's a brand-new job. Ask what drew them to it instead.")
add("CURRENT", "Do you like your job?",
    "A lot of people I speak to say the job's fine on paper, but something's off. How do you honestly feel about it?",
    "Normalise", "They said 'it's fine' or sound guarded.", "They're already venting. Just let them.")
add("CURRENT", "What's your schedule like?",
    "What does a normal week of {work} actually look like for you?",
    "Real life", "To get a story instead of a yes or no.", "They've just described their week.")
add("CURRENT", "How does that affect you?",
    "And with {pain}, how's that actually been affecting you, outside of work?",
    "Their words", "Right after they state a fact. Turn it into an impact.", "They've already told you the impact.")
add("CURRENT", "Why is that bad?",
    "You mentioned {pain}. What's the hardest part of that for you?",
    "Their words", "They named a problem without any feeling.", "They're emotional already. Just repeat their line back.")
add("CURRENT", "How does that feel?",
    "And what's that been like for you, day to day?",
    "Clean", "Any time you get a fact (Scott: situation, then impact).", "You've asked 'how does that feel' twice already. Change the angle.")
add("CURRENT", "What do you mean?",
    "When you say '{word}', what do you mean by that?",
    "Echo", "They used a vague or loaded word.", "You've already asked them to explain it once (George's loop).")
add("CURRENT", "Can you explain?",
    "'{word}.' (pause) What do you mean?",
    "Echo", "To slow down on a heavy word (Atefur).", "With one-word answerers who need easier questions.")
add("CURRENT", "Why did you say that word?",
    "What makes you use the word '{word}'?",
    "Echo", "A strong, unusual word (Atefur's 'cycle').", "Ordinary words. It sounds odd.")
add("CURRENT", "How long has it been like that?",
    "And how long have you been feeling like that?",
    "Timeframe", "After an impact. It tells you which path the call takes (course).", "")
add("CURRENT", "Is it new?",
    "Has it always been like that, or is it more recent?",
    "Timeframe", "To find out whether it's a recent event or a long-running pain.", "They've told you when it started.")
add("CURRENT", "Tell me more.",
    "Walk me through what happened with {tried}.",
    "Their words", "They mention a past attempt.", "They haven't tried anything.")
add("CURRENT", "Why is it a problem?",
    "Most people in your spot are doing alright, honestly. So why is it still something you want to solve?",
    "Contrast", "Vague 'I'm fine' prospects (Atefur's contrast challenge).", "People in visible pain. It sounds dismissive.")
add("CURRENT", "Is it boring?",
    "Honestly, {topic} is repetitive too. So knowing that, why do you actually want to change?",
    "Contrast", "They keep saying 'boring' (Scott's reframe).", "They've given a real reason already.", B)
add("CURRENT", "Why do you want more money?",
    "What's {work} bringing in for you right now, roughly? … And how much would you need for it to be worth the change?",
    "Clean", "'More money' on repeat (Scott). Pull them down to the numbers.", "Health or personal offers.", B)
add("CURRENT", "Is anything else going on?",
    "No judgment at all. Most people I speak to have a story behind it. What happened, if you don't mind me asking?",
    "Normalise", "Sensitive topics: credit, weight, a divorce.", "Light topics. It makes them heavier.")
add("CURRENT", "Can you be honest?",
    "You can be honest, by the way. There's no judgment here. What's the part that really gets to you?",
    "Reason", "They're giving surface answers (Atefur).", "They're already being open.")
add("CURRENT", "Why are you telling me this?",
    "I'm not asking for the sake of it. The better I understand you, the better {closer} can help, like a personal trainer would. So what's really going on with {topic}?",
    "Reason", "They push back on the questions.", "Nobody's pushing back. It sounds defensive.")

# ---------------------------------------------------------------- TIMEFRAME / TRIED
add("TIMEFRAME", "How long have you been looking into it?",
    "And {topic} is one of those things people sit on for ages before they actually do anything. How long's it been on your radar?",
    "Normalise", "Before the timeframe question. It takes the shame out of a long time.", "They've already said how long.")
add("TIMEFRAME", "How long?",
    "Give me the bigger picture. How long have you been looking at {topic}?",
    "Context", "Moving from current situation to timeframe (your script).", "")
add("TIMEFRAME", "What have you tried?",
    "And in that time, what have you actually tried so far?",
    "Clean", "Always, after the timeframe (course).", "")
add("TIMEFRAME", "Did it work?",
    "You mentioned {tried}. How did that go?",
    "Their words", "They named a past attempt.", "")
add("TIMEFRAME", "Why didn't it work?",
    "And looking back on {tried}, what do you think went wrong?",
    "Their words", "They tried something and it failed. This shows whether they've been burnt.", "They're still upset about it. Let them vent first.")
add("TIMEFRAME", "Why haven't you done anything?",
    "{time} is a while to be thinking about it, and no judgment, most people do exactly the same. What do you think has stopped you from taking the leap so far?",
    "Normalise", "They've wanted it a while and done nothing (course).", "Recent leads. Ask what happened recently instead.")

# ---------------------------------------------------------------- ROADBLOCK
add("ROADBLOCK", "What's stopping you?",
    "If you had to put a finger on the one thing holding you back from {aim}, what would it be?",
    "Context", "The main roadblock question (course).", "")
add("ROADBLOCK", "Do you need help?",
    "What do you think it'd take for you to actually {aim}?",
    "Clean", "Instead of 'could you do it on your own?' (Scott). They say the bucket themselves.", "")
add("ROADBLOCK", "So you need guidance?",
    "You said {roadblock}. What do you think it'd take to get past that?",
    "Their words", "They named the roadblock. Get them to name the solution too.", "")
add("ROADBLOCK", "Why not do it yourself?",
    "And if it's just a time thing, why not keep going on your own, as opposed to getting help from someone like us? … So what were you hoping we could do for you?",
    "Contrast", "They say time is the problem (Atefur #4).", "They've already said they need help.")
add("ROADBLOCK", "Why do you need us?",
    "There's a lot of free stuff out there for {topic}. What made you reach out, instead of just using that?",
    "Contrast", "They mention YouTube or free content.", "")
add("ROADBLOCK", "Why haven't you done it already?",
    "Why do you think you haven't hit {goal} yet?",
    "Clean", "Direct, for sophisticated prospects already doing it (Miro).", "Beginners. It sounds like blame.")
add("ROADBLOCK", "Would a coach help?",
    "So if you had the right guidance, and someone keeping you accountable, do you think you'd get there?",
    "Assumptive", "Only after they've said the roadblock in their own words (Miro). This is leading on purpose.", "Before they've named it. That's putting the answer in their mouth.")

# ---------------------------------------------------------------- WHY NOW
add("WHY NOW", "Why now?",
    "I get that it's been {time}, life gets in the way… but why now? Why is now a good time where you think, okay, let me figure this out and give it my all?",
    "Timeframe", "They've wanted it a while. It respects the delay before asking.", "They told you a recent trigger. Just ask about the event.")
add("WHY NOW", "What changed?",
    "You've had this on your mind for {time}. What's different now compared to back then?",
    "Timeframe", "Scott's version. It's short and works with vague leads.", "")
add("WHY NOW", "Did something happen?",
    "What's happened recently that's made you actually want to do something about it?",
    "Clean", "A recent want. There's usually an event (course).", "They've been at it for years. Ask what's different now.")
add("WHY NOW", "So that was the trigger?",
    "You mentioned {event}. Was that the moment, or had it been building before that?",
    "Their words", "They mentioned an event in passing.", "")
add("WHY NOW", "When did you decide?",
    "When's 'just now'? Like, how long ago was that? … And what shifted for you in that moment?",
    "Echo", "A vague 'I just decided' (Atefur #5).", "They gave a clear answer.")
add("WHY NOW", "Why is it urgent?",
    "And why is it important for you to sort this out now, rather than in a year?",
    "Contrast", "To get the stakes in their words.", "You've already got a clear deadline.")

# ---------------------------------------------------------------- GOAL
add("GOAL", "How much do you want to make?",
    "Everyone's number's different. Some people just want a few hundred extra for bills, some want to replace their job. What would make {topic} actually worth your time, say a year from now?",
    "Normalise", "Bizopp goal question. It takes the pressure off.", "Health, credit or personal offers.", B)
add("GOAL", "What's your goal?",
    "If everything went the way you want, what would you want {topic} bringing in a month, six to twelve months from now?",
    "Context", "Bizopp, straight after roadblock or why-now (course).", "", B)
add("GOAL", "Goal?",
    "So what's the goal here? What are we looking to make from {topic} every month, a year from now?",
    "Context", "Your script line. It's quick.", "", B)
add("GOAL", "Where do you want to be?",
    "If everything went perfectly, where would you want to be with {topic} six to twelve months from now?",
    "Context", "Health, credit and personal offers.", "Bizopp. Ask for a number instead.", NONBIZ)
add("GOAL", "What would success look like?",
    "Picture six months from now and this has worked. What's different for you, day to day?",
    "Real life", "Non-money goals. It gets a picture, not a number.", "", NONBIZ)
add("GOAL", "Why that number?",
    "{goal}. What would that actually change for you?",
    "Their words", "Right after they name the goal (course: the number is the goal, the meaning is the motivation).", "")
add("GOAL", "Why do you want it?",
    "Nobody really wants the number itself, it's what it gives them. What would {goal} give you?",
    "Normalise", "When they give the number and stop.", "They've already explained the meaning.")
add("GOAL", "Is it important?",
    "And why is {goal} important to you right now, specifically?",
    "Clean", "After the meaning, to tie in the timing (course).", "")
add("GOAL", "What's your dream?",
    "And what would {meaning} actually mean for you?",
    "Their words", "They gave the meaning. Go one layer deeper.", "You're two layers in already. Dig straight down, then move on.")
add("GOAL", "Is that the end goal?",
    "And is {goal} the end goal, or more like the first milestone?",
    "Clean", "Bizopp. It finds bigger ambition.", "Fragile prospects. Don't push big goals.", B)

# ---------------------------------------------------------------- URGENCY
add("URGENCY", "How serious are you?",
    "On a scale of 1 to 10, how important is it for you to {aim}?",
    "Clean", "Every call (Scott step 6).", "")
add("URGENCY", "How much of a priority is this?",
    "Given {roadblock} is what's been holding you back, how much of a priority is fixing it for you right now?",
    "Their words", "After the roadblock. It ties the urgency to their words (Miro).", "")
add("URGENCY", "Why that number?",
    "Seven's a strong number. What makes it a seven for you?",
    "Clean", "Any score of 7 or more. They sell themselves (course).", "")
add("URGENCY", "What would make it a 10?",
    "And what's stopping it from being a nine or ten?",
    "Clean", "Finds the hidden objection or fear to flag for the closer.", "")
add("URGENCY", "Why so low?",
    "How come only a five? … Is this something you're actually ready to change now, or something you want to keep kicking down the road?",
    "Contrast", "Scores of 6 or below. Ask why, then a binary challenge (course).", "")
add("URGENCY", "What if nothing changes?",
    "Just playing devil's advocate here: what happens if nothing changes over the next six months?",
    "Future pace", "To get the cost of doing nothing, in their words (course).", "")
add("URGENCY", "Are you okay with that?",
    "Say a year from now you're still {stuck}. How would that sit with you?",
    "Future pace", "They shrug off the urgency (Scott).", "Emotional prospects. It can feel cruel.")
add("URGENCY", "Will you settle?",
    "Is that what you're willing to settle for?",
    "Contrast", "They say 'it's fine, I'll manage' (Scott). Ask it once.", "More than once. That turns it into a boxing match.")
add("URGENCY", "Why are you on the call then?",
    "Totally fair. How come you're on the call today, then?",
    "Clean", "They said yes, they'll settle (Scott). Then let them go if it's still yes.", "")

# ---------------------------------------------------------------- MONEY (setup)
add("MONEY", "Let's talk about money.",
    "Okay, let me ask a couple of questions on the money side, just so I know where you're at with {topic}. Cool?",
    "Reason", "Moving into money, after urgency.", "Before you've found the pain (habit #4).")
add("MONEY", "I need to ask about your finances.",
    "So I can make sure {closer}'s call is actually useful for you, a couple of quick money questions.",
    "Reason", "An alternative money setup that's about their benefit.", "")

# capital
add("MONEY", "How much do you make?",
    "So your goal's {goal}. I just want to understand the gap between where you're at and that. How far would you say you are right now, with your current monthly income?",
    "Reason", "Capital offers. Atefur #4, word for word.", "", CAP)
add("MONEY", "What's your income?",
    "And what's {work} bringing in for you a month right now, roughly?",
    "Their words", "Capital offers. Quick and plain.", "", CAP)
add("MONEY", "How much do you save?",
    "And you know how expenses are nowadays, the way the economy's going… how much would you say you're able to put aside each month from your current income?",
    "Real life", "Every offer. A reason before the question (Atefur's 'because').", "")
add("MONEY", "Is that every month?",
    "And is that on a tight month, or is that your usual every month?",
    "Clean", "Straight after the monthly number (your script).", "")
add("MONEY", "How much is saved?",
    "And outside the monthly stuff, in total, how much have you been able to put away so far?",
    "Context", "After monthly savings.", "")
add("MONEY", "How much capital do you have?",
    "I'm sure you know in {topic} it takes money to make money, right? So how much would you say you've set aside in terms of capital?",
    "Reason", "Capital offers only. Your script line.", "Program offers. There's no capital to talk about.", CAP)
add("MONEY", "Why don't you want to tell me?",
    "Yeah man, I'm sure you know in {topic} it takes money to make money. If you go to a personal trainer, the first thing he asks is what you're working with. Just a rough figure.",
    "Reason", "Capital offers, when they push back (script and Atefur).", "", CAP)
add("MONEY", "Where is the money?",
    "Some people have it sitting in the bank ready to go, some have it in stocks or a pension they don't want to touch. Where's yours mostly?",
    "Normalise", "After the total. It finds money that's off-limits.", "")
add("MONEY", "Why do you need the total?",
    "Cash flow's one thing, but the baseline's what {closer} builds the plan around. Some people come in with fifty K, some with two. Totally different plan.",
    "Reason", "They ask why the total matters (Atefur #5).", "")
add("MONEY", "Do you have a credit card?",
    "Some people prefer to spread things out rather than pay all at once. Have you got credit available, or would you rather keep it to savings?",
    "Normalise", "Bizopp, said confidently. No pause, no apology.", "Credit repair, or anyone you know is struggling.", B)

# program
add("MONEY", "How much do you earn?",
    "A big part of what we do is help people grow their income. If {topic} worked, what would you want to be making a month? … And where are you at right now?",
    "Reason", "Program offers. Money through income, with no capital line.", "Capital offers. Use the capital line there.", PROG)
add("MONEY", "Can you afford it?",
    "And if {closer} finds the right fit for you, is investing in yourself something you'd be in a position to do right now, or is money genuinely tight?",
    "Contrast", "Program, health and personal offers. Binary on purpose. No price.", "Before you know the pain.", PROG + HEALTH + PERS)
add("MONEY", "Why are you asking about money?",
    "Just so {closer} can put a plan together that's realistic for where you're at. There's no point building a plan around money you don't have.",
    "Reason", "Program offers, when they push back.", "", PROG + HEALTH + PERS)
add("MONEY", "Are you a student with no money?",
    "Just so I don't waste your time, if you're looking at our coaching, it's a mid four-figure investment. Is that something that'd be viable for you right now, or is it completely out of the question?",
    "Reason", "Students, unemployed or low income, early (Scott).", "People with a good job. It's unnecessary.", B)

# health / personal / credit
add("MONEY", "How much do you spend?",
    "What are you spending on {spend} right now?",
    "Real life", "Health, personal and credit offers. Start with what they already spend.", "", NONBIZ)
add("MONEY", "What's your income?",
    "And just so I've got the full picture, what's coming in for you each month, roughly?",
    "Reason", "Health, personal and credit offers.", "", NONBIZ)
add("MONEY", "Do you have money left?",
    "And after rent and bills, what's left at the end of a usual month?",
    "Real life", "Credit repair. Help is usually monthly.", "", CREDIT)
add("MONEY", "Can you pay monthly?",
    "And if there was proper help with this, would something monthly from that be doable for you?",
    "Clean", "Credit repair. Never promise results.", "", CREDIT)
add("MONEY", "Will you use your savings?",
    "That's the {goal} money, so I'm guessing you want that to stay the {goal} money.",
    "Their words", "They mention money with a purpose. Protect it.", "")

# ---------------------------------------------------------------- DECISION / PITCH / BOOK / LOCK
add("BOOK", "Do you need to ask your wife?",
    "Is a decision like this something you'd make on your own, or would you talk it through with someone?",
    "Clean", "Before the pitch, every call.", "")
add("BOOK", "Bring your wife.",
    "Since it'd be both of your money, it'd be worth having them on the call with {closer} too, so they hear it straight and can ask their own questions.",
    "Reason", "Joint decisions. It raises show and close rates.", "")
add("BOOK", "I'll connect you with our closer.",
    "So from what you said, it's {pain}, you want {goal} so you can have {meaning}, and what you said you need is help with {roadblock}. Next step would be a Zoom with {closer}, one of {owner}'s head coaches. He'll map out a plan for exactly that. How does that sound?",
    "Their words", "The pitch: a recap in their words, then the bridge and the value (Scott).", "")
add("BOOK", "Want to book a call?",
    "Would it be helpful if we set up a Zoom with {closer} to run through how we could help you get past {roadblock}, so you can {aim}?",
    "Assumptive", "A softer pitch, for warm, nervous leads (Miro).", "")
add("BOOK", "Our coach can help you.",
    "Based on our conversation, it sounds like you need to get past {roadblock} so you can {aim}, which is exactly what we've helped a lot of people with. Would you be down to hop on a Zoom with {closer} and figure out a game plan?",
    "Their words", "A pitch variant (Miro), good when you've got a clear problem and goal.", "")
add("BOOK", "When are you free?",
    "Let me check {closer}'s calendar. Does tomorrow afternoon work, or would Thursday be better?",
    "Assumptive", "Always two options. No open question (course).", "")
add("BOOK", "Is morning okay?",
    "What works best for you, morning, afternoon or evening?",
    "Clean", "Narrowing down after the day.", "")
add("BOOK", "What's your email?",
    "What's your best email for the call details? … And is this number good for a reminder text?",
    "Clean", "Lock-in (your script).", "")
add("BOOK", "Accept the invite.",
    "I've just sent the invitation. Can you check your email real quick and accept it for me, so it's in your calendar?",
    "Reason", "Every booking. The top predictor of showing up.", "")
add("BOOK", "Make sure you show up.",
    "Okay, you're locked in. Just to double check, are you 100% sure that works, and nothing's coming up that could clash?",
    "Clean", "Commitment to show up (your script).", "")
add("BOOK", "Don't miss it.",
    "And if for some reason life gets in the way, just message me and we'll move it. For the call, find a quiet space and be at a computer if you can. {closer} will break it all down.",
    "Real life", "Closing the booking (your script).", "")
add("BOOK", "Bring your stuff.",
    "If you can, have your {tried} stuff open on the call. {closer} will want to look at it.",
    "Their words", "They mentioned a past attempt. It gets them invested in the call.", "")

# ---------------------------------------------------------------- MORE PATTERNS (round 2)
add("OPEN", "Did you do the quiz?",
    "You did {owner}'s quiz about {topic} earlier. What made you take it?",
    "Context", "Quiz leads. It reminds them with specifics.", "If it was weeks ago. Remind them when it was.")
add("OPEN", "Are you doing the challenge?",
    "I saw you're on day 3 of {owner}'s challenge on {topic}. How's it going so far?",
    "Their words", "Challenge leads. Open on their progress.", "They dropped out on day 1. Ask what happened instead.")
add("OPEN", "Do you want to upgrade?",
    "You've been in {owner}'s community a few weeks now. How are you finding it so far?",
    "Context", "Paying members (the upsell call). Onboard first.", "Never open with the upgrade.")
add("OPEN", "You missed your call.",
    "Hey, it's Stefan from {owner}'s team. You were booked in with {closer} yesterday. No stress at all, just making sure you're good. What happened?",
    "Normalise", "No-show rebooks. No guilt.", "")
add("INTENT", "What got you interested?",
    "What got you looking at {topic} this week, specifically?",
    "Timeframe", "Fresh leads. It gets the trigger early.", "Old leads. 'This week' doesn't fit.")
add("INTENT", "What does that mean?",
    "And when you say '{vague}', what does that look like for you?",
    "Echo", "A vague intent answer (Scott: change the angle).", "They've already given a concrete goal.")
add("INTENT", "What made you think it could work?",
    "What's the one thing about {topic} that made you think, okay, this could actually be it?",
    "Their words", "Excited leads. It gets their belief in their words.", "Sceptical leads. They'll say 'nothing'.")
add("SOFT QUAL", "Full time?",
    "And {work}, is that full-time for you at the moment?",
    "Their words", "After they name the job.", "")
add("CURRENT", "What's the worst part?",
    "You mentioned {work}. What's the part of it that gets to you the most?",
    "Their words", "They named the job but not the pain.", "They're already telling you.")
add("CURRENT", "How does it affect your family?",
    "And how's {pain} been at home, with the people around you?",
    "Their words", "Impact beyond work. Family is often the North Star.", "They live alone and don't mention anyone.")
add("CURRENT", "What do others think?",
    "If someone close to you described how {pain} has been for you, what would they say?",
    "Real life", "Guarded prospects. They'll say through someone else what they won't say directly.", "Open prospects. It's not needed.")
add("CURRENT", "How bad is it?",
    "When {pain} is at its worst, what does that actually look like?",
    "Their words", "To get a specific moment instead of a general complaint.", "")
add("CURRENT", "Is it every day?",
    "You said '{word}'. Is that how it feels most days, or just some days?",
    "Echo", "They used a strong word once. It checks how big it is.", "As your default. It's a binary.")
add("CURRENT", "What does it cost you?",
    "What does {pain} actually cost you, week to week?",
    "Their words", "To turn a fact into a cost.", "Credit and health calls, where it might feel like blame.")
add("CURRENT", "So your goal is…?",
    "Okay, so basically your main goal is to {aim}, correct?",
    "Their words", "A recap, only after they've said it themselves (your script).", "If you're adding words they didn't say. Then it's you labelling it.")
add("TIMEFRAME", "Anything else?",
    "And before {tried}, had you tried anything else?",
    "Their words", "To get the full history and any burn.", "")
add("TIMEFRAME", "How much did you put in?",
    "And with {tried}, how much time or money did you put into it?",
    "Their words", "Finds whether they've been burnt, and how much.", "")
add("TIMEFRAME", "What did you learn?",
    "What did {tried} teach you about what you actually need?",
    "Their words", "Sophisticated prospects. They name the gap themselves.", "Beginners who tried nothing.")
add("ROADBLOCK", "What was missing?",
    "So with {tried} not getting you there, what do you think was missing?",
    "Their words", "After a failed attempt. It leads to the roadblock bucket.", "")
add("ROADBLOCK", "Is it knowledge or discipline?",
    "With {topic}, is it more that you don't know what to do, or you know what to do but don't do it consistently?",
    "Contrast", "Only for problem-unaware prospects (course: then binary is okay).", "By default. Ask 'what do you think it'd take?' first.")
add("ROADBLOCK", "What would you do first?",
    "And if {roadblock} was sorted tomorrow, what's the first thing you'd do?",
    "Their words", "It makes the solution feel real.", "")
add("ROADBLOCK", "What's hardest?",
    "What's the part of {topic} that feels hardest to figure out on your own?",
    "Clean", "Open roadblock question, on any call.", "")
add("WHY NOW", "How did that feel?",
    "And {event}, how did that leave you feeling?",
    "Their words", "They named the trigger but not how it felt.", "")
add("WHY NOW", "Would you be here otherwise?",
    "If {event} hadn't happened, do you think you'd even be on this call?",
    "Contrast", "To make them see how big the trigger was.", "Grief or crisis triggers. Never with those.")
add("GOAL", "By when?",
    "And by when would you want {goal}?",
    "Timeframe", "After the goal. It gets a deadline in their words.", "")
add("GOAL", "What would you do?",
    "When you picture {meaning}, what's the first thing you'd do?",
    "Real life", "Makes the goal vivid. It's great before urgency.", "")
add("GOAL", "Who else?",
    "And who else would {goal} change things for?",
    "Their words", "Finds the family or partner reason.", "")
add("GOAL", "What would it prove?",
    "And what would hitting {goal} prove to you?",
    "Their words", "Identity-driven prospects (ego, 'still researching', the reunion).", "")
add("URGENCY", "Are you ready?",
    "On a scale of 1 to 10, how ready are you to actually do something about {pain}?",
    "Their words", "A temp check using their pain instead of the goal.", "")
add("URGENCY", "What if it's still there?",
    "And if {roadblock} is still there a year from now, how does that look for you?",
    "Future pace", "To get the cost of their roadblock, in their words.", "")
add("URGENCY", "This year or someday?",
    "Is {aim} something you want to sort out this year, or more of a someday thing?",
    "Contrast", "Low urgency (course: binary to challenge).", "They've already scored an 8 or more.")
add("MONEY", "What have you set aside?",
    "And with {aim} in mind, what have you got set aside for it right now?",
    "Their words", "Bizopp, after monthly savings. It ties the money to their goal.", "", B)
add("BOOK", "Let's book you in.",
    "Based on what you said about {pain}, I think a call with {closer} makes sense. He'll look at {roadblock} specifically. Tomorrow at 6, or Thursday?",
    "Assumptive", "A short pitch for warm leads, with two times.", "Sceptical leads. Use the full recap.")
add("BOOK", "Anything else?",
    "And so {closer} can prep properly, is there anything else about {topic} you'd want him to know?",
    "Reason", "End of the booking. Often brings up a hidden objection.", "")
add("BOOK", "Reminder text.",
    "(text) Hey [name], Stefan from {owner}'s team. You're locked in for [day] at [time] with {closer}. Link's in your email. Any issues, just text me here.",
    "Real life", "Right after booking. It cuts no-shows.", "")
add("BOOK", "Are you still coming?",
    "(call, 1 hour before) Hey [name], it's Stefan from {owner}'s team. Just making sure you're still good for [time] with {closer} today?",
    "Real life", "The reminder call on the day.", "")
