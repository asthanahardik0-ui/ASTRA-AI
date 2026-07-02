import streamlit as st

from services.ai_service import model

from services.pdf_service import extract_text
from services.memory_service import save_memory
from services.export_service import export_pdf
from services.xp_service import add_xp

def show_pdf_chatbot():

    st.title("📄 AI PDF Chatbot")

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if uploaded_file:

        with st.spinner("Reading PDF..."):

            pdf_text = extract_text(uploaded_file)

        st.success("PDF Loaded Successfully!")
        add_xp(8)

        st.session_state.user = user

        question = st.text_input(
            "Ask anything from this PDF"
        )

        mode = st.selectbox(

            "Answer Mode",

            [

                "Normal",

                "Beginner",

                "Exam",

                "Formula Only"

            ]

        )

        if st.button("Ask ASTRA"):

            prompt = f"""

You are ASTRA.

Answer ONLY using the following PDF.

PDF:

{pdf_text}

Question:

{question}

Mode:

{mode}

If the answer is not found inside the PDF,

reply

"This topic is not available in the uploaded PDF."

"""

            with st.spinner("Thinking..."):

                response = model.generate_content(prompt)

            st.markdown("## 📖 Answer")

            st.write(response.text)

            add_xp(20)
            unlock_badge("📚 Bookworm")
            save_memory(
    "PDF Chatbot",
    "Asked a question from a PDF."
)
            export_pdf(response.text, "ASTRA_PDF_Answer.pdf")

            with open("ASTRA_PDF_Answer.pdf", "rb") as pdf:
                st.download_button(
                    "📥 Download Answer",
                    pdf,
                    file_name="ASTRA_PDF_Answer.pdf",
                    mime="application/pdf",
                    use_container_width=True
    )
