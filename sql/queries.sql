

-- -------------------------------------------------------------
-- 1. Total Employee Count
-- -------------------------------------------------------------

SELECT COUNT(*) AS TotalEmployees
FROM Employees;


-- -------------------------------------------------------------
-- 2. Employee Count by Gender
-- -------------------------------------------------------------
SELECT
    Gender,
    COUNT(*) AS EmployeeCount
FROM Employees
GROUP BY Gender
ORDER BY EmployeeCount DESC;


-- -------------------------------------------------------------
-- 3. Employee Count by Lab
-- -------------------------------------------------------------

SELECT
    l.LabName,
    COUNT(*) AS EmployeeCount
FROM Employees e
JOIN Labs l
    ON e.LabID = l.LabID
GROUP BY l.LabName
ORDER BY EmployeeCount DESC;


-- -------------------------------------------------------------
-- 4. Employee Count by Cluster
-- -------------------------------------------------------------

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


-- -------------------------------------------------------------
-- 5. Employee Count by Designation
-- -------------------------------------------------------------

SELECT
    d.DesignationName,
    COUNT(*) AS EmployeeCount
FROM Employees e
JOIN Designations d
    ON e.DesignationID = d.DesignationID
GROUP BY d.DesignationName
ORDER BY EmployeeCount DESC;


-- -------------------------------------------------------------
-- 6. Average Age by Designation
-- -------------------------------------------------------------

SELECT
    d.DesignationName,
    ROUND(AVG(e.Age), 2) AS AverageAge
FROM Employees e
JOIN Designations d
    ON e.DesignationID = d.DesignationID
GROUP BY d.DesignationName
ORDER BY AverageAge DESC;


-- -------------------------------------------------------------
-- 7. Average Age by Lab
-- -------------------------------------------------------------

SELECT
    l.LabName,
    ROUND(AVG(e.Age), 2) AS AverageAge
FROM Employees e
JOIN Labs l
    ON e.LabID = l.LabID
GROUP BY l.LabName
ORDER BY AverageAge DESC;


-- -------------------------------------------------------------
-- 8. Average Age by Cluster
-- -------------------------------------------------------------

SELECT
    c.ClusterName,
    ROUND(AVG(e.Age), 2) AS AverageAge
FROM Employees e
JOIN Labs l
    ON e.LabID = l.LabID
JOIN Clusters c
    ON l.ClusterID = c.ClusterID
GROUP BY c.ClusterName
ORDER BY AverageAge DESC;


-- -------------------------------------------------------------
-- 9. Gender Distribution (for Pie Chart)
-- -------------------------------------------------------------
SELECT
    Gender,
    COUNT(*) AS Count
FROM Employees
GROUP BY Gender;


-- -------------------------------------------------------------
-- 10. KPI Counts (used in dashboard header cards)
-- -------------------------------------------------------------
SELECT COUNT(*) AS TotalEmployees  FROM Employees;
SELECT COUNT(*) AS TotalLabs       FROM Labs;
SELECT COUNT(*) AS TotalClusters   FROM Clusters;
SELECT COUNT(*) AS TotalDesignations FROM Designations;