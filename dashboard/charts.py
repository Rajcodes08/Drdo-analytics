import plotly.express as px


def employee_cluster_chart(df):

    fig = px.bar(
        df,
        x="ClusterName",
        y="EmployeeCount",
        text_auto=True,
        color_discrete_sequence=["#1565C0"]
    )

    fig.update_layout(
        template="plotly_white",
        height=360,
        title="",
        margin=dict(l=20, r=20, t=20, b=20)
    )

    return fig


def employee_lab_chart(df):

    fig = px.bar(
        df,
        x="LabName",
        y="EmployeeCount",
        text_auto=True,
        color_discrete_sequence=["#00897B"]
    )

    fig.update_layout(
        template="plotly_white",
        height=360,
        title="",
        margin=dict(l=20, r=20, t=20, b=20)
    )

    return fig


def employee_designation_chart(df):

    fig = px.bar(
        df,
        x="DesignationName",
        y="EmployeeCount",
        text_auto=True,
        color_discrete_sequence=["#1565C0"]
    )

    fig.update_layout(
        template="plotly_white",
        height=360,
        title="",
        margin=dict(l=20, r=20, t=20, b=20)
    )

    return fig


def age_cluster_chart(df):

    fig = px.bar(
        df,
        x="ClusterName",
        y="AverageAge",
        text_auto=".2f",
        color_discrete_sequence=["#8E24AA"]
    )

    fig.update_layout(
        template="plotly_white",
        height=360,
        title="",
        margin=dict(l=20, r=20, t=20, b=20)
    )

    return fig


def age_lab_chart(df):

    fig = px.bar(
        df,
        x="LabName",
        y="AverageAge",
        text_auto=".2f",
        color_discrete_sequence=["#8E24AA"]
    )

    fig.update_layout(
        template="plotly_white",
        height=360,
        title="",
        margin=dict(l=20, r=20, t=20, b=20)
    )

    return fig


def age_designation_chart(df):

    fig = px.bar(
        df,
        x="DesignationName",
        y="AverageAge",
        text_auto=".2f",
        color_discrete_sequence=["#8E24AA"]
    )

    fig.update_layout(
        template="plotly_white",
        height=360,
        title="",
        margin=dict(l=20, r=20, t=20, b=20)
    )

    return fig
