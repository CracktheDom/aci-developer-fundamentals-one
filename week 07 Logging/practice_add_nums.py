import logging


def add_numbers(x, y):
    """Adds two numbers and returns the sum"""
    try:
        return x + y
    except:
        return f"Cannot add {type(x)} and {type(y)}"


logging.basicConfig(
    filemode="a",
    format="%(asctime)s %(levelname)s %(message)s",
    level=logging.INFO,
)
