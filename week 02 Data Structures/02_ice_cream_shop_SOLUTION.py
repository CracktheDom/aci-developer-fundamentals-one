"""
You are opening an ice cream shop.
You sell ice cream in a cone or in a cup.  Each cone or cup can have 1 to 3 scoops of ice cream of any flavor.
You currently have 7 available flavors: vanilla, strawberry, chocolate, cherry, mint, peach, and grape.
Write a program that greets customers and takes their ice cream order.  Allow customers to order multiple cones or cups with a different flavor possible for each scoop.
If a customer enters an invalid option, notify them of the error and prompt them again.
"""

# Model Solution

# Available flavors tuple
ice_cream_flavors = (
    "vanilla",
    "strawberry",
    "chocolate",
    "cherry",
    "mint",
    "peach",
    "grape",
)
# Available containers tuple
containers = ("cone", "cup")

# Available number of scoops tuple
allowed_number_of_scoops = (1, 2, 3)

# Empty list to hold orders
items = []

# Greet the customer.
print("Welcome to the Ice Cream Shop!")

# Order loop
order_complete = False
while not order_complete:
    # Store empty dict to hold current order item
    item = {}
    # Initilize scoops as a key that holds an empty list
    item["scoops"] = []

    # Container choice
    container_chosen = False
    while container_chosen == False:
        order_container = input("Would you like your ice cream in a 'cone' or 'cup'? ")

        # validate user input
        if order_container in containers:
            # store container size in item dict
            item["container"] = order_container
            container_chosen = True

        # Invalid input. Ask user to reenter choice.
        else:
            print(
                "We don't sell that type of container.  Please enter 'cone' or 'cup'."
            )
            container_chosen = False

    # How many scoops?
    number_of_scoops = 0
    scoops_chosen = False
    while scoops_chosen == False:
        number_of_scoops = input(
            f"How many scoops would you like in your {order_container} (1, 2, or 3)? "
        )
        # Validate that input is numeric and allowed
        if (
            number_of_scoops.isnumeric()
            and int(number_of_scoops) in allowed_number_of_scoops
        ):
            scoops_chosen = True

        # Invalid input. Ask user to reenter choice.
        else:
            print("Please enter a scoop quantity of 1, 2, or 3.")
            scoops_chosen == False

    # What flavors for each scoop?
    print(
        "We sell the following flavors:  vanilla, strawberry, chocolate, cherry, mint, peach, or grape."
    )
    # Loop through a numeric list to gather flavor for each scoop
    for i in range(int(number_of_scoops)):
        # What flavor for scoop x
        flavor_chosen = False
        while flavor_chosen == False:
            # Gets flavor info for each scoop. 
            # Use i+1 because range starts at zero
            scoop_flavor = input(f"What flavor would you like for scoop {i + 1}? ")

            # Validates flavor in available flavors
            if scoop_flavor in ice_cream_flavors:
                flavor_chosen = True
                # Adds scoop flavor to dict for current item order
                item["scoops"].append(scoop_flavor)
            else:
                print(
                    "We don't have that flavor.  Please try vanilla, strawberry, chocolate, cherry, mint, peach, or grape."
                )
                flavor_chosen = False

    # Add the item dictionary to the ordered items list.
    items.append(item)

    # Would you like to order another cone or cup?

    continue_chosen = False
    while continue_chosen == False:
        continue_order = input("Would you like to order another item (yes/no)? ")
        if continue_order in ("yes", "no"):
            if continue_order == "yes":
                order_complete = False
            else:
                order_complete = True

            continue_chosen = True
        else:
            print("Please enter 'yes' to continue your order or 'no' to stop.")


# Print the order summary. Use \n to space output. 
print("\nYou placed the following order:\n ")

# Loop through each item on the items list
for item in items:
    # Use dict notation to access order info 
    print(f"{item['container']} with {(len(item['scoops']))} scoops")
    
    # Include flavor detail for each scoop
    # Use enumerate and \t to format output
    for e, scoop in enumerate(item["scoops"]):
        print(f"\t{e+1}. {scoop}")

print("Thank you for your patronage!")
