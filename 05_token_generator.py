import random

# main routine

tokens = ["unicorn", "horse", "zebra", "donkey"]
balance = 100

#  testing loop generate 20 tokens
for item in range(0, 20):
    chosen = random.choice(tokens)


    print(chosen)