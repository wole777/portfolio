# Triathlon Awards

# Define a reusable function to capture event times in minutes from a user
def get_minutes():

    while True:
        try:
            user_input = float(input("Enter the minutes here: "))
            return user_input
        except ValueError:
            print("Invalid entry. Please enter numbers only.")


# Call the function to get event minutes from the user

print("Enter the athletes total swimming time in minutes")
swimming = get_minutes()

print("Enter the athletes total cycling time in minutes")
cycling = get_minutes()

print("Enter the athletes total running time in minutes")
running = get_minutes()

# Add the numbers to a list
time_list = [swimming, cycling, running]

# Print out the total time in minutes rounded to the nearest whole number
total_time = round(sum(time_list))
print(f"The total time taken by the athlete to complete the triathlon is: {total_time} minutes")

# Calculate and display the award that the participant will receive
if total_time <= 100:
    print("The athlete will receive the Honorary colours award!")
elif 100 <= total_time <= 105:
    print("The athlete will receive the Honorary half colours award!")
elif 105 <= total_time <= 110:
    print("The athlete will receive the Honorary scroll award!")
else:
    print("The athlete will receive no award.")