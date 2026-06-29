import streamlit as st


def load_css():

    st.markdown("""
    <style>

    .block-container{
        padding-top:2rem;
        padding-bottom:2rem;
        padding-left:3rem;
        padding-right:3rem;
    }

    [data-testid="stMetric"]{
        background-color:#f8f9fa;
        border:1px solid #dcdcdc;
        padding:15px;
        border-radius:12px;
        text-align:center;
        box-shadow:2px 2px 8px rgba(0,0,0,0.08);
    }

    </style>
    """, unsafe_allow_html=True)