import config
import os
import time
import psutil
from generators.employees import generate_employees
from generators.positions import generate_positions
from generators.departments import generate_departments
from generators.devices import generate_devices
from generators.events import generate_events
from reports.execution_report import generate_report_entry
from validators.main import validate

os.makedirs(config.CSV_OUTPUT_DIRECTORY, exist_ok=True)


def save_dataframe(df, filename, start_time, current_total_size):
    path = f"{config.CSV_OUTPUT_DIRECTORY}/{filename}.csv"

    df.to_csv(path, index=False)

    elapsed_time = time.perf_counter() - start_time
    file_size_mb = os.path.getsize(path) / (1024 * 1024)
    new_total_size = current_total_size + file_size_mb
    df_len = len(df)
    print(
        f"✓ {filename}.csv: "
        f"{df_len} records "
        f"({elapsed_time:.3f}s, {file_size_mb:.2f} MB)"
    )
    
    if filename == "events":
        return new_total_size, df_len
    return new_total_size, None


def main():
    print("Starting data generation...\n")

    total_file_size = 0.0
    total_start = time.perf_counter()

    step_start = time.perf_counter()
    device_df = generate_devices()
    total_file_size, _ = save_dataframe(device_df, "devices", step_start, total_file_size)

    step_start = time.perf_counter()
    departments_df = generate_departments()
    total_file_size, _ = save_dataframe(departments_df, "departments", step_start, total_file_size)

    step_start = time.perf_counter()
    positions_df = generate_positions(departments_df)
    total_file_size, _ = save_dataframe(positions_df, "positions", step_start, total_file_size)

    step_start = time.perf_counter()
    employees_df = generate_employees(positions_df)
    total_file_size, _ = save_dataframe(employees_df, "employees", step_start, total_file_size)

    step_start = time.perf_counter()
    events_df = generate_events(
        employees_df,
        positions_df,
        departments_df
    )
    total_file_size, generated_events_count = save_dataframe(events_df, "events", step_start, total_file_size)

    total_time = time.perf_counter() - total_start

    print(f"\nGeneration completed in {total_time:.3f}s")
    process = psutil.Process(os.getpid())
    memory_usage_mb = process.memory_info().rss / 1024 / 1024
    generate_report_entry(total_time, memory_usage_mb, generated_events_count, total_file_size)
    if config.RUN_VALIDATIONS:
        validate()

if __name__ == "__main__":
    main()