# Spotify-inspired Music Recommendation Assistant
# This program recommends music based on genre and mood

def main():
    # Welcome message
    print("🎶=== Spotify-inspired Music Recommendation Assistant ===🎶")
    print("Discover your next favorite song in just a few clicks!\n")

    # Ask for user name
    user_name = input("👋 What's your name? ")
    print(f"\nHello, {user_name}! Let's find the perfect track for you.\n")

    # Step 1: Genre Selection
    print("🎼 Please choose a genre:")
    print("1. K-pop")
    print("2. Malay")
    print("3. English")

    # Get user choice for genre
    genre_choice = input("Enter your choice (1-3): ").strip()
    # Validate input (must be 1–3)
    while genre_choice not in ["1", "2", "3"]:
        print("❌ Invalid choice! Please enter 1, 2, or 3.")
        genre_choice = input("Enter your choice (1-3): ").strip()

    # Assign genre based on input
    if genre_choice == "1":
        genre = "K-pop"
    elif genre_choice == "2":
        genre = "Malay"
    else:
        genre = "English"

    print(f"\n✨ Great! You selected {genre} songs.\n")

    # Step 2: Mood Selection
    print("😊 Now choose your mood:")
    print("1. Happy")
    print("2. Focus")
    print("3. Workout")
    print("4. Sad")

    # Get user choice for mood
    mood_choice = input("Enter your choice (1-4): ").strip()

if __name__ == "__main__":
    main()