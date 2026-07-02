import streamlit as st
from auth.register import show_register

st.set_page_config(
    page_title="ASTRA Register",
    page_icon="🚀",
    layout="centered"
)

show_register()