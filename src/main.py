from src.recommender import load_songs, recommend_songs
 
# Three core profiles requested by the evaluation phase
PROFILES = {
    "High-Energy Pop": {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.85,
    },
    "Chill Lofi": {
        "favorite_genre": "lofi",
        "favorite_mood": "chill",
        "target_energy": 0.35,
    },
    "Deep Intense Rock": {
        "favorite_genre": "rock",
        "favorite_mood": "intense",
        "target_energy": 0.9,
    },
    # Adversarial / edge-case profiles, designed to try to "trick" the scoring
    "Conflicted: High Energy Pop + Moody": {
        "favorite_genre": "pop",
        "favorite_mood": "moody",
        "target_energy": 0.9,
    },
    "Genre Not In Catalog": {
        "favorite_genre": "hiphop",
        "favorite_mood": "happy",
        "target_energy": 0.6,
    },
}
 
 
def format_recommendations(recommendations):
    """Return a formatted multi-line string for a list of (song, score, reasons) tuples."""
    lines = []
    for rank, (song, score, reasons) in enumerate(recommendations, start=1):
        reason_text = ", ".join(reasons) if reasons else "no strong matches"
        lines.append(f"{rank}. {song['title']} — {song['artist']}")
        lines.append(f"   Score: {score}")
        lines.append(f"   Reasons: {reason_text}")
        lines.append("-" * 60)
    return "\n".join(lines)
 
 
def main():
    """Load the catalog and print top-5 recommendations for every test profile."""
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")
 
    for name, prefs in PROFILES.items():
        print(f"\n=== Profile: {name} ===")
        print(f"    {prefs}")
        print("=" * 60)
        recommendations = recommend_songs(prefs, songs, k=5)
        print(format_recommendations(recommendations))
 
 
if __name__ == "__main__":
    main()
 