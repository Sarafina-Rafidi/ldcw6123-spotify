# Spotify-inspired Music Recommendation Assistant
# This program recommends music based on genre and mood, inspired by Spotify's personalized discovery.
# Connects to Brian Winston's innovation model by addressing the social need for accessible, personalized music.

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
    # Validate input (must be 1–4)
    while mood_choice not in ["1", "2", "3", "4"]:
        print("❌ Invalid choice! Please enter a number between 1 and 4.")
        mood_choice = input("Enter your choice (1-4): ").strip()

    # Step 3: Recommendations based on genre + mood
    recommendation = ""  # Placeholder for final recommendation

    # K-pop recommendations
    if genre == "K-pop":
        if mood_choice == "1":
            recommendation = "Artist: BTS | Song: Dynamite 🎇"
        elif mood_choice == "2":
            recommendation = "Artist: Blackpink | Song: Lovesick Girls 🎧"
        elif mood_choice == "3":
            recommendation = "Artist: Stray Kids | Song: God's Menu 💪"
        elif mood_choice == "4":
            recommendation = "Artist: IU | Song: Through the Night 🌙"

    # Malay recommendations
    elif genre == "Malay":
        if mood_choice == "1":
            recommendation = "Artist: KRU | Song: Awas 🎉"
        elif mood_choice == "2":
            recommendation = "Artist: Yuna | Song: Dan Sebenarnya 🎧"
        elif mood_choice == "3":
            recommendation = "Artist: Faizal Tahir | Song: Gemuruh ⚡"
        elif mood_choice == "4":
            recommendation = "Artist: Siti Nurhaliza | Song: Bukan Cinta Biasa 💔"

    # English recommendations
    else:
        if mood_choice == "1":
            recommendation = "Artist: Pharrell Williams | Song: Happy 😄"
        elif mood_choice == "2":
            recommendation = "Artist: Lo-fi Girl | Song: Study Beats 🎧"
        elif mood_choice == "3":
            recommendation = "Artist: Survivor | Song: Eye of the Tiger 🐯"
        elif mood_choice == "4":
            recommendation = "Artist: Adele | Song: Someone Like You 💔"

    # Final Output: Display personalized recommendation
    print(f"\n🎵 {user_name}, here's a {genre} song for your mood:")
    print(recommendation)
    print("\nThanks for using the Music Assistant! 💖 Enjoy your music 🎶")

# Run the program only if this file is executed directly
if __name__ == "__main__":
    main()