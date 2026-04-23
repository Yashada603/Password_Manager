import json
import os
from crypto_utils import encrypt_data, decrypt_data

DATA_FILE = "vault.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_password(site, username, password):
    data = load_data()
    encrypted_pass = encrypt_data(password)
    data[site] = {"username": username, "password": encrypted_pass}
    save_data(data)

def get_password(site):
    data = load_data()
    if site in data:
        decrypted = decrypt_data(data[site]["password"])
        return data[site]["username"], decrypted
    return None, None

def delete_password(site):
    data = load_data()
    if site in data:
        del data[site]
        save_data(data)
        return True
    return False