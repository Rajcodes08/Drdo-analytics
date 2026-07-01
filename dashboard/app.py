from pathlib import Path

import duckdb

import streamlit as st
from styles import load_css
from ui import show_sidebar, show_kpis
from queries import (
    get_cluster_employee_count,
    get_lab_employee_count,
    get_designation_employee_count,
    get_designation_average_age,
    get_cluster_average_age,
    get_lab_average_age,
    get_lab_employee_count_by_cluster
)
from charts import (
    employee_cluster_chart,
    employee_lab_chart,
    employee_designation_chart,
    age_cluster_chart,
    age_lab_chart,
    age_designation_chart
)
from streamlit_plotly_events import plotly_events
# -----------------------------------------------------
# Page Config
# -----------------------------------------------------

st.set_page_config(
    page_title="DRDO Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)
load_css()
# -----------------------------------------------------
# Paths
# -----------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATABASE_FILE = PROJECT_ROOT / "data" / "processed" / "drdo.duckdb"

conn = duckdb.connect(DATABASE_FILE)

# -----------------------------------------------------
# Sidebar
# -----------------------------------------------------

analysis, analyze_by = show_sidebar()
if "selected_cluster" not in st.session_state:
    st.session_state.selected_cluster = None


# -----------------------------------------------------
# Title
# -----------------------------------------------------

st.markdown("""
<h1 style='text-align:center; color:#1f4e79;'>
🛡️ DRDO Human Resource Analytics Dashboard
</h1>

<p style='text-align:center; color:gray; font-size:18px;'>
Employee Analytics using DuckDB + Streamlit
</p>
""", unsafe_allow_html=True)

st.divider()

# -----------------------------------------------------
# KPIs
# -----------------------------------------------------

show_kpis(conn)


# -----------------------------------------------------
# Employee Count by Cluster
# -----------------------------------------------------

cluster_df = get_cluster_employee_count(conn)
cluster_fig = employee_cluster_chart(cluster_df)



# -----------------------------------------------------
# Employee Count by Lab
# -----------------------------------------------------

lab_df = get_lab_employee_count(conn)
lab_fig = employee_lab_chart(lab_df)


# -----------------------------------------------------
# Average Age by Designation
# -----------------------------------------------------

designation_df = get_designation_average_age(conn)
designation_age_fig = age_designation_chart(designation_df)


designation_count_df = get_designation_employee_count(conn)
designation_count_fig = employee_designation_chart(designation_count_df)


cluster_age_df = get_cluster_average_age(conn)
cluster_age_fig = age_cluster_chart(cluster_age_df)


lab_age_df = get_lab_average_age(conn)
lab_age_fig = age_lab_chart(lab_age_df)

# -----------------------------------------------------
# Main Analysis Area
# -----------------------------------------------------

st.divider()

st.header(f"📊 {analysis} Analysis")

st.caption(f"Grouped by {analyze_by}")

if analysis == "Employee Count":

    if analyze_by == "Cluster":

        if st.session_state.selected_cluster is None:

            selected_points = plotly_events(
                cluster_fig,
                click_event=True,
                hover_event=False,
                select_event=False,
                override_height=360
            )

            if selected_points:
                st.session_state.selected_cluster = selected_points[0]["x"]
                st.rerun()

        else:

            cluster_name = st.session_state.selected_cluster

            st.subheader(f"📍 {cluster_name}")

            lab_df = get_lab_employee_count_by_cluster(
                conn,
                cluster_name
            )

            lab_fig = employee_lab_chart(lab_df)

            st.plotly_chart(
                lab_fig,
                use_container_width=True
            )

            if st.button("⬅ Back to Clusters"):
                st.session_state.selected_cluster = None
                st.rerun()
    elif analyze_by == "Lab":

        st.plotly_chart(lab_fig, use_container_width=True)

    elif analyze_by == "Designation":

        st.plotly_chart(
            designation_count_fig,
            use_container_width=True
        )
elif analysis == "Average Age":

    if analyze_by == "Cluster":

        st.plotly_chart(
            cluster_age_fig,
            use_container_width=True
        )


    elif analyze_by == "Lab":

        st.plotly_chart(
            lab_age_fig,
            use_container_width=True
        )

    elif analyze_by == "Designation":

        st.plotly_chart(
            designation_age_fig,
            use_container_width=True
        )
conn.close()