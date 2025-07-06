import pandas as pd
import numpy as np
import random
from datetime import timedelta

# Define static value pools
condition_map = {
    "Stroke": "ICU", "Heart Failure": "ICU", "Fracture": "Orthopedics",
    "Asthma": "Pediatrics", "COPD": "Pulmonology", "Diabetes": "Endocrinology",
    "Pregnancy": "Obstetrics", "Alzheimer's": "Geriatrics", "Infection": "General Medicine",
    "Appendicitis": "Surgery"
}
discharge_outcomes = ["Home", "Transferred to Rehab", "Expired"]
insurance_types = ["Private", "Medicare", "Medicaid", "Uninsured"]

def get_age_group(age):
    if age <= 12: return "0-12"
    elif age <= 24: return "13-24"
    elif age <= 40: return "25-40"
    elif age <= 60: return "41-60"
    else: return "61+"

def get_severity(condition, age):
    base = {
        "Stroke": 8, "Heart Failure": 8, "Fracture": 4,
        "Asthma": 3, "COPD": 6, "Diabetes": 5,
        "Pregnancy": 3, "Alzheimer's": 7, "Infection": 5, "Appendicitis": 6
    }[condition]
    noise = np.random.randint(-2, 2)
    age_adj = 1 if age >= 70 else 0
    return int(np.clip(base + noise + age_adj, 1, 10))

def get_length_of_stay(severity, department):
    base = severity + np.random.randint(0, 4)
    dept_mod = 3 if department == "ICU" else (1 if department == "Pediatrics" else 2)
    return int(np.clip(base + dept_mod, 1, 30))

def get_discharge_status(severity, age):
    if severity >= 9 and age >= 75:
        return "Expired"
    elif severity >= 7:
        return random.choices(["Transferred to Rehab", "Home"], weights=[0.7, 0.3])[0]
    return "Home"

def get_readmission(severity, los):
    return "Yes" if severity >= 7 and los >= 7 and random.random() < 0.5 else "No"

def get_insurance(age):
    if age >= 65:
        return "Medicare"
    return random.choices(insurance_types, weights=[0.5, 0.1, 0.3, 0.1])[0]

def generate_notes(condition, outcome):
    templates = [
        "Patient treated for {condition}. Discharge outcome: {outcome}.",
        "Clinical course involved {condition}; patient was {outcome.lower()}.",
        "{condition} managed during admission; status: {outcome}.",
        "{outcome} following treatment for {condition}.",
        "Patient case: {condition}. Final status: {outcome}."
    ]
    return random.choice(templates).format(condition=condition, outcome=outcome)

# Dataset generator
def generate_patient_dataset(n=500, seed=42):
    random.seed(seed)
    np.random.seed(seed)

    data = []
    for i in range(1, n + 1):
        pid = i
        age = np.random.randint(0, 95)
        age_group = get_age_group(age)
        gender = random.choice(["Male", "Female", "Other"])
        condition = random.choice(list(condition_map.keys()))
        department = condition_map[condition]
        severity = get_severity(condition, age)
        length_of_stay = get_length_of_stay(severity, department)
        admission_date = pd.to_datetime("2023-01-01") + pd.to_timedelta(np.random.randint(0, 365), unit="days")
        discharge_date = admission_date + timedelta(days=length_of_stay)
        discharge_status = get_discharge_status(severity, age)
        readmission = get_readmission(severity, length_of_stay)
        insurance = get_insurance(age)
        notes = generate_notes(condition, discharge_status)

        data.append([
            pid, admission_date.date(), discharge_date.date(), age, age_group, gender,
            condition, department, severity, length_of_stay, insurance,
            discharge_status, readmission, notes
        ])

    columns = [
        "Patient_ID", "Admission_Date", "Discharge_Date", "Age", "Age_Group", "Gender",
        "Condition_Type", "Department", "Severity_Score", "Length_of_Stay", "Insurance_Type",
        "Discharge_Status", "Readmission_Within_30_Days", "Clinical_Notes"
    ]
    return pd.DataFrame(data, columns=columns)

# Example usage:
df = generate_patient_dataset()
df.to_csv("improved_hospital_patient_dataset.csv", index=False)
