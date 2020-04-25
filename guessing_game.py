"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random

BREAK_WORDS = ["q", "quit", "break", "exit"]
MIN_NUMBER = 1
MAX_NUMBER = 20

high_score = 0
num_of_guesses = 0


def pluralize_try(num):
    if num == 1:
        return "try"
    return "tries"


def pluralize_guess(num):
    if num == 1:
        return "guess"
    return "guesses"


def display_intro():
    print("""
********** Welcome to Number Guesser! ***********
Instructions: Enter a number between {} and {}.
If you guess the number correctly, you win!
Otherwise you will need to guess again.
If at anytime you want to quit, just type 'quit'
""".format(MIN_NUMBER, MAX_NUMBER))


def display_high_score():
    global high_score
    if num_of_guesses < high_score or high_score == 0:
        high_score = num_of_guesses
    print("The current high score is {} {}\n".format(high_score, pluralize_try(high_score)))


def display_farewell():
    print("Thanks for playing! Goodbye!")


def make_guess(num, answer):
    if num < MIN_NUMBER or num > MAX_NUMBER:
        print("Guess must be between {} and {}".format(MIN_NUMBER, MAX_NUMBER))
        return False

    global num_of_guesses
    num_of_guesses += 1
    if num == answer:
        print("Congratulations, you win!")
        print("It took you {} {} to guess correctly".format(num_of_guesses, pluralize_guess(num_of_guesses)))
        return True

    print("It's {}".format("lower" if answer < num else "higher"))
    print("You have made {} {} so far".format(num_of_guesses, pluralize_guess(num_of_guesses)))


def play_round():
    global num_of_guesses
    num_of_guesses = 0
    answer = random.randint(MIN_NUMBER, MAX_NUMBER)
    round_over = False

    while not round_over:
        guess = input("Please enter a number > ")
        if guess.lower() in BREAK_WORDS:
            break

        try:
            round_over = make_guess(int(guess), answer)
        except ValueError:
            print("Sorry, your guess must be a number!")


def start_game():
    display_intro()

    keep_playing = True

    while keep_playing:
        play_round()
        display_high_score()

        choice = input("Play another round (yes/no)? ")
        if choice.lower() in ["n", "no"]:
            keep_playing = False

    display_farewell()


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
