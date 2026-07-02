import streamlit as st
import google.generativeai as genai
from services.memory_service import save_memory
from services.export_service import export_pdf
from services.xp_service import add_xp

# Configure Gemini
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")


def show_timetable_generator():

    st.title("📅 AI Timetable Generator")

    st.write("Generate a personalized study timetable using AI.")

    subjects = st.text_input(
        "Subjects (comma separated)",
        placeholder="Maths, Physics, Chemistry, AI"
    )

    hours = st.slider(
        "Study Hours Per Day",
        1,
        12,
        4
    )

    exam = st.text_input(
        "Nearest Exam",
        placeholder="AI Practical on 10 July"
    )

    weak = st.text_input(
        "Weak Subject",
        placeholder="Physics"
    )

    mode = st.selectbox(
        "Study Mode",
        [
            "Normal",
            "Exam Preparation",
            "One Night Revision",
            "Burnout Prevention"
        ]
    )

    if st.button("🚀 Generate Timetable"):

        prompt = f"""
Create a professional study timetable.

Subjects:
{subjects}

Available Hours:
{hours}

Nearest Exam:
{exam}

Weak Subject:
{weak}

Mode:
{mode}

Requirements:

- Time table from morning to night
- Include breaks
- Include revision
- Include motivation
- Include Pomodoro sessions
- Display in table format
"""

        with st.spinner("Generating Timetable..."):

            response = model.generate_content(prompt)

            st.success("Timetable Generated!")
            add_xp(5)

            st.markdown(response.text)
            save_memory(
    "Timetable Generator",
    "Created a study timetable."
)
            export_pdf(answer, "ASTRA_Timetable.pdf")

            with open("ASTRA_Timetable.pdf", "rb") as pdf:
                st.download_button(
                    "📥 Download Timetable",
                    pdf,
                    file_name="ASTRA_Timetable.pdf",
                    mime="application/pdf",
                    suse_container_width=True
    )