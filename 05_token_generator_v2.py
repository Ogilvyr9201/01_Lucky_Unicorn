import random

# main routine

tokens = ["unicorn", "horse", "zebra", "donkey"]
balance = 100

#  testing loop generate 20 tokens
for item in range(0, 20):
    chosen = random.choice(tokens)

    # adjust balance
    if chosen == "unicorn":
        balance += 4
    elif chosen == "donkey":
        balance -= 1
    else:
        balance -= 0.5

    # Output

    print("Token: {} , Balance ${}".format(chosen, balance))