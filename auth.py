import hashlib
import os

MASTER_FILE = "master.hash"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def set_master_password():
    password = input("Set Master Password: ")
    hashed = hash_password(password)
    with open(MASTER_FILE, "w") as f:
        f.write(hashed)
    print("Master password set successfully!")

def verify_master_password():
    if not os.path.exists(MASTER_FILE):
        set_master_password()
        return True

    password = input("Enter Master Password: ")
    hashed = hash_password(password)

    with open(MASTER_FILE, "r") as f:
        stored = f.read()

    return hashed == stored