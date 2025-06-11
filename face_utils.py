import face_recognition
import os
import cv2

def load_known_faces(dataset_path):
    known_encodings = []
    known_names = []

    for filename in os.listdir(dataset_path):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(dataset_path, filename)
            image = face_recognition.load_image_file(image_path)
            encodings = face_recognition.face_encodings(image)

            if encodings:
                known_encodings.append(encodings[0])
                known_names.append(os.path.splitext(filename)[0])
            else:
                print(f"[WARNING] No faces found in {filename}, skipping.")

    return known_encodings, known_names


def find_matching_photos(photo_dir, known_encodings, tolerance=0.5):
    matched_photos = []

    for filename in os.listdir(photo_dir):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            path = os.path.join(photo_dir, filename)
            image = face_recognition.load_image_file(path)
            encodings = face_recognition.face_encodings(image)

            for face_encoding in encodings:
                matches = face_recognition.compare_faces(known_encodings, face_encoding, tolerance)
                if True in matches:
                    matched_photos.append(filename)
                    break  # If one face matches, no need to check others in the same photo

    return matched_photos
