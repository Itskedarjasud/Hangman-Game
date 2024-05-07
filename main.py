# importing library
import random

# importing files
import hangman_art
import words

# Select a random word from the word list
chosen_word = random.choice(words.word_list)

# Initialize a list to display the hidden word
display = []
for letter in chosen_word:
    display.append("_")
print(display)

end = False
lives = 6
print(hangman_art.logo)

# Main game loop
while not end:   
    # Ask the player for a guess
    guess = input("guess a letter: ")
    guess = guess.lower()  # Convert the guess to lowercase to handle case insensitivity
    
    # Check if the guess has already been entered
    if guess in display:
        print("You entered it previously")
    
    index = 0
    # Iterate over each character in the chosen word
    for char in chosen_word:
        index += 1
        
        # If the guessed letter matches a character in the word, reveal it in the display
        if guess == char:
            display[index - 1] = guess
   
    # If the guessed letter is not in the word, decrement lives and check for game over
    if guess not in chosen_word:
        print(f"{guess} is not in the word")
        lives -= 1
        if lives == 0:
            end = True
            print("You Loose")
            print(f"The Word is {chosen_word}")
       
    print(display)
    
    # If there are no underscores left in the display, the player has won
    if "_" not in display:
        end = True
        print("You win")
        print(f"The Word is {chosen_word}")
    
    # Print the hangman art corresponding to the current number of lives left
    print(hangman_art.stages[lives])
