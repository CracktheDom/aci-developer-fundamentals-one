import pytest
from find_unique_letter_combos import find_unique_letter_combinations


@pytest.mark.parametrize(
    "string, result",
    [
        ("aA", 1),
        ("aAbB", 2),
        ("abcABC", 3),
        ("aAaAa", 0),
        ("abAB", 2),
        ("aAbBcCdD", 4),
        ("", 0),
        ("aAAbBB", 2),
        ("AaBbCcDd", 0),
        ("aB", 0),
    ],
)
def test_find_unique_letter_combinations(string, result):
    assert find_unique_letter_combinations(string) == result
