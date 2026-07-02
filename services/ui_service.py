import streamlit as st
import os


def load_css():
    css_path = os.path.join("assets", "css", "styles.css")

    if os.path.exists(css_path):
        with open(css_path, encoding="utf-8") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )
    else:
        st.error(f"CSS file not found:\n{css_path}")