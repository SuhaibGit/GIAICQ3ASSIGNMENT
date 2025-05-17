import streamlit as st
import hashlib
from cryptography.fernet import Fernet

# Initialize session state
if "stored_data" not in st.session_state:
    st.session_state.stored_data = {}

if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0

if "reauthorized" not in st.session_state:
    st.session_state.reauthorized = False

# Generate or load encryption key (stays same during session)
if "fernet_key" not in st.session_state:
    st.session_state.fernet_key = Fernet.generate_key()
    st.session_state.cipher = Fernet(st.session_state.fernet_key)

cipher = st.session_state.cipher

# Hash passkey
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

# Encrypt data
def encrypt_data(text):
    return cipher.encrypt(text.encode()).decode()

# Decrypt data
def decrypt_data(encrypted_text, passkey):
    hashed_passkey = hash_passkey(passkey)

    for value in st.session_state.stored_data.values():
        if value["encrypted_text"] == encrypted_text and value["passkey"] == hashed_passkey:
            st.session_state.failed_attempts = 0
            return cipher.decrypt(encrypted_text.encode()).decode()
    
    st.session_state.failed_attempts += 1
    return None

# UI
st.title("🛡️ Secure Data Encryption System")

menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    st.subheader("🏠 Welcome")
    st.write("This app allows you to securely **store and retrieve data** using a passkey.")

elif choice == "Store Data":
    st.subheader("📂 Store Data")
    user_data = st.text_area("Enter data:")
    passkey = st.text_input("Enter passkey:", type="password")

    if st.button("Encrypt & Save"):
        if user_data and passkey:
            hashed_passkey = hash_passkey(passkey)
            encrypted_text = encrypt_data(user_data)
            unique_key = f"data_{len(st.session_state.stored_data) + 1}"
            st.session_state.stored_data[unique_key] = {
                "encrypted_text": encrypted_text,
                "passkey": hashed_passkey
            }
            st.success("✅ Data encrypted and stored successfully!")
            st.write(f"🔐 Encrypted text (save this to retrieve):\n`{encrypted_text}`")
        else:
            st.error("⚠️ Please enter both data and passkey.")

elif choice == "Retrieve Data":
    if st.session_state.failed_attempts >= 3 and not st.session_state.reauthorized:
        st.warning("🔐 Too many failed attempts. Please login.")
        st.switch_page("Login")

    st.subheader("🔍 Retrieve Data")
    encrypted_text = st.text_area("Paste your encrypted text:")
    passkey = st.text_input("Enter passkey:", type="password")

    if st.button("Decrypt"):
        if encrypted_text and passkey:
            result = decrypt_data(encrypted_text, passkey)

            if result:
                st.success(f"✅ Decrypted Data:\n\n{result}")
            else:
                remaining = 3 - st.session_state.failed_attempts
                st.error(f"❌ Incorrect passkey! Attempts left: {remaining}")
                if st.session_state.failed_attempts >= 3:
                    st.warning("🚫 Too many failed attempts. Redirecting to Login.")
                    st.experimental_rerun()
        else:
            st.error("⚠️ Please provide both encrypted text and passkey.")

elif choice == "Login":
    st.subheader("🔑 Reauthorization")
    master_password = st.text_input("Enter master password:", type="password")

    if st.button("Login"):
        if master_password == "admin123":
            st.session_state.failed_attempts = 0
            st.session_state.reauthorized = True
            st.success("✅ Reauthorized! You can now access 'Retrieve Data'.")
        else:
            st.error("❌ Incorrect master password.")
