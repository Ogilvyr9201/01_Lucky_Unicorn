import random

# Have Set balance for testing
balance = 10

rounds_played = 0

play_again = input("Press <enter> to Play ").lower()
while play_again == "":

    # increase number of rounds played
    rounds_played += 1

    # print round number
    print()
    print("***Round #{}***".format(rounds_played))
    chosen_num = random.randint(1, 100)

    # adjust balance
    # if random picks 1-5
    # user gets a unicorn: +$4.00
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4

    # if random picks 6-36
    # user gets a donkey: -$1.00
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1
    # if random picks -5
    # user gets a horse/donkey: -$0.50
    else:
        # if num is even token is horse
        if chosen_num % 2 == 0:
            chosen = "horse"

        # other wise its zebra
        else:
            chosen = "zebra"
        balance -= 0.5

    # Output
    print("You got {}. Your balance is ${:.2f}".format(chosen, balance))


    if balance < 1:
        play_again = "xxx"
        print()
        print("Sorry you have run out of money :(")
    else:
        print()
        play_again = input(" Press <enter> to play agan "
                           "or 'xxx' to quit ")
print()
print("Final Balance: $", balance)