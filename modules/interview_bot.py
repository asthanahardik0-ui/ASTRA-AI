import streamlit as st
from services.ai_service import model
from services.memory_service import save_memory
from services.export_service import export_pdf
from services.xp_service import add_xp


def show_interview_bot():

    st.title("🎤 Smart Interview Bot")

    interview_type = st.selectbox(
        "Interview Type",
        [
            "HR Interview",
            "Technical Interview",
            "Python Interview",
            "Artificial Intelligence Viva",
            "College Viva"
        ]
    )

    if st.button("Generate Question"):

        prompt = f"""
Generate ONE interview question for

{interview_type}

Do not give the answer.
Only ask one question.
"""

        response = model.generate_content(prompt)

        st.session_state.question = response.text

    if "question" in st.session_state:

        st.markdown("## 🎯 Question")

        st.write(st.session_state.question)

        answer = st.text_area("Your Answer")

        if st.button("Evaluate Answer"):

            prompt = f"""
You are an interview evaluator.

Question:

{st.session_state.question}

Student Answer:

{answer}

Give:

⭐ Score out of 10

✅ Strengths

❌ Weaknesses

💡 Correct Answer

📈 Improvement Tips
"""

            response = model.generate_content(prompt)
            add_xp(5)

            st.session_state.user = user

    

            st.markdown(response.text)
            save_memory(
    "Interview Bot",
    "Completed an interview practice session."
)