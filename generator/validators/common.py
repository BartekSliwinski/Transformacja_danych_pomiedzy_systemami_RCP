import config
import pandas as pd
from pathlib import Path

def load_csv(name):
    path = Path(config.CSV_OUTPUT_DIRECTORY) / name

    date_columns = {
        "employees.csv": ["HireDate", "ModifiedDate"],
        "events.csv": ["EventTime"]
    }

    return pd.read_csv(
        path,
        parse_dates=date_columns.get(name, [])
    )

def validation_passed(results):
    return all(results.values())

def display_results(filename, results):
    width = 35
    print("=" * width)
    print(f"Validating: {filename}...")
    print("=" * width)
    for name, result in results.items():
        
        print(f"{'🟢' if result else '🔴'}: {name}" )
    print("-" * width)
    print(f"Validation result: {"PASSED" if validation_passed(results) else "FAILED"}")
    print("\n")
    