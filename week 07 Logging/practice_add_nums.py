import logging


def add_numbers(x, y):
    """Adds two numbers and returns the sum"""
    if type(x) is not type(y):
        logging.warning("Args may not be compatible")

    if type(x) is str and type(y) is str:
        logging.error("Result is concatenated string")

    if (type(x) is not type(y)) and (type(x) in (bool, str) or type(y) in (bool, str)):
        logging.critical("Result '' cannot be processed")
        return ""

    logging.debug(f"x = {x}, y = {y}")
    logging.info(f"Function returns {x + y}")
    return x + y


logging.basicConfig(
    filemode="a",
    format="%(asctime)s %(levelname)s %(message)s",
    level=logging.INFO,
)
