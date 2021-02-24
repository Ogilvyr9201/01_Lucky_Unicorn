import random

# main routine

tokens = ["unicorn", "horse", "zebra", "donkey"]
STARTING_BALANCE = 100

balance = STARTING_BALANCE

#  testing loop generate 20 tokens
for item in range(0, 100):
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
    print("Token: {} , Balance: ${:.2f}".format(chosen, balance))

# Output

print()
print("Starting Balance: ${:.2f}".format(STARTING_BALANCE))
print("Final Balance: ${:.2f}".format(balance))