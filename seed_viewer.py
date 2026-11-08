import json
import secrets
from pathlib import Path
from werkzeug.security import generate_password_hash

users_file = Path(__file__).parent / "data" / "users.json"

with open(users_file, "r", encoding="utf-8") as file:
    users = json.load(file)

username = "viewer123"

if any(user["username"] == username for user in users):
    print("Viewer account already exists.")
else:
    password = secrets.token_urlsafe(12)

    users.append({
        "username": username,
        "password": generate_password_hash(password),
        "role": "viewer"
    })

    with open(users_file, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)

    print("Viewer account created successfully!")
    print("Username:", username)
    print("Password:", password)