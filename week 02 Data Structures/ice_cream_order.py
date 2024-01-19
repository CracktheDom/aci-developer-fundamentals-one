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


def get_container_type():
    isContainerChosen = False
    while not isContainerChosen:
        # prompt for input for container type, while loop until valid input
        container_response = input(
            f"What type of container would you like, {CONTAINER_CHOICE[0]} or {CONTAINER_CHOICE[1]}? "
        ).lower()

        # validate container input
        if container_response in CONTAINER_CHOICE:
            # add container response to order variable, possibly dict
            order_list.append({"container_type": "container_response"})
            isContainerChosen = True
        else:  # invalid input => print error msg & restart loop
            print(
                f"Try again.\nChoose between {CONTAINER_CHOICE[0]} or {CONTAINER_CHOICE[1]}: "
            )


def get_num_scoops():
    isScoopsSelected = False
    while not isScoopsSelected:
        # prompt for input of # of scoops
        num_scoops_response = input(
            f"How many scoops would you like?\nYou can choose up to {len(NUMBER_OF_SCOOPS)} scoops? "
        )
        # validate scoop response
        if num_scoops_response.isnumeric():
            if num_scoops_response <= len(NUMBER_OF_SCOOPS):
                num_scoops_response = int(num_scoops_response)

                # add scoop response to order variable
                order_list.append({"num_of_scoops": num_scoops_response})

                isScoopsSelected = True
        else:  # invalid input => print error msg & restart loop
            print(
                f"Try again.\nChoose between {NUMBER_OF_SCOOPS[0]}, {NUMBER_OF_SCOOPS[1]} or {NUMBER_OF_SCOOPS[2]} scoops(s): "
            )
    return num_scoops_response


def get_flavors(num_of_scoops: int):
    ordinal_map = {"1": "first", "2": "second", "3": "third"}
    isFlavorSelected = False  # Initialize loop variable
    while not isFlavorSelected:
        # Initialize list of possible multiple flavors
        flavor_selections = []
        print(
            f"Flavors: vanilla, strawberry, chocolate, cherry, mint, peach, grape".title()
        )

        # prompt for input of # of flavor(s)
        flavor_response = input(
            f"Which flavor would you like for your {ordinal_map[{len(flavor_selections) + 1}]} scoop? "
        ).lower()

        # validate flavor(s) response
        if flavor_response in FLAVORS:
            # add flavor_response to list of flavor selections
            flavor_selections.append(flavor_response)

            # check if all flavors have been selected
            if len(flavor_selections) == num_of_scoops:
                isFlavorSelected = True

                # add flavor selection to order list
                order_list.append({"flavor": flavor_selections})

        else:  # invalid input => print error msg & restart loop
            print(f"Try again.\nChoose between {FLAVORS}")

    # prompt if order is complete
    # if yes, change flag, exit order while loop, display details of order
    # if no, restart order while loop


def make_order():
    # start the order probably use while loop
    while not isOrderComplete:
        get_container_type()
        scoops = get_num_scoops()
        get_flavors(scoops)


# constant variables
CONTAINER_CHOICE: tuple[str, str] = (cone, cup)
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
order_list: list[dict[str:str]] = list()
isOrderComplete = False
isValidInput = False

print("Greetings, how can I help you today?")
