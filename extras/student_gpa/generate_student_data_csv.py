#!/usr/bin/env python3

import csv
from random import choice, randint, uniform
from first_names import first_names
from last_names import last_names
from datetime import datetime


def generate_full_name() -> str:
    """
    Generate a random full name consisting of a first name and a last name.

    The names are chosen based on a random 'origin' from the first_names and last_names files.

    Returns:
        str: The generated full name.
    """
    # Select a random 'origin' from the keys of the first_names dictionary
    origin = choice(list(first_names.keys()))

    # Select a random first name from the list of first names of the chosen origin
    first_name = choice(first_names[origin])

    # Select a random last name from the list of last names of the chosen origin
    last_name = choice(last_names[origin])

    # Return the full name in "First Last" format
    return f"{first_name} {last_name}"


def generate_student_data_file() -> None:
    # generate file name
    date_time: str = datetime.now().strftime("%m%d%Y_%H%M%S")
    file_name: str = f"student_records_{date_time}.csv"

    # Open CSV file in write mode
    with open(file_name, mode="w", newline="") as file_object:
        csv_writer = csv.writer(file_object)
        csv_writer.writerow(["Student ID", "Full Name", "GPA"])

        for _ in range(NUM_OF_RECORDS):
            # Generate random 4 digit student ID
            student_id = randint(1000, 9999)

            full_name = generate_full_name()

            # Return a random floating-point number N such that a <= N <= b
            grade_point_average = round(uniform(GPA_MIN, GPA_MAX), 2)

            csv_writer.writerow([student_id, full_name, grade_point_average])


NUM_OF_RECORDS: int = 30  # number of records to be generated
GPA_MIN: float = 1.50
GPA_MAX: float = 4.00

if __name__ == "__main__":
    generate_student_data_file()
    print("CSV file generation complete.")
