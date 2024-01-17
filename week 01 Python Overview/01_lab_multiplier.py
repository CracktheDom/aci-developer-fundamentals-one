# This python program prompts the user for two integers
# and prints a formatted string of the response to the user.

# Get first integer from user
number1 = input("Please enter your first integer: ")
if number1.isnumeric():
    number1 = int(number1)
else:
    while not number1.isnumeric():
        number1 = input("Please enter a valid integer: ")

# Get second integer from user
number2 = input("Please enter your second integer: ")
if number2.isnumeric():
    number2 = int(number2)
else:
    while not number2.isnumeric():
        number2 = input("Please enter a valid integer: ")

# Calculate the product of two inputs
product = int(number1) * int(number2)

# Print out the result
print(f"The product of your integers is {product}.")
