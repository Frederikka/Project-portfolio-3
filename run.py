import os
import random


def clear():
    """
    Function to clear the terminal
    """

    os.system(('cls' if os.name == 'nt' else 'clear'))


def intro_screen():
    """
    Function for the intro screen and instructions
    """

    print("Welcome to 'Voyage for Valhalla'\n")
    print("""
              |    |    |                   Voyage for Valhalla is a word game.
             )_)  )_)  )_)                  If a letter you guess is in the
            )___))___))___)                 random word, it will show.
           )____)____)_____)                If a guessed letter is not in the
         _____|____|____|______             chosen word, you will lose a life.
-------- |                   /---------     You have 5 lives to guess before
                                            the boat sinks and you lose!
     ^^^^^ ^^^^^^^^^^^^^^^^^^^^^
  ^^^^      ^^^^     ^^^    ^
  ^^^^      ^^^         ^                   Good luck!
    """)
    print("---------------------------------------")
    name = ''
    name_is_valid = False
    while not name_is_valid:
        name = input("Enter your name here to begin play: ").strip()
        if validate_name(name):
            name_is_valid = True
        else:
            print('Please enter a valid name (Letters or spaces only).')
    clear()
    return name


def validate_name(name):
    """
    Function to determine if name is valid
    """
    if name == '':
        return False
    for letter in name:
        if not (letter.isalpha() or letter.isspace()):
            return False
    return True


def print_boat_stages(lives):
    """
    Function to display the boat's stages in the game
    """
    if (lives == 5):
        print("""
              |    |    |
             )_)  )_)  )_)
            )___))___))___)
           )____)____)_____)
 --------_____|____|____|______-----
---------|                   /---------
  ^^^^^ ^^^^^^^^^^^^^^^^^^^^^
    ^^^^      ^^^^     ^^^    ^^
         ^^^^      ^^^

            """)
    elif (lives == 4):
        print("""
              |    |    |
             )_)  )_)  )_)
            )___))___))___)
           )____)____)_____)
 --------_____|____|____|_____-----
  ^^^^^ ^^^^^^^^^^^^^^^^^^^^^
    ^^^^      ^^^^     ^^^    ^^
         ^^^^      ^^^
            """)
    elif (lives == 3):
        print("""
              |    |    |
             )_)  )_)  )_)
            )___))___))___)
           )____)____)_____)
  ^^^^^ ^^^^^^^^^^^^^^^^^^^^^
    ^^^^      ^^^^     ^^^    ^^
         ^^^^      ^^^

            """)
    elif (lives == 2):
        print("""
              |    |    |
             )_)  )_)  )_)
            )___))___))___)
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


def get_words():
    """Function to return word from words list
    """
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


def main():
    """
    Function for main functions with while loop for answer options
    """
    name = intro_screen()
    clear()
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
                    print(f'You already guessed the letter "{user_guess}"')
                elif user_guess not in answer:
                    print(f'"{user_guess}" is not in the word!')
                    lives -= 1
                    guessed_letters.append(user_guess)
                else:
                    print(f'"{user_guess}" is in the word, well done!')
                    guessed_letters.append(user_guess)
                    for index in range(0, len(answer)):
                        if answer[index] == user_guess:
                            current_word[index] = user_guess
                    if answer == ''.join(current_word):
                        guessed = True
            elif len(user_guess) == len(answer) and user_guess.isalpha():
                if user_guess != answer:
                    print(f'"{user_guess}" is not in the word')
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
            print(f'You won, {name}! Well done! The word was "{answer}".')
        input('Press any key to try again! ')
        clear()


# Code for "if" condition to run "if" statement when game is being played


if __name__ == "__main__":
    main()
