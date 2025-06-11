
# CognitoPics

CognitoPics is a privacy-focused, AI-powered photo gallery application that uses facial recognition 
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
##  Future Enhancements

The Smart Gallery project is designed with scalability and innovation in mind. Below are some planned improvements and advanced features to be integrated in future iterations:

- **Mobile App UI Integration**  
  Develop a dedicated mobile interface to bring Smart Gallery features to Android/iOS platforms for enhanced accessibility and convenience.

- **Visual Redesign (Locker / Netflix-style UI)**  
  Implement a more engaging and immersive user interface with thematic layouts like a secure photo locker or a Netflix-style image grid for better visual appeal.

- **Backend Migration to Flask or FastAPI**  
  Shift to a backend framework like Flask for more flexibility, allowing features like user authentication, file management APIs, and deeper customization.

- **Login System & Multi-user Support**  
  Add secure user authentication to personalize and isolate vaults, enabling safe usage across different users.

- **Cloud Storage Option**  
  Integrate encrypted cloud storage (like AWS S3 or Firebase) for secure remote backups, while maintaining privacy-first principles.

- **Face Blur / Auto-Hide Filters**  
  Introduce optional filters to auto-blur or conceal sensitive faces dynamically based on user-defined rules.

- **Activity Logs and Notifications**  
  Log important events like image uploads or unlock attempts and provide basic notifications or audit trails.



## Notes

* All encryption and image handling is done locally on the user's device.
* No images are uploaded or stored externally.
* Make sure the required folders (`dataset`, `photos`, `locked_photos`) exist before running.
* Make sure to install all dependencies using:
```bash
   pip install -r requirements.txt
   ```


---

## License

This project is licensed under the MIT License.

Let me know if you want a version that includes images, GIF demos, or deployment instructions!

