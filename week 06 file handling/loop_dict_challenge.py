#!/usr/bin/env python3


import json
import jsonschema

# Define a JSON schema.
schema = {
    "type": "object",
    "properties": {
        "firstname": {"type": "string"},
        "lastname": {"type": "string"},
        "age": {"type": "integer"},
    },
    "required": ["firstname", "lastname", "age"],
}


with open("./hobbies.json", "r") as json_file:
    json_dict: dict[str : str | int] = json.load(json_file)

    for key, value in json_dict.items():
        if key == "hobbies":
            print(key)
            for elem in value:
                print(f"\t{elem}")
        else:
            print(f"{key}: {value}")

# Validate a JSON document against the schema.
document = {"firstname": "John", "lastname": "Stiles", "age": 28}
try:
    jsonschema.validate(document, schema)
except jsonschema.exceptions.ValidationError as x:
    print(x)
