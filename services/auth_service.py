import json
import os
import hashlib

USERS_FILE = "data/users.json"


def load_users():
    if not os.path.exists(USERS_FILE):
        return []

    try:
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []


def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def generate_student_id():
    users = load_users()

    if not users:
        return "ASTRA-000001"

    last_id = users[-1]["student_id"]

    number = int(last_id.split("-")[1]) + 1

    return f"ASTRA-{number:06d}"


def register_user(name, student_class, password):
    users = load_users()

    student_id = generate_student_id()

    user = {
        "student_id": student_id,
        "name": name,
        "class": student_class,
        "password": hash_password(password),
        "xp": 0,
        "level": 1,
        "badges": [],
        "study_streak": 0,
        "completed_quizzes": 0,
        "uploaded_pdfs": 0,
        "daily_goal": 2,
        "weak_subject": "",
        "target_exam": "",
        "exam_date": ""
    }

    users.append(user)

    save_users(users)

    return student_id


def login_user(student_id, password):
    users = load_users()

    hashed = hash_password(password)

    for user in users:
        if (
            user["student_id"] == student_id
            and user["password"] == hashed
        ):
            return user

    return None


def get_user(student_id):
    users = load_users()

    for user in users:
        if user["student_id"] == student_id:
            return user

    return None


def update_user(updated_user):
    users = load_users()

    for i, user in enumerate(users):
        if user["student_id"] == updated_user["student_id"]:
            users[i] = updated_user
            break

    save_users(users)
def save_current_user(user):
    users = load_users()

    for i, u in enumerate(users):
        if u["student_id"] == user["student_id"]:
            users[i] = user
            break

    save_users(users)


def current_user():
    import streamlit as st

    if "user" in st.session_state:
        return st.session_state.user

    return None