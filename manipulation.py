# Get user input and save it in a variable
str_manip = input("Please enter a sentence: ")

# Perform string manipulations on the sentence
str_manip_length = len(str_manip)
print(f"The sentence is {str_manip_length} characters long.")

# Get the last letter
last_letter = str_manip[-1]
# Replace the last letter with the @ symbol and print
changed = str.replace(str_manip, last_letter, "@")
print(f"The last letter which is '{last_letter}' replaced everywhere with the @ symbol gives: '{changed}'")

# Printing the last three characters in str_manip backwards
last_three_letters = str_manip[-3:]
for i in last_three_letters:
    last_three_letters_1 = last_three_letters[0]
    last_three_letters_2 = last_three_letters[1]
    last_three_letters_3 = last_three_letters[2]
print(f"The last three letters in reverse are: '{last_three_letters_3}{last_three_letters_2}{last_three_letters_1}'")

# Creating a five-letter word made up of the first three characters and the last two characters in str_manip
first_three_characters = str_manip[:3]
last_three_characters = str_manip[-3:]
print(f"The first three and the last two characters together are: '{first_three_characters}{last_three_characters}'")