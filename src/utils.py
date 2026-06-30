"""
src/utils.py

Utility helper functions shared across the pipeline.
Covers path resolution, directory setup, and DuckDB connection management.
"""

from pathlib import Path
import duckdb


# -------------------------------------------------------------
# Project root path — works regardless of where script is run from
# -------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent


def get_db_path() -> Path:
    """Returns the absolute path to the DuckDB database file."""
    return PROJECT_ROOT / "data" / "processed" / "drdo.duckdb"


def get_excel_path() -> Path:
    """Returns the absolute path to the raw Excel source file."""
    return PROJECT_ROOT / "data" / "raw" / "drdo_project_data.xlsx"


def get_output_dir(subfolder: str = "") -> Path:
    """
    Returns the absolute path to an outputs subdirectory.
    Creates the directory if it does not exist.

    Args:
        subfolder: "reports" or "charts" or "" for the root outputs folder.

    Returns:
        Path object to the requested output directory.

    Example:
        get_output_dir("reports") → /path/to/project/outputs/reports/
    """
    path = PROJECT_ROOT / "outputs" / subfolder if subfolder else PROJECT_ROOT / "outputs"
    path.mkdir(parents=True, exist_ok=True)
    return path


def get_connection() -> duckdb.DuckDBPyConnection:
    """
    Opens and returns a DuckDB connection to drdo.duckdb.

    The caller is responsible for closing the connection
    when done (conn.close()).

    Returns:
        An open DuckDB connection object.

    Example:
        conn = get_connection()
        df = conn.execute("SELECT COUNT(*) FROM Employees").fetchdf()
        conn.close()
    """
    db_path = get_db_path()

    if not db_path.exists():
        raise FileNotFoundError(
            f"Database not found at: {db_path}\n"
            f"Run src/load_data.py first to create it."
        )

    return duckdb.connect(db_path)


def table_exists(conn: duckdb.DuckDBPyConnection, table_name: str) -> bool:
    """
    Checks whether a table exists in the DuckDB database.

    Args:
        conn: An open DuckDB connection.
        table_name: Name of the table to check.

    Returns:
        True if the table exists, False otherwise.

    Example:
        if not table_exists(conn, "Employees"):
            print("Run load_data.py first.")
    """
    result = conn.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = ?
    """, [table_name]).fetchone()

    return result[0] > 0


def print_table_summary(conn: duckdb.DuckDBPyConnection) -> None:
    """
    Prints a summary of all tables in the database with their row counts.
    Useful for verifying that load_data.py ran successfully.

    Args:
        conn: An open DuckDB connection.
    """
    tables = ["Employees", "Labs", "Clusters", "Designations"]

    print("\n📋 Database Table Summary")
    print("-" * 30)

    for table in tables:
        if table_exists(conn, table):
            count = conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
            print(f"  {table:<20} {count:>5} rows")
        else:
            print(f"  {table:<20}  ⚠ not found")

    print("-" * 30)