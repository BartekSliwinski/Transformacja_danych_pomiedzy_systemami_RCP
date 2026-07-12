import config
import pandas as pd
from validators.common import load_csv, validation_passed, display_results

def are_ids_unique(df):
    return df["EventID"].is_unique

def are_there_no_nulls(df):
    return not df.isnull().any().any()


def event_time_after_simulation_start_date(df):
    return (df["EventTime"].dt.date >= pd.to_datetime(config.SIMULATION_START_DATE).date()).all()

def event_time_before_simulation_end_date(df):
    return (df["EventTime"].dt.date <= pd.to_datetime(config.SIMULATION_END_DATE).date()).all()

def event_time_hour_after_working_hours_start(df):
    return (df["EventTime"].dt.hour >= config.WORKING_HOURS_START).all()

def right_event_type(df):
    return df["EventType"].isin(["IN", "OUT"]).all()

def employee_id_exists_in_employees_csv(df):
    employees_df = load_csv("employees.csv")
    return df["EmployeeID"].isin(employees_df["EmployeeID"]).all()

def device_id_exists_in_device_csv(df):
    device_df = load_csv("devices.csv")
    return df["DeviceID"].isin(device_df["DeviceID"]).all()

def events_are_sorted(df):
    return df["EventTime"].is_monotonic_increasing

def out_is_after_in(df):
    grouped = df.sort_values("EventTime").groupby(
        ["EmployeeID"]
    )

    for _, employee_events in grouped:
        last_event = None

        for event in employee_events["EventType"]:
            if event == "IN":
                last_event = "IN"

            elif event == "OUT":
                if last_event != "IN":
                    return False
                last_event = "OUT"

    return True

def employees_have_even_number_of_events(df):
    events_per_employee = df.groupby("EmployeeID").size()
    return (events_per_employee % 2 == 0).all()

def run_validations(df):
    validations = {
        "Event IDs are unique": are_ids_unique(df),
        "No null values": are_there_no_nulls(df),
        "Events are after simulation start date": event_time_after_simulation_start_date(df),
        "Events are before simulation end date": event_time_before_simulation_end_date(df),
        "Event types are correct": right_event_type(df),
        "Employee IDs exist in employees table": employee_id_exists_in_employees_csv(df),
        "Device IDs exist in devices table": device_id_exists_in_device_csv(df),
        "Events are sorted by time": events_are_sorted(df),
        "OUT events happen after IN events": out_is_after_in(df),
        "Employees have even number of events": employees_have_even_number_of_events(df),
    }

    return validations

def validate_events():
    name = "events.csv"
    df = load_csv(name)
    results = run_validations(df)
    display_results(name, results)

def main():
    validate_events()

if __name__ == "__main__":
    main()
