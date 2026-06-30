from pathlib import Path

import duckdb
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent

EXCEL_FILE = PROJECT_ROOT / "data" / "raw" / "drdo_project_data.xlsx"
DATABASE_FILE = PROJECT_ROOT / "data" / "processed" / "drdo.duckdb"

conn = duckdb.connect(DATABASE_FILE)

excel_file = pd.ExcelFile(EXCEL_FILE)

#print("Connected to DuckDB successfully!")

for sheet in excel_file.sheet_names:
    df = pd.read_excel(EXCEL_FILE, sheet_name=sheet)

    conn.register("temp_df", df)

    conn.execute(f"""
        CREATE OR REPLACE TABLE {sheet} AS
        SELECT * FROM temp_df
    """)

    print(f"✓ Loaded {sheet}")

conn.close()

print("\nAll tables loaded successfully!")