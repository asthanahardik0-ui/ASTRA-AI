import streamlit as st
from services.auth_service import login_user


def show_login():

    st.title("🚀 ASTRA AI")

    st.subheader("Student Login")

    st.markdown("---")

    student_id = st.text_input(
        "🆔 Student ID",
        placeholder="Example: ASTRA-000001"
    )

    password = st.text_input(
        "🔒 Password",
        type="password"
    )

    st.markdown("---")

    login = st.button(
        "🔓 Login",
        use_container_width=True
    )

    register = st.button(
        "✨ Create New Account",
        use_container_width=True
    )

    if login:

        user = login_user(student_id, password)

        if user:

            st.session_state.logged_in = True
            st.session_state.user = user

            st.success("Login Successful!")

            st.rerun()

        else:

            st.error("Invalid Student ID or Password.")

    if register:

        st.session_state.show_register = True
        st.rerun()