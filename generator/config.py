CSV_OUTPUT_DIRECTORY = "output"

RUN_VALIDATIONS = True

NUM_OF_EMPLOYEES = 500

HIRING_STARTING_DATE = "2020-01-01"

SIMULATION_START_DATE = "2025-01-01"
SIMULATION_END_DATE = "2026-12-31"

WORKING_HOURS_START = 6

SEED = 67

ACTIVE_EMPLOYEE_RATIO = 0.92


ADD_ERRORS = True
MISSING_EVENT_RATIO = 0.02
DUPLICATE_EVENT_RATIO = 0.01

OVERTIME_PROBABILITY = 0.15
SHIFT_DURATION_MEAN = 8
SHIFT_DURATION_STD = 0.05

POSITIONS_IN_DEPARTMENTS = {
    "IT": [
        "Data Engineer",
        "Data Analyst",
        "Software Developer",
        "DevOps Engineer",
        "QA Engineer",
        "System Administrator"
    ],

    "HR": [
        "HR Specialist",
        "Recruiter",
        "HR Coordinator",
        "HR Business Partner"
    ],

    "Finance": [
        "Accountant",
        "Financial Analyst",
        "Payroll Specialist",
    ],

    "Sales": [
        "Sales Representative",
        "Account Manager",
        "Sales Manager",
        "Business Development Specialist"
    ],

    "Marketing": [
        "Marketing Specialist",
        "Content Manager",
        "Copywriter",
        "SEO Specialist",
        "Graphic Designer"
    ],

    "Production": [
        "Production Operator",
        "Shift Supervisor",
        "Production Planner",
        "Quality Control Specialist"
    ],

    "Warehouse": [
        "Warehouse Worker",
        "Forklift Operator",
        "Logistics Coordinator",
        "Inventory Specialist"
    ],

    "Support": [
        "Customer Support Specialist",
        "Technical Support Engineer",
        "Service Desk Agent",
        "Support Team Lead"
    ]
}
NUM_OF_DEPARTMENTS = len(POSITIONS_IN_DEPARTMENTS)
NUM_OF_POSITIONS = sum(len(dep) for dep in POSITIONS_IN_DEPARTMENTS.values())

DEVICES = [
    "MAIN01", "MAIN02", "MAIN03",
    "SERVICE01", 
    "WAREHOUSE01",
    "PRODUCTION01", "PRODUCTION02"
]
NUM_OF_DEVICES = len(DEVICES)

DEPARTMENT_DEVICES = {
    "IT": [1, 2],
    "HR": [1],
    "Finance": [1, 3],
    "Sales": [2, 3],
    "Marketing": [2],
    "Production": [6, 7],
    "Warehouse": [5],
    "Support": [4, 3]
}