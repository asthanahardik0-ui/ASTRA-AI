import streamlit as st
from services.auth_service import current_user, save_current_user


def check_achievements():

    user = current_user()

    if user is None:
        return

    badges = user.get("badges", [])

    unlocked = []

    # -------------------------
    # XP Achievements
    # -------------------------

    if user["xp"] >= 50 and "🥉 Beginner" not in badges:
        badges.append("🥉 Beginner")
        unlocked.append("🥉 Beginner")

    if user["xp"] >= 100 and "🥈 Learner" not in badges:
        badges.append("🥈 Learner")
        unlocked.append("🥈 Learner")

    if user["xp"] >= 250 and "🥇 Dedicated Student" not in badges:
        badges.append("🥇 Dedicated Student")
        unlocked.append("🥇 Dedicated Student")

    if user["xp"] >= 500 and "🏆 ASTRA Master" not in badges:
        badges.append("🏆 ASTRA Master")
        unlocked.append("🏆 ASTRA Master")

    if user["xp"] >= 1000 and "👑 ASTRA Legend" not in badges:
        badges.append("👑 ASTRA Legend")
        unlocked.append("👑 ASTRA Legend")

    # -------------------------
    # Save
    # -------------------------

    user["badges"] = badges

    save_current_user(user)

    st.session_state.user = user

    # -------------------------
    # Show Achievement Popup
    # -------------------------

    for badge in unlocked:

        st.balloons()

        st.success(f"🎉 Achievement Unlocked!\n\n{badge}")