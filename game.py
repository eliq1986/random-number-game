import random
guess_attempts = 1


def start_game():

    winning_message = """
    You got it!!
    It only took you {} attempt(s).
    Thank you for playing
    """

    player_name = input("Please enter your name ")

    print(f"Welcome to the greatest number guessing game {player_name}.\nThe computer at this time is generating a random number between 1 and 10")

    # creates random number
    def get_random_number():
        return random.randint(1,10)


    def you_win_message(number_of_attempts):
        global guess_attempts
        print(winning_message.format(guess_attempts))
        guess_attempts = 1


    def play_again():
        response_to_continue = input("Would you like to play again? yes/no ")
        if response_to_continue.lower() == "yes":
            play()
        elif response_to_continue.lower() == "no":
            print("Thanks for playing")

    def incorrect_guess(phrase):
        print(phrase)
        global guess_attempts
        guess_attempts += 1

    def play():
        random_number = get_random_number()
        while True:
            try:
                player_guess = int(input("Guess a number? "))
            except ValueError:
                print("Sorry but that is not a valid entry. Please enter an integer i.e 3")
            else:
                if player_guess < 1 or player_guess > 10:
                    incorrect_guess("Sorry but that guess is not a valid option")
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
