import streamlit as st


def custom_ui():
    st.markdown(
        f"""
        <style>
        .stAppDeployButton {{
            display: none;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )