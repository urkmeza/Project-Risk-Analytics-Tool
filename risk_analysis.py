import pandas as pd
import numpy as np
from datetime import datetime
import os

def calculate_pert_and_risk(planned, optimistic, pessimistic, risk_factor, complexity):

    # Calculate PERT expected duration
    expected_duration = (optimistic + (4 * planned) + pessimistic) / 6
    
    # Calculate risk score based on duration variance and stakeholder complexity
    
    base_risk = expected_duration / planned
    weighted_risk = base_risk * (1 + (risk_factor * (complexity / 5)))
    
    return round(weighted_risk, 2)

def run_automation(input_file):
    # 1. Load the input data
    if not os.path.exists(input_file):
        print(f"Error: The file '{input_file}' was not found.")
        return

    print(f"Loading data from {input_file}...")
    df = pd.read_csv(input_file)
    print(f"Success: {len(df)} tasks loaded. Starting analysis...")

    # 2. Automated Risk Analysis
    # Applying the logic to each row in the dataframe
    df['Risk_Score'] = df.apply(lambda x: calculate_pert_and_risk(
        x['PlannedDays'], x['OptimisticDays'], x['PessimisticDays'], 
        x['RiskFactor'], x['Complexity']), axis=1)

    # Assigning status based on risk thresholds
    df['Status'] = np.where(df['Risk_Score'] > 1.3, 'CRITICAL', 'STABLE')

    # 3. Exporting Results (Automated Reporting)
    # Generate a filename with the current date
    today = datetime.now().strftime('%Y-%m-%d')
    output_filename = f"Project_Risk_Report_{today}.csv"
    df.to_csv(output_filename, index=False)
    
    print("-" * 30)
    print(f"Analysis Complete!")
    print(f"Report Generated: {output_filename}")
    print("-" * 30)
    
    # Print a summary of critical tasks for the user
    critical_tasks = df[df['Status'] == 'CRITICAL']
    if not critical_tasks.empty:
        print(f"ALERT: Found {len(critical_tasks)} critical tasks that require attention.")
    else:
        print("All tasks are currently within stable risk limits.")

if __name__ == "__main__":
    # Ensure the 'input_projects.csv' file exists in the same directory
    run_automation('input_projects.csv')
