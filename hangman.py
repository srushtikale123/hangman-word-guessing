import random
import time

# Categories with words
categories = {
    "Animals": ["elephant", "tiger", "kangaroo", "giraffe"],
    "Fruits": ["banana", "apple", "mango", "pineapple"],
    "Actors": ["al pacino", "brad pitt", "tom cruise", "johnny depp"],
    "Tech": ["python", "keyboard", "laptop", "internet"]
}

def choose_category():
    print("\nAvailable Categories:")
    for idx, category in enumerate(categories, 1):
        print(f"{idx}. {category}")
    choice = int(input("Select category number: "))
    category = list(categories.keys())[choice - 1]
    return category, random.choice(categories[category]).upper()

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters or letter == " " else "_" for letter in word])

def multiplayer_setup():
    word = input("Player 1, enter a word for Player 2 to guess: ").upper()
    hint = input("Enter a hint for the word (e.g., actor, tech): ")
    print("\n" * 50)  # Clear screen effect
    return hint, word

def play_hangman(single_player=True):
    if single_player:
        hint, word = choose_category()
    else:
        hint, word = multiplayer_setup()

    guessed_letters = []
    attempts = 6
    time_limit = 60  # seconds
    start_time = time.time()

    print("\n🎮 Welcome to Hangman!")
    print(f"Hint: {hint}")
    print(f"You have {attempts} attempts and {time_limit} seconds!")

    while attempts > 0:
        if time.time() - start_time > time_limit:
            print("\n⏰ Time's up!")
            break

        print("\nWord:", display_word(word, guessed_letters))
        guess = input("Enter a letter: ").upper()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            print("✅ Good guess!")
            guessed_letters.append(guess)
        else:
            print("❌ Wrong guess.")
            attempts -= 1
            guessed_letters.append(guess)
            print(f"Remaining attempts: {attempts}")

        if all(letter in guessed_letters or letter == " " for letter in word):
            print("\n🎉 You won! The word was:", word)
            break
    else:
        print("\n💀 You lost! The word was:", word)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        main_menu()

def main_menu():
    print("\n--- Hangman Game Modes ---")
    print("1. Single Player (Choose category)")
    print("2. Multiplayer (2-player word setup)")
    mode = input("Choose game mode (1 or 2): ")

    if mode == "1":
        play_hangman(single_player=True)
    elif mode == "2":
        play_hangman(single_player=False)
    else:
        print("Invalid option. Starting single player by default.")
        play_hangman(single_player=True)

main_menu()
