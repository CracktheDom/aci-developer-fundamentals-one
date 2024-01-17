
import logging
from datetime import datetime, timedelta

logging.basicConfig(filename="part_lifetime.log", 
                    format="%(asctime)s %(levelname)s %(message)s", 
                    level=logging.INFO)

def validate_part(value):
    if len(value) == 4:
        return value.isalnum()
    
def validate_numeric(value):
    return value.isnumeric()

def validate_date(value):
    try:
        datetime.strptime(value, "%m/%d/%Y %H:%M")
        return True
    except:
        return False

def valid_input(prompt, reprompt, func_validate):
    input_is_valid = False
    while input_is_valid == False:
        i_input = input(prompt)

        if func_validate(i_input):
            input_is_valid = True

        else:
            print(reprompt)
            input_is_valid = False

    return i_input

part_prompt = """Please enter the part id number. This is a 4 character alphanumeric code.  """
part_reprompt = "There is no record of that part id."
part_id = valid_input(part_prompt, part_reprompt, validate_part)

service_prompt = """Please enter the date and time that the part went into service (mm/dd/YYYY HH:MM):  """
service_reprompt = "The date you entered is not in the correct format."
service_date = valid_input(service_prompt, service_reprompt, validate_date)

hours_prompt = "Please enter the maximum lifetime hours of the part:  "
hours_reprompt = "The value you entered is not numeric."
max_hours = valid_input(hours_prompt, hours_reprompt, validate_numeric)

service_datetime = datetime.strptime(service_date, "%m/%d/%Y %H:%M")

maximum_service_hours = int(max_hours)

hours_in_service = (datetime.now() - service_datetime) / timedelta(hours=1)

hours_remaining = round((maximum_service_hours - hours_in_service),2)
percent_remaining = round(hours_remaining/maximum_service_hours * 100, 2)

if percent_remaining > 20:
    logging.info(f"""Part id: {part_id} is good. It has {hours_remaining} hours of service remaining.""")
    print(f"The part is good and has {hours_remaining} hours left.")
    
elif hours_remaining <= 0:
    logging.critical(f"""Part id: {part_id} has exceeded the recommended service hours. Replace immediately.""")
    print ("""The part has exceeded recommended service time. Replace immediately.""")
else:
    logging.warning(f"""Part id {part_id} has less than 20% of service time remaining. Replace in less than {hours_remaining} hours.""")
    print("Part has less than 20% of service hours remaining. Replace soon.")
    
