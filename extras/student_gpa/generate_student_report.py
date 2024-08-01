#!/usr/bin/env python3

import csv

"""
Student GPAs report
Read student records from a csv file with 3 columns: studentID, name, GPA
Calculate average GPA, and print top 3 students with highest GPA
"""


# create a Student class with studentId, name and gpa instance variables
class Student:
    def __init__(self, student_data: list[int, str, float]) -> None:
        self.studentId: int = student_data[0]
        self.name: str = student_data[1]
        self.gpa: float = float(student_data[2])

    def __str__(self):
        # override  __str__ method for student class
        return f"{self.studentId} {self.name} {self.gpa}"

    def __lt__(self, other):
        # override the __lt__ to sort the students by their gpa in descending order
        return self.gpa > other.gpa

    def __eq__(self, other):
        # override the __eq__ method to check if two students have the same gpa
        return self.gpa == other.gpa

    def __gt__(self, other):
        # override the __gt__ method to check if a student has a higher gpa than another student
        return self.gpa > other.gpa

    def __ge__(self, other):
        # override the __ge__ method to check if a student has a higher gpa than another student
        return self.gpa >= other.gpa


def calculate_average_gpa(students: list[Student, ...]) -> float:
    """
    Calculates the average GPA amongst a list of Student objects.

    Args:
        students (list[Student]): A list of Student objects

    Returns:
        float: The average GPA amongst a list of Student objects.
    """
    total: float = 0
    for student in students:
        total += student.gpa
    return total / len(students)


def display_top_three(students: list[Student, ...]) -> str:
    """
    Display the top three students with the top GPA.

    Args:
        students: (list[Student]): A list of Student objects

    Returns:
        str: A string that displays the top three students with the highest GPA.
    """
    students.sort()  # sort list by Student.gpa
    top_three = [students[i].name for i in range(3)]
    return ", ".join(top_three)


def generate_report() -> None:
    """
    Generate a report that calculates average GPA, and print the top 3 students with highest GPA
    """

    # Read student records from a file
    with open("student_records_07312024_194422.csv", newline="") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")

        # skip the header in the csv file
        next(csv_reader)

        # store the Student object in a list called students - this is a list of Student objects
        students: list[Student, ...] = [Student(row) for row in csv_reader]

    report_title: str = "Student Report"

    # print header for report
    print("*" * 30 + "\n" + f"{report_title:^30}" + "\n" + "*" * 30)

    # display average GPA
    print(f"Average Student GPA: {calculate_average_gpa(students):.2f}")

    # display top 3 students
    print(f"Top Three students: {display_top_three(students)}")


if __name__ == "__main__":
    generate_report()
