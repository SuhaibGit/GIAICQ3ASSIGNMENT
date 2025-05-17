import streamlit as st
import re
import random
import string
blacklist = {"password", "123456", "password123", "admin", "letmein", "qwerty"}
WEIGHTS = {
    "length": 1.5,
    "case": 1,
    "digit": 1,
    "special": 1.5
}

def check_password_strength(password):
    score = 0
    messages = []

    if password in blacklist:
        return 0, ["❌ This password is too common and easily guessable."]

    if len(password) >= 8:
        score += WEIGHTS["length"]
    else:
        messages.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += WEIGHTS["case"]
    else:
        messages.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += WEIGHTS["digit"]
    else:
        messages.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += WEIGHTS["special"]
    else:
        messages.append("❌ Include at least one special character (!@#$%^&*).")

    return score, messages

def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(length))


st.title("🔐 Password Strength Checker & Generator")

tab1, tab2 = st.tabs(["Check Password", "Generate Password"])

with tab1:
    user_password = st.text_input("Enter your password:", type="password")
    if user_password:
        score, feedback = check_password_strength(user_password)
        st.markdown(f"### 🔎 Strength Score: `{score:.1f} / 5`")

        if score >= 4.5:
            st.success("✅ Strong Password!")
        elif score >= 3:
            st.warning("⚠️ Moderate Password - Improve it for better security.")
        else:
            st.error("❌ Weak Password - Use the suggestions below.")

        for msg in feedback:
            st.write(msg)

with tab2:
    length = st.slider("Choose password length:", 8, 20, 12)
    if st.button("🔁 Generate Password"):
        new_password = generate_strong_password(length)
        st.text_input("Generated Password:", value=new_password, type="default")

