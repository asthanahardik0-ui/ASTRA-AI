import streamlit as st
import random
from datetime import datetime

from services.profile_service import load_profile
from services.progress_service import load_progress
from services.analytics_service import get_dashboard_data
from PIL import Image
from services.auth_service import current_user

logo = Image.open("assets/logo.png")
st.image(logo, width=120)


def show_home():

    # ==========================================
    # LOAD DATA
    # ==========================================

    profile = current_user()
    progress = load_progress()
    dashboard = get_dashboard_data()
    achievement = dashboard["achievement"]

    name = profile.get("name", "Student")
    goal = profile.get("daily_goal", 2)
    weak_subject = profile.get("weak_subject", "Not Set")
    target_exam = profile.get("target_exam", "Not Set")
    streak = profile.get("study_streak", 0)

    xp = achievement.get("xp", 0)
    level = achievement.get("level", 1)

    today_hours = progress.get("today_hours", 0)

    if goal <= 0:
        goal = 1

    percentage = min(today_hours / goal, 1.0)

    # ==========================================
    # GREETING
    # ==========================================

    hour = datetime.now().hour

    if hour < 12:
        greeting = "🌅 Good Morning"

    elif hour < 17:
        greeting = "☀️ Good Afternoon"

    else:
        greeting = "🌙 Good Evening"

    # ==========================================
    # HERO
    # ==========================================

    st.title("🚀 ASTRA AI")

    st.subheader(
        "Artificial Student Tracking and Research Assistant"
    )

    st.success(f"{greeting}, **{name}**!")

    st.write(
        "### Your Personal AI-Powered Study Companion"
    )

    st.markdown("---")

    # ==========================================
    # DATE & TIME
    # ==========================================

    col1, col2 = st.columns(2)

    with col1:
        st.info(
            f"📅 {datetime.now().strftime('%A, %d %B %Y')}"
        )

    with col2:
        st.info(
            f"🕒 {datetime.now().strftime('%I:%M %p')}"
        )

    st.markdown("---")

    # ==========================================
    # QUICK STATS
    # ==========================================

    st.header("📊 Dashboard")

    user = current_user()

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric("⭐ Level", user.get("level", 1))
    c2.metric("🏆 XP", user.get("xp", 0))
    c3.metric("🔥 Streak", user.get("study_streak", 0))
    c4.metric("📚 Quizzes", user.get("completed_quizzes", 0))

    badges = user.get("badges", [])

    c5.metric("🏅 Badges", len(badges))

    st.markdown("---")

    # ==========================================
    # TODAY'S FOCUS
    # ==========================================

    st.header("🎯 Today's Focus")

    a1, a2 = st.columns(2)

    with a1:

        st.info(f"📚 Weak Subject\n\n**{weak_subject}**")

        st.info(f"🎓 Target Exam\n\n**{target_exam}**")

    with a2:

        st.info(f"📖 Study Goal\n\n**{goal} Hours**")

        st.info(f"📈 Hours Studied\n\n**{today_hours} Hours**")

    st.markdown("---")

    # ==========================================
    # QUICK ACTIONS
    # ==========================================

    st.header("⚡ ASTRA Features")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.success("🤖 AI Doubt Solver")

        st.write("Ask any study question instantly.")

        st.success("📝 Notes Generator")

        st.write("Generate smart notes using AI.")

        st.success("💻 Code Explainer")

        st.write("Understand programming easily.")

    with c2:

        st.success("❓ Quiz Generator")

        st.write("Practice with AI quizzes.")

        st.success("📄 PDF Chatbot")

        st.write("Chat with your PDFs.")

        st.success("📅 Timetable")

        st.write("Generate smart study plans.")

    with c3:

        st.success("🎤 Interview Bot")

        st.write("Practice interviews.")

        st.success("📊 Analytics Dashboard")

        st.write("Track your progress.")

        st.success("🧠 Study Coach")

        st.write("Get personalized guidance.")

    st.markdown("---")

    # ==========================================
    # DAILY PROGRESS
    # ==========================================

    st.header("📈 Today's Study Progress")

    st.progress(percentage)

    st.write(
        f"### {today_hours} / {goal} Hours Completed"
    )

    if percentage >= 1:

        st.success("🎉 Excellent! Goal Achieved!")

    elif percentage >= 0.75:

        st.info("🔥 Great work! Almost done.")

    elif percentage >= 0.5:

        st.warning("💪 Keep studying!")

    else:

        st.error("📚 Let's start studying!")

    st.markdown("---")

    # ==========================================
    # LEVEL PROGRESS
    # ==========================================

    st.header("🏆 Level Progress")

    level_progress = (xp % 100) / 100

    st.progress(level_progress)

    st.caption(
        f"{100 - (xp % 100)} XP needed for Level {level + 1}"
    )

    st.markdown("---")

    # ==========================================
    # QUOTE OF THE DAY
    # ==========================================

    quotes = [

        "Learning never exhausts the mind. — Leonardo da Vinci",

        "Success comes from consistency, not perfection.",

        "Small daily improvements lead to remarkable results.",

        "Dream big. Study smart. Stay consistent.",

        "Discipline beats motivation every time.",

        "The expert in anything was once a beginner.",

        "Every study session is a step toward success."

    ]

    st.header("💡 Quote of the Day")

    st.info(random.choice(quotes))

    st.markdown("---")

    # ==========================================
    # ABOUT ASTRA
    # ==========================================

    st.header("🚀 About ASTRA")

    st.write("""
**ASTRA** stands for **Artificial Student Tracking and Research Assistant**.

It is your all-in-one AI learning companion designed to help students:

- 🤖 Solve doubts instantly
- 📝 Generate notes
- 📚 Create quizzes
- 📄 Chat with PDFs
- 💻 Explain code
- 🎤 Practice interviews
- 📅 Build study timetables
- 📊 Track learning progress
- 🧠 Receive personalized study guidance
""")

    st.markdown("---")

    # ==========================================
    # FOOTER
    # ==========================================

    st.caption(
        "🚀 ASTRA AI v1.0 | Powered by Google Gemini | Developed by Hardik Asthana"
    )