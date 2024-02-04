# This python program prompts the user for two integers
# and prints a formatted string of the response to the user.

# Get first integer from user
while True:
    try:
        first_number = int(input("Please enter your first integer: "))
        break
    except ValueError:
        print("Please enter a valid integer\n")

# Get second integer from user
while True:
    try:
        second_number = int(input("Please enter your second integer: "))
        break
    except ValueError:
        print("Please enter a valid integer\n")


# Calculate the product of two inputs & print out the result
print(f"The product of your integers is {int(first_number) * int(second_number):,}.")
