import os
import json
import hashlib
from cryptography.fernet import Fernet
from base64 import urlsafe_b64encode

CONFIG_FILE = "config.json"

def generate_key(password):
    """Generate a symmetric encryption key based on the password."""
    key = hashlib.sha256(password.encode()).digest()
    return urlsafe_b64encode(key)

def set_password(password):
    """Hash and store the password in config.json"""
    hashed = hashlib.sha256(password.encode()).hexdigest()
    with open(CONFIG_FILE, "w") as f:
        json.dump({"password_hash": hashed}, f)

def verify_password(input_password):
    """Verify if entered password matches the stored hash"""
    if not os.path.exists(CONFIG_FILE):
        return False

    with open(CONFIG_FILE, "r") as f:
        data = json.load(f)

    stored_hash = data.get("password_hash")
    input_hash = hashlib.sha256(input_password.encode()).hexdigest()
    return input_hash == stored_hash

def encrypt_photos(folder_path, password):
    """Encrypt all photos in the given folder using the password."""
    key = generate_key(password)
    fernet = Fernet(key)

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "rb") as f:
                data = f.read()

            encrypted = fernet.encrypt(data)
            with open(file_path, "wb") as f:
                f.write(encrypted)

    print("[INFO] All photos encrypted.")

def decrypt_photos(folder_path, password):
    """Decrypt all photos in the given folder using the password."""
    key = generate_key(password)
    fernet = Fernet(key)

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "rb") as f:
                encrypted_data = f.read()

            try:
                decrypted = fernet.decrypt(encrypted_data)
                with open(file_path, "wb") as f:
                    f.write(decrypted)
            except Exception:
                print(f"[ERROR] Decryption failed for {filename}. Possibly incorrect password.")
                continue

    print("[INFO] All photos decrypted (where possible).")
