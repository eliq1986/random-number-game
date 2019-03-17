"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.

    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
player_name = input("Please enter your name ")
print(f"Welcome to the greatest number guessing game {player_name}.\nThe computer at this time is generating a random number between 1 and 10")

# creates random number
def get_random_number():
    return random.randint(1,10)

def you_win_message(number_of_attempts):
    print("Got it")
    print("It only took you {} attempt(s)".format(number_of_attempts))
    print("Thank you for playing {}".format(player_name))

guess_attempts = 1

def play():
    guess_attempts = 1
    continuously_prompt = True
    random_number = get_random_number()
    while continuously_prompt:
        try:
            player_guess = int(input("Guess a number? "))
        except ValueError:
            print("Sorry but that is not a valid entry. Please enter an integer i.e 3")
        else:
            if player_guess < 1 or player_guess > 10:
                print("Sorry but that guess is not a valid option")
                guess_attempts += 1
            elif player_guess == random_number:
                you_win_message(guess_attempts)
                break
            elif player_guess > random_number:
                print("The number is too high")
                guess_attempts += 1
            elif player_guess < random_number:
                print("The number is too low")
                guess_attempts += 1
play()
response_to_continue = input("Would you like to play again?")







if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
