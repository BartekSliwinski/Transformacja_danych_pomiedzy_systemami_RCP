import config
import pandas as pd
from validators.common import load_csv, validation_passed, display_results

def are_ids_unique(df):
    return df["EmployeeID"].is_unique

def is_there_right_amount_of_employees(df):
    return len(df) == config.NUM_OF_EMPLOYEES

def are_there_no_nulls(df):
    return not df.isnull().any().any()

def are_phone_numbers_unique(df):
    return df["PhoneNumber"].is_unique

def are_emails_unique(df):
    return df["Email"].is_unique

def hire_date_before_modified_date(df):
    return (df["HireDate"] <= df["ModifiedDate"]).all()

def hire_date_after_hiring_starting_date(df):
    return (df["HireDate"] >= config.HIRING_STARTING_DATE).all()

def right_status(df):
    return (df["Status"].isin(["Active", "Inactive"])).all()

def hire_date_before_simulation_end(df):
    return (df["HireDate"] <= config.SIMULATION_END_DATE).all()

def modified_date_before_simulation_end(df):
    return (df["ModifiedDate"] <= config.SIMULATION_END_DATE).all()

def position_id_exists_in_positions_csv(df):
    positions_df = load_csv("positions.csv")
    return df["PositionID"].isin(positions_df["PositionID"]).all()

def emails_contain_at_symbol(df):
    return (df["Email"].str.contains('@')).all()

def phone_number_is_9_digit_long(df):
    return (df["PhoneNumber"].astype(str).str.len() == 9).all()


def run_validations(df):
    validations = {
        "Employee IDs are unique": are_ids_unique(df),
        "Correct number of employees": is_there_right_amount_of_employees(df),
        "No null values": are_there_no_nulls(df),
        "Phone numbers are unique": are_phone_numbers_unique(df),
        "Emails are unique": are_emails_unique(df),
        "Hire date is before modified date": hire_date_before_modified_date(df),
        "Status values are correct": right_status(df),
        "Hire dates are before simulation end": hire_date_before_simulation_end(df),
        "Hire dates are after hiring starting date": hire_date_after_hiring_starting_date(df),
        "Modified dates are before simulation end": modified_date_before_simulation_end(df),
        "Position IDs exist in positions table": position_id_exists_in_positions_csv(df),
        "Emails contain @ symbol": emails_contain_at_symbol(df),
        "Phone numbers have 9 digits": phone_number_is_9_digit_long(df)
    }

    return validations

def validate_employees():
    name = "employees.csv"
    df = load_csv(name)
    results = run_validations(df)
    display_results(name, results)

def main():
    validate_employees()

if __name__ == "__main__":
    main()