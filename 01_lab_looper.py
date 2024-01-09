"""
The Python program below prompts a user to input integers. When the user enters 'quit',
the program displays statistics about the numbers the user has entered.
Modify the code below so that it also displays the sum, minimum, maximum, and average of
the user input.
"""
# Initialize variables
value = ""
my_sum = 0
count = []

# Accept user input until the user types 'quit'
while value != "quit":
    value = input("Enter a number [or 'quit' to finish]: ")
    # If the user does not enter 'quit', process the number.
    if value != "quit":
        if value.isnumeric():
            number = int(value)  # cast input as int
            count.append(number)
            my_sum += number  # add current number to running total
        else:
            print("You must enter a number. Please try again.")
            continue  # continue with the next iteration of the loop

num_of_int = len(count)

# Print summary of results
print(f"You entered {num_of_int} integer{'' if num_of_int == 1 else "s"}.")
print(
    f"The minimum is {min(count)}, the maximum is {max(count)}, and the average of the inputted values is {sum(count)/num_of_int}"
)
