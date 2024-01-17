# Model Solution
value = ""
my_sum = 0
my_min = 0
my_max = 0
count = 0
my_average = 0
# Accept user input until the user types 'quit'
while value != "quit":
    value = input("Enter a number [or 'quit' to finish]: ")
    # If the user does not enter 'quit', process the number.
    if value != "quit":
        if value.isnumeric():
            count += 1
            number = int(value)
            # Handle the special case for the first number entered.
            if count == 1:
                my_min = number
                my_max = number
            
            # Add number to sum.
            my_sum += number
            
            # Checking for new minimum
            if number < my_min:
                my_min = number
            # Checking for new maximum
            if number  > my_max:
                my_max = number
            # Calculate the average.
            my_average = my_sum / count
            
        else:
            print("You must enter a number. Please try again.")
            continue
    

    
    # Print summary of results.
print(f"You entered {count} integers.")
print(f"Min = {my_min}")
print(f"Max = {my_max}")
print(f"Sum = {my_sum}")
print(f"Average = {my_average}")
