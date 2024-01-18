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
Flavor               vanilla, strawberry, chocolate, cherry, mint, peach, or grape

Write a program that greets customers and takes their ice cream order. Allow
customers to order multiple cones or cups, with a different flavor possible for
each scoop. If a customer enters an invalid option, notify them of the error
and prompt them again."""

# constant variables
SERVING_CHOICE = (cone, cup)
NUMBER_OF_SCOOPS = (1, 2, 3)
FLAVORS = (vanilla, strawberry, chocolate, cherry, mint, peach, grape)

# Initialize variables
order_id = 0
isOrderComplete = False
isValidInput = False

print("Greetings, how can I help you today?")
while not isOrderComplete:


    # start the order probably use while loop

    # prompt for input for container type, while loop until valid input
    # validate container input
    # add container response to order variable, possibly dict
    # invalid input => print error msg & restart loop

    # prompt for input of # of scoops
    # validate scoop response
    # add scoop response to order variable
    # invalid input => print error msg & restart loop

    # iterate over # of scoops
    # prompt for input of # of flavor(s)
    # validate flavor(s) response
    # add flavor(s) response to order variable
    # invalid input => print error msg & restart loop

    # prompt if order is complete
    # if yes, change flag, exit order while loop, display details of order
    # if no, restart order while loop
