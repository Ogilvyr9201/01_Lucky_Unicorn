import random


# Functions

# Defines yes no questions
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("<error> Please say yes or no")
            print()


# Defines the instructions
def instructions():
    statement_generator("How To Play", "|", "=")
    print()
    print("Chose a starting amount between 1 and 10.")
    print()
    print("Press <enter> to play.")
    print("You will either get Donkey, horse, Zebra, or Unicorn")
    print()
    print("The game costs $1 to play each Round")
    print("depending on what you get you can either "
          "win or lose some money")
    print()
    print("Each Token is worth")
    print("Unicorn: $4.00")
    print("Horse: $-0.50")
    print("Zebra: $-0.50")
    print("Donkey: $-1.00")
    print()
    print("You can quit any time by typing 'xxx'")
    print()
    return ""


# Defines the umber checker
def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask question
            response = int(input(question))

            # if response is too high
            if low < response <= high:
                return response

            # output with error
            else:
                print(error)

        except ValueError:
            print(error)


# Defines Decoration
def statement_generator(statement, side_deco, top_bottom_deco):
    sides = side_deco * 3

    statement = "{} {} {}".format(sides, statement, sides)

    top_bottom = top_bottom_deco * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Main routines
# Title


statement_generator("Welcome to the lucky Unicorn Game", "|", "=")
print()

# Ask if the user has played before
played_before = yes_no("Have you played this game before? ")

if played_before == "no":
    print()
    instructions()

statement_generator("Lets Play!", "$", "-")
print()

# Ask how much the user how much they want to play with
how_much = num_check("How much would you like to play with? ", 0, 10)

balance = how_much

rounds_played = 0

play_again = input("Press <enter> to Play ").lower()
while play_again == "":

    # increase number of rounds played
    rounds_played += 1

    # print round number
    print()
    statement_generator("Round {}".format(rounds_played), "*", "-")
    print()
    chosen_num = random.randint(1, 100)

    # adjust balance
    # if random picks 1-5
    # user gets a unicorn: +$4.00
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        prize_deco = "$"
        balance += 4

    # if random picks 6-36
    # user gets a donkey: -$1.00
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        prize_deco = "D"
        balance -= 1
    # if random picks -5
    # user gets a horse/donkey: -$0.50
    else:
        # if num is even token is horse
        if chosen_num % 2 == 0:
            chosen = "horse"
            prize_deco = "H"

        # other wise its zebra
        else:
            chosen = "zebra"
            prize_deco = "Z"
        balance -= 0.5

    # Output
    output = (": You got {}. Your balance is ${:.2f} :".format(chosen, balance))

    statement_generator(output, prize_deco, "=")

    if balance < 1:
        play_again = "xxx"
        print()
        print("Sorry you have run out of money :(")
    else:
        print()
        play_again = input(" Press <enter> to play again or 'xxx' to quit ")
print()
statement_generator("Final Balance: {:.2f}".format(balance), "$", "=")
