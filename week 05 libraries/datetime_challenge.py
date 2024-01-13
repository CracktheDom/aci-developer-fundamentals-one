"""Write a function that takes a date as input and returns the number of
 days until the next Friday. Develop and test your answer in your
 practice.py file in your AWS Cloud9 console. Complete each of the
 following steps to answer this challenge. Select each option as your
 complete it.

 Expect the date to be provided as a string with the format mm-dd-YYYY.
  Reformat and create a datetime object.

 """


import datetime


def next_friday(date: str) -> int:
    date_format = "%m-%d-%Y"
    new_date = datetime.datetime.strptime(date, date_format)
    day_of_week = int(new_date.strftime("%w"))
    if day_of_week <= 5:
        return 5 - day_of_week
    return day_of_week


assert next_friday("7-28-2023") == 0
assert next_friday("7-29-2023") == 6
assert next_friday("8-2-2023") == 2
