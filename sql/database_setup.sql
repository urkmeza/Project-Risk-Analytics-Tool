## Project Tasks and Risk Factors Table 
CREATE TABLE ProjectTasks (
    TaskID INT PRIMARY KEY,
    TaskName VARCHAR(100),
    PlannedDays INT,
    OptimisticDays INT, ## Best case
    PessimisticDays INT, ## Worst case
    RiskFactor FLOAT, ##  0.1 to 1.0 (Side effects, supplier risks etc.)
    [cite_start]StakeholderComplexity INT ## 1 to 5 
);

## Data entery sample (EG: Factory establishment in EG
INSERT INTO ProjectTasks VALUES (1, 'Production Line Transfer', 45, 40, 65, 0.4, 5);
INSERT INTO ProjectTasks VALUES (2, 'Tool Installation', 30, 25, 45, 0.2, 3);
