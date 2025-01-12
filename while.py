# Program that continually asks the user to enter a number until the user enters -1.
# The program calculates the average of the valid numbers entered. 0 is not a valid number.

# Initialise a list to store the numbers
num_list = []

# Initialise a number variable
num = 0

# Print a welcome message
print("Hi! This programme calculates the average of all the numbers you enter.")

# Prompt the user continually for number entries.
while num != -1:
    num = int(input("Enter a whole number. To quit, enter -1: "))
    # Exclude 0s from the list and quit on -1
    if num == -1 or num == 0:
        continue
    # Build the list
    num_list.append(num)

# Print the result
print(f"Your valid numbers are: {num_list} and their average is {sum(num_list)/len(num_list)}")