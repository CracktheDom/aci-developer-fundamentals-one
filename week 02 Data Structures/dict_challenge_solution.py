"""
Write a program that takes user input to create an inventory for a new store. 
The inventory should be stored as a dictionary. 
Users should have the option to add or remove items from the inventory.
When the user is finished adding or removing items, print the final inventory. 
"""

more_edits = True
inventory = {}

while more_edits:
    # provide answer choices for users. \n creates a new line for each choice
    choice = int(input("What would you like to do? Enter a number \n \
    1. Add new inventory item \n \
    2. Increase quantity of existing item \n \
    3. Decrease quantity of existing item \n \
    4. Quit this program \n"))
    
    
    if choice == 1: 
        # user enter key
        item_name = input("What is the name of item? ")
        # user enters corresponding value
        item_quant = int(input("How many of them do you have? "))
        # store key and value in dict
        inventory[item_name] = item_quant
    elif choice == 2: 
        # user provides key
        item_name = input("What is the name of the item? ")
        # if the key does not exist, rerun while loop
        if item_name not in inventory.keys():
            print ("That item is not in this inventory. Try again. \n\n")
        else:
            # if the key exists, gather amount of increase
            increase_amt = int(input("How many would you like to add? "))
            inventory[item_name] += increase_amt
    elif choice == 3:
        # user provides key
        item_name = input("What is the name of the item? ")
        # if the key does not exist, restart loop
        if item_name not in inventory.keys():
            print ("That item is not in this inventory.")
        else: 
            #if the key exists, gather amount of decrease
            decrease_amt = int(input("How many would you like to remove? "))
            inventory[item_name] -= decrease_amt
    else:
        more_edits = False

print (inventory)

    