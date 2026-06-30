# DRDO Employee Analytics Dashboard

A Python-based HR analytics dashboard built using **DuckDB, SQL, Pandas, Plotly, and Streamlit**. The project ingests employee data from Excel, stores it in DuckDB, performs SQL-based analysis, generates visualizations, and presents interactive insights through a Streamlit dashboard.

---

## Features

- Load Excel data into a DuckDB database
- Perform SQL-based employee analytics
- Generate CSV reports automatically
- Create static charts using Matplotlib
- Interactive dashboard built with Streamlit
- KPI cards for quick insights
- Dynamic visualizations using Plotly

---

## Tech Stack

- Python
- DuckDB
- Pandas
- SQL
- Streamlit
- Plotly
- Matplotlib

---

## Project Structure

```
drdo-analytics/
│
├── dashboard/
│   ├── app.py              # Main Streamlit application
│   ├── charts.py           # Plotly chart functions
│   ├── queries.py          # SQL query functions
│   ├── styles.py           # Custom CSS
│   └── ui.py               # Sidebar and KPI cards
│
├── data/
│   ├── raw/
│   │   └── drdo_project_data.xlsx
│   └── processed/
│       └── drdo.duckdb
│
├── outputs/
│   ├── charts/
│   └── reports/
│
├── src/
│   ├── load_data.py        # Loads Excel into DuckDB
│   ├── sql_analysis.py     # Executes SQL analysis
│   └── charts.py           # Generates charts
│
├── run_pipeline.py
├── requirements.txt
└── README.md
```

---

## Pipeline

The project follows the workflow below:

```
Excel Workbook
       │
       ▼
Load Data into DuckDB
       │
       ▼
Execute SQL Analysis
       │
       ▼
Generate Reports & Charts
       │
       ▼
Launch Streamlit Dashboard
```

---

## Database Schema

The project consists of five tables:

- Employees
- Labs
- Clusters
- Designations
- Promotions

Relationships:

```
Clusters
    │
    ▼
Labs
    │
    ▼
Employees
    │
    ▼
Promotions

Designations ─────────► Employees
```

---

## Dashboard Features

### KPI Cards

- Total Employees
- Total Labs
- Total Clusters
- Total Designations

### Employee Analytics

- Employee Count by Cluster
- Employee Count by Lab
- Employee Count by Designation

### Age Analytics

- Average Age by Cluster
- Average Age by Lab
- Average Age by Designation

---

## Installation

Clone the repository

```bash
git clone <repository-url>
cd drdo-analytics
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

Execute the complete pipeline

```bash
python run_pipeline.py
```

Or run each step manually

```bash
python src/load_data.py

python src/sql_analysis.py

python src/charts.py

streamlit run dashboard/app.py
```

---

## Output

Running the project generates:

```
data/processed/
    drdo.duckdb

outputs/reports/
    *.csv

outputs/charts/
    *.png
```

and launches the Streamlit dashboard.

---

## Sample Insights

The dashboard provides insights such as:

- Total employee distribution
- Gender distribution
- Employees by Cluster
- Employees by Lab
- Average age by designation
- Average age by cluster

---

## Future Improvements

- Interactive filtering
- Search functionality
- Department-wise analytics
- Promotion trend analysis
- Export reports to PDF/Excel
- Authentication for dashboard access

