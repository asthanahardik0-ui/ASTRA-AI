import streamlit as st
from services.gemini_service import ask_gemini
from services.memory_service import save_memory
from services.export_service import export_pdf
from services.xp_service import add_xp



def show_doubt_solver():

    st.title("🤖 AI Doubt Solver")

    st.write("Ask any study-related question and ASTRA will answer it.")

    mode = st.selectbox(
        "Choose Explanation Mode",
        [
            "Beginner",
            "Exam Mode",
            "Formula Only",
            "Detailed",
            "Explain Like Class 6"
        ]
    )

    question = st.text_area(
        "Enter Your Question",
        height=150,
        placeholder="Example: Explain Newton's First Law"
    )

    if st.button("🚀 Ask ASTRA"):

        if question.strip() == "":
            st.warning("Please enter a question.")
            return

        with st.spinner("🤖 ASTRA is thinking..."):

            prompt = f"""
You are ASTRA (Artificial Student Tracking and Research Assistant).

Answer the following question.

Mode:
{mode}

Question:
{question}

Give a clear, accurate, student-friendly answer according to the selected mode.
"""

            answer = ask_gemini(prompt)

            st.success("✅ Answer Generated!")
            add_xp(5)
            st.session_state.user = user

            st.markdown("### 📖 Answer")

            st.write(answer)

            save_memory(
                "AI Doubt Solver",
                "Solved a student doubt."
            )

            # Add XP
            add_xp(10)
            unlock_badge("🧠 Doubt Solver")

            # Export PDF
            export_pdf(answer, "ASTRA_Doubt_Solution.pdf")

            # Download Button
            with open("ASTRA_Doubt_Solution.pdf", "rb") as pdf:

                st.download_button(
                    label="📥 Download Answer",
                    data=pdf,
                    file_name="ASTRA_Doubt_Solution.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )