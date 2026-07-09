import config
import pandas as pd
from datetime import datetime, timedelta
import holidays
import random
from generators.employees import generate_employees
from generators.positions import generate_positions
from generators.departments import generate_departments
from generators.devices import generate_devices
from errors.worklog_errors import get_worklogs_errors

random.seed(config.SEED)

def get_working_days():
    pl_holidays = holidays.country_holidays('PL', years=[2025, 2026]) #WAŻNE Do poprawy: zmienić na dynamiczny zakres lat
    custom_pl_business_day = pd.offsets.CustomBusinessDay(holidays=list(pl_holidays.keys()))

    working_days = pd.date_range(start=config.SIMULATION_START_DATE, end=config.SIMULATION_END_DATE, freq=custom_pl_business_day)
   
    return working_days

def create_employee_devices_lookup(employees_df, positions_df, departments_df):
    employee_positions = positions_df.merge(employees_df, on="PositionID", how="left")
    employee_departments = departments_df.merge(employee_positions, on="DepartmentID", how="left")
    employee_departments.sort_values(["EmployeeID"], inplace=True)

    employee_in_department = dict(zip(employee_departments["EmployeeID"], employee_departments["DepartmentName"]))
    employee_devices = {}
    for employee_id, dept_name in employee_in_department.items():
        employee_devices[employee_id] = config.DEPARTMENT_DEVICES.get(dept_name, ["MAIN01", "MAIN02", "MAIN03"])
    return employee_devices


def get_start_offset():
    seconds = random.randint(0, 14400)
    return seconds

def get_shift_duration():
    shift_duration = random.gauss(config.SHIFT_DURATION_MEAN, config.SHIFT_DURATION_STD)
    return shift_duration

def get_overtime_minutes():
    overtime = 0
    if random.random() < config.OVERTIME_PROBABILITY:
        value = random.gauss(60, 15)
        overtime = max(1, min(value, 120))
    return overtime


def generate_worklogs(employees_df, positions_df, departments_df):
    employee_devices_lookup = create_employee_devices_lookup(employees_df, positions_df, departments_df)
    
    days = get_working_days()
    rows = []
    for day in days:
        employees_that_worked_that_day = employees_df[(employees_df["HireDate"] <= day) & ((employees_df["Status"] == "Active") | (employees_df["ModifiedDate"] > day))]
        active_ids = employees_that_worked_that_day["EmployeeID"].to_list()

        for employee_id in active_ids:
            starting_time = day + timedelta(hours=config.WORKING_HOURS_START)+ timedelta(seconds=get_start_offset())
            device = random.choice(list(employee_devices_lookup[employee_id]))

            start_of_shift = {
                "EmployeeID": employee_id,
                "DeviceID": device,
                "EventType": "IN",
                "EventTime": starting_time
            }
            end_of_shift = {
                "EmployeeID": employee_id,
                "DeviceID": device,
                "EventType": "OUT",
                "EventTime": (
                    starting_time + 
                    timedelta(hours=round(get_shift_duration(), 2)) +
                    timedelta(minutes=get_overtime_minutes())
                )
            }
            events = get_worklogs_errors(start_of_shift, end_of_shift)
            rows.extend(events)

    df = pd.DataFrame(rows)
    df = df.sort_values(by=["EventTime"], ascending=True)
    df.insert(0, "WorkLogID", range(1, len(df)+1))
    return df
    

def main():
    departments_df = generate_departments()
    positions_df = generate_positions(departments_df)
    employees_df = generate_employees(positions_df)

    df = generate_worklogs(employees_df, positions_df, departments_df)
    print(df)
    df.to_csv(f"{config.CSV_OUTPUT_DIRECTORY}/worklogs.csv", index=False)

if __name__ == "__main__":
    main()
