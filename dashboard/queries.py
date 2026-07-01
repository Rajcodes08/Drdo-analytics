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
    GROUP BY
        c.ClusterID,
        c.ClusterName
    ORDER BY c.ClusterID ASC;
    """).fetchdf()

def get_lab_employee_count(conn):

    return conn.execute("""
    SELECT
        l.LabName,
        COUNT(*) AS EmployeeCount
    FROM Employees e
    JOIN Labs l
        ON e.LabID = l.LabID
    GROUP BY
        l.LabID,
        l.LabName
    ORDER BY l.LabID ASC;
    """).fetchdf()
def get_designation_employee_count(conn):

    return conn.execute("""
    SELECT
        d.DesignationName,
        COUNT(*) AS EmployeeCount
    FROM Employees e
    JOIN Designations d
        ON e.DesignationID = d.DesignationID
    GROUP BY
        d.DesignationName,
        d.GradeLevel
    ORDER BY d.GradeLevel ASC;
    """).fetchdf()

def get_designation_average_age(conn):

    return conn.execute("""
    SELECT
        d.DesignationName,
        ROUND(AVG(e.Age), 1) AS AverageAge
    FROM Employees e
    JOIN Designations d
        ON e.DesignationID = d.DesignationID
    GROUP BY
        d.DesignationName,
        d.GradeLevel
    ORDER BY d.GradeLevel ASC;
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
    GROUP BY
        c.ClusterID,
        c.ClusterName
    ORDER BY c.ClusterID ASC;
    """).fetchdf()

def get_lab_average_age(conn):

    return conn.execute("""
    SELECT
        l.LabName,
        ROUND(AVG(e.Age), 1) AS AverageAge
    FROM Employees e
    JOIN Labs l
        ON e.LabID = l.LabID
    GROUP BY
        l.LabID,
        l.LabName
    ORDER BY l.LabID ASC;
    """).fetchdf()