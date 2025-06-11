
```markdown
# Smart Gallery

Smart Gallery is a privacy-focused AI-powered photo gallery that detects faces in images, allows users to hide selected photos, and stores them securely in a password-protected vault. It includes a clean and modern UI built with Streamlit.

---

## Features

- Face recognition to match uploaded faces against gallery photos
- Secure vault using AES encryption to lock selected photos
- Password-protected decryption to unlock and restore hidden photos
- Interactive and responsive UI with tabbed layout and image previews
- Local storage handling for user images

---

## Tech Stack

- Frontend: Streamlit
- Backend: Python
- Libraries:
  - face_recognition
  - cryptography
  - Pillow
  - streamlit

---

## Folder Structure

```

SmartGallery/
│
├── app.py                  # Main Streamlit app
├── face\_utils.py           # Face detection & recognition functions
├── gallery\_utils.py        # Image grid, upload, and folder utilities
├── encrypt\_utils.py        # AES encryption & decryption logic
├── requirements.txt        # Required Python packages
│
├── dataset/                # Uploaded face images
├── photos/                 # User's gallery photos
├── locked\_photos/          # Encrypted hidden images

````

---

## How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/isha54ry/Smart-Gallery.git
   cd Smart-Gallery
````

2. Create a virtual environment:

   ```bash
   conda create -n smartgallery python=3.10
   conda activate smartgallery
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

---

## Notes

* All encryption and image handling is done locally on the user's device.
* No images are uploaded or stored externally.
* Make sure the required folders (`dataset`, `photos`, `locked_photos`) exist before running.

---

## License

This project is licensed under the MIT License.

```

---

Let me know if you want a version that includes images, GIF demos, or deployment instructions!
```
