import streamlit as st

from services.ai_service import model
from services.profile_service import load_profile
from services.memory_service import save_memory
from services.export_service import export_pdf
from services.auth_service import current_user
from services.xp_service import add_xp


def show_code_explainer():
    profile = current_user()
    st.title("💻 ASTRA Code Explainer")
    st.subheader("Artificial Student Tracking and Research Assistant")

    st.markdown("---")

    st.info(f"👋 Welcome {profile['name']}")

    language = st.selectbox(
        "Programming Language",
        [
            "Python",
            "C",
            "C++",
            "Java",
            "JavaScript",
            "HTML",
            "CSS",
            "SQL"
        ]
    )

    explanation_mode = st.selectbox(
        "Explanation Mode",
        [
            "Beginner",
            "Intermediate",
            "Exam Preparation",
            "Line by Line"
        ]
    )

    code = st.text_area(
        "Paste Your Code Here",
        height=300,
        placeholder="Paste your program here..."
    )

    if st.button("🚀 Explain Code", use_container_width=True):

        if code.strip() == "":
            st.warning("Please paste some code first.")
            return

        prompt = f"""
You are ASTRA.

Full Form:
Artificial Student Tracking and Research Assistant.

Student Name:
{profile['name']}

Class:
{profile['class']}

Programming Language:
{language}

Explanation Mode:
{explanation_mode}

Explain the following code.

Code:

{code}

Your explanation should include:

1. Purpose of the program
2. Line-by-line explanation
3. Important concepts used
4. Time Complexity (if applicable)
5. Space Complexity (if applicable)
6. Common mistakes
7. Interview Questions
8. Viva Questions
9. Beginner-friendly explanation
10. Summary
"""

        with st.spinner("🧠 ASTRA is analyzing your code..."):

            try:

                response = model.generate_content(prompt)

                answer = response.text

                st.success("✅ Code Explained Successfully!")
                add_xp(10)
                st.session_state.user = user

                st.markdown(answer)

                # Save activity
                save_memory(
                    "Code Explainer",
                    "Explained a programming program."
                )

                # Add XP
                add_xp(15)
                unlock_badge("💻 Code Master")
                
                # Export PDF
                export_pdf(answer, "Code_Explanation.pdf")

                with open("Code_Explanation.pdf", "rb") as pdf_file:

                    st.download_button(
                        label="📥 Download Explanation as PDF",
                        data=pdf_file,
                        file_name="ASTRA_Code_Explanation.pdf",
                        mime="application/pdf",
                        use_container_width=True
                    )

            except Exception as e:

                st.error("❌ Something went wrong while generating the explanation.")

                st.exception(e)

    st.markdown("---")

    st.header("💡 Programming Tips")

    st.info("✅ Always use meaningful variable names.")
    st.info("✅ Comment difficult parts of your code.")
    st.info("✅ Practice writing code daily.")
    st.info("✅ Learn debugging techniques.")
    st.info("✅ Understand logic instead of memorizing code.")

    st.markdown("---")

    st.caption("🚀 Powered by Gemini AI | Developed under ASTRA")