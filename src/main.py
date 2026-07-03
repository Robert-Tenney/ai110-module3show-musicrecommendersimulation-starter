from src.recommender import load_songs, recommend_songs
 
# Default "pop / happy" taste profile used for CLI verification
DEFAULT_USER_PREFS = {
    "favorite_genre": "pop",
    "favorite_mood": "happy",
    "target_energy": 0.75,
}
 
 
def main():
    """Load the catalog, run recommendations for the default profile, and print them."""
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")
 
    recommendations = recommend_songs(DEFAULT_USER_PREFS, songs, k=5)
 
    print("\nTop Recommendations")
    print("=" * 60)
    for rank, (song, score, reasons) in enumerate(recommendations, start=1):
        reason_text = ", ".join(reasons) if reasons else "no strong matches"
        print(f"{rank}. {song['title']} — {song['artist']}")
        print(f"   Score: {score}")
        print(f"   Reasons: {reason_text}")
        print("-" * 60)
 
 
if __name__ == "__main__":
    main()
 