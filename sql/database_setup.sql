-- ==========================================================
-- PROJECT RISK ANALYTICS DATABASE SCHEMA
-- Purpose: To store and pre-analyze industrial project tasks
-- Author: Anil Urkmez (PMP, Six Sigma Black Belt)
-- ==========================================================

CREATE TABLE ProjectTasks (
    task_id INT PRIMARY KEY,
    task_name VARCHAR(255) NOT NULL,
    category VARCHAR(50),
    planned_days INT NOT NULL,
    optimistic_days INT NOT NULL,
    pessimistic_days INT NOT NULL,
    risk_factor FLOAT DEFAULT 0.0,
    stakeholder_complexity INT CHECK (stakeholder_complexity BETWEEN 1 AND 5),
    cost_impact_euro DECIMAL(15, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO ProjectTasks (task_id, task_name, category, planned_days, optimistic_days, pessimistic_days, risk_factor, stakeholder_complexity, cost_impact_euro)
VALUES 
(1, 'Production Line Transfer - Egypt', 'Manufacturing', 45, 40, 75, 0.6, 5, 2000000.00),
(2, 'Vendor Selection & Negotiation', 'Procurement', 20, 15, 35, 0.4, 4, 500000.00),
(3, 'ISO 9001 Audit Preparation', 'Quality', 15, 12, 25, 0.2, 2, 50000.00),
(4, 'IT Infrastructure Setup', 'IT', 30, 25, 55, 0.5, 3, 150000.00),
(5, 'Greenfield Factory Foundation', 'Construction', 60, 55, 90, 0.7, 5, 5000000.00);

CREATE VIEW View_Critical_Path_Analysis AS
SELECT 
    task_name,
    planned_days,
    (optimistic_days + (4 * planned_days) + pessimistic_days) / 6 AS pert_expected_duration,
    CASE 
        WHEN stakeholder_complexity >= 4 THEN 'High Stakeholder Management Required'
        ELSE 'Standard Management'
    END AS management_strategy
FROM ProjectTasks
WHERE risk_factor > 0.5;
