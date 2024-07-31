def are_anagrams(word1, word2):
    # Convert both words to lowercase to make comparison easier

    word1 = word1.lower()
    word2 = word2.lower()

    # Sort the letters of both words alphabetically
    word1 = sorted(word1)
    word2 = sorted(word2)

    # Check if the sorted words are equal
    if word1 == word2:
        return True
    else:
        return False


print(are_anagrams("Fired", "fried"))
assert are_anagrams("top", "pot") == True
assert are_anagrams("listen", "enlist") == True
assert are_anagrams("schoolmaster", "the classroom") == True
assert are_anagrams("debit card", "bad credit") == True
assert are_anagrams("pottery", "lottery") == False
