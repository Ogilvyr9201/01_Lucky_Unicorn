# Loop
loop = ""

while loop == "":

    # Ask user if they have played before
    show_instructions = input("Have you played my game before? ").lower()
    print()

    # If they say yes, output 'program continues'
    if show_instructions == "yes":
        print("Program continues")

    # If they say no, out put 'display instructions'
    elif show_instructions == "no":
        print("Display instructions")

    # If they put in anything else output error message
    else:
        print("Please say yes or no")
        print()