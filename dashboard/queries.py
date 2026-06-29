def get_cluster_employee_count(conn):

    return conn.execute("""
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

def get_lab_employee_count(conn):

    return conn.execute("""
    SELECT
        l.LabName,
        COUNT(*) AS EmployeeCount
    FROM Employees e
    JOIN Labs l
        ON e.LabID = l.LabID
    GROUP BY l.LabName
    ORDER BY EmployeeCount DESC;
    """).fetchdf()

def get_designation_employee_count(conn):

    return conn.execute("""
    SELECT
        d.DesignationName,
        COUNT(*) AS EmployeeCount
    FROM Employees e
    JOIN Designations d
        ON e.DesignationID = d.DesignationID
    GROUP BY d.DesignationName
    ORDER BY EmployeeCount DESC;
    """).fetchdf()

def get_designation_average_age(conn):

    return conn.execute("""
    SELECT
        d.DesignationName,
        ROUND(AVG(e.Age), 2) AS AverageAge
    FROM Employees e
    JOIN Designations d
        ON e.DesignationID = d.DesignationID
    GROUP BY d.DesignationName
    ORDER BY AverageAge DESC;
    """).fetchdf()

def get_cluster_average_age(conn):

    return conn.execute("""
    SELECT
        c.ClusterName,
        ROUND(AVG(e.Age),2) AS AverageAge
    FROM Employees e
    JOIN Labs l
        ON e.LabID = l.LabID
    JOIN Clusters c
        ON l.ClusterID = c.ClusterID
    GROUP BY c.ClusterName
    ORDER BY AverageAge DESC;
    """).fetchdf()

def get_lab_average_age(conn):

    return conn.execute("""
    SELECT
        l.LabName,
        ROUND(AVG(e.Age),2) AS AverageAge
    FROM Employees e
    JOIN Labs l
        ON e.LabID = l.LabID
    GROUP BY l.LabName
    ORDER BY AverageAge DESC;
    """).fetchdf()

def get_gender_distribution(conn):

    return conn.execute("""
    SELECT
        Gender,
        COUNT(*) AS Count
    FROM Employees
    GROUP BY Gender;
    """).fetchdf()
