import subprocess
import sys


def run_step(title, script):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

    result = subprocess.run([sys.executable, script])

    if result.returncode != 0:
        print(f"\n❌ {title} Failed")
        sys.exit(result.returncode)

    print("✅ Completed")


def main():
    print("=" * 60)
    print("DRDO EMPLOYEE ANALYTICS PIPELINE")
    print("=" * 60)

    run_step("Step 1: Loading Excel into DuckDB", "src/load_data.py")
    run_step("Step 2: Running SQL Analysis", "src/sql_analysis.py")
    run_step("Step 3: Generating Charts", "src/charts.py")

    print("\nLaunching Streamlit Dashboard...\n")

    subprocess.run([
        "streamlit",
        "run",
        "dashboard/app.py"
    ])


if __name__ == "__main__":
    main()