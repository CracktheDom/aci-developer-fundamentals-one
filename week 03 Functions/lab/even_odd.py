"""
Define a function that returns True if a number is even, and false if it is odd.
Define a function that returns True if a number is odd, and false if it is even.
Write a loop that calls the functions on values 0 - 9
"""


def is_even(integer: int) -> bool:
    return integer % 2 == 0


def is_odd(integer: int) -> bool:
    return integer % 2 != 0


for idx in range(10):
    print(f"Is {idx} even? {is_even(idx)}\n" f"Is {idx} odd? {is_odd(idx)}")
