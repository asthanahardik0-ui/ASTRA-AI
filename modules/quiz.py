import streamlit as st
from services.gemini_service import ask_gemini
from services.memory_service import save_memory
from services.export_service import export_pdf
from services.auth_service import current_user, save_current_user
from services.xp_service import add_xp


def show_quiz_generator():
    
    
    st.title("❓ ASTRA Quiz Generator")
    st.subheader("Generate Professional AI-Based Quizzes")

    st.markdown("---")

    topic = st.text_input(
        "Enter Topic",
        placeholder="Example: Artificial Intelligence"
    )

    quiz_type = st.selectbox(
        "Quiz Type",
        [
            "📝 Multiple Choice (MCQ)",
            "✅ True / False",
            "✍ Fill in the Blanks",
            "📖 Short Answer",
            "📚 Long Answer"
        ]
    )

    difficulty = st.selectbox(
        "Difficulty Level",
        [
            "Easy",
            "Medium",
            "Hard"
        ]
    )

    number = st.slider(
        "Number of Questions",
        min_value=5,
        max_value=25,
        value=10
    )

    st.markdown("---")

    if st.button("🚀 Generate Quiz", use_container_width=True):

        if topic.strip() == "":
            st.warning("Please enter a topic.")
            return

        with st.spinner("🤖 ASTRA is preparing your quiz..."):

            prompt = f"""
You are ASTRA (Artificial Student Tracking and Research Assistant).

Generate a quiz with the following details:

Topic:
{topic}

Quiz Type:
{quiz_type}

Difficulty:
{difficulty}

Number of Questions:
{number}

Instructions:

• If MCQ:
- 4 options
- Correct answer
- Short explanation

• If True / False:
- Mention True or False
- Give explanation

• If Fill in the Blanks:
- Mention correct answers separately

• If Short Answer:
- Give model answers

• If Long Answer:
- Give detailed exam-style answers

Format the quiz neatly using headings and bullet points.
"""

            try:

                answer = ask_gemini(prompt)

                st.success("✅ Quiz Generated Successfully!")
                add_xp(10)


                st.markdown("## 📚 Generated Quiz")

                st.markdown(answer)

                # Save to History
                save_memory(
                    "Quiz Generator",
                    topic,
                    answer
                )

                # Add XP
                add_xp(20)
                unlock_badge("🥇 Quiz Master")

                # Export PDF
                export_pdf(answer, "ASTRA_Quiz.pdf")

                with open("ASTRA_Quiz.pdf", "rb") as pdf:

                    st.download_button(
                        label="📥 Download Quiz",
                        data=pdf,
                        file_name="ASTRA_Quiz.pdf",
                        mime="application/pdf",
                        use_container_width=True
                    )

            except Exception as e:

                st.error("❌ Failed to generate quiz.")
                st.exception(e)