import random

words = ["apple", "mango", "tiger", "table", "river"]

word = random.choice(words)

guessed_letters = []
attempts = 6

print("Welcome to Hangman Game!")

while attempts > 0:

    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if guess in word:
        guessed_letters.append(guess)
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

if attempts == 0:
    print("Game Over!")
    print("The word was:", word)