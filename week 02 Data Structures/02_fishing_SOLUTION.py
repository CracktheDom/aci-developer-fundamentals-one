"""
Mary and Martha went on a fishing trip and caught several fish. The data below contains a
record of their day. The weight of the fish is in ounces, and the length of the fish is in inches.

Write a program to perform the following tasks:
* Add an item to each dictionary that indicates who caught the fish.
* Merge the two lists together into a single list
* Display the average weight of the fish from both catches.
* Display the average length of the fish from both catches.
* Print the angler, id, and weight of any fish caught that weighed 24 ounces or more.
"""

marys_catch = [
{"id": 1, "length": 17.0, "weight": 18.2},
{"id": 2, "length": 22.0, "weight": 27.1},
{"id": 3, "length": 20.25, "weight": 21.9},
{"id": 4, "length": 12.5, "weight": 11.5},
{"id": 5, "length": 25.75, "weight": 33.4},
]

marthas_catch = [
{"id": 1, "length": 24.75, "weight": 29.3},
{"id": 2, "length": 9.25, "weight": 6.0},
{"id": 3, "length": 12.0, "weight": 16.8},
{"id": 4, "length": 22.5, "weight": 28.6},
{"id": 5, "length": 23.0, "weight": 29.7},
]

# Add an item to each dictionary that indicates who caught the fish.
for fish in marys_catch:
    fish["angler"] = "Mary"
for fish in marthas_catch:
    fish["angler"] = "Martha"
    
# Merge the two lists together into new list
total_catch = marys_catch + marthas_catch

# Initialize variables to calculate and display the average weight and length of the fish from both catches.
total_weight = 0
total_length = 0
fish_count = len(total_catch)

# Sum the weights and lengths of all fishes
for fish in total_catch:
    total_weight += fish["weight"]
    total_length += fish["length"]

# Divide total by number of fishes to calculate mean
average_weight = total_weight / fish_count
average_length = total_length / fish_count

# Print the average weights and lengths
print(
f"Average weight = {average_weight} , Average length = {average_length}"
)

print("\nCatches with higher than avarage weight:\n")

# Print the angler, id, and weight of any fish caught that weighed more than 24 ounces.

bigger_fishes = [fish for fish in total_catch if fish['weight'] > average_weight]

for fish in bigger_fishes:
    print(f"Angler: {fish['angler']}, Id: {fish['id']}, Weight: {fish['weight']}"
        )



