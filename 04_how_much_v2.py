# Functions
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

# main routine
how_much = num_check("How much would you like to play with? ", 0, 10)

print("You have asked to play with {}.".format(how_much))