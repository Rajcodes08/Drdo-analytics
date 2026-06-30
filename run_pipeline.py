import subprocess
import sys

steps = [
    ("Loading Excel data into DuckDB", "src/load_data.py"),
    ("Running SQL Analysis", "src/sql_analysis.py"),
    ("Generating Charts", "src/charts.py"),
]

print("=" * 60)
print("        DRDO EMPLOYEE ANALYTICS PIPELINE")
print("=" * 60)

for title, script in steps:
    print(f"\n>> {title}...")

    result = subprocess.run([sys.executable, script])

    if result.returncode != 0:
        print(f"\n❌ Failed while running {script}")
        sys.exit(result.returncode)

    print("✅ Done")

print("\n🚀 Launching Streamlit Dashboard...\n")

subprocess.run(
    [
        "streamlit",
        "run",
        "dashboard/app.py"
    ]
)