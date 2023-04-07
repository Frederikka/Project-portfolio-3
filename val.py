import os
import random

# Function to clear the terminal
def clear():
    os.system(('cls' if os.name == 'nt' else 'clear'))

# Function for the intro screen and instructions
def intro_screen(): 
    print("Welcome to 'Voyage for Valhalla'\n")
    print("""
              |    |    |                Voyage for Valhalla is a word game.
             )_)  )_)  )_)               If a letter you guess is in the chosen
            )___))___))___)\             random word, it will show.
           )____)____)_____)\\            If a guessed letter is not in the
         _____|____|____|____\\\__        chosen word, you will lose a life.
---------\                   /---------  You have 5 lives to guess before the
  ^^^^^ ^^^^^^^^^^^^^^^^^^^^^            boat sinks and you lose the game.
    ^^^^      ^^^^     ^^^    ^^    
         ^^^^      ^^^                   Good luck!
    """)
    print("---------------------------------------")
    name = input("Enter your name here to begin play: ")
    clear()
    return name  

# Function to display the boat's stages in the game
def print_boat_stages(lives):    
    if (lives == 5):
        print("""
              |    |    |                 
             )_)  )_)  )_)              
            )___))___))___)\            
           )____)____)_____)\\
 --------_____|____|____|____\\\__-----
---------\                   /---------
  ^^^^^ ^^^^^^^^^^^^^^^^^^^^^
    ^^^^      ^^^^     ^^^    ^^
         ^^^^      ^^^
            """)
    elif (lives == 4):
        print("""                         
              |    |    |                 
             )_)  )_)  )_)              
            )___))___))___)\            
           )____)____)_____)\\
 --------_____|____|____|____\\\__-----
  ^^^^^ ^^^^^^^^^^^^^^^^^^^^^
    ^^^^      ^^^^     ^^^    ^^
         ^^^^      ^^^
            """)               
    elif (lives == 3):
        print("""
              |    |    |                 
             )_)  )_)  )_)              
            )___))___))___)\            
           )____)____)_____)\\
  ^^^^^ ^^^^^^^^^^^^^^^^^^^^^
    ^^^^      ^^^^     ^^^    ^^
         ^^^^      ^^^

            """)      
    elif (lives == 2):
        print("""
              |    |    |                 
             )_)  )_)  )_)              
            )___))___))___)\            
  ^^^^^ ^^^^^^^^^^^^^^^^^^^^^
    ^^^^      ^^^^     ^^^    ^^
         ^^^^      ^^^      
          
            """)              
    elif (lives == 1):
        print("""
              |    |    |                 
             )_)  )_)  )_)              
  ^^^^^ ^^^^^^^^^^^^^^^^^^^^^
    ^^^^      ^^^^     ^^^    ^^
         ^^^^      ^^^
            """)         

# Function to return word from words list
def get_words():
    return [
        'delightful',
        'sound',
        'shoes',
        'connect',
        'malicious',
        'explode',
        'spooky',
        'pies',
        'fill',
        'fowl',
        'vessel',
        'awake',
        'billowy',
        'green',
        'sugar',
        'remove',
        'marvelous',
        'bag',
        'jealous',
        'prevent'
    ]   

# Function for main functions with while loop for answer options
def main():
    name = intro_screen()
    while True:
        guessed_letters = []
        lives = 5
        current_word = []
        guessed = False
        answer = random.choice(get_words())
        current_word = ['_' for x in range(len(answer))]

        while not guessed and lives > 0:
            print_boat_stages(lives)
            print(f"Lives: {lives}")
            print(f'Current word: {" ".join(current_word)}\n')
            user_guess = input(f'Please guess a letter, {name}: ')
            clear()
            if len(user_guess) == 1 and user_guess.isalpha():
                if user_guess in guessed_letters:
                    print(f'You already guessed the letter "{user_guess.upper()}". Please try again! ')
                elif user_guess not in answer:
                    print(f'"{user_guess.upper()}" is not in the word! Please try again!')
                    lives -= 1
                    guessed_letters.append(user_guess)
                else:
                    print(f'"{user_guess.upper()}" is in the word, well done!')
                    guessed_letters.append(user_guess)
                    for index in range(0, len(answer)):
                        if answer[index] == user_guess:
                            current_word[index] = user_guess
                    if answer == ''.join(current_word):
                        guessed = True
            elif len(user_guess) == len(answer) and user_guess.isalpha():
                if user_guess != answer:
                    print(f'"{user_guess.upper()}" is not in the word')
                    lives -= 1
                else:
                    guessed = True
            else:
                print('Not a valid response, please try again!')
        if lives == 0:
            print("""
            UH OH...
  ^^^^^ ^^^^^^^^^^^^^^^^^^^^^
    ^^^^      ^^^^     ^^^    ^^
         ^^^^      ^^^
            """) 
            print(f'You died, {name}. Oh dear.. The word was "{answer}".')
        else:
            print(f'You won, {name}! Congratulations, you live to fight another day. The word was "{answer}".')
        input('Press any key to try again! ')
        clear()
         