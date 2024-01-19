import logging


def process_data() -> list[int]:
    """
    Process user input to create a list of integers.

    Returns:
    - list[int]: A list of integers entered by the user.

    Note:
    - The user is prompted to enter a list of numbers separated by commas.
    - If the input is not comma-separated, the user is prompted to try again
    until a valid input is provided.
    """

    # Log the start function activity
    logging.info("The function has started")

    # Prompt user for imput
    response: str = input(
        "Enter a list of numbers separated by commas, i.e. 5, 8, 6, 92: "
    )

    # Check for valid input, if invalid ask user again for input
    if "," not in response:
        input_is_valid = False
        logging.error("Not comma-separated values entered")
        while not input_is_valid:
            response = input("Try again: ")
            if "," in response:
                input_is_valid = True
            else:
                input_is_valid = False
                logging.error("Still no comma-separated values entered")
    else:
        input_is_valid = True  # valid input was initially entered

        """
        Strip blank space from string & split characters between commas into
        a list
        """
        num_list = [int(num) for num in response.replace(" ", "").split(",")]

        # Log information about numbers entered
        logging.info(f"The number of integers inputted is {len(num_list)}")
        logging.info(f"The function returns {num_list}")
    return num_list


"""
Set up logging behavior to append INFO and higher level messages along with
time, date, & log level to 'filename'
"""
logging.basicConfig(
    filename="example.log",
    filemode="a",
    format="%(asctime)s %(levelname)s %(message)s",
    level=logging.INFO,
)

print(process_data())
