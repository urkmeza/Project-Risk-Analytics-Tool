import pandas as pd
import numpy as np


# Apply PERT analysis (PMP) and specific risk scoring methodology.

def calculate_pert_and_risk(planned, optimistic, pessimistic, risk_factor, complexity):
    
    
    # PERT Formula: 
    
    expected_duration = (optimistic + (4 * most likely) + pessimistic) / 6
    
    # Risk Score: A combination of time variance, stakeholder complexity, and external risks. 
    # Designed based on 30+ stakeholder management experiences.
    
    base_risk = expected_duration / planned
    weighted_risk = base_risk * (1 + (risk_factor * (complexity / 5)))
    
    return round(weighted_risk, 2)

# Sample Project Data (Inspired by large-scale projects like the Egypt Factory Project)
data = {
    'TaskName': ['Production Line Transfer', 'Vendor Selection', 'Tool Installation', 'ISO Audit Preparation'],
    'PlannedDays': [45, 20, 30, 15],
    'OptimisticDays': [40, 15, 25, 12],
    'PessimisticDays': [70, 40, 50, 25],
    'RiskFactor': [0.6, 0.4, 0.3, 0.2],  # Vendor and installation risks
    'Complexity': [5, 4, 3, 2] # [cite: 15] # Stakeholder complexity level
}

df = pd.DataFrame(data)

# Apply risk analysis
df['Risk_Score'] = df.apply(lambda x: calculate_pert_and_risk(
    x['PlannedDays'], x['OptimisticDays'], x['PessimisticDays'], 
    x['RiskFactor'], x['Complexity']), axis=1)

# Determine the criticality level.
df['Status'] = np.where(df['Risk_Score'] > 1.3, 'CRITICAL', 'STABLE')

print("--- Project Risk Analysis Report ---")
print(df[['TaskName', 'Risk_Score', 'Status']].sort_values(by='Risk_Score', ascending=False))
