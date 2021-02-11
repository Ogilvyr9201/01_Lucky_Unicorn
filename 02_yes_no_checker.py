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

# Main routines
show_instructions = yes_no("Have you played this game before? ")

print("you choose {}.".format(show_instructions))
print()

having_fun = yes_no("Are you having fun? ")
print("You said {} :)".format(having_fun))
