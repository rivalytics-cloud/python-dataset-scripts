import random
import pandas as pd
import numpy as np

# 1. Define static value pools
ROLES = [
    "ICU Nurse", "ER Nurse", "Pediatric Nurse",
    "Resident Physician", "Surgeon", "General Practitioner",
    "Outpatient Medical Assistant", "Inpatient Medical Assistant",
    "Radiology Technician", "Surgical Technician",
    "Mental Health Therapist", "Physical Rehab Therapist",
    "Admin - HR", "Admin - Finance", "Admin - Scheduling"
]

DEPARTMENTS = {
    "ICU Nurse": "ICU", "ER Nurse": "Emergency", "Pediatric Nurse": "Pediatrics",
    "Resident Physician": "General Medicine", "Surgeon": "Surgery",
    "General Practitioner": "Internal Medicine",
    "Outpatient Medical Assistant": "Outpatient Clinic",
    "Inpatient Medical Assistant": "Inpatient Care",
    "Radiology Technician": "Radiology",
    "Surgical Technician": "Operating Room",
    "Mental Health Therapist": "Behavioral Health",
    "Physical Rehab Therapist": "Physical Therapy",
    "Admin - HR": "Administration",
    "Admin - Finance": "Administration",
    "Admin - Scheduling": "Administration"
}

SHIFT_TYPES = ["Day", "Night", "Rotating"]
EAP_ACCESS_OPTIONS = ["Yes", "No"]

WORKPLACE_FACTORS = {
    "Workload": ["Heavy Workload", "Understaffing", "Poor Shift Coverage"],
    "Emotional": ["Secondary Trauma", "Emotional Strain"],
    "Systemic": ["Career Stagnation", "Lack of Autonomy", "Poor Communication"],
    "Interpersonal": ["Low Recognition", "Bullying", "Management Conflict"]
}

FACTOR_SEVERITY = {
    "Heavy Workload": 3, "Understaffing": 2, "Poor Shift Coverage": 1,
    "Secondary Trauma": 3, "Emotional Strain": 2,
    "Career Stagnation": 2, "Lack of Autonomy": 1, "Poor Communication": 2,
    "Low Recognition": 1, "Bullying": 3, "Management Conflict": 2
}

# 2. Define logic functions
def get_burnout_label(stress_level):
    if stress_level <= 4:
        return "Never"
    elif 5 <= stress_level <= 7:
        return "Occasionally"
    return "Often"

def get_job_satisfaction(burnout):
    return random.randint(*{
        "Never": (4, 5),
        "Occasionally": (2, 4),
        "Often": (1, 3)
    }[burnout])

def get_turnover_intent(stress, satisfaction):
    if stress >= 8 and satisfaction <= 2:
        return "Yes"
    return random.choices(["No", "Yes"], weights=[0.8, 0.2])[0]

def get_mh_absences(eap, stress):
    if eap == "Yes":
        return int(np.clip(np.random.poisson(1.5) + (10 - stress), 0, 15))
    else:
        return int(np.clip(np.random.poisson(3.5) + stress, 0, 30))

def generate_notes(factors):
    templates = [
        "Reported challenges with {factor}.",
        "Ongoing issues around {factor} noted.",
        "Frequent stress due to {factor}.",
        "Voiced concerns regarding {factor}.",
        "No formal complaint, but signs of {factor} present."
    ]
    return random.choice(templates).format(factor=random.choice(factors))

# 3. Generate dataset
def generate_healthcare_mental_health_dataset(n=5000, seed=42):
    random.seed(seed)
    np.random.seed(seed)
    data = []

    for i in range(1, n + 1):
        emp_id = f"HCP-{i:05d}"
        role = random.choice(ROLES)
        dept = DEPARTMENTS[role]
        shift = random.choice(SHIFT_TYPES)
        experience = round(np.random.uniform(0.5, 25), 1)
        eap = random.choices(EAP_ACCESS_OPTIONS, weights=[0.7, 0.3])[0]

        # Choose 2–3 stressors
        factor_pool = [random.choice(v) for k, v in random.sample(list(WORKPLACE_FACTORS.items()), 3)]
        stress = int(np.clip(sum(FACTOR_SEVERITY[f] for f in factor_pool) + random.randint(0, 3), 1, 10))

        burnout = get_burnout_label(stress)
        satisfaction = get_job_satisfaction(burnout)
        turnover = get_turnover_intent(stress, satisfaction)
        absences = get_mh_absences(eap, stress)
        note = generate_notes(factor_pool)

        data.append([
            emp_id, role, dept, shift, experience,
            ", ".join(factor_pool), stress, burnout,
            satisfaction, eap, absences, turnover, note
        ])

    columns = [
        "Employee ID", "Employee Role", "Department", "Shift Type", "Years of Experience",
        "Workplace Factors", "Stress Level", "Burnout Frequency", "Job Satisfaction",
        "Access to EAPs", "Mental Health Absences", "Turnover Intention", "Notes"
    ]

    return pd.DataFrame(data, columns=columns)

# 4. Export
df = generate_healthcare_mental_health_dataset()
df.to_csv("healthcare_workforce_mental_health.csv", index=False)
