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


# Validation functions
def validate_scoops(value):
    """Returns True if the user has entered a valid number of scoops"""
    if value.isnumeric():
        num_scoop = int(value)
        if num_scoop in allowed_number_of_scoops:
            return True
    else:
        return False
        
def validate_flavor(value):
    """Returns True if user has selected from available ice cream flavors"""
    return value in ice_cream_flavors

def validate_container(value):
    """Returns True if the user has selected from available containers"""
    return value in containers

def validate_yes_no(value):
    """Returns True if a user entered 'yes' or 'no'"""
    return value in ('yes', 'no')
    
def valid_input(prompt, reprompt, func_validation):
    """Runs a loop until the user enters valid input"""
    input_is_valid = False
    while input_is_valid == False:
        i_input = input(prompt)
        if func_validation(i_input):
            input_is_valid = True
        else:
            print(reprompt)
            input_is_valid = False
    return i_input


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
    container_prompt = "Would you like your ice cream in a 'cone' or a 'cup'? "
    container_reprompt = "We don't sell that type of container. "
    item["container"] = valid_input(container_prompt, container_reprompt, validate_container)
    
    
    # How many scoops?
    scoops_prompt = f"How many scoops would you like in your {item['container']}, (1, 2, or 3)? "
    scoops_reprompt = "Please enter a scoop quantity of 1, 2, or 3. " 
    number_of_scoops = valid_input(scoops_prompt, scoops_reprompt, validate_scoops)
    
    # What flavors for each scoop?
    print(
        f"We sell the following flavors: {ice_cream_flavors}"
    )
    
    for i in range(int(number_of_scoops)):
        flavor_prompt = f"What flavor would you like for scoop {i + 1}? "
        flavor_reprompt = f"We don't have that flavor. Please choose from: {ice_cream_flavors}"
        scoop_flavor = valid_input(flavor_prompt, flavor_reprompt, validate_flavor)
        item["scoops"].append(scoop_flavor)
        
    # Add the item dictionary to the ordered items list.
    items.append(item)
    
    # Prompt for additional orders
    continue_prompt = "Would you like to order another? "
    continue_reprompt = "Please enter 'yes' to continue your order or 'no' to stop. "
    
    continue_order = valid_input(continue_prompt, continue_reprompt, validate_yes_no)
    
    # Sets order complete to False or True
    order_complete = continue_order == "no"
    

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
