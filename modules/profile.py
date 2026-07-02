import streamlit as st

from services.profile_service import load_profile
from services.profile_service import save_profile
from services.auth_service import current_user


def show_profile():

    profile = current_user()

    st.title("👤 Student Profile")

    name = st.text_input("Name", profile["name"])

    student_class = st.text_input("Class", profile["class"])

    school = st.text_input("School", profile["school"])

    goal = st.number_input(
        "Daily Study Goal (Hours)",
        1,
        12,
        profile["daily_goal"]
    )

    weak = st.text_input(
        "Weak Subject",
        profile["weak_subject"]
    )

    exam = st.text_input(
        "Target Exam",
        profile["target_exam"]
    )

    if st.button("💾 Save Profile"):

        profile["name"] = name
        profile["class"] = student_class
        profile["school"] = school
        profile["daily_goal"] = goal
        profile["weak_subject"] = weak
        profile["target_exam"] = exam

        save_profile(profile)

        st.success("Profile Saved Successfully!")