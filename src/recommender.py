import csv
 
# Scoring weights, from the Phase 2 "Algorithm Recipe"
GENRE_WEIGHT = 2.0
MOOD_WEIGHT = 3.0
ENERGY_WEIGHT = 2.0
 
 
def load_songs(path="data/songs.csv"):
    """Read songs.csv into a list of dicts, converting numeric fields to floats."""
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        songs = []
        for row in reader:
            for numeric_field in ("energy", "danceability", "acousticness", "tempo_bpm"):
                if row.get(numeric_field):
                    row[numeric_field] = float(row[numeric_field])
            songs.append(row)
        return songs
 
 
def score_song(user_prefs, song):
    """Score one song against user_prefs, returning (score, list_of_reasons)."""
    score = 0.0
    reasons = []
 
    # favorite_genre / favorite_mood can be a single string or a list of strings
    genre_prefs = user_prefs.get("favorite_genre", [])
    mood_prefs = user_prefs.get("favorite_mood", [])
    if isinstance(genre_prefs, str):
        genre_prefs = [genre_prefs]
    if isinstance(mood_prefs, str):
        mood_prefs = [mood_prefs]
 
    if song.get("genre") in genre_prefs:
        score += GENRE_WEIGHT
        reasons.append(f"genre match (+{GENRE_WEIGHT})")
 
    if song.get("mood") in mood_prefs:
        score += MOOD_WEIGHT
        reasons.append(f"mood match (+{MOOD_WEIGHT})")
 
    target_energy = user_prefs.get("target_energy")
    if target_energy is not None and "energy" in song:
        energy_gap = abs(song["energy"] - target_energy)
        energy_points = round(max(0.0, ENERGY_WEIGHT * (1 - energy_gap)), 2)
        if energy_points > 0:
            score += energy_points
            reasons.append(f"energy similarity (+{energy_points})")
 
    return round(score, 2), reasons
 
 
def recommend_songs(user_prefs, songs, k=5):
    """Score every song and return the top k as (song, score, reasons) tuples, highest first."""
    scored = [(song, *score_song(user_prefs, song)) for song in songs]
    ranked = sorted(scored, key=lambda entry: entry[1], reverse=True)
    return ranked[:k]
 