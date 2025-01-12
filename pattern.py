# Using the asterisk '*' character to output an arrow pattern

# Declare variables
new_line = ""
char_1 = "*"

# Use a for loop combined with an if-else statement to generate the pattern
for i in range(1, 10):
    new_line += char_1
    # Print the first five lines in ascending order
    if i < 6:
        print(new_line)
    # Print the last four lines in descending order
    else:
        j = 10 - i
        print(new_line[0:j])