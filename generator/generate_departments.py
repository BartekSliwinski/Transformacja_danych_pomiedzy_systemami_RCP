import config
import pandas as pd
import numpy as np

DEPARTMENTS = [
    "IT", "HR", "Marketing", "Finance", 
    "Sales", "Production", "Warehouse", "Support"
]


def check_number_of_departments():
    if len(DEPARTMENTS) != config.NUM_OF_DEPARTMENTS:
        raise ValueError(
            f"Config mismatch: expected {config.NUM_OF_DEPARTMENTS}, got {len(DEPARTMENTS)}."
        )

def generate_departments():
    np.random.seed(config.SEED)

    df = pd.DataFrame({
        "DepartmentID": range(1, len(DEPARTMENTS)+1),
        "DepartmentName": DEPARTMENTS
    })

    return df

if __name__ == "__main__":
    check_number_of_departments()
    df = generate_departments()
    print(df)
    df.to_csv("output/departments.csv", index=False)