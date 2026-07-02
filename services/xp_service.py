import streamlit as st
from services.auth_service import current_user, save_current_user
from services.achievement_service import check_achievements


def add_xp(points):

    user = current_user()

    if user is None:
        return

    old_level = user.get("level", 1)

    user["xp"] = user.get("xp", 0) + points

    user["level"] = (user["xp"] // 100) + 1

    save_current_user(user)

    st.session_state.user = user
    check_achievements()

    st.toast(f"⭐ +{points} XP Earned!")

    if user["level"] > old_level:

        st.balloons()

        st.success(
            f"🎉 Congratulations! You reached Level {user['level']}!"
        )