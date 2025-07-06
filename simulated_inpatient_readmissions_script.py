import pandas as pd
import numpy as np
import random

def generate_simulated_inpatient_data(num_rows=10000, seed=42):
    np.random.seed(seed)
    random.seed(seed)

    genders = ['Female', 'Other', 'Male']
    diagnosis_codes = ['F32.9', 'I50.9', 'M54.5', 'E11.9', 'R07.9', 'J44.9', 'I10']

    data = []

    for i in range(num_rows):
        patient_id = f"P{i:05d}"
        age = np.random.randint(18, 90)
        gender = np.random.choice(genders, p=[0.338, 0.332, 0.33])
        diagnosis = np.random.choice(diagnosis_codes)
        lab_abnormalities = np.random.poisson(2.5)
        lab_abnormalities = min(max(lab_abnormalities, 0), 10)
        length_of_stay = np.random.randint(1, 15)
        num_procedures = np.random.randint(0, 5)

        # Risk score based on weighted sum of other features, scaled between 0 and 1
        raw_risk = (
            0.3 * (age / 89) +
            0.2 * (lab_abnormalities / 10) +
            0.3 * (length_of_stay / 14) +
            0.2 * (num_procedures / 4)
        )
        risk_score = np.clip(raw_risk + np.random.normal(0, 0.05), 0, 1)

        # Readmission based on risk score: higher risk = higher chance
        readmission_prob = 0.3 + 0.6 * risk_score  # Between 0.3 and 0.9
        readmission = np.random.rand() < readmission_prob
        readmission_flag = 'Yes' if readmission else 'No'

        data.append([
            patient_id, age, gender, diagnosis,
            lab_abnormalities, length_of_stay, num_procedures,
            round(risk_score, 6), readmission_flag
        ])

    columns = [
        'Patient_ID', 'Age', 'Gender', 'Diagnosis_Code',
        'Lab_Abnormalities', 'Length_of_Stay', 'Number_of_Procedures',
        'Risk_Score', 'Readmission_Within_30_Days'
    ]

    return pd.DataFrame(data, columns=columns)

# Example usage:
df_simulated = generate_simulated_inpatient_data()
df_simulated.to_csv("simulated_inpatient_dataset.csv", index=False)
