# Functions
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


def instructions():
    print("**** How to Play ****")
    print()
    print("The rules go here")
    print()
    return""


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


# Main routines

# Ask if the user has played before
played_before = yes_no("Have you played this game before? ")

if played_before == "no":
    instructions()

print()

# Ask how much the user how much they wamt to play with
how_much = num_check("How much would you like to play with? ", 0, 10)

print("You have asked to play with {}.".format(how_much))

