import random
from hangman_words import word_list
from hangman_art import logo, stages


# Drawing from words
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 7
print(logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}\n")
    guess = input("Guess a letter: ").lower()

    # Checking the guess
    if guess in chosen_word:
        print(f"You've already guessed '{guess}'\n")
        if lives < 7:
            print(stages[lives])

    # Changing _ for a letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    # If guess not in chosen word
    if guess not in chosen_word:
        print(f"You guessed '{guess}', that's not in the word. You lose a life.\n")
        lives -= 1
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print(f"You lose. The word was '{chosen_word}'\n")

    # Check if user has got all letters
    if "_" not in display:
        end_of_game = True
        print(f"You win. The word was '{chosen_word}'")