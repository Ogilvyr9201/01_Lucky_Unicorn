# Have Set balance for testing
balance = 5

rounds_played = 0

play_again = input("Press <enter> to Play ").lower()
while play_again == "":

    # increase number of rounds played
    rounds_played += 1

    # print round number
    print()
    print("***Round #{}***".format(rounds_played))
    balance -= 1
    print("Balance: ${:.2f}".format(balance))
    print()

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money :(")
    else:
        play_again = input(" Press <enter> to play agan "
                           "or 'xxx' to quit ")
print()
print("Final Balance: $", balance)