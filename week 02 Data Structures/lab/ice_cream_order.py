#!/usr/bin/env python3

import logging

"""
For this task, imagine that you are the proud owner of an ice cream shop. As
an entrepreneur, you know that increased efficiency can be the thing that sets
you apart from other stores. With all that you now know about iterables, data
types, conditionals, and user input, you're ready to build the logic for an
application that can automatically take customer orders.

To create a complete order, your order-taker needs to know how the ice cream
should be served, the number of scoops requested, and the flavor of ice cream
for each scoop. The following table includes the suggested options.

options                                   Available choices
Serving choice                               cone or cup
Number of scoops                             1, 2, or 3
Flavor               vanilla, strawberry, chocolate, cherry, mint, peach, or
                                             grape

Write a program that greets customers and takes their ice cream order. Allow
customers to order multiple cones or cups, with a different flavor possible for
each scoop. If a customer enters an invalid option, notify them of the error
and prompt them again.
"""


def get_container_type(order_item_dict: dict) -> dict:
    """
    Prompt the user for the type of container and validate the input.

    Args:
    - order_item_dict (dict): The dictionary representing the current item in
      the order.

    Returns:
    - dict: Updated order_item_dict with the chosen container type.

    Note:
    - The function uses global variables and logs information about the process.
    """
    # Entry point for logging
    logging.debug(f"{__LINE_FILL}Entering get_container_type(){__LINE_FILL}")

    is_container_chosen: bool = False  # Initialize loop variable/flag
    while not is_container_chosen:
        # prompt for input for container type, while loop until valid input
        container_response = input(
            f"What type of container would you like, {__CONTAINER_CHOICE[0]} or "
            f"{__CONTAINER_CHOICE[1]}? "
        ).lower()
        logging.debug(f"Contents of {container_response=}")

        # validate container input
        if container_response in __CONTAINER_CHOICE:
            # add container response to order variable, possibly dict
            order_item_dict["container_type"] = container_response

            print(f'You selected a {order_item_dict.get("container_type")}.')
            is_container_chosen = True  # switch loop variable to exit loop
            logging.debug(f'Contents of {order_item_dict.get("container_type")=}')
        else:  # invalid input => print error msg & restart loop
            print(
                f"\nTry again.\nChoose between {__CONTAINER_CHOICE[0]} or "
                f"{__CONTAINER_CHOICE[1]}: "
            )
    # logging contents of order_item_dict that is being returned
    logging.debug(f"get_container_type() returning {order_item_dict=}")

    return order_item_dict


def get_num_scoops(order_item_dict: dict) -> dict:
    """
    Prompt the user for the number of scoops and validate the input.

    Args:
    - order_item_dict (dict): The dictionary representing the current item in
      the order.

    Returns:
    - dict: Updated order_item_dict with the chosen number of scoops.

    Note:
    - The function uses global variables and logs information about the process.
    """
    # Entry point for logging
    logging.debug(f"{__LINE_FILL}Entering get_num_scoops(){__LINE_FILL}")

    is_scoops_selected: bool = False  # Initialize loop flag/variable
    while not is_scoops_selected:
        # prompt for input of # of scoops
        num_scoops_response: str = input(
            "\nHow many scoops would you like?"
            f"\nYou can choose up to {len(__NUMBER_OF_SCOOPS)} scoops? "
        )
        # validate scoop response
        try:
            # convert response to int datatype
            num_scoops_response = int(num_scoops_response)

            # checking if user is requesting designated amount of scoops
            if 0 < num_scoops_response <= max(__NUMBER_OF_SCOOPS):
                # add scoop response to order_item_dict
                order_item_dict["num_of_scoops"] = num_scoops_response

                print(
                    f"You selected {order_item_dict.get('num_of_scoops')} "
                    f"scoop{'s' if order_item_dict.get('num_of_scoops') != 1 else ''}."
                )
                is_scoops_selected = True  # switch loop variable to exit loop
            else:  # invalid number of scoops
                raise ValueError(
                    f"\nTry again.\nChoose between {__NUMBER_OF_SCOOPS[0]}, "
                    f"{__NUMBER_OF_SCOOPS[1]}, or {__NUMBER_OF_SCOOPS[2]} scoops: "
                )

        # input not numeric => print error msg & restart loop
        except ValueError:
            print(
                f"\nTry again.\nChoose between {__NUMBER_OF_SCOOPS[0]}, "
                f"{__NUMBER_OF_SCOOPS[1]} or {__NUMBER_OF_SCOOPS[2]} scoops(s): "
            )

    # logging contents of order_item_dict that is being returned
    logging.debug(f"{__LINE_FILL}get_num_scoops() returning {order_item_dict=}")

    return order_item_dict


def get_flavors(order_item_dict: dict) -> dict:
    """
    Prompt the user for flavors and validate the input.

    Args:
    - order_item_dict (dict): The dictionary representing the current item in
      the order.

    Returns:
    - dict: Updated order_item_dict with the chosen flavors.

    Note:
    - The function uses global variables and logs information about the process.
    """
    logging.debug(f"{__LINE_FILL}Entering get_flavors(){__LINE_FILL}")

    # dict to provide correct string for first, second or third scoop
    ordinal_map: dict[int:str] = {1: "first", 2: "second", 3: "third"}

    is_flavor_selected: bool = False  # Initialize loop variable

    # Initialize list that may contain more than one flavor
    flavor_selections: list = list()

    print(
        f"Next, select your {order_item_dict['num_of_scoops']} "
        f"flavor{'s' if order_item_dict['num_of_scoops'] != 1 else ''}"
    )

    while not is_flavor_selected:
        print(
            "\nAvailable flavors: vanilla, strawberry, "
            "chocolate, cherry, mint, peach, grape".title()
        )

        print("Input 'V' for Vanilla")
        print("Input 'S' for Strawberry")
        print("Input 'L' for Chocolate")
        print("Input 'Y' for Cherry")
        print("Input 'M' for Mint")
        print("Input 'P' for Peach")
        print("Input 'G' for Grape")

        # prompt for input of # of flavor(s)
        flavor_response = input(
            f"\nWhich flavor would you like for your "
            f"{ordinal_map.get(len(flavor_selections) + 1)} scoop? "
        ).lower()

        # validate flavor(s) response
        if flavor_response in __FLAVORS.keys():
            # map user input to string
            flavor_selection: str = __FLAVORS.get(flavor_response)

            print(
                  f"\nYou selected {flavor_selection.title()} as your "
                  f"{ordinal_map.get(len(flavor_selections) + 1)} scoop."
            )

            # add flavor_response to list of flavor selections
            flavor_selections.append(flavor_selection)

            # check if all flavors have been selected
            if len(flavor_selections) == order_item_dict["num_of_scoops"]:
                is_flavor_selected = True

                # add flavor selection to dict
                order_item_dict["flavors"] = flavor_selections

                logging.debug(f"Flavors added to {order_item_dict['flavors']=}")

        else:  # invalid input => print error msg & restart loop
            print(f"Try again.\nChoose between {', '.join(__FLAVORS.values())}")

    # logging contents of order_item_dict that is being returned
    logging.debug(f"get_flavors() returning {order_item_dict=}")

    return order_item_dict


def make_ice_cream_order(order_item_dict: dict, order_list: list) -> list[dict]:
    """
    Create an ice cream order by calling the functions to get container type,
    number of scoops, and flavors.

    Args:
    - order_item_dict (dict): The dictionary representing the current item in
      the order.
    - order_list (list): The list containing the entire order.

    Returns:
    - list: Updated order_list with the current order.

    Note:
    - The function logs information about the process.
    """
    logging.debug(f"{__LINE_FILL}Entered make_ice_cream_order(){__LINE_FILL}")
    is_order_complete: bool = False  # Initialize loop variable

    # start the order probably use while loop
    while not is_order_complete:
        item_complete: dict = get_flavors(  # get flavors
            # gets number of scoops
            get_num_scoops(
                # gets container type
                get_container_type(order_item_dict)
            )
        )
        order_complete_response: str = ""  # Initialize loop variable

        while order_complete_response not in ("y", "n"):
            # prompt if order is complete
            order_complete_response = input(
                "\nWould like to add something to your order? "
                "\nInput 'Y' for Yes "
                "\nInput 'N' for No: "
            ).lower()

            """
            if order is complete, change flag, exit order while loop,
            display details of order
            """
            if order_complete_response == "n":
                is_order_complete = True  # switch loop variable to exit loop

            # add more items to order, restart order while loop
            elif order_complete_response == "y":
                print("\nLet's get started on your next item!\n")

                # reinitialize order_item_dict to accept attributes for new item
                order_item_dict: dict[str: str | int | list] = {
                    "container_type": "",
                    "num_of_scoops": 0,
                    "flavors": [],
                }

                logging.debug(f"Item complete, reinitializing {order_item_dict=}")

            else:  # invalid input
                print("Try again\n")

            # add completed item to order list
            order_list.append(item_complete)

            logging.debug(f"Contents of {order_item_dict}=")
            logging.debug(f"Contents of {item_complete}=")

    # logging contents of order_list that is being returned
    logging.debug(f"make_ice_cream_order() returning {order_list}=")

    return order_list


def print_order(order_list: list[dict]):
    for order in order_list:
        print(f"You ordered a {order['container_type']} with ", end="")
        for flavor in order["flavors"]:
            print(f"a scoop of {flavor.title()}", end=", ")

    print("\nThank you for your order.")


# fmt off

# Constant variables
__LINE_FILL: str = r'-' * 12
__CONTAINER_CHOICE: tuple[str] = ('cone', 'cup')
__NUMBER_OF_SCOOPS: tuple[int] = (1, 2, 3)
__FLAVORS: dict[str:str] = {
    'v': 'Vanilla',
    's': 'Strawberry',
    'l': 'Chocolate',
    'y': 'Cherry',
    'm': 'Mint',
    'p': 'Peach',
    'g': 'Grape',
}


# Initialize variables
order_list: list = list()
item_dict: dict[str: str | int | list] = {
    "container_type": "",
    "num_of_scoops": 0,
    "flavors": [],
}

# set up logging configuration
logging.basicConfig(
    level=logging.DEBUG,
    filemode="a",
    filename="ice_cream.log",
    format="{asctime} {levelname} {message}",
    style="{",
)
# fmt on

# print("Greetings, how can I help you today?")
# order_list = make_ice_cream_order(item_dict, order_list)
# print_order(order_list)

if __name__ == "__main__":
    make_ice_cream_order(item_dict, order_list)

# TODO: Think about modularity, break repetitive validation into separate function(s)
