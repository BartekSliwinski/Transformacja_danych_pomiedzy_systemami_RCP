import config
import pandas as pd
from validators.common import load_csv, validation_passed, display_results
from validators.employees import validate_employees
from validators.events import validate_events

def validate():
    validate_employees()
    validate_events()

if __name__ == "__main__":
    validate()