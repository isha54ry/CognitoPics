import streamlit as st
import os
import shutil
from face_utils import load_known_faces, find_matching_photos
from gallery_utils import move_matched_photos
from encrypt_utils import set_password, verify_password, encrypt_photos, decrypt_photos

# Ensure folders exist
for folder in ["dataset", "photos", "locked_photos"]:
    os.makedirs(folder, exist_ok=True)
st.set_page_config(page_title="Smart Gallery", layout="wide")
# Custom CSS for background and styling
st.markdown("""
    <style>
        body {
            background-color: #f2f6fc;
        }
        .main {
            background-color: #ffffff;
            border-radius: 12px;
            padding: 2rem;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        h1, h2 {
            color: #2c3e50;
        }
        .stButton button {
            background-color: #1f77b4;
            color: white;
            border-radius: 8px;
            height: 3em;
            width: 100%;
        }
        .stButton button:hover {
            background-color: #155c9e;
        }
    </style>
""", unsafe_allow_html=True)

# Page title

st.markdown("<div class='main'>", unsafe_allow_html=True)
st.title(" Smart Gallery")
st.caption(" Protect your privacy by hiding and encrypting photos of selected individuals.")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    " Upload Faces",
    " Upload Gallery",
    " Hide Faces",
    " Unlock Photos"
])

# Tab 1: Upload Faces
with tab1:
    st.header("Upload Face Images for Detection (dataset/)")
    uploaded_faces = st.file_uploader("Upload 1-3 clear face images of the person you want to hide", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
    if uploaded_faces:
        for img in uploaded_faces:
            with open(os.path.join("dataset", img.name), "wb") as f:
                f.write(img.getbuffer())
        st.success(f" Uploaded {len(uploaded_faces)} face image(s).")

# Tab 2: Upload Gallery
with tab2:
    st.header("Upload Gallery Photos (photos/)")
    uploaded_gallery = st.file_uploader("Upload gallery photos to scan", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
    if uploaded_gallery:
        for img in uploaded_gallery:
            with open(os.path.join("photos", img.name), "wb") as f:
                f.write(img.getbuffer())
        st.success(f" Uploaded {len(uploaded_gallery)} photo(s).")

# Tab 3: Hide Photos
with tab3:
    st.header("Detect & Hide Matching Photos")
    st.markdown("**🔑 Set a password to encrypt matched photos**")
    password = st.text_input("Enter password", type="password")
    confirm_pwd = st.text_input("Confirm password", type="password")

    if st.button("🔒 Hide and Encrypt"):
        if not password or password != confirm_pwd:
            st.error("❌ Passwords do not match or are empty.")
        else:
            set_password(password)
            encodings, names = load_known_faces("dataset")
            if not encodings:
                st.warning("⚠️ No face data found. Please upload face images first.")
            else:
                matched_photos = find_matching_photos("photos", encodings)
                if matched_photos:
                    move_matched_photos(matched_photos, "photos", "locked_photos")
                    encrypt_photos("locked_photos", password)
                    st.success(f"🔐 {len(matched_photos)} photo(s) matched, encrypted, and hidden successfully.")
                else:
                    st.info("✅ No matching faces found in gallery.")

# Tab 4: Unlock Photos
with tab4:
    st.header("Unlock Hidden Photos")
    st.markdown("**🔓 Enter your password to decrypt hidden photos**")
    unlock_pwd = st.text_input("Password", type="password")
    if st.button("🔓 Unlock Photos"):
        if verify_password(unlock_pwd):
            decrypt_photos("locked_photos", unlock_pwd)
            st.success("✅ Photos successfully decrypted.")
        else:
            st.error("❌ Incorrect password. Try again.")

st.markdown("</div>", unsafe_allow_html=True)
