import random

def choose_word():
    word_list = ["python", "hangman", "programming", "computer", "developer", "game", "openai"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    secret_word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    
    while attempts > 0:
        print("\nAttempts left:", attempts)
        display = display_word(secret_word, guessed_letters)
        print(display)

        if "_" not in display:
            print("Congratulations! You guessed the word:", secret_word)
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            print("Incorrect guess.")
            attempts -= 1

    if attempts == 0:
        print("\nSorry, you're out of attempts. The word was:", secret_word)

hangman()
