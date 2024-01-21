#!/usr/bin/env python3

"""For this task, imagine that you are the proud owner of an ice cream shop. As
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
and prompt them again."""


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
    global item_num_key
    isContainerChosen: bool = False  # Initialize loop variable/flag
    while not isContainerChosen:
        # prompt for input for container type, while loop until valid input
        container_response = input(
            f"What type of container would you like, {CONTAINER_CHOICE[0]} or {CONTAINER_CHOICE[1]}? "
        ).lower()

        # validate container input
        if container_response in CONTAINER_CHOICE:
            # add container response to order variable, possibly dict
            order_item_dict["container_type"] = container_response

            print(f'You selected a {order_item_dict["container_type"]}.')
            isContainerChosen = True  # switch loop variable to exit loop
        else:  # invalid input => print error msg & restart loop
            print(
                f"Try again.\nChoose between {CONTAINER_CHOICE[0]} or {CONTAINER_CHOICE[1]}: "
            )
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
    global item_num_key
    isScoopsSelected: bool = False  # Initialize loop flag/variable
    while not isScoopsSelected:
        # prompt for input of # of scoops
        num_scoops_response = input(
            f"\nHow many scoops would you like?\nYou can choose up to {len(NUMBER_OF_SCOOPS)} scoops? "
        )
        # validate scoop response
        if num_scoops_response.isnumeric():

            # convert response to int datatype
            num_scoops_response = int(num_scoops_response)

            # checking if user is requesting designated amount of scoops
            if 0 < num_scoops_response <= max(NUMBER_OF_SCOOPS):
                # add scoop response to order_item_dict
                order_item_dict["num_of_scoops"] = num_scoops_response

                print(
                    f'You selected {order_item_dict["num_of_scoops"]} scoop{'s' if order_item_dict["num_of_scoops"] > 1 else ""}.'
                )
                isScoopsSelected = True  # switch loop variable to exit loop
            else:  # invalid number of scoops
                print(f"\nTry again.\nChoose between {NUMBER_OF_SCOOPS[0]}, {NUMBER_OF_SCOOPS[1]} or {NUMBER_OF_SCOOPS[2]} scoops(s): ")
        else:  # input not numeric => print error msg & restart loop
            print(f"\nTry again.\nChoose between {NUMBER_OF_SCOOPS[0]}, {NUMBER_OF_SCOOPS[1]} or {NUMBER_OF_SCOOPS[2]} scoops(s): ")
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
    global item_num_key

    # dict to provide correct string for first, second or third scoop
    ordinal_map: dict[str: str] = {
        "1": "first",
        "2": "second",
        "3": "third"
    }

    isFlavorSelected: bool = False  # Initialize loop variable

    # Initialize list that may contain more than one flavor
    flavor_selections: list = list()

    while not isFlavorSelected:
        print(
            f"\nAvailable flavors: vanilla, strawberry, chocolate, cherry, mint, peach, grape".title()
        )

        # prompt for input of # of flavor(s)
        flavor_response = input(
            f"\nWhich flavor would you like for your {ordinal_map[str(len(flavor_selections) + 1)]} scoop? "
        ).lower()

        # validate flavor(s) response
        if flavor_response in FLAVORS:
            # add flavor_response to list of flavor selections
            print(f"You selected {flavor_response}")
            flavor_selections.append(flavor_response)

            # check if all flavors have been selected
            if len(flavor_selections) == order_item_dict['num_of_scoops']:
                isFlavorSelected = True

                # add flavor selection to dict
                order_item_dict["flavors"] = flavor_selections


        else:  # invalid input => print error msg & restart loop
            print(f"Try again.\nChoose between {FLAVORS}")
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
    - The function uses global variables and logs information about the process.
    """
    global item_num
    global item_num_key
    isOrderComplete = False
    isOrderComplete: bool = False  # Initialize loop variable

    # start the order probably use while loop
    while not isOrderComplete:
        order_container = get_container_type(order_item_dict)
        order_scoops = get_num_scoops(order_container)
        item_complete = get_flavors(order_scoops)
        order_response = ""

        while order_response not in ("y", "n"):
            # prompt if order is complete
            order_response = input(
                "\nWould like to add something to your order? (Y)es or (N)o: "
            ).lower()

            # if order is complete, change flag, exit order while loop, display details of order
            if order_response == "n":
                isOrderComplete = True

                # add completed item to order list
                order_list.append(item_complete)


            elif order_response == "y":
            # add more items to order, restart order while loop
                print("\nLet's get started on your next item!\n")
                item_num += 1  # increment item number

                # create new value for new item attributes
                item_num_key = f"item_{item_num}"

                # add completed order to order list
                order_list.append(item_complete)

                # add a new order (dict) to order list
                order_list.append({item_num_key: {}})


            else:  # invalid input
                print("Try again\n")
    return order_list


def print_order(order_list: list[dict]):
    global item_num_key
    for order in order_list:
        print(
              f"You ordered a {order[item_num_key]["container_type"]} with ",
              end=""
        )
        for flavor in order[item_num_key]["flavor"]:
            print(f"a scoop of {flavor.title()}", end=", ")


# Constant variables
CONTAINER_CHOICE: tuple[str, str] = ("cone", "cup")
NUMBER_OF_SCOOPS: tuple[int, int, int] = (1, 2, 3)
FLAVORS: tuple[str, str, str, str, str, str, str] = (
    "vanilla",
    "strawberry",
    "chocolate",
    "cherry",
    "mint",
    "peach",
    "grape",
)

# Initialize variables
item_num = 1
item_num_key = f"item_{item_num}"
order: dict[str:dict] = {item_num_key: dict()}
order_list: list[dict[str:str, str:int, str : list[str | str | str]]] = []


print("Greetings, how can I help you today?")
make_ice_cream_order(order[item_num_key], order_list)
# print_order(order_list)
