import random 

wordlist = ["hangman", "llama", "python"]

bad_guesses = []

random_number = random.randint(0, len(wordlist) - 1)
word = wordlist[random_number]

print("Welcome to HANGMAN!")
print(word)
def get_word():
    random_number = random.randint(0, len(wordlist) - 1)
    return wordlist[random_number]


def create_board(word):
    board = []

    for letter in word:
        board.append("_")

    return board


def display_board(board, bad_guesses):
    print("\nWelcome to HANGMAN!")
    print(board)

    if len(bad_guesses) > 0:
        print(gallows[len(bad_guesses) - 1])

    print("Bad Guesses:", bad_guesses)


def play_game():
    word = get_word()
    board = create_board(word)
    bad_guesses = []

    while True:

        display_board(board, bad_guesses)

        # Check if player won
        if "_" not in board:
            print("\n🎉 YOU WON! The word was '" + word + "'")
            print("Thank you for playing!")
            break

        # Check if player lost
        if len(bad_guesses) == 6:
            print(gallows[5])
            print("\n💀 YOU LOST! The word was '" + word + "'")
            print("Thank you for playing!")
            break

        guess = input("\nGuess a letter: ").lower().strip()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("\n⚠️  Please enter ONE letter.")
            input("Press [enter] to continue.")
            continue

        # Check for repeated guesses
        if guess in board or guess in bad_guesses:
            print("\n⚠️ You already guessed that letter!")
            input("Press [enter] to continue.")
            continue

        # Correct guess
        if guess in word:
            print("\n✅ '" + guess + "' is in the word!")

            for i in range(len(word)):
                if word[i] == guess:
                    board[i] = guess

        # Incorrect guess
        else:
            print("\n❌ '" + guess + "' is not in the word.")
            bad_guesses.append(guess)

        input("Press [enter] to continue.")


# Start the game
play_game()
# Hangman drawings
gallows = [
    """
+---+
|
|
|
|
=======
""",
    """
+---+
|   O
|
|
|
=======
""",
    """
+---+
|   O
|   |
|
|
=======
""",
    """
+---+
|   O
|  /|
|
|
=======
""",
    """
+---+
|   O
|  /|\
|  /
|
=======
""",
    """
+---+
|   O
|  /|\
|  / \
|
=======
"""
]