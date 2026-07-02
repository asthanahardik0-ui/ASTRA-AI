import streamlit as st


def initialize_session():

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if "user" not in st.session_state:
        st.session_state.user = None

    if "show_register" not in st.session_state:
        st.session_state.show_register = False


def logout():

    st.session_state.logged_in = False
    st.session_state.user = None
    st.session_state.show_register = False

    st.rerun()