
from flask import (
    Flask, render_template, request, redirect,
    url_for, session, flash, send_from_directory
)

from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

from pathlib import Path
from datetime import datetime
import json
import os
import uuid


# --------------------------------
# 1. FLASK APPLICATION
# --------------------------------

app = Flask(__name__)

app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024


app.secret_key = os.environ.get(
    "TRUSTVAULT_SECRET_KEY",
    "trustvault_demo_secret_key"
)


# --------------------------------
# 2. PROJECT FOLDERS
# --------------------------------

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
UPLOAD_FOLDER = BASE_DIR / "uploads"

ALLOWED_EXTENSIONS = {"pdf", "docx", "jpg", "jpeg", "png"}

def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


DATA_DIR.mkdir(exist_ok=True)
UPLOAD_FOLDER.mkdir(exist_ok=True)


# --------------------------------
# 3. JSON FILE LOCATIONS
# --------------------------------

USERS_FILE = DATA_DIR / "users.json"
DOCUMENTS_FILE = DATA_DIR / "documents.json"
AUDIT_LOGS_FILE = DATA_DIR / "audit_logs.json"

for file_path in [
    USERS_FILE,
    DOCUMENTS_FILE,
    AUDIT_LOGS_FILE
]:
    if not file_path.exists():
        file_path.write_text("[]", encoding="utf-8")


# --------------------------------
# 4. JSON FILE FUNCTIONS
# --------------------------------

def load_users():
    with open(USERS_FILE, "r", encoding="utf-8") as file:
        users = json.load(file)

    if not isinstance(users, list):
        raise ValueError("users.json must contain a list.")

    return users


def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)


def load_documents():
    try:
        with open(DOCUMENTS_FILE, "r", encoding="utf-8") as file:
            documents = json.load(file)

        return documents if isinstance(documents, list) else []

    except json.JSONDecodeError:
        raise RuntimeError("documents.json contains invalid JSON.")


def save_documents(documents):
    with open(DOCUMENTS_FILE, "w", encoding="utf-8") as file:
        json.dump(documents, file, indent=4)


# --------------------------------
# 5. AUDIT LOG FUNCTION
# --------------------------------

def add_audit_log(username, action, details=""):

    try:
        with open(AUDIT_LOGS_FILE, "r", encoding="utf-8") as file:
            logs = json.load(file)

        if not isinstance(logs, list):
            logs = []

    except (FileNotFoundError, json.JSONDecodeError):
        logs = []

    log_entry = {
        "username": username,
        "action": action,
        "details": details,
        "timestamp": datetime.now().isoformat()
    }

    logs.append(log_entry)

    with open(AUDIT_LOGS_FILE, "w", encoding="utf-8") as file:
        json.dump(logs, file, indent=4)


# --------------------------------
# 6. ADMIN ACCESS CHECK
# --------------------------------

def admin_required():

    if "username" not in session:
        return redirect(url_for("login"))

    if session.get("role") != "admin":
        flash("Access denied. Admin permission required.")
        return redirect(url_for("dashboard"))

    return None


# --------------------------------
# 7. HOME PAGE
# --------------------------------

@app.route("/")
def home():

    if "username" in session:
        return redirect(url_for("dashboard"))

    return redirect(url_for("login"))


# --------------------------------
# 8. USER REGISTRATION
# --------------------------------

@app.route("/register", methods=["GET", "POST"])
def register():
    

    if request.method == "POST":

        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        if not username or not password:
            flash("Please enter username and password.")
            return render_template("register.html")

        if len(password) < 8:
            flash("Password must contain at least 8 characters.")
            return render_template("register.html")

        if confirm_password and password != confirm_password:
            flash("Passwords do not match.")
            return render_template("register.html")

        users = load_users()

        # Check duplicate usernames (case-insensitive)
        existing_user = next(
            (
                user for user in users
                if user.get("username", "").casefold() == username.casefold()
            ),
            None
        )

        if existing_user:
            flash("Username already exists. Please choose another username.")
            return render_template("register.html")

        hashed_password = generate_password_hash(password)

        new_user = {
            "username": username,
            "password": hashed_password,
            "role": "user"
        }

        users.append(new_user)
        save_users(users)

        add_audit_log(
            username,
            "REGISTER",
            "New user registered successfully"
        )

        flash("Registration successful. Please login.")

        return redirect(url_for("login"))

    return render_template("register.html")


# --------------------------------
# 9. USER LOGIN
# --------------------------------


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        users = load_users()

        user = next(
            (u for u in users if u.get("username") == username),
            None
        )

        if user and check_password_hash(user["password"], password):

            session.clear()

            session["username"] = username
            session["role"] = user.get("role", "user")

            add_audit_log(
                username,
                "LOGIN",
                "User logged in successfully"
            )

            return redirect(url_for("dashboard"))

        add_audit_log(
            username or "Unknown",
            "LOGIN_FAILED",
            "Invalid username or password"
        )

        flash("Invalid username or password.")

        return redirect(url_for("login"))

    return render_template("login.html")

# --------------------------------
# 10. USER DASHBOARD
# --------------------------------

@app.route("/dashboard")
def dashboard():

    if "username" not in session:
        return redirect(url_for("login"))

    documents = load_documents()

    return render_template(
        "dashboard.html",
        username=session["username"],
        documents=documents,
        role=session.get("role", "user")
    )




# --------------------------------
# 11. DOCUMENT UPLOAD
# --------------------------------

@app.route("/upload", methods=["GET", "POST"])
def upload():

    if "username" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        uploaded_file = (
            request.files.get("file")
            or request.files.get("document")
        )

        if uploaded_file is None or uploaded_file.filename == "":
            flash("Please select a document.")
            return redirect(url_for("upload"))

        original_name = secure_filename(uploaded_file.filename)

        if not original_name:
            flash("Invalid filename.")
            return redirect(url_for("upload"))

        # Check allowed file extensions
        if not allowed_file(original_name):
            flash("Invalid file type. Upload PDF, DOCX, JPG, JPEG or PNG only.")
            return redirect(url_for("upload"))

        document_id = str(uuid.uuid4())

        stored_name = document_id + "_" + original_name

        uploaded_file.save(UPLOAD_FOLDER / stored_name)

        documents = load_documents()

        new_document = {
            "id": document_id,
            "filename": original_name,
            "stored_name": stored_name,
            "owner": session["username"],
            "uploaded_at": datetime.now().isoformat()
        }

        documents.append(new_document)

        save_documents(documents)

        add_audit_log(
            session["username"],
            "DOCUMENT_UPLOAD",
            f"Uploaded document: {original_name}"
        )

        flash("Document uploaded successfully.")

        return redirect(url_for("dashboard"))

    return render_template("upload.html")



# --------------------------------
# 12. SECURE DOCUMENT DOWNLOAD
# --------------------------------

@app.route("/download/<document_id>")
def download_document(document_id):

    if "username" not in session:
        return redirect(url_for("login"))

    documents = load_documents()

    document = next(
        (doc for doc in documents if doc.get("id") == document_id),
        None
    )

    if document is None:
        flash("Document not found.")
        return redirect(url_for("dashboard"))

    if document.get("owner") != session["username"]:

        add_audit_log(
            session["username"],
            "UNAUTHORIZED_DOWNLOAD",
            "Attempted to download another user's document"
        )

        flash("You are not authorized to download this document.")
        return redirect(url_for("dashboard"))

    stored_name = document.get("stored_name", "")

    if not stored_name or Path(stored_name).name != stored_name:
        flash("Invalid stored filename.")
        return redirect(url_for("dashboard"))

    file_path = UPLOAD_FOLDER / stored_name

    if not file_path.is_file():
        flash("The document file could not be found.")
        return redirect(url_for("dashboard"))

    add_audit_log(
        session["username"],
        "DOCUMENT_DOWNLOAD",
        f"Downloaded document: {document.get('filename', stored_name)}"
    )

    return send_from_directory(
        UPLOAD_FOLDER,
        stored_name,
        as_attachment=True,
        download_name=document.get("filename", stored_name)
    )


# --------------------------------
# 13. ADMIN-ONLY AUDIT LOGS
# --------------------------------

@app.route("/audit-logs")
def audit_logs():

    access_check = admin_required()

    if access_check is not None:
        return access_check

    try:
        with open(AUDIT_LOGS_FILE, "r", encoding="utf-8") as file:
            logs = json.load(file)

        if not isinstance(logs, list):
            logs = []

    except (FileNotFoundError, json.JSONDecodeError):
        logs = []

    logs.reverse()

    return render_template(
        "audit_logs.html",
        logs=logs,
        username=session["username"]
    )


# --------------------------------
# 14. USER LOGOUT
# --------------------------------

@app.route("/logout")
def logout():

    if "username" in session:

        username = session["username"]

        add_audit_log(
            username,
            "LOGOUT",
            "User logged out successfully"
        )

        session.clear()

    flash("You have logged out successfully.")

    return redirect(url_for("login"))


# --------------------------------
# 15. RUN APPLICATION
# --------------------------------

if __name__ == "__main__":

    print("================================")
    print(" TRUSTVAULT APPLICATION STARTED ")
    print("================================")

    print("Documents file:", DOCUMENTS_FILE.resolve())
    print("Audit logs file:", AUDIT_LOGS_FILE.resolve())

    app.run(debug=True)
