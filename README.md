# TrustVault – Secure File Storage and Management System

## 1. Project Overview

TrustVault is a web-based secure file storage and management application developed using Python and Flask. It allows users to register, log in, upload, and download their personal documents securely.

The application also maintains audit logs to record important user activities, helping administrators monitor system usage.

## 2. Features

- User registration and login
- Secure password hashing
- Session-based authentication
- File upload with a 5 MB size limit
- File extension validation
- Secure filename handling
- Users can download only their own documents
- Admin-only audit log access
- Records user activities such as login, logout, upload, and download
- JSON-based data storage

## 3. Technologies Used

- **Programming Language:** Python
- **Framework:** Flask
- **Security:** Werkzeug
- **Data Storage:** JSON
- **Frontend:** HTML and CSS

## 4. Project Structure

```text
TrustVault/
│
├── app.py
├── requirements.txt
├── README.md
├── THREATS.md
├── PROMPTS.md
├── .gitignore
├── .env.example
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── upload.html
│   └── audit_logs.html
│
├── static/
│   └── style.css
│
├── data/
│   ├── users.json
│   ├── documents.json
│   └── audit_logs.json
│
└── uploads/
```

*Note: The data and uploads folders are created locally by the application and are excluded from the public GitHub repository.*

## 5. Installation and Setup

### Step 1: Install Python

Install Python 3 on your computer.

### Step 2: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd TrustVault
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate the Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Configure the Secret Key

Set a strong, private `TRUSTVAULT_SECRET_KEY` environment variable before running the application. Do not publish your actual secret key.

### Step 7: Run the Application

```bash
python app.py
```

Open your browser and visit:

http://127.0.0.1:5000

## 6. File Upload Validation

The application accepts the following file formats:

- PDF
- DOCX
- JPG
- JPEG
- PNG

Maximum upload size: **5 MB**

## 7. Audit Logging

TrustVault records important activities, including:

- User registration
- Successful login
- Failed login
- File upload
- File download
- Unauthorized download attempts
- Logout

Administrators can view the audit logs through the admin audit log page.

## 8. Security Features

- Password hashing using Werkzeug
- Session-based authentication
- File extension validation
- Secure filename handling
- Document ownership verification
- Admin role verification
- Audit logging

## 9. Future Enhancements

- Database integration
- Two-factor authentication
- Email notifications
- Advanced file encryption
- Improved admin dashboard
- Cloud-based