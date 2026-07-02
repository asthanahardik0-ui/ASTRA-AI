import streamlit as st
from services.ai_service import model
from services.memory_service import save_memory
from services.export_service import export_pdf
from services.xp_service import add_xp

def show_flashcards():

    st.title("🃏 ASTRA Flashcards Generator")
    st.subheader("Artificial Student Tracking and Research Assistant")

    st.markdown("---")

    topic = st.text_input(
        "Enter Topic",
        placeholder="Example: Artificial Intelligence"
    )

    number = st.slider(
        "Number of Flashcards",
        5,
        25,
        10
    )

    if st.button("🚀 Generate Flashcards", use_container_width=True):

        if topic.strip() == "":
            st.warning("Please enter a topic.")
            return

        prompt = f"""
You are ASTRA.

Create {number} flashcards on:

{topic}

Format:

Flashcard 1

Question:
...

Answer:
...

Flashcard 2

Question:
...

Answer:
...

Use simple language.
"""

        with st.spinner("Generating Flashcards..."):

            try:

                response = model.generate_content(prompt)

                answer = response.text

                st.success("✅ Flashcards Generated!")
                add_xp(10)
                
                st.session_state.user = user

                st.markdown(answer)

                save_memory(
                    "Flashcards",
                    topic,
                    answer
                )
                # Add XP
                add_xp(15)
                unlock_badge("🃏 Flashcard Creator")
                export_pdf(
                    answer,
                    "ASTRA_Flashcards.pdf"
                )

                with open("ASTRA_Flashcards.pdf", "rb") as pdf:

                    st.download_button(
                        "📥 Download Flashcards",
                        pdf,
                        file_name="ASTRA_Flashcards.pdf",
                        mime="application/pdf",
                        use_container_width=True
                    )

            except Exception as e:

                st.error("Something went wrong.")

                st.exception(e)