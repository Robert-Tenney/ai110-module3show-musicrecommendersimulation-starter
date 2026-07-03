# 🎵 Music Recommender Simulation

## Project Summary

MoodDial is a rule-based recommender that scores a 20-song catalog against
a user's stated genre, mood, and target energy level. Each song earns
points for matching genre (+2.0), matching mood (+1.0), and how close its
energy is to the user's target (up to +2.0), and every recommendation
comes with a plain-language list of reasons so the scoring is never a
black box. Testing across multiple profiles — including deliberately
adversarial ones — surfaced a real bias in the design: because genre and
energy together outweigh mood, a song like "Gym Hero" (pop, but
*intense*) can outrank a genuinely happy song for a user who explicitly
asked for "pop and happy." That finding is documented in `MODEL_CARD.md`
alongside a weight-shift experiment testing whether rebalancing the
scoring can fix it.
---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.
Some features that each song uses in my system are Genre, Mood and Energy.
Some infromation that my "UserProfile" Stores are the users preferences in things such as genre, mood, energy and temp. 
My Recommender computes a score for each song by seeing wether or not a certain feature is the same as or close to the values stored in UserProfile. This is also how my program chooses which songs to recommend by displaying the highest scoring songs based on these values
---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

Top Recommendations
============================================================
1. Golden Hour Drive — Prism Coast
   Score: 6.9
   Reasons: genre match (+2.0), mood match (+3.0), energy similarity (+1.9)
------------------------------------------------------------
2. Sunrise City — Neon Echo
   Score: 6.86
   Reasons: genre match (+2.0), mood match (+3.0), energy similarity (+1.86)
------------------------------------------------------------
3. Rooftop Lights — Indigo Parade
   Score: 4.98
   Reasons: mood match (+3.0), energy similarity (+1.98)
------------------------------------------------------------
4. Skyline Bloom — Indigo Parade
   Score: 4.98
   Reasons: mood match (+3.0), energy similarity (+1.98)
------------------------------------------------------------
5. Gym Hero — Max Pulse
   Score: 3.64
   Reasons: genre match (+2.0), energy similarity (+1.64)
------------------------------------------------------------

C:\Users\u\ai110-module3show-musicrecommendersimulation-starter>py -m src.main
Loaded songs: 20

=== Profile: High-Energy Pop ===
    {'favorite_genre': 'pop', 'favorite_mood': 'happy', 'target_energy': 0.9}
============================================================
1. Sunrise City — Neon Echo
   Score: 4.84
   Reasons: genre match (+2.0), mood match (+1.0), energy similarity (+1.84)
------------------------------------------------------------
2. Golden Hour Drive — Prism Coast
   Score: 4.8
   Reasons: genre match (+2.0), mood match (+1.0), energy similarity (+1.8)
------------------------------------------------------------
3. Gym Hero — Max Pulse
   Score: 3.94
   Reasons: genre match (+2.0), energy similarity (+1.94)
------------------------------------------------------------
4. Iron Tempo — Max Pulse
   Score: 3.9
   Reasons: genre match (+2.0), energy similarity (+1.9)
------------------------------------------------------------
5. Rooftop Lights — Indigo Parade
   Score: 2.72
   Reasons: mood match (+1.0), energy similarity (+1.72)
------------------------------------------------------------

=== Profile: Chill Lofi ===
    {'favorite_genre': 'lofi', 'favorite_mood': 'chill', 'target_energy': 0.3}
============================================================
1. Rainy Shelf — Paper Lanterns
   Score: 4.94
   Reasons: genre match (+2.0), mood match (+1.0), energy similarity (+1.94)
------------------------------------------------------------
2. Library Rain — Paper Lanterns
   Score: 4.9
   Reasons: genre match (+2.0), mood match (+1.0), energy similarity (+1.9)
------------------------------------------------------------
3. Late Night Pages — LoRoom
   Score: 4.84
   Reasons: genre match (+2.0), mood match (+1.0), energy similarity (+1.84)
------------------------------------------------------------
4. Midnight Coding — LoRoom
   Score: 4.76
   Reasons: genre match (+2.0), mood match (+1.0), energy similarity (+1.76)
------------------------------------------------------------
5. Focus Flow — LoRoom
   Score: 3.8
   Reasons: genre match (+2.0), energy similarity (+1.8)
------------------------------------------------------------

=== Profile: Deep Intense Rock ===
    {'favorite_genre': 'rock', 'favorite_mood': 'intense', 'target_energy': 0.95}
============================================================
1. Storm Runner — Voltline
   Score: 4.92
   Reasons: genre match (+2.0), mood match (+1.0), energy similarity (+1.92)
------------------------------------------------------------
2. Thunder Circuit — Voltline
   Score: 4.88
   Reasons: genre match (+2.0), mood match (+1.0), energy similarity (+1.88)
------------------------------------------------------------
3. Iron Tempo — Max Pulse
   Score: 3.0
   Reasons: mood match (+1.0), energy similarity (+2.0)
------------------------------------------------------------
4. Gym Hero — Max Pulse
   Score: 2.96
   Reasons: mood match (+1.0), energy similarity (+1.96)
------------------------------------------------------------
5. Sunrise City — Neon Echo
   Score: 1.74
   Reasons: energy similarity (+1.74)
------------------------------------------------------------

=== Profile: Conflicted: High Energy + Sad Mood ===
    {'favorite_genre': 'pop', 'favorite_mood': 'melancholic', 'target_energy': 0.9}
============================================================
1. Gym Hero — Max Pulse
   Score: 3.94
   Reasons: genre match (+2.0), energy similarity (+1.94)
------------------------------------------------------------
2. Iron Tempo — Max Pulse
   Score: 3.9
   Reasons: genre match (+2.0), energy similarity (+1.9)
------------------------------------------------------------
3. Sunrise City — Neon Echo
   Score: 3.84
   Reasons: genre match (+2.0), energy similarity (+1.84)
------------------------------------------------------------
4. Golden Hour Drive — Prism Coast
   Score: 3.8
   Reasons: genre match (+2.0), energy similarity (+1.8)
------------------------------------------------------------
5. Storm Runner — Voltline
   Score: 1.98
   Reasons: energy similarity (+1.98)
------------------------------------------------------------

=== Profile: Genre Not In Catalog ===
    {'favorite_genre': 'hiphop', 'favorite_mood': 'happy', 'target_energy': 0.6}
============================================================
1. Skyline Bloom — Indigo Parade
   Score: 2.72
   Reasons: mood match (+1.0), energy similarity (+1.72)
------------------------------------------------------------
2. Rooftop Lights — Indigo Parade
   Score: 2.68
   Reasons: mood match (+1.0), energy similarity (+1.68)
------------------------------------------------------------
3. Golden Hour Drive — Prism Coast
   Score: 2.6
   Reasons: mood match (+1.0), energy similarity (+1.6)
------------------------------------------------------------
4. Sunrise City — Neon Echo
   Score: 2.56
   Reasons: mood match (+1.0), energy similarity (+1.56)
------------------------------------------------------------
5. Night Drive Loop — Neon Echo
   Score: 1.7
   Reasons: energy similarity (+1.7)
------------------------------------------------------------

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried
Halving the genre weight (2.0 → 1.0) and doubling the energy weight
(2.0 → 4.0), tested against the High-Energy Pop profile:

--- ORIGINAL WEIGHTS (genre=2.0, mood=1.0, energy=2.0) ---
1. Sunrise City — Neon Echo          Score: 4.94
2. Golden Hour Drive — Prism Coast   Score: 4.9
3. Gym Hero — Max Pulse              Score: 3.84
4. Iron Tempo — Max Pulse            Score: 3.8
5. Rooftop Lights — Indigo Parade    Score: 2.82

--- EXPERIMENT: genre halved (1.0), energy doubled (4.0) ---
1. Sunrise City — Neon Echo          Score: 5.88
2. Golden Hour Drive — Prism Coast   Score: 5.8
3. Gym Hero — Max Pulse              Score: 4.68
4. Rooftop Lights — Indigo Parade    Score: 4.64
5. Iron Tempo — Max Pulse            Score: 4.6
## Limitations and Risks

Some limitations are that it pulls from a small cataloug of songs that mostly fits your preferences in music which can be a bad thing since there is the possiblity that a song you never knew you would like will never be recommended. Additonally some catagories such as genre and energy have stronger influence in the recommender than mood.


## Reflection

I learned that recommenders run into issues of bias when the developer puts more "weight"(or empathisis/priority) on certain aspects of music. This could be a problem when a user is looking for songs that EXACTLY match their listed preferences since one of the preferneces they included could have a lot less "weight" in the recommendation algorithm. Additioanlly I learned that these "weights" can be used to turn data into predictions by comparing songs to each other and seeing which ones have the highest score based on those values.


