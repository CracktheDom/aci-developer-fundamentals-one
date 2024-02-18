"""
You are given a string of "letters" made of N English letters. Count the number
of different letters that appear in both uppercase and lowercase where all
lowercase occurrences of the given letter appear before any uppercase
occurrence.

For example, for letters = "aaAbcCABBc" the answer is 2. The condition is met
for letters 'a' and 'b', but not for 'c'.
"""


def find_unique_letter_combinations(letters: str) -> int:
    """
    Finds the number of unique letter combinations in a given string.

    Args:
        letters (str): The string containing letter combinations.

    Returns:
        int: The number of unique letter combinations.
    """
    unique_letters: set[str] = set()  # Set to store unique letters
    lowercase_seen: set[str] = set()  # Set to track lowercase letters encountered

    for letter in letters:
        if letter.islower():
            lowercase_seen.add(letter)
        elif letter.isupper():
            # Check if the lowercase version of the letter has been seen before
            if (
                letter.lower() in lowercase_seen
                # Check if the lowercase letter does not occur after the uppercase letter
                and letter.lower() not in letters[letters.index(letter) :]
            ):
                # Add the uppercase letter to unique_letters if conditions are met
                unique_letters.add(letter)

    return len(unique_letters)


# Test cases
assert find_unique_letter_combinations("aaAbcCABBc") == 2
assert find_unique_letter_combinations("xyzXYZabcABC") == 6
assert find_unique_letter_combinations("ABCabcAefG") == 0
