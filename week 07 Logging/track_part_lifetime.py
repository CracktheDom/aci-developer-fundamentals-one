"""
For this task, you will write a program that collects user input about a part
and the length of usage. When the program is finished running, it should tell
the user the number of hours that the part has been in service, and whether the
part should be replaced or not. Additionally, it should log informational,
warning, and critical messages about the part's service time to a separate file
as it runs.
"""


from string import ascii_lowercase
from random import choice, randint
import datetime
import logging


# get user input for part ID
def set_part_id() -> str:
    """
    Set a valid part ID based on user input.

    Returns:
    - str: Valid part ID in the format {2 letters}{2 digits}.

    Note:
    - The function prompts the user until a valid part ID is entered.
    - A valid part ID should consist of 2 alphabetical characters followed by 2 numeric characters.
    """
    logging.info("Entered the set_part_id function")
    while True:
        response = input(
            f"Please enter a 4-character string (2 alphabetic, 2 numeric) i.e. {choice(ascii_lowercase)}{choice(ascii_lowercase)}{randint(10, 99)}: "
        )

        # validate input is alphanumeric & four chars long
        if len(response) == 4 and response[:2].isalpha() and response[2:].isnumeric():
            logging.info(f"Correct format of part ID inputted: {response}")
            return response
        else:
            logging.error(f"Incorrect part number inputted: {response}")
            print(
                f"Try again, please use correct format, i.e. {choice(ascii_lowercase)}{choice(ascii_lowercase)}{randint(10, 99)}"
            )


def set_install_date(part_id: str) -> datetime:
    """
    Set the installation date for a specific part ID.

    Args:
    - part_id (str): The identifier of the part for which the installation date is being set.

    Returns:
    - datetime: The installation date as a datetime object.

    Note:
    - The function prompts the user to input the installation date in the format MM-DD-YYYY.
    - If the input is invalid, it provides an error message and asks for a correct format.
    - The function logs the entered date or any errors encountered during the process.
    """
    logging.info("Entered the set_install_date function")
    response_datetime: str = ""
    date_format: str = "%m-%d-%Y"

    while not isinstance(response_datetime, datetime.datetime):
        try:
            response_date = input(
                f"Please enter the date when part ID: {part_id} was installed.\nUse the format MM-DD-YYYY: "
            )

            # Convert valid string into datetime object
            response_datetime = datetime.datetime.strptime(response_date, date_format)

            logging.info(f"Date entered correctly: {response_datetime}")
            return response_datetime
        except ValueError as e:
            print(f"Error: {e}\n Use this format: MM-DD-YYYY, i.e. 02-02-2022")
            logging.error(f"Incorrect date format inputted: {response_date}")


def get_max_part_life(part_install_date: datetime.datetime, part_id: str):
    """
    Calculate the remaining service life of a part, log relevant information, and provide recommendations for replacement.

    Args:
    - part_install_date (datetime.datetime): The installation date of the part.
    - part_id (str): The unique identifier of the part.

    Returns:
    - None

    Logging Levels:
    - INFO: Parts with more than 20% of their maximum service time remaining.
    - WARNING: Parts with 20% or less of their maximum service time remaining.
    - CRITICAL: Parts that have exceeded their maximum service time.

    Note:
    - The function prompts the user for the maximum life of the part, in hours.
    - It calculates the number of hours the part has been in service.
    - It logs information about the part's service time and provides recommendations for replacement.
    """

    logging.info("Entered the get_max_part_life function")
    is_valid_input = False

    # Calculate hours in use
    part_hours_in_use = (
        datetime.datetime.now() - part_install_date
    ).total_seconds() / 3600

    print(f"This part, {part_id}, has been in use for {part_hours_in_use} hours")
    logging.info(
        f"This part, {part_id}, has been in use for {part_hours_in_use:.3f} hours"
    )

    # Validate input for maximum life of the part
    while not is_valid_input:
        try:
            response_max_life = input(
                f"What is the maximum life of part {part_id}? (in hours) "
            )
            if not response_max_life.isnumeric():
                print("Please enter valid input (in hours), i.e. 1000")
            elif response_max_life.isnumeric():
                max_life_hours = int(response_max_life)
                is_valid_input = True
                logging.info(
                    f"Max life of part id, {part_id}, is {max_life_hours} hours"
                )
        except ValueError as e:
            print(f"Error with max life input: {e}")

    # Determine remaining life of the part
    percent_maxlife_remaining = 1 - (part_hours_in_use / max_life_hours)

    # Log recommendations based on remaining life
    if percent_maxlife_remaining <= 0:
        logging.critical(
            f"Part id: {part_id} has exceeded its service life. REPLACE IMMEDIATELY!!!"
        )
    elif percent_maxlife_remaining > 0.20:  # more than 20% life remaining
        logging.info(
            f"Part id: {part_id} is good with {(max_life_hours - part_hours_in_use):.3f} hours remaining."
        )
    elif percent_maxlife_remaining <= 0.20:
        logging.warning(
            f"Part id: {part_id} has less than 20% of service life remaining. Replace in less than {(max_life_hours - part_hours_in_use):.3f} hours."
        )


logging.basicConfig(
    filename="part_lifetime.log",
    format="{asctime} {levelname} {message}",
    style="{",
    level=logging.INFO,
)


part_id = set_part_id()
install_date = set_install_date(part_id)
get_max_part_life(part_install_date=install_date, part_id=part_id)
