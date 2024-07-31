def are_anagrams(first_word: str, second_word: str) -> bool:
    """
    Check if two words are anagrams of each other.

    Args:
        first_word (str): The first word to compare.
        second_word (str): The second word to compare.

    Returns:
        bool: True if the words are anagrams, False otherwise.
    """
    # Remove white space and convert all letters to lowercase
    first_word = first_word.replace(" ", "").lower()
    second_word = second_word.replace(" ", "").lower()

    # Check if the sets of characters in both words are equal
    # and if the lengths of the words are equal
    return set(first_word) == set(second_word) and len(first_word) == len(second_word)


assert are_anagrams("top", "pot") == True
assert are_anagrams("listen", "enlist") == True
assert are_anagrams("schoolmaster", "the classroom") == True
assert are_anagrams("debit card", "bad credit") == True
assert are_anagrams("pottery", "lottery") == False
