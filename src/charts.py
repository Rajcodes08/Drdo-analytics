from pathlib import Path

import duckdb
import matplotlib.pyplot as plt

# ---------------------------------------------------
# Project Paths
# ---------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATABASE_FILE = PROJECT_ROOT / "data" / "processed" / "drdo.duckdb"

CHART_DIR = PROJECT_ROOT / "outputs" / "charts"
CHART_DIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------
# Connect to DuckDB
# ---------------------------------------------------
conn = duckdb.connect(DATABASE_FILE)

# ---------------------------------------------------
# Chart 1 - Employee Count by Cluster
# ---------------------------------------------------
df = conn.execute("""
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

plt.figure(figsize=(10,6))
plt.bar(df["ClusterName"], df["EmployeeCount"])
plt.title("Employee Count by Cluster")
plt.xlabel("Cluster")
plt.ylabel("Employees")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(CHART_DIR / "employee_count_by_cluster.png")
plt.close()

# ---------------------------------------------------
# Chart 2 - Employee Count by Lab
# ---------------------------------------------------
df = conn.execute("""
SELECT
    l.LabName,
    COUNT(*) AS EmployeeCount
FROM Employees e
JOIN Labs l
ON e.LabID = l.LabID
GROUP BY l.LabName
ORDER BY EmployeeCount DESC;
""").fetchdf()

plt.figure(figsize=(12,6))
plt.bar(df["LabName"], df["EmployeeCount"])
plt.title("Employee Count by Lab")
plt.xlabel("Lab")
plt.ylabel("Employees")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig(CHART_DIR / "employee_count_by_lab.png")
plt.close()

# ---------------------------------------------------
# Chart 3 - Average Age by Designation
# ---------------------------------------------------
df = conn.execute("""
SELECT
    d.DesignationName,
    ROUND(AVG(e.Age),2) AS AverageAge
FROM Employees e
JOIN Designations d
ON e.DesignationID=d.DesignationID
GROUP BY d.DesignationName
ORDER BY AverageAge DESC;
""").fetchdf()

plt.figure(figsize=(8,5))
plt.bar(df["DesignationName"], df["AverageAge"])
plt.title("Average Age by Designation")
plt.xlabel("Designation")
plt.ylabel("Average Age")
plt.tight_layout()
plt.savefig(CHART_DIR / "average_age_designation.png")
plt.close()

# ---------------------------------------------------
# Chart 4 - Gender Distribution
# ---------------------------------------------------
df = conn.execute("""
SELECT
Gender,
COUNT(*) AS Count
FROM Employees
GROUP BY Gender;
""").fetchdf()

plt.figure(figsize=(6,6))
plt.pie(
    df["Count"],
    labels=df["Gender"],
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Gender Distribution")
plt.savefig(CHART_DIR / "gender_distribution.png")
plt.close()

conn.close()

print("Charts generated successfully!")