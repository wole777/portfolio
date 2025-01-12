# ---- Take in a user’s name using input() and then print out (output) the name. ----
# Start by asking the user to enter their name
#   Check that a valid name is entered as more than one character
#       If name entry is invalid, prompt for another attempt till correct
# Print out correct name entry in a greeting

while True:
    try:
        name_of_user = input('Please enter your name: ')
        if len(name_of_user) > 1:
            break
    except ValueError:
        pass

print(f'Hi, {name_of_user}')

# ---- Take in a user’s age and print it out. ----
# Start by asking the user to enter their age
#   Check that a valid integer is entered
#       If age entry is invalid, prompt for another attempt till correct
# Print out correct age entry in a message

while True:
    try:
        age_of_user = int(input('Please enter your age: '))
        break
    except ValueError:
        pass

print(f'You entered your age as {age_of_user}')

# ---- Print the string “Hello World!” on a new line. ----
print('Hello World!')

''' I got some help with the except statement on stack overflow 
# (https://stackoverflow.com/questions/2244270/get-a-try-statement-to-loop-around-until-correct-value-obtained) '''