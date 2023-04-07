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