# Functions


# main routine

error = "Please enter a whole number between 1 and 10\n"

valid = False
while not valid:
    try:
        # ask question
        response = int(input("How much would you like to play with? "))

        # if response is too high
        if 0 < response <= 10:
            print("You have asked to play with {}.".format(response))

        # output with error
        else:
            print(error)

    except ValueError:
        print(error)