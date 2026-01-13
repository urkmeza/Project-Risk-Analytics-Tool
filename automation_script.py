import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os

def calculate_pert_and_risk(planned, optimistic, pessimistic, risk_factor, complexity):
    """
    Applies PERT methodology and risk weighting logic.
    """
    expected_duration = (optimistic + (4 * planned) + pessimistic) / 6
    base_risk = expected_duration / planned
    weighted_risk = base_risk * (1 + (risk_factor * (complexity / 5)))
    return round(weighted_risk, 2)

def generate_visualizations(df):
    """
    Creates professional charts for stakeholders to visualize risks.
    """
    print("Generating risk visualization charts...")
    
    # Set the style
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))
    
    # Define colors based on status (Red for Critical, Green for Stable)
    palette = {"CRITICAL": "#e74c3c", "STABLE": "#2ecc71"}
    
    # Create a bar plot
    ax = sns.barplot(
        x="Risk_Score", 
        y="TaskName", 
        hue="Status", 
        data=df.sort_values("Risk_Score", ascending=False),
        palette=palette
    )
    
    # Add a vertical line for the critical threshold (1.3)
    plt.axvline(x=1.3, color='black', linestyle='--', label='Critical Threshold')
    
    plt.title(f"Project Risk Assessment Matrix - {datetime.now().strftime('%Y-%m-%d')}", fontsize=15)
    plt.xlabel("Calculated Risk Score", fontsize=12)
    plt.ylabel("Project Task / Milestone", fontsize=12)
    plt.legend(title="Risk Level")
    
    # Save the chart as an image for the report/GitHub README
    plt.tight_layout()
    chart_filename = "Project_Risk_Visual.png"
    plt.savefig(chart_filename)
    print(f"Success: Chart saved as {chart_filename}")
    plt.close()

def run_automation(input_file):
    # 1. Data Loading
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return

    df = pd.read_csv(input_file)
    
    # 2. Analysis Logic
    df['Risk_Score'] = df.apply(lambda x: calculate_pert_and_risk(
        x['PlannedDays'], x['OptimisticDays'], x['PessimisticDays'], 
        x['RiskFactor'], x['Complexity']), axis=1)

    df['Status'] = np.where(df['Risk_Score'] > 1.3, 'CRITICAL', 'STABLE')

    # 3. Generating Visualization
    generate_visualizations(df)

    # 4. Automated Export
    today = datetime.now().strftime('%Y-%m-%d')
    output_filename = f"Project_Risk_Report_{today}.csv"
    df.to_csv(output_filename, index=False)
    
    print(f"Analysis Complete! Report: {output_filename}")

if __name__ == "__main__":
    run_automation('input_projects.csv')
