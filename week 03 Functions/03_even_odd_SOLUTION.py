"""
Define a function that returns True if a number is even, and false if it is odd. 
Define a function that returns True if a number is odd, and false if it is even.
Write a loop that calls the functions on values 0 - 9
"""
# Function that takes an integer as a parameter and returns True if the integer is even or False if it is odd
def isEven(num):
    return num % 2 == 0

# Function that takes an integer as a parameter and returns True if the integer is even or False if it is odd
def isOdd(num):
    return num % 2 == 1
    
# Loop through numbers 0 through 9 and print if the number is even or not by calling the above created function
for i in range(10):
    print(f"{i} is even: {isEven(i)}")
    
# Loop through numbers 0 through 9 and print if the number is odd or not by calling the above created function
for i in range(10):
    print(f"{i} is odd: {isOdd(i)}")
    
