import os
import shutil

def ensure_folder(folder_path):
    """Create the folder if it doesn't exist."""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def move_matched_photos(matched_filenames, source_folder, destination_folder):
    """Move the matched photos to a secure folder."""
    ensure_folder(destination_folder)

    for filename in matched_filenames:
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)

        if not os.path.exists(destination_path):
            shutil.move(source_path, destination_path)
            print(f"[INFO] Moved: {filename}")
        else:
            print(f"[SKIP] Already exists: {filename}")
