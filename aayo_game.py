# Display the Hangman game title
# source ASCII ART
print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
''')

# Import the random module to select a random word
import random

# List of Hangman stages (visual representation of the hangman)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# List of possible words for the game
word_list = [
    "ability", "bizarre", "captain", "dynamic", "eclipse", "fragile", "glimmer", "harmony", 
    "illusion", "journey", "kingdom", "luminous", "magnify", "nectars", "organic", "paradox", 
    "quantum", "respite", "serenity", "texture", "unicorn", "victory", "whisper", "xenopus", 
    "yawning", "zealous", "abandon", "believe", "collect", "decline", "eagerly", "fantasy", 
    "graceful", "harvest", "inspire", "justice", "kindred", "liberty", "mystery", "notable", 
    "outlook", "precise", "quality", "rejoice", "sincere", "triumph", "umbrella", "vibrant", 
    "welfare", "xylitol", "yearning", "zealots", "amazing", "bravery", "clarify", "distant", 
    "elegant", "freedom", "gateway", "horizon", "imagine", "journey", "kindled", "loyalty", 
    "miracle", "nurture", "orchard", "passion", "quicken", "radiant", "sanctum", "tension", 
    "ultimate", "venture", "warrior", "xenon", "yielding", "zephyr", "affable", "bracket", 
    "courage", "delight", "endeavor", "foster", "glacier", "healing", "insight", "justice", 
    "kinship", "luminary", "mariner", "nostalgic", "optimism", "purpose", "quaint", "revelry", 
    "solitary", "tapestry"
]

# Choose a random word from the word_list
chosen_word = random.choice(word_list)

# Create an initial display with underscores for each letter in the chosen word
display = []
for _ in range(0, len(chosen_word)):
    display += "_"

# Set the initial number of lives and lives lost
Lives = 6
Lives_lost = 0

# Flag to track if the game has ended
end_of_game = False

# Main game loop
while not end_of_game:
    guess = input("guess a letter: ").lower()  # Prompt user to guess a letter
    if guess in display:
        print(f"You have already guessed '{guess}'")
    
    # Check if the guessed letter is in the chosen word and update the display
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # If the guessed letter is not in the chosen word, decrease lives
    if guess not in chosen_word:
        print(f"Chosen letter '{guess}' is not in the chosen word.")
        Lives -= 1 
        Lives_lost += 1
        print(f"You lose {Lives_lost} life!")
        if Lives == 0:
            end_of_game = True
            print("You lose all lives!\nYou got hanged")
            print(stages[Lives])

    # Print the current state of the display and the hangman stage
    print("".join(display))
    print(stages[Lives])
    
    # Check if the player has won
    if "_" not in display:
        end_of_game = True
        print("YOU WIN!")

# Reveal the chosen word at the end of the game
print(f"The word was: {chosen_word}")
