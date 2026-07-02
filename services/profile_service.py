import json
import os

PROFILE = "data/student_profile.json"

# Default profile values
DEFAULT_PROFILE = {
    "name": "Student",
    "class": "XII",
    "weak_subject": "Artificial Intelligence",
    "daily_goal": 2,
    "target_exam": "Final Exam",
    "exam_date": "2026-03-01",
    "study_streak": 0,
    "completed_quizzes": 0,
    "uploaded_pdfs": 0
}


def load_profile():
    # Create file if it doesn't exist
    if not os.path.exists(PROFILE):
        save_profile(DEFAULT_PROFILE)
        return DEFAULT_PROFILE

    try:
        with open(PROFILE, "r") as f:
            profile = json.load(f)

        # Add any missing keys automatically
        for key, value in DEFAULT_PROFILE.items():
            profile.setdefault(key, value)

        # Save updated profile if new keys were added
        save_profile(profile)

        return profile

    except Exception:
        save_profile(DEFAULT_PROFILE)
        return DEFAULT_PROFILE


def save_profile(profile):
    os.makedirs("data", exist_ok=True)

    with open(PROFILE, "w") as f:
        json.dump(profile, f, indent=4)