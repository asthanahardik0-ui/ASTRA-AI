import streamlit as st
import pandas as pd
from datetime import datetime

from services.analytics_service import get_dashboard_data
from services.progress_service import load_progress, save_progress
from services.auth_service import current_user




def show_dashboard():

    dashboard = get_dashboard_data()

    profile = current_user()
    progress = dashboard["progress"]
    achievement = dashboard["achievement"]
    history = dashboard["memory"]

    st.title("📊 ASTRA Analytics Dashboard")
    st.subheader(f"👋 Welcome {profile.get('name', 'Student')}")

    st.divider()

    # ===========================
    # TOP METRICS
    # ===========================

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "🔥 Study Streak",
        f"{profile.get('study_streak', 0)} Days"
    )

    c2.metric(
        "🎯 Daily Goal",
        f"{profile.get('daily_goal', 2)} Hours"
    )

    c3.metric(
        "⭐ Level",
        achievement["level"]
    )

    c4.metric(
        "🏆 XP",
        achievement["xp"]
    )

    st.divider()

    # ===========================
    # LEVEL PROGRESS
    # ===========================

    st.subheader("⭐ Level Progress")

    progress_percent = (achievement["xp"] % 100) / 100

    st.progress(progress_percent)

    st.caption(
        f"{100-(achievement['xp']%100)} XP needed for next level."
    )

    st.divider()

    # ===========================
    # STUDENT ANALYTICS
    # ===========================

    st.subheader("📈 Student Analytics")

    a1, a2, a3 = st.columns(3)

    a1.metric(
        "AI Activities",
        len(history)
    )

    a2.metric(
        "Completed Quizzes",
        profile.get("completed_quizzes", 0)
    )

    a3.metric(
        "Uploaded PDFs",
        profile.get("uploaded_pdfs", 0)
    )

    st.divider()

    # ===========================
    # WEEKLY STUDY HOURS
    # ===========================

    st.subheader("📈 Weekly Study Hours")

    study = pd.DataFrame({

        "Day": [
            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri",
            "Sat",
            "Sun"
        ],

        "Hours": [
            2,
            3,
            4,
            2,
            5,
            4,
            progress["today_hours"]
        ]

    })

    st.line_chart(study.set_index("Day"))

    st.divider()

    # ===========================
    # SUBJECT DISTRIBUTION
    # ===========================

    st.subheader("📚 Subject Distribution")

    subject_data = {

        profile.get("weak_subject", "Artificial Intelligence"): 40,
        "Mathematics": 25,
        "Science": 20,
        "English": 15

    }

    st.bar_chart(subject_data)

    st.divider()

    # ===========================
    # AI MODULE USAGE
    # ===========================

    st.subheader("🤖 AI Module Usage")

    module_count = {}

    for item in history:

        module = item.get("module", "Unknown")

        module_count[module] = module_count.get(module, 0) + 1

    if module_count:

        st.bar_chart(module_count)

    else:

        st.info("No activity yet.")

    st.divider()

    # ===========================
    # ACHIEVEMENTS
    # ===========================

    st.subheader("🏆 Achievements")

    badges = profile.get("badges", [])

    if badges:
        cols = st.columns(2)

        for i, badge in enumerate(badges):
            cols[i % 2].success(badge)

    else:
        st.info("No achievements unlocked yet.")

    # ===========================
    # EXAM COUNTDOWN
    # ===========================

    st.subheader("📅 Exam Countdown")

    try:

        exam = datetime.strptime(
            profile.get("exam_date", "2026-03-01"),
            "%Y-%m-%d"
        )

        days = (exam - datetime.now()).days

        if days > 0:

            st.metric(
                "Days Remaining",
                f"{days} Days"
            )

        elif days == 0:

            st.success("🎉 Best of Luck! Today is your exam.")

        else:

            st.error("Exam date has passed.")

    except:

        st.warning("Please set your exam date.")

    st.divider()

    # ===========================
    # TODAY'S STUDY PROGRESS
    # ===========================

    st.subheader("📚 Today's Study Progress")

    hours = st.number_input(
        "Hours Studied",
        min_value=0.0,
        max_value=24.0,
        value=float(progress["today_hours"]),
        step=0.5
    )

    if st.button("💾 Save Progress"):

        save_progress(hours)

        st.success("Progress Saved Successfully!")

    goal = max(profile.get("daily_goal", 2), 1)

    score = min(hours / goal, 1.0)

    st.progress(score)

    st.write(f"### {hours} / {goal} Hours Completed")

    st.divider()

    # ===========================
    # PRODUCTIVITY SCORE
    # ===========================

    st.subheader("⚡ Productivity Score")

    productivity = int(score * 100)

    st.metric(
        "Today's Score",
        f"{productivity}%"
    )

    st.progress(productivity / 100)

    st.divider()

    # ===========================
    # SMART RECOMMENDATION
    # ===========================

    st.subheader("🧠 ASTRA Recommendation")

    if productivity < 50:

        st.warning(
            "📚 Study for one more hour today to stay on track."
        )

    elif productivity < 80:

        st.info(
            "🔥 Great progress! Complete today's goal."
        )

    else:

        st.success(
            "🎉 Excellent! You achieved today's study target."
        )

    st.divider()

    # ===========================
    # RECENT ACTIVITIES
    # ===========================

    st.subheader("📚 Recent AI Activities")

    if history:

        for item in history[-10:][::-1]:

            st.info(
                f"{item.get('module','Unknown')} • {item.get('title','Activity')}"
            )

    else:

        st.info("No recent activity.")

    st.divider()

    st.caption("🚀 Powered by ASTRA AI v1.0")