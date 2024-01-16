"""Write a function that takes a date as input and returns the number of
 days until the next Friday. Develop and test your answer in your
 practice.py file in your AWS Cloud9 console. Complete each of the
 following steps to answer this challenge. Select each option as your
 complete it.

 Expect the date to be provided as a string with the format mm-dd-YYYY.
  Reformat and create a datetime object.

 """


import datetime


def next_friday(date: str) -> int:
    """
    Calculate the number of days until the next Friday from the given date.

    Args:
    - date (str): The input date in the format "MM-DD-YYYY".

    Returns:
    - int: The number of days until the next Friday (0 if the input date is
    already a Friday).

    Raises:
    - ValueError: If the input date is not in the correct format.

    Example:
    >>> next_friday("7-28-2023")
    0
    >>> next_friday("7-29-2023")
    6
    >>> next_friday("8-2-2023")
    2
    """
    date_format = "%m-%d-%Y"

    # Convert the input date string to a datetime object
    try:
        new_date = datetime.datetime.strptime(date, date_format)
    except ValueError:
        raise ValueError("Invalid date format. Please use 'MM-DD-YYYY'.")

    # Get the day of the week (0 is Monday, 1 is Tuesday, ..., 6 is Sunday)
    day_of_week = int(new_date.strftime("%w"))

    # Calculate the number of days until the next Friday
    if day_of_week <= 5:
        return 5 - day_of_week
    return day_of_week


# Test cases
assert next_friday("7-28-2023") == 0
assert next_friday("7-29-2023") == 6
assert next_friday("8-2-2023") == 2
