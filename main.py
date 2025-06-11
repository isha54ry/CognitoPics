import getpass
from face_utils import load_known_faces, find_matching_photos
from gallery_utils import move_matched_photos
from encrypt_utils import set_password, verify_password, encrypt_photos, decrypt_photos

def main():
    print("=== Smart Gallery Privacy Tool ===")

    while True:
        print("\nChoose an option:")
        print("1. Set password")
        print("2. Hide photos of a person")
        print("3. Unlock hidden photos")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            pwd = getpass.getpass("Set a new password: ")
            confirm = getpass.getpass("Confirm password: ")
            if pwd == confirm:
                set_password(pwd)
                print("[INFO] Password set successfully.")
            else:
                print("[ERROR] Passwords do not match.")

        elif choice == "2":
            print("[INFO] Loading known faces from dataset...")
            encodings, names = load_known_faces("dataset")

            if not encodings:
                print("[ERROR] No known faces found. Please add images to the dataset folder.")
                continue

            print("[INFO] Scanning photos...")
            matched_photos = find_matching_photos("photos", encodings)

            if matched_photos:
                print(f"[INFO] Found {len(matched_photos)} matching photos.")
                move_matched_photos(matched_photos, "photos", "locked_photos")
                pwd = getpass.getpass("Enter password to lock photos: ")
                if verify_password(pwd):
                    encrypt_photos("locked_photos", pwd)
                    print("[SUCCESS] Matching photos encrypted and locked.")
                else:
                    print("[ERROR] Incorrect password. Photos were moved but not encrypted.")
            else:
                print("[INFO] No matching photos found.")

        elif choice == "3":
            pwd = getpass.getpass("Enter password to unlock: ")
            if verify_password(pwd):
                decrypt_photos("locked_photos", pwd)
                print("[SUCCESS] Photos unlocked.")
            else:
                print("[ERROR] Incorrect password.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("[ERROR] Invalid option. Please choose 1-4.")

if __name__ == "__main__":
    main()
# This is the main entry point for the Smart Gallery Privacy Tool.
# It provides a command-line interface for users to set a password, hide photos of a person, and unlock hidden photos.