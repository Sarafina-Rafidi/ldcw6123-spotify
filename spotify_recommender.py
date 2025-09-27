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

if __name__ == "__main__":
    main()