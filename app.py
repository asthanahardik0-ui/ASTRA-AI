import streamlit as st

from config import APP_NAME, FULL_NAME, VERSION
from modules.home import show_home
from modules.doubt_solver import show_doubt_solver
from modules.notes_generator import show_notes_generator
from modules.code_explainer import show_code_explainer
from modules.quiz import show_quiz_generator
from services.ui_service import load_css
from modules.timetable import show_timetable_generator
from modules.pdf_chatbot import show_pdf_chatbot
from modules.interview_bot import show_interview_bot
from modules.study_coach import show_study_coach
from modules.dashboard import show_dashboard
from modules.profile import show_profile
from modules.flashcards import show_flashcards
from modules.settings import show_settings
from auth.login import show_login
from auth.register import show_register
from auth.session import initialize_session
from services.auth_service import current_user
# ==========================================
# PAGE CONFIGURATION
# ==========================================
initialize_session()

if not st.session_state.logged_in:

    if st.session_state.show_register:
        show_register()
    else:
        show_login()

    st.stop()
load_css()

# ==========================================
# SIDEBAR
# ==========================================

user = current_user()

st.sidebar.title("🚀 ASTRA")

st.sidebar.markdown(
    "### Artificial Student Tracking and Research Assistant"
)

st.sidebar.markdown("---")

if user:

    st.sidebar.success(f"👤 {user['name']}")

    st.sidebar.caption(f"🆔 {user['student_id']}")

    st.sidebar.info(f"🎓 Class {user['class']}")

    col1, col2 = st.sidebar.columns(2)

    with col1:
        st.metric(
            "⭐ Level",
            user["level"]
        )

    with col2:
        st.metric(
            "🏆 XP",
            user["xp"]
        )

st.sidebar.markdown("---")
menu = st.sidebar.radio(
    "Navigation",
    (
        "🏠 Home",
        "🧠 AI Study Coach",
        "🤖 AI Doubt Solver",
        "📄 AI PDF Chatbot",
        "📝 AI Study Notes Generator",
        "📅 AI Timetable Generator",
        "💻 AI Code Explainer",
        "🎤 Smart Interview Bot",
        "❓ Quiz Generator",
        "🃏 Flashcards Generator",
        "📊 Productivity Dashboard",
        "⚙️ Settings",
        "ℹ About ASTRA"
    )
)

st.sidebar.markdown("---")
st.sidebar.success(f"{APP_NAME} v{VERSION}")
from auth.session import logout

st.sidebar.markdown("---")

if st.sidebar.button("🚪 Logout", use_container_width=True):
    logout()

# ==========================================
# PAGES
# ==========================================

if menu == "🏠 Home":
    show_home()

elif menu == "🧠 AI Study Coach":
    show_study_coach()

elif menu == "🤖 AI Doubt Solver":
    show_doubt_solver()

elif menu=="👤 Profile":
    show_profile()

elif menu == "📄 AI PDF Chatbot":
    show_pdf_chatbot()

elif menu == "📝 AI Study Notes Generator":
    show_notes_generator()

elif menu == "📅 AI Timetable Generator":
    show_timetable_generator()

elif menu == "💻 AI Code Explainer":
    show_code_explainer()

elif menu=="🎤 Smart Interview Bot":
    show_interview_bot()

elif menu == "❓ Quiz Generator":
    show_quiz_generator()

elif menu == "🃏 Flashcards Generator":
    show_flashcards()

elif menu == "📊 Productivity Dashboard":
    show_dashboard()

elif menu == "⚙️ Settings":
    show_settings()

elif menu == "ℹ About ASTRA":
    st.title("🚀 ASTRA")

    st.subheader(FULL_NAME)

    st.markdown("---")

    st.write("""
### Version
1.0

### Technologies Used
- Python
- Streamlit
- Google Gemini AI
- Firebase (Coming Soon)

### Developer
Class 12 AI Capstone Project

### Description
ASTRA (Artificial Student Tracking and Research Assistant) is an AI-powered educational platform designed to help students study smarter.

It provides:
- AI Doubt Solver
- PDF Chatbot
- Study Notes Generator
- Timetable Generator
- Code Explainer
- Interview Bot
- Quiz Generator
- Flashcards
- Productivity Dashboard
""")