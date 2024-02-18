#!/usr/bin/env python3

from check_password_attributes import *


"""
Task: Password checker

Many websites prompt users to create a password to protect their account. The
companies hosting websites often have different requirements to ensure that
user passwords include a significant degree of complexity. When you enter a new
password, it can be checked for complexity and assigned a strength score.

For this task, you will write a module that includes functions that check a
string for complexity, and return a password strength score to the user. Then,
you will write a script that imports the module. When it runs, it should ask the user for a password and print the strength score, along with some context to explain if the password is strong enough.

Use the following steps to help you build the program:

    1. Create the module file. Define functions to check if the user included special characters, uppercase letters, lowercase letters, and numbers. Each check should add a point to the overall strength score if the check is successful.

    2. Return a strength score for each password that it checks.

    3. Write a script that imports the appropriate function(s), and asks the user to input a password. When the program runs, it should print out the strength of the provided password and a message about whether it is strong enough, or if the user should try again.
"""


def compute_password_strength(password: str) -> int:
    """
    Compute the strength score of a password based on certain attributes.

    Args:
        password (str): The password to assess.

    Returns:
        int: The strength score of the password.
    """
    strength_score: int = 0
    if contains_upper(password):
        strength_score += 1
    if contains_special(password):
        strength_score += 1
    if contains_lower(password):
        strength_score += 1
    if contains_number(password):
        strength_score += 1
    if is_long_enough(password):
        strength_score += 1
    return strength_score


def main():
    """
    Main function to assess the strength of a password.
    """
    while True:
        # Compute the strength score of the input password
        strength_score = compute_password_strength(
            input("Input your password to assess its strength: ")
        )

        # Evaluate the strength score and print the result
        if strength_score == 5:
            print(f"Password Strength: {strength_score}\nStrong Password")
            break
        else:
            print(f"Password Strength: {strength_score}\nWeak Password\nTry Again")


if __name__ == "__main__":
    main()
