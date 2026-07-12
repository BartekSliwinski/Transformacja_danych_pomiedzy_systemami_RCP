import config
import pandas as pd
from pathlib import Path

REPORT_FILENAME = "execution_history.csv"
REPORT_PATH = Path("reports") / "execution_history.csv"

def generate_report_entry(execution_time_seconds,memory_usage_mb, generated_events_count, output_size_mb):
    execution_date = pd.Timestamp.now().floor('s')
    employees_count = config.NUM_OF_EMPLOYEES
    simulation_start_date = config.SIMULATION_START_DATE
    simulation_end_date = config.SIMULATION_END_DATE
    simulation_years = pd.Timestamp(simulation_end_date).year - pd.Timestamp(simulation_start_date).year + 1
    seed = config.SEED

    report_data = {
        "Execution_Date": execution_date,
        "Employees": employees_count,
        "Simulation_Start": simulation_start_date,
        "Simulation_End": simulation_end_date,
        "Simulation_Years": simulation_years,
        "Seed": seed,
        "Execution_Time": round(execution_time_seconds, 2),
        "Memory_Usage_In_MB": round(memory_usage_mb,2),
        "Generated_Events_Count": generated_events_count,
        "Output_Size_In_MB": round(output_size_mb,2)
    }
    save_execution_report(report_data)

def save_execution_report(report_data):
    df = pd.DataFrame([report_data])
    plik_istnieje = REPORT_PATH.exists()
    df.to_csv(REPORT_PATH, mode='a', index=False, header= not plik_istnieje)