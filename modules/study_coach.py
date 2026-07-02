import streamlit as st
from services.ai_service import model
from services.profile_service import load_profile
from services.memory_service import save_memory
from services.export_service import export_pdf
from services.auth_service import current_user
from services.xp_service import add_xp

def show_study_coach():

    profile = current_user()
    st.title("🧠 ASTRA AI Study Coach")
    st.subheader("Artificial Student Tracking and Research Assistant")

    st.markdown("---")

    st.success(f"👋 Welcome {profile['name']}")

    col1, col2 = st.columns(2)

    with col1:
        st.info(f"🎓 Class : {profile['class']}")
        st.info(f"📚 Weak Subject : {profile['weak_subject']}")

    with col2:
        st.info(f"🎯 Daily Goal : {profile['daily_goal']} Hours")
        st.info(f"📅 Target Exam : {profile['target_exam']}")

    st.markdown("---")

    st.header("📖 Tell ASTRA About Your Study Goal")

    study_goal = st.text_area(
        "Study Goal",
        height=180,
        placeholder="""
Examples:

• My AI exam is in 3 days.
• I am weak in Python loops.
• I need a one-night revision.
• Prepare me for my Physics viva.
• Help me score above 90%.
"""
    )

    mode = st.selectbox(
        "🎯 Select Study Mode",
        [
            "📘 Beginner Mode",
            "📝 Exam Mode",
            "⚡ One Night Revision",
            "💀 Burnout Prevention Mode"
        ]
    )

    difficulty = st.selectbox(
        "📊 Difficulty Level",
        [
            "Easy",
            "Medium",
            "Hard"
        ]
    )

    st.markdown("---")

    if st.button("🚀 Generate Complete Study Plan", use_container_width=True):

        if study_goal.strip() == "":
            st.warning("Please enter your study goal.")
            return

        with st.spinner("🧠 ASTRA is creating your personalized study plan..."):

            prompt = f"""
You are ASTRA.

Full Form:
Artificial Student Tracking and Research Assistant.

Student Profile

Name:
{profile['name']}

Class:
{profile['class']}

Weak Subject:
{profile['weak_subject']}

Daily Goal:
{profile['daily_goal']} Hours

Target Exam:
{profile['target_exam']}

Study Mode:
{mode}

Difficulty:
{difficulty}

Student Goal:
{study_goal}

Prepare a COMPLETE personalized study guide.

Include:

# 1 Personalized Study Timetable

Morning to Night Schedule

Include Breaks

Include Pomodoro Sessions

# 2 Important Topics

Most Important Concepts

High Weightage Topics

# 3 Short Notes

Easy Language

Bullet Points

# 4 Revision Strategy

# 5 Practice Questions

5 Subjective Questions

5 MCQs with Answers

# 6 Flashcards

Question & Answer

# 7 Common Mistakes

# 8 Exam Tips

# 9 Sleep & Health Advice

# 10 Motivation

Use Beautiful Headings.

Use Bullet Points.

Keep everything organized.
"""

            try:

                response = model.generate_content(prompt)

                answer = response.text

                st.balloons()

                st.success("✅ Study Plan Generated Successfully!")
                add_xp(15)

                with st.expander(
                    "📚 View Your Complete AI Study Plan",
                    expanded=True
                ):

                    st.markdown(answer)

                # Save Activity
                save_memory(
                    "Study Coach",
                    "Generated a personalized study plan."
                )

                # Add XP
                add_xp(30)      
                unlock_badge("🎯 Goal Achiever")    

                # Export PDF
                export_pdf(
                    answer,
                    "ASTRA_Study_Plan.pdf"
                )

                # Download Button
                with open("ASTRA_Study_Plan.pdf", "rb") as pdf:

                    st.download_button(
                        label="📥 Download Study Plan",
                        data=pdf,
                        file_name="ASTRA_Study_Plan.pdf",
                        mime="application/pdf",
                        use_container_width=True
                    )

            except Exception as e:

                st.error("❌ Something went wrong.")

                st.exception(e)

    st.markdown("---")

    st.header("💡 ASTRA Smart Tips")

    tips = [
        "📚 Study difficult subjects first.",
        "🍅 Follow the Pomodoro Technique (25 min study + 5 min break).",
        "💧 Drink enough water while studying.",
        "😴 Sleep at least 7–8 hours before exams.",
        "📝 Practice writing answers instead of only reading.",
        "🎯 Focus on weak subjects every day."
    ]

    for tip in tips:
        st.info(tip)

    st.markdown("---")

    st.caption("🚀 Powered by Gemini AI | Developed under ASTRA")