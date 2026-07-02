import streamlit as st
from services.auth_service import register_user


def show_register():

    st.title("🚀 Create Your ASTRA Account")

    st.subheader("Artificial Student Tracking and Research Assistant")

    st.markdown("---")

    name = st.text_input(
        "👤 Full Name",
        placeholder="Enter your name"
    )

    student_class = st.selectbox(
        "🎓 Select Class",
        [
            "6", "7", "8", "9", "10",
            "11", "12",
            "College"
        ]
    )

    password = st.text_input(
        "🔒 Create Password",
        type="password"
    )

    confirm = st.text_input(
        "🔒 Confirm Password",
        type="password"
    )

    st.markdown("---")

    if st.button(
        "✨ Create Account",
        use_container_width=True
    ):

        if not name.strip():
            st.error("Please enter your name.")
            return

        if len(password) < 6:
            st.error("Password should be at least 6 characters.")
            return

        if password != confirm:
            st.error("Passwords do not match.")
            return

        student_id = register_user(
            name,
            student_class,
            password
        )

        st.success("🎉 Account Created Successfully!")

        st.info(f"🆔 Your Student ID: **{student_id}**")

        st.warning(
            "⚠️ Please save your Student ID. "
            "You'll need it every time you log in."
        )

        st.balloons()