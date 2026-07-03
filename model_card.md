# 🎧 Model Card: Music Recommender Simulation

1. Model Name

MoodDial 1.0


2. Intended Use

MoodDial is a rule-based song recommender that suggests tracks from a
fixed catalog based on a simple taste profile (favorite genre, favorite
mood, and a target energy level).


It generates a ranked top-k list of songs from the existing catalog —
it does not discover new music outside songs.csv.
It assumes the user can articulate their taste as one genre, one mood,
and a rough energy preference (0.0–1.0). It does not infer preferences
from listening history or behavior.
This is a classroom exploration project, not a production system. It's
meant to demonstrate how a transparent, rule-based scoring approach
works before comparing it to ML-based recommenders later.



3. How the Model Works

Think of it like a judge scoring contestants. Every song in the catalog
gets evaluated against the user's stated taste, one point at a time:


If the song's genre matches what the user said they like, it gets a
solid chunk of points.
If the mood matches too, it gets a smaller bonus.
Then the model checks how close the song's energy level is to what the
user asked for — the closer it is, the more points it earns, but it's
a sliding scale rather than all-or-nothing.


Once every song has a total score, they're sorted from highest to
lowest, and the top few are handed back as recommendations — along with
a plain-English list of why each one scored the way it did (e.g.
"genre match" or "energy similarity"), so it's never a black box.

What changed from the starter logic: the original design only supported
a single genre and single mood per user. It was expanded to accept
either a single value or a list, so someone who likes both "intense
rock" and "chill lofi" can be represented honestly instead of being
forced to average the two into something meaningless.


4. Data


The catalog contains 20 songs across 7 artists, each with genre,
mood, energy, tempo, valence, danceability, and acousticness.
Genres represented: lofi (6), pop (4), rock (2), ambient (2), jazz
(2), synthwave (2), indie pop (2).
Moods represented: chill (6), happy (4), intense (4), relaxed (2),
moody (2), focused (2).
The dataset is intentionally uneven — lofi makes up 30% of the
catalog, while several genres have only 2 songs each.
Notably, two artists (Max Pulse and Neon Echo) each have songs
spanning different moods within the same genre — e.g. Max Pulse's
"Gym Hero" and "Iron Tempo" are pop/intense, while other pop songs are
pop/happy. This is deliberate: it's what makes the genre-vs-mood bias
(see Limitations) visible in testing.
Missing from the dataset: sad/melancholic moods, hip-hop, country,
metal, and any genre with more than one energy/mood combination
represented across many songs (most genres here cluster tightly
around one mood).



5. Strengths


Works well for users with a clear, singular taste — e.g. a "lofi/
chill" profile returns four LoRoom/Paper Lanterns tracks in a row,
all genuinely low-energy and mellow, exactly as expected.
The energy-similarity scoring correctly separates high-energy from
low-energy catalogs: a Deep Intense Rock profile surfaces Storm Runner
and Thunder Circuit (both 0.89+ energy) well ahead of anything calmer.
Because every recommendation comes with reasons, it's easy to sanity
check the results — if something ranks oddly, you can immediately see
which factor is driving it rather than guessing.



6. Limitations and Bias


The "Gym Hero problem": genre + energy can override an actual mood
match. Testing the High-Energy Pop profile (genre: pop, mood: happy,
energy: 0.85) put Gym Hero — a pop/intense song with no mood match
at all — at #3, ahead of Rooftop Lights, a song that actually matches
the "happy" mood. In plain terms: the system found a pop song with
similar energy and treated that as "close enough," even though a
listener who explicitly said they wanted happy music would probably
find Gym Hero's mood jarring next to the songs it's competing with.
This isn't a bug — it's a direct consequence of genre (+2.0) and
energy (up to +2.0) together being able to outweigh mood (+1.0) on
their own.
Energy and mood are scored independently, with no coherence check.
A "pop + moody" profile (a combination that doesn't exist anywhere in
the catalog) still returned confident-looking results — Gym Hero and
Iron Tempo topped the list purely on genre + energy, with zero actual
mood matches in the entire top 5. The system never signals that it
couldn't satisfy the stated mood at all.
The dataset shapes results as much as the scoring does. Lofi makes
up 30% of the catalog (6 of 20 songs) while genres like rock, ambient,
jazz, synthwave, and indie pop have only 2 each. A lofi fan gets a
deep, varied top 5; a rock or jazz fan gets a shallow one by
comparison — not because their taste is unusual, but because there's
simply less catalog to draw from.
Requesting a genre that isn't in the catalog fails silently. The
"Genre Not In Catalog" test (favorite_genre: "hiphop") returned indie
pop and pop songs instead, with no indication to the user that their
stated genre was never actually used in scoring.



7. Evaluation

Five profiles were tested against the 20-song catalog: three core
profiles (High-Energy Pop, Chill Lofi, Deep Intense Rock) and two
adversarial edge cases designed to try to break the scoring logic.

High-Energy Pop (genre: pop, mood: happy, energy: 0.85) → top 2
results (Sunrise City, Golden Hour Drive) matched intuition perfectly —
both are happy, high-energy pop songs. But #3 was Gym Hero, a pop song
with an intense mood and no happy match at all. See "The Gym Hero
problem" below.

Chill Lofi (genre: lofi, mood: chill, energy: 0.35) → all top 4
results were genuine genre+mood matches (Library Rain, Rainy Shelf,
Late Night Pages, Midnight Coding), since lofi/chill is the best-covered
combination in the dataset. This is the cleanest result of all five
profiles — no bias visible here because the catalog has enough depth in
this lane.

Deep Intense Rock (genre: rock, mood: intense, energy: 0.9) →
Storm Runner and Thunder Circuit tied at the top, both genuine rock/
intense matches. Gym Hero and Iron Tempo (pop/intense) placed #3 and
#4 on mood + energy alone — a smaller-scale version of the same pattern
as the High-Energy Pop test.

Comparing Chill Lofi vs. Deep Intense Rock: these two profiles pull
in opposite directions, and the system handles that correctly — Chill
Lofi surfaces the catalog's lowest-energy, most acoustic songs, while
Deep Intense Rock surfaces the highest-energy, least-acoustic ones.
Energy is doing real, correct work separating "wind down" from "turn it
up" music.

The Gym Hero problem: this is the clearest and most important
finding from testing. For a user who says "pop" and "happy," Gym Hero —
a pop song, but with an intense mood — placed #3, ahead of Rooftop
Lights, a song that actually is happy. In plain language: the system
saw "same genre, similar energy" and treated that as a strong enough
signal on its own, even though anyone who explicitly asked for "happy"
music would likely be surprised to get an intense gym-hype track instead
of something more genuinely upbeat-and-warm. This happens because genre
(+2.0) and energy (up to +2.0) combined can outscore an actual mood
match (+1.0) even when the mood is flatly wrong.

Conflicted profile (genre: pop, mood: "moody" — a mood that doesn't
exist among any pop songs in the catalog) — the system never signaled
that it couldn't find a real match. It just returned the highest-energy
pop songs (Gym Hero, Iron Tempo) as if they were good answers, with zero
actual mood matches anywhere in the top 5.

Genre Not In Catalog profile (genre: "hiphop") — no error. The
system silently substituted indie pop and pop songs based on mood and
energy alone, presenting them with the same confidence as if the genre
had actually matched.

Weight-shift experiment: halving the genre weight (2.0 → 1.0) and
doubling the energy weight (2.0 → 4.0) for the High-Energy Pop profile
moved Rooftop Lights (the mood-matched song) up from #5 to #4 — but Gym
Hero still held #3. This shows the bias isn't purely about the genre
weight being too high; energy similarity alone is strong enough to keep
a mood-mismatched song near the top even after the genre weight is cut
in half. Fixing this fully would likely require either lowering the
energy weight too, or adding a mood-mismatch penalty rather than just a
mood-match bonus.

What surprised me most: that halving the genre weight wasn't enough
to dislodge Gym Hero. I expected the mood-matched song to take over the
#3 spot once genre's advantage was cut, but energy alone carried Gym
Hero across the gap. It's a reminder that these three factors don't
operate independently in practice — you have to test combinations of
weight changes, not just one at a time, to actually understand the
system's behavior.

Full terminal output for all five profiles is in README.md under
"Sample Recommendation Output."


8. Future Work


Add weighted scoring for danceability and acousticness, which are
already in the CSV but currently unused.
Add a diversity penalty or cap so the top-k list can't be dominated by
a single artist.
Support "taste ranges" instead of a single target_energy (e.g. a user
who's fine with anything from 0.5–0.9 rather than one exact number).
Improve explanations by including how close an energy match was in
plain language (e.g. "very close energy match" vs. "roughly similar
energy") instead of just the point value.
Explore a hybrid approach — keep the rule-based scoring for
transparency, but blend in a lightweight similarity model (e.g.
cosine similarity over the numeric features) to catch songs that are a
strong overall fit despite missing an exact genre or mood label.
## 9. Personal Reflection  

I learned that recommender systems uses factors as the genre and energy levels of the music you listen to in order to suggest what other songs you might like to listen to. Additionally I found it interesting that some factors take stronger preference in the recommender than others(for example in this recommender genre and energy have a heavier influecne than mood)