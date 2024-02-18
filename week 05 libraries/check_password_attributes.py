from string import digits, ascii_lowercase, ascii_uppercase, punctuation


def is_str(password: str) -> bool:
    """
    Check if the input is a string.

    Args:
        password (str): The input to check.

    Returns:
        bool: True if the input is a string, False otherwise.
    """
    return isinstance(password, str)


def contains_special(password: str) -> bool:
    """
    Check if the password contains any special characters.

    Args:
        password (str): The password to check.

    Returns:
        bool: True if the password contains any special characters, False otherwise.
    """
    return any([char in punctuation for char in password])


def contains_upper(password: str) -> bool:
    """
    Check if the password contains any uppercase letters.

    Args:
        password (str): The password to check.

    Returns:
        bool: True if the password contains any uppercase letters, False otherwise.
    """
    return any([char in ascii_uppercase for char in password])


def contains_lower(password: str) -> bool:
    """
    Check if the password contains any lowercase letters.

    Args:
        password (str): The password to check.

    Returns:
        bool: True if the password contains any lowercase letters, False otherwise.
    """
    return any([char in ascii_lowercase for char in password])


def contains_number(password: str) -> bool:
    """
    Check if the password contains any numeric digits.

    Args:
        password (str): The password to check.

    Returns:
        bool: True if the password contains any numeric digits, False otherwise.
    """
    return any([char in digits for char in password: str])


def is_long_enough(password: str) -> bool:
    """
    Check if the length of password is at least 12 characters.

    Args:
        password (str): The password to check.

    Returns:
        bool: True if the password is at least 12 characters long, False otherwise.
    """
    return len(password) >= SUFFICIENT_PASSWORD_LENGTH


SUFFICIENT_PASSWORD_LENGTH = 12
