import config
import random
from datetime import timedelta

random.seed(config.SEED)

def select_error_type():
    value = random.random()

    threshold1 = config.MISSING_EVENT_RATIO
    threshold2 = threshold1 + config.DUPLICATE_EVENT_RATIO
    if value < threshold1:
        return "MISSING"
    elif value < threshold2:
        return "DUPLICATE"
    else:
        return "IDEAL"
    
def is_it_the_starting_event():
    return random.random() < 0.5
    

def get_event_errors(start_of_shift, end_of_shift):
    match select_error_type():
        case "IDEAL":
            return [start_of_shift, end_of_shift]
        case "MISSING":
            if is_it_the_starting_event() == True:
                return [end_of_shift]
            else:
                return [start_of_shift]
        case "DUPLICATE":
            if is_it_the_starting_event() == True:
                duplicated_event_time = start_of_shift["EventTime"] + timedelta(seconds=random.randrange(1,5))
                duplicated_event = {
                    "EmployeeID": start_of_shift["EmployeeID"],
                    "DeviceID": start_of_shift["DeviceID"],
                    "EventType": "IN",
                    "EventTime": duplicated_event_time
                }
                return [start_of_shift, duplicated_event, end_of_shift]
            else:
                duplicated_event_time = end_of_shift["EventTime"] + timedelta(seconds=random.randrange(1,5))
                duplicated_event = {
                    "EmployeeID": end_of_shift["EmployeeID"],
                    "DeviceID": end_of_shift["DeviceID"],
                    "EventType": "OUT",
                    "EventTime": duplicated_event_time
                }
                return [start_of_shift, end_of_shift, duplicated_event]
        case "SWAPPED":
            return [end_of_shift, start_of_shift]