import streamlit as st
from PIL import Image


def set_page_title(title):
    favicon = Image.open('./interface/ressources/logo-lux.png')
    st.set_page_config(
        page_title=title,
        page_icon=favicon,
    )
    st.markdown(unsafe_allow_html=True, body=f"""
        <iframe height=0 srcdoc="<script>
            parent.document.title = '{title}';
        </script>" />
    """)
