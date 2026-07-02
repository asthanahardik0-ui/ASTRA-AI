import streamlit as st
from auth.session import logout
from services.auth_service import (
    current_user,
    save_current_user,
    hash_password
)


def show_settings():

    user = current_user()

    if user is None:
        st.error("Please login first.")
        return

    st.title("⚙️ Settings")

    st.markdown("---")

    # ==========================
    # ACCOUNT
    # ==========================

    st.header("👤 Account")

    name = st.text_input(
        "Name",
        value=user.get("name", "")
    )

    st.text_input(
        "Student ID",
        value=user.get("student_id", ""),
        disabled=True
    )

    student_class = st.selectbox(
        "Class",
        [
            "6","7","8","9","10",
            "11","12","College"
        ],
        index=[
            "6","7","8","9","10",
            "11","12","College"
        ].index(user.get("class","12"))
    )

    if st.button("💾 Save Account"):

        user["name"] = name
        user["class"] = student_class

        save_current_user(user)

        st.session_state.user = user

        st.success("Account updated successfully!")

    st.divider()

    # ==========================
    # PASSWORD
    # ==========================

    st.header("🔒 Change Password")

    new_password = st.text_input(
        "New Password",
        type="password"
    )

    confirm_password = st.text_input(
        "Confirm Password",
        type="password"
    )

    if st.button("🔑 Update Password"):

        if len(new_password) < 6:

            st.error("Password must be at least 6 characters.")

        elif new_password != confirm_password:

            st.error("Passwords do not match.")

        else:

            user["password"] = hash_password(new_password)

            save_current_user(user)

            st.session_state.user = user

            st.success("Password updated successfully!")

    st.divider()

    # ==========================
    # STUDY SETTINGS
    # ==========================

    st.header("📚 Study Preferences")

    goal = st.number_input(
        "Daily Goal (Hours)",
        1,
        24,
        int(user.get("daily_goal",2))
    )

    weak = st.text_input(
        "Weak Subject",
        value=user.get("weak_subject","")
    )

    exam = st.text_input(
        "Target Exam",
        value=user.get("target_exam","")
    )

    exam_date = st.date_input(
        "Exam Date"
    )

    if st.button("📚 Save Study Preferences"):

        user["daily_goal"] = goal
        user["weak_subject"] = weak
        user["target_exam"] = exam
        user["exam_date"] = str(exam_date)

        save_current_user(user)

        st.session_state.user = user

        st.success("Study preferences updated!")

    st.divider()

    # ==========================
    # PROGRESS
    # ==========================

    st.header("🏆 Progress")

    c1, c2 = st.columns(2)

    c1.metric("⭐ Level", user.get("level",1))
    c2.metric("🏆 XP", user.get("xp",0))

    c3, c4 = st.columns(2)

    c3.metric("🔥 Study Streak", user.get("study_streak",0))
    c4.metric("📚 Quizzes", user.get("completed_quizzes",0))

    c5, c6 = st.columns(2)

    c5.metric("📄 PDFs", user.get("uploaded_pdfs",0))
    c6.metric("🏅 Badges", len(user.get("badges",[])))

    st.divider()

    # ==========================
    # BADGES
    # ==========================

    st.header("🏅 Achievements")

    badges = user.get("badges", [])

    if badges:

        for badge in badges:

            st.success(badge)

    else:

        st.info("No achievements unlocked yet.")

    st.divider()

    # ==========================
    # LOGOUT
    # ==========================

    st.header("🚪 Logout")

    if st.button(
        "Logout",
        use_container_width=True
    ):
        logout()

    st.divider()

    # ==========================
    # ABOUT
    # ==========================

    st.header("ℹ️ About ASTRA")

    st.info("""
**ASTRA AI v1.0**

Artificial Student Tracking and Research Assistant

Powered by Google Gemini AI

Developed by Hardik Asthana
""")