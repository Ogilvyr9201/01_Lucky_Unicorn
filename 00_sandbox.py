# Higher lower game V1, 16/09/20
# V1 Basic Program
# V2 program loops
# V3 best guess is added
# V4 Adds a win and lose
# V5 Tidy up code

import random


def num_check(num_type, question, num):
    valid = False
    while not valid:
        try:
            response = num_type(input(question))
            if num < response:
                valid = True
                return response
            else:
                print("Please enter a number more then {}".format(num))
                print()
        except ValueError:
            print("Please enter a number more then {}".format(num))
            print()


# Title and instructions
print("Higher / Lower Guessing game")
print("All you have to is guess the randomly generated number")
start = input("Press <enter> to start! ")

if start == "":
    # Ask user for integers
    print()
    print()

    low_integer = num_check(int, "What is your Low number? ", 0)

    high_integer = num_check(int, "What is your High Number? ", low_integer)

    num_guess = num_check(int, "How many Guesses do you get? ", 0)

    rounds = num_check(int, "How many Rounds do you want to play? ", 0)
    print()

    # Start
    best_guess = "_"
    num_rounds = 0
    while num_rounds < rounds:

        # pick a Random number
        secret = random.randrange(low_integer, high_integer)
        print()

        num_guesses = 0
        guess = -1
        if num_guesses == num_guess:
            print("You did not get the number in the amont of guesses given :(")
            print()
        else:
            while num_guesses < num_guess and guess != secret:
                valid_guess = False
                while not valid_guess:

                    try:
                        guess = int(input("Guess a number between {} and {}:   ".format(low_integer, high_integer)))
                        print()

                        if guess < low_integer or guess > high_integer:
                            print("Your Guess is not valid plesae enter something between {} and {}".format(low_integer,
                                                                                                            high_integer))
                            print()

                        else:
                            num_guesses += 1
                            valid_guess = True

                    except ValueError:
                        print("Your Guess is not valid plesae enter something between {} and {}".format(low_integer,
                                                                                                        high_integer))
                        print()

                # Compare guesses
                if num_guesses == num_guess:
                    print("You lost, you didnt get the number within the specified amount of guesses.")
                    num_rounds += 1
                elif guess < secret:
                    print("Its higher")
                    print()
                elif guess > secret:
                    print("Its Lower")
                    print()
                else:
                    win = ""
                    print("Correct")
                    print()
                    num_rounds += 1
                    if win == "":
                        print("Congratulations you geussed it in {} trys".format(num_guesses))

                        # Update Best Guess
                        if num_guesses < best_guess:
                            best_guess = num_guesses

# Finish
print()
print("Out of your {} rounds your Best Score was {} guesses".format(rounds, best_guess))

# Jesus

jesus = "jesus is the meaning of life"
