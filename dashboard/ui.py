import streamlit as st


def show_sidebar(cluster_list):
    st.sidebar.title("🛡️ DRDO Analytics")

    st.sidebar.markdown("---")

    analysis = st.sidebar.radio(
        "Choose Analysis",
        [
            "Employee Count",
            "Average Age"
        ]
    )

    analyze_options = [
        "Cluster",
        "Lab (Within Cluster)",
        "Designation"
    ]

    analyze_by = st.sidebar.selectbox(
        "Analyze By",
        analyze_options
    )

    selected_cluster = None

    if analyze_by == "Lab (Within Cluster)":

        # We'll populate this from the database in the next step
        selected_cluster = st.sidebar.selectbox(
            "Select Cluster",
            cluster_list["ClusterName"].tolist()
        )
    st.sidebar.markdown("---")

    st.sidebar.info(
        """
        **Project**

        DRDO Human Resource Analytics

        Backend:
        DuckDB

        Frontend:
        Streamlit + Plotly
        """
    )

    return analysis, analyze_by, selected_cluster

def show_kpis(conn):

    total_employees = conn.execute("""
    SELECT COUNT(*) FROM Employees;
    """).fetchone()[0]

    total_labs = conn.execute("""
    SELECT COUNT(*) FROM Labs;
    """).fetchone()[0]

    total_clusters = conn.execute("""
    SELECT COUNT(*) FROM Clusters;
    """).fetchone()[0]

    total_designations = conn.execute("""
    SELECT COUNT(*) FROM Designations;
    """).fetchone()[0]

    col1, col2, col3, col4 = st.columns(4)

    cards = [
        ("👨", "Employees", total_employees, "#1565C0"),
        ("🧪", "Labs", total_labs, "#00897B"),
        ("🏢", "Clusters", total_clusters, "#FB8C00"),
        ("🎖️", "Designations", total_designations, "#8E24AA"),
    ]

    for col, (icon, title, value, color) in zip(
        [col1, col2, col3, col4],
        cards
    ):
        with col:
            st.markdown(
                f"""
<div style="
background:#ffffff;
border-left:6px solid {color};
border-radius:12px;
padding:20px;
box-shadow:0 4px 12px rgba(0,0,0,0.08);
">

<div style="
font-size:18px;
color:#666;
font-weight:600;
">
{icon} {title}
</div>

<div style="
font-size:42px;
font-weight:700;
color:{color};
margin-top:10px;
">
{value}
</div>

</div>
""",
                unsafe_allow_html=True,
            )

    st.markdown("<br>", unsafe_allow_html=True)