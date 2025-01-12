# Define a reusable function to capture numbers from a user
def get_number():

    while True:
        try:
            user_input = int(input("Enter a whole number: "))
            return user_input
        except ValueError:
            print("Invalid entry. Please enter whole numbers only.")


# Call the function to get three integers from the user
first_number = get_number()
second_number = get_number()
third_number = get_number()
# Add the numbers to a list
num_list = [first_number, second_number, third_number]
# Print the numbers
print(f"You entered: {num_list}")

# Print out the sum of the three integers
print(f"Their sum is: {sum(num_list)}")

# The first number minus the second number
print(f"The difference between the first number and second number is: {first_number-second_number}")

# The third number multiplied by the first number
print(f"The third number multiplied by the first number is: {third_number*first_number}")

# The sum of all three numbers divided by the third number
try:
    print(f"The sum of all three numbers divided by the third number is: {(sum(num_list))/third_number:.1f}")
except ZeroDivisionError:
    print("You are dividing by zero. Try again.")
finally:
    exit()