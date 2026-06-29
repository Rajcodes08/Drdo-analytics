from pathlib import Path

import duckdb
import pandas as pd

# Project Paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATABASE_FILE = PROJECT_ROOT / "data" / "processed" / "drdo.duckdb"
OUTPUT_DIR = PROJECT_ROOT / "outputs" / "reports"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Connect to DuckDB
conn = duckdb.connect(DATABASE_FILE)

# -------------------------------
# Query 1 - Total Employees
# -------------------------------
total_employees = conn.execute("""
SELECT COUNT(*) AS TotalEmployees
FROM Employees;
""").fetchdf()

print("\n===== Total Employees =====")
print(total_employees)

total_employees.to_csv(
    OUTPUT_DIR / "total_employees.csv",
    index=False
)

# -------------------------------
# Query 2 - Employee Count by Gender
# -------------------------------
gender_count = conn.execute("""
SELECT
    Gender,
    COUNT(*) AS EmployeeCount
FROM Employees
GROUP BY Gender
ORDER BY EmployeeCount DESC;
""").fetchdf()

print("\n===== Employee Count by Gender =====")
print(gender_count)

gender_count.to_csv(
    OUTPUT_DIR / "employee_count_by_gender.csv",
    index=False
)

# -------------------------------
# Query 3 - Average Age by Designation
# -------------------------------
avg_age_designation = conn.execute("""
SELECT
    d.DesignationName,
    ROUND(AVG(e.Age),2) AS AverageAge
FROM Employees e
JOIN Designations d
ON e.DesignationID = d.DesignationID
GROUP BY d.DesignationName
ORDER BY AverageAge DESC;
""").fetchdf()

print("\n===== Average Age by Designation =====")
print(avg_age_designation)

avg_age_designation.to_csv(
    OUTPUT_DIR / "average_age_by_designation.csv",
    index=False
)

# -------------------------------
# Query 4 - Employee Count by Lab
# -------------------------------
employee_lab = conn.execute("""
SELECT
    l.LabName,
    COUNT(*) AS EmployeeCount
FROM Employees e
JOIN Labs l
ON e.LabID = l.LabID
GROUP BY l.LabName
ORDER BY EmployeeCount DESC;
""").fetchdf()

print("\n===== Employee Count by Lab =====")
print(employee_lab)

employee_lab.to_csv(
    OUTPUT_DIR / "employee_count_by_lab.csv",
    index=False
)

# -------------------------------
# Query 5 - Employee Count by Cluster
# -------------------------------
employee_cluster = conn.execute("""
SELECT
    c.ClusterName,
    COUNT(*) AS EmployeeCount
FROM Employees e
JOIN Labs l
ON e.LabID = l.LabID
JOIN Clusters c
ON l.ClusterID = c.ClusterID
GROUP BY c.ClusterName
ORDER BY EmployeeCount DESC;
""").fetchdf()

print("\n===== Employee Count by Cluster =====")
print(employee_cluster)

employee_cluster.to_csv(
    OUTPUT_DIR / "employee_count_by_cluster.csv",
    index=False
)

conn.close()

print("\nSQL Analysis Completed Successfully!")