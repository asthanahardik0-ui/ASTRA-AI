import json
import os

PROFILE = "data/student_profile.json"
PROGRESS = "data/progress.json"
MEMORY = "data/memory.json"
ACHIEVEMENT = "data/achievements.json"


def load_json(file_path, default):
    """
    Safely load a JSON file.
    Returns default data if the file doesn't exist or is invalid.
    """

    if not os.path.exists(file_path):
        return default

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default


def get_dashboard_data():
    profile = load_json(PROFILE, {
        "name": "Student",
        "class": "XII",
        "weak_subject": "Artificial Intelligence",
        "daily_goal": 2,
        "target_exam": "Final Exam",
        "exam_date": "2026-03-01",
        "study_streak": 0,
        "completed_quizzes": 0,
        "uploaded_pdfs": 0
    })

    progress = load_json(PROGRESS, {
        "today_hours": 0
    })

    memory = load_json(MEMORY, [])

    achievement = load_json(ACHIEVEMENT, {
        "level": 1,
        "xp": 0,
        "badges": []
    })

    return {
        "profile": profile,
        "progress": progress,
        "memory": memory,
        "achievement": achievement
    }