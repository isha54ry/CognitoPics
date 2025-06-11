
# Smart Gallery

Smart Gallery is a privacy-focused, AI-powered photo gallery application that uses facial recognition 
to detect and match faces within a user's photo collection. It allows users to hide selected images in 
a password-protected vault using AES encryption, ensuring sensitive images remain private. 

Built with Python and Streamlit, the app features a responsive and modern UI with organized tabs, 
image previews, and smooth navigation. All operations, including encryption and decryption, are 
handled locally, and no internet or cloud storage is involved — making Smart Gallery a secure, 
offline-first solution for personal photo management.


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

Let me know if you want a version that includes images, GIF demos, or deployment instructions!

