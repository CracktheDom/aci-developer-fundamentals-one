import logging
import json
import os


def parse_products(file_path: str) -> list[dict]:
    """
    Parse products from a JSON file and create a list of dictionaries with
    product information.

    Args:
    - file_path (str): The path to the JSON file containing product information.

    Returns:
    - list[dict[str: tuple[float, str]]]: A list of dictionaries representing
    products, each with a name, price, and description.

    Note:
    - If the file_path does not exist, an empty list is returned.
    - If a product in the JSON file is missing a name or price, it is logged as
    an error.
    """
    inventory_list = list()

    try:
        if os.path.exists(file_path):
            with open(file_path) as file_obj:
                json_obj: list[dict[str : str | float]] = json.load(file_obj)
    except IOError as e:
        logging.error(f"{e}: {file_path} does not exist")
        print(f"{file_path} does not exist")
        return inventory_list

    for obj_elem in json_obj:
        if "price" in obj_elem and "name" in obj_elem:
            inventory_dict: dict[str : tuple[float, str]] = {
                obj_elem["name"]: (obj_elem["price"], obj_elem["description"])
            }
            inventory_list.append(inventory_dict)
            logging.info(f'{obj_elem["name"]} added to inventory')
        elif "price" not in obj_elem or "name" not in obj_elem:
            logging.error(
                f"Product name and/or price is missing from {obj_elem.__repr__()}"
            )

    return inventory_list


def write_to_json_file(json_file_path: str, products_list: list):
    """
    Write a list of products to a JSON file.

    Args:
    - json_file_path (str): The path to the JSON file where the products will
      be written.
    - products_list (list): A list of dictionaries representing products, each
      with a name, price, and description.

    Note:
    - If an error occurs during writing, it is logged and error is displayed.
    """
    try:
        with open(json_file_path, "w") as file_pointer:
            json.dump(products_list, indent=4, fp=file_pointer)
            logging.info(f"Successfully wrote data to {file_pointer=}")
    except Exception as e:
        logging.error(
            f"An error occurred while trying to write to {file_pointer}, error is: {e}"
        )
        print(f"An error occurred while trying to write to {json_file_path}")


# Configure logging
logging.basicConfig(
    filename="./prod_validation.log",
    format="{asctime} {levelname} {message}",
    style="{",
    level=logging.INFO,
)

if __name__ == "__main__":
    write_to_json_file("./inventory.json", parse_products("./prod_sample.json"))
