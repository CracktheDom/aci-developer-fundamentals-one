'''  module that includes functions that check a string for complexity, and return a password strength
score to the user.
'''
#Define the string that contains all the special characters
special_characters = "`~!@#$%^&*()_-+={}[]:;\"'\"<,>.?/"

#create a function that returns True if a character in the given string is a number
def contains_numeric(str):
    for char in str:
        if char.isnumeric():
            return True
    return False
    
#create a function that returns True if a character in the given string is in Uppercase
def contains_upper(str):
    for char in str:
        if char.isupper():
            return True
    return False

#create a function that returns True if a character in the given string is in Lowercase
def contains_lower(str):
    for char in str:
        if char.islower():
            return True
    return False

#create a function that returns True if a character in the given string belongs to the set of special characters defined above
def contains_special(str):
    for char in str:
        if char in special_characters:
            return True
    return False
    
#Password strength calculator function that calls the above functions to calculate and return the strength score of the given password string
def password_strength(str):
    strength = 0
    
    if contains_upper(str):
        strength += 1
        
    if contains_lower(str):
        strength += 1
        
    if contains_special(str):
        strength += 1
        
    if contains_numeric(str):
        strength += 1
        
    if len(str) > 8:
        strength += 1
        
    return strength
    
