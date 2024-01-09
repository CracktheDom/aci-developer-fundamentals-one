"""
Mary and Martha went on a fishing trip and caught several fish. The data below
contains a record of their day. The weight of the fish is in ounces, and the
length of the fish is in inches.

Write a program to perform the following tasks:
* Add an item to each dictionary that indicates who caught the fish.
* Merge the two lists together into a single list
* Display the average weight of the fish from both catches.
* Display the average length of the fish from both catches.
* Print the angler, id, and weight of any fish caught that weighed 24 ounces or more.
"""

import statistics

marys_catch: list[dict[str : float | int]] = [
    {"id": 1, "length": 17.0, "weight": 18.2},
    {"id": 2, "length": 22.0, "weight": 27.1},
    {"id": 3, "length": 20.25, "weight": 21.9},
    {"id": 4, "length": 12.5, "weight": 11.5},
    {"id": 5, "length": 25.75, "weight": 33.4},
]

marthas_catch: list[dict[str : float | int]] = [
    {"id": 1, "length": 24.75, "weight": 29.3},
    {"id": 2, "length": 9.25, "weight": 6.0},
    {"id": 3, "length": 12.0, "weight": 16.8},
    {"id": 4, "length": 22.5, "weight": 28.6},
    {"id": 5, "length": 23.0, "weight": 29.7},
]

for angler_catch in marys_catch:
    angler_catch["angler"] = "Mary"

for angler_catch in marthas_catch:
    angler_catch["angler"] = "Martha"

merged_list = marys_catch + marthas_catch
weight_list = [elem["weight"] for elem in merged_list]
length_list = [elem["length"] for elem in merged_list]
heavy_list = [elem for elem in merged_list if elem["weight"] >= 24.0]

print(marys_catch)
print(merged_list)
print(f"average weight: {statistics.mean(weight_list)}")
print(f"average length: {statistics.mean(length_list)}")
for elem in heavy_list:
    print(f"angler: {elem['angler']} id: {elem['id']} weight: {elem['weight']}")
