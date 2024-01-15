import logging


def process_data() -> list[int]:
    logging.info("The function has started")
    response: str = input(
        "Enter a list of numbers separated by commas, i.e. 5, 8, 6, 92: "
    )
    if "," not in response:
        input_is_valid = False
        logging.error("not comma separated values entered")
        while not input_is_valid:
            response = input("Try again ")
            if "," in response:
                input_is_valid = True
            else:
                input_is_valid = False
                logging.error("still no comma separated values entered")
    else:
        input_is_valid = True
        num_list = [int(num) for num in response.replace(" ", "").split(",")]
        logging.info(f"The numbers of integers inputted is {len(num_list)}")
        logging.info(f"The function returns {num_list}")
    return num_list


logging.basicConfig(
    filename="example.log",
    filemode="a",
    format="%(asctime)s %(levelname)s %(message)s",
    level=logging.INFO,
)

print(process_data())
