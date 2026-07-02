import streamlit as st
from services.gemini_service import ask_gemini
from services.memory_service import save_memory
from services.export_service import export_pdf
from services.xp_service import add_xp


def show_notes_generator():

    st.title("📝 AI Study Notes Generator")

    st.write("Paste your chapter or topic below.")

    mode = st.selectbox(
        "Select Notes Type",
        [
            "Short Notes",
            "Detailed Notes",
            "One Night Revision",
            "Important Questions",
            "Flashcards",
            "Explain Like Class 6",
            "Summary"
        ]
    )

    chapter = st.text_area(
        "Paste Chapter Here",
        height=250,
        placeholder="Paste your chapter or topic..."
    )

    if st.button("🚀 Generate Notes"):

        if chapter.strip() == "":
            st.warning("Please paste some text.")
            return

        with st.spinner("ASTRA is generating notes..."):

            prompt = f"""
You are ASTRA (Artificial Student Tracking and Research Assistant).

Generate {mode} from the following text.

Text:

{chapter}

Make the output neat, easy to read and suitable for students.
"""

            answer = ask_gemini(prompt)

            add_xp(15)

            st.success("Notes Generated!")
            add_xp(15)

            st.markdown("## 📚 Generated Notes")

            st.write(answer)
            save_memory(
    "Notes Generator",
    "Generated study notes."
)
            export_pdf(answer, "ASTRA_Notes.pdf")

            with open("ASTRA_Notes.pdf", "rb") as pdf:
                st.download_button(
                    "📥 Download Notes",
                    pdf,
                    file_name="ASTRA_Notes.pdf",
                    mime="application/pdf",
                    use_container_width=True
                 )