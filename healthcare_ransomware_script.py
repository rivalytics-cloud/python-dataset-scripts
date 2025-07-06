import pandas as pd
import numpy as np
import random

def generate_ransomware_dataset(n=5000, seed=42):
    np.random.seed(seed)
    random.seed(seed)

    org_types = ['Hospital', 'Clinic', 'Insurance', 'Pharma', 'Research Lab']
    org_type_probs = [0.4066, 0.2994, 0.104, 0.0958, 0.0942]

    org_sizes = ['Medium', 'Large', 'Small']
    org_size_probs = [0.5598, 0.2422, 0.198]

    threats = ['1-50', '50-350', '350+']
    threat_probs = [0.405, 0.4024, 0.1926]

    monitoring_freqs = ['Daily', 'Weekly', 'Monthly', 'More than once per day']
    monitoring_probs = [0.3996, 0.3006, 0.1514, 0.1484]

    entry_methods = [
        'Compromised Credentials', 'Exploited Vulnerability',
        'Phishing Email', 'RDP Exploit',
        'Malicious Website', 'Infected Removable Media'
    ]
    entry_probs = [0.3538, 0.3322, 0.1888, 0.0802, 0.0256, 0.0194]

    data = []
    for i in range(n):
        incident_id = f"RAN2024{i+1:05d}"
        attack_date = pd.Timestamp('2024-01-01') + pd.to_timedelta(np.random.randint(0, 365), unit='days')

        org_type = np.random.choice(org_types, p=org_type_probs)
        org_size = np.random.choice(org_sizes, p=org_size_probs)
        facilities_affected = np.random.randint(1, 25)

        threat_level = np.random.choice(threats, p=threat_probs)
        monitoring_freq = np.random.choice(monitoring_freqs, p=monitoring_probs)
        entry_method = np.random.choice(entry_methods, p=entry_probs)

        backup_compromised = np.random.rand() < 0.64
        data_encrypted = np.random.rand() < 0.85
        data_stolen = np.random.rand() < 0.23
        paid_ransom = np.random.rand() < 0.49

        infection_rate = np.random.normal(loc=60, scale=15)
        infection_rate = np.clip(infection_rate, 11.2, 90.0)

        base_recovery = 30 + (20 if backup_compromised else -10) + np.random.normal(0, 10)
        recovery_time = int(np.clip(base_recovery, 2, 120))

        base_restore = 50
        if paid_ransom:
            base_restore += 15
        if not backup_compromised:
            base_restore += 10
        base_restore += np.random.normal(0, 10)
        data_restored = round(np.clip(base_restore, 0, 91.13), 2)

        ransomware_incidents = np.random.poisson(lam=2.5)
        ransomware_incidents = int(np.clip(ransomware_incidents, 1, 7))

        data.append([
            incident_id, attack_date, org_type, org_size, facilities_affected,
            threat_level, monitoring_freq, backup_compromised, round(infection_rate, 2),
            data_encrypted, data_stolen, recovery_time, entry_method,
            paid_ransom, data_restored, ransomware_incidents
        ])

    columns = [
        'id', 'attack_date', 'org_type', 'org_size', 'facilities_affected',
        'cyber_threats_tracked', 'monitoring_freq', 'backup_compromised',
        'ransomware_infection_rate_(%)', 'data_encrypted', 'data_stolen',
        'recovery_time_(days)', 'entry_method', 'paid_ransom',
        'data_restored', 'ransomware_incidents'
    ]
    return pd.DataFrame(data, columns=columns)

# Example usage
df = generate_ransomware_dataset()
df.to_csv("simulated_healthcare_ransomware_dataset.csv", index=False)
