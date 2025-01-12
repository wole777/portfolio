# ------- Converting variables from one type to another -------
# Declare the variables
# For each variable, convert them to the required type
# Print each converted variable on a new line

# This was my initial attempt before I decided on the method below
# num1 = int(99.23)
# num2 = float(23)
# num3 = str(150)
# string1 = int('100')

# Declare variables
num1 = 99.23
num2 = 23
num3 = 150
string1 = '100'

# Put variables in a list and cast to the required types
values = [int(num1), float(num2), str(num3), int(string1)]

# Print each variable on a new line
for i in values:
    print(i)