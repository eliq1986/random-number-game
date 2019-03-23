# Create by Elijah Quesada
# Python3
# March 20th, 2019
# Guess A Random Number

import random

# GLOBAL variable
guess_attempts = 1


def start_game():

    # Returns high score
    def get_high_score():
        if winning_scores:
            print("The current score to beat is {}".format(min(winning_scores)))
        else:
            print("Theres currently no high score...how about setting the bar")



    winning_scores = []

# Welcome Message
    welcome_message = "Welcome to the greatest number guessing game {}.\nThe computer at this time is generating a random number between 1 and 10"

# Winning Message
    winning_message = """
    You got it!!
    It only took you {} attempt(s).
    Thank you for playing
    """


    player_name = input("Please enter your name ")

    print(welcome_message.format(player_name))

# Returns random number
    def get_random_number():
        return random.randint(1,10)

# Displays winning message
    def you_win_message(number_of_attempts):
        global guess_attempts
        winning_scores.append(guess_attempts)
        print(winning_message.format(guess_attempts))
        guess_attempts = 1

# Function runs after game ends
    def play_again():
        while True:
            response_to_continue = input("Would you like to play again? yes/no ")
            if response_to_continue.lower() == "yes":
                play()
                break
            elif response_to_continue.lower() == "no":
                print("Thanks for playing")
                break
            else:
                print("Please enter yes or no")

# Displays incorrect phrase to user
    def incorrect_guess(phrase):
        print(phrase)
        global guess_attempts
        guess_attempts += 1

# Function runs until game is over
    def play():
        get_high_score()
        random_number = get_random_number()
        while True:
            try:
                player_guess = int(input("Guess a number? "))
            except ValueError:
                print("Sorry but that is not a valid entry. Please enter an integer i.e 3")
            else:
                if player_guess < 1 or player_guess > 10:
                    incorrect_guess("Sorry but that guess is outside the range")
                elif player_guess == random_number:
                    you_win_message(guess_attempts)
                    play_again()
                    break
                elif player_guess > random_number:
                    incorrect_guess("The number is too high")
                elif player_guess < random_number:
                    incorrect_guess("The number is too low")
    play()


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
