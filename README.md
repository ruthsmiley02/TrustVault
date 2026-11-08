# TrustVault – Secure File Storage and Management System

## 1. Project Overview

TrustVault is a web-based secure file storage and management application developed using Python and Flask.

It allows users to register, log in, upload, download, organize, search, share, and manage documents with access permissions.

The application includes document ownership verification, read/edit sharing permissions, administrator-only audit logs, and automated security tests.

## 2. Features

### User Authentication
- User registration and login.
- Secure password hashing using Werkzeug.
- Session-based authentication.
- Logout functionality.

### Document Management
- Upload and download documents.
- Maximum upload size of 5 MB.
- File extension validation.
- Secure filename handling.
- Document ownership verification.
- Owner-only document deletion.

### Document Sharing
- Share documents with other registered users.
- Grant read or edit permissions.
- Revoke previously granted permissions.
- Prevent unauthorized users from sharing documents.

### Document Search
- Search by filename.
- Filter by document owner.
- Filter by category.
- Filter by upload date.
- Combine multiple search filters.

### Audit Logging
- User registration.
- Successful and failed login attempts.
- Document uploads and downloads.
- Unauthorized download attempts.
- Document deletion.
- Document sharing and permission revocation.
- Logout.
- Administrator-only audit log access.

## 3. Technologies Used

| Component | Technology |
|---|---|
| Programming Language | Python |
| Web Framework | Flask |
| Security | Werkzeug |
| Data Storage | JSON |
| Frontend | HTML, CSS |
| Testing | Pytest |
| Deployment | Render |
| Version Control | Git and GitHub |

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
|--API_DOCUMENTATION.md
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
├── uploads/
│
└── tests/
    └── test_security.py
```

**Note:** The `data` and `uploads` folders are used for application data and uploaded documents. Their actual contents should not be committed publicly.

## 5. Installation and Setup

### Step 1: Install Python

Install Python 3 on your computer.

### Step 2: Clone the Repository

```bash
git clone https://github.com/ruthsmiley02/TrustVault.git
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

Create a `.env` file in the main TrustVault project folder.

Copy the contents of `.env.example` into `.env`.

Generate a strong secret key using:

```bash
python -c "import secrets; print(secrets.token_hex(32))"


### Step 7: Run the Application

```bash
python app.py
```

Open your browser:

http://127.0.0.1:5000

## 6. File Upload Validation

Supported file formats:

- PDF
- DOCX
- JPG
- JPEG
- PNG

Maximum upload size: **5 MB**

The application uses secure filename handling and file extension validation.

## 7. Document Permission Management

TrustVault supports the following access rules:

| User type | Permission |
|---|---|
| Administrator | Access to administrator audit logs |
| Document owner | Manage, download, share, revoke, and delete owned documents |
| Shared user with read permission | Download shared documents |
| Shared user with edit permission | Download shared documents |

**Implementation note:** The current application uses `admin` and `user` account roles. Document ownership and per-document read/edit permissions provide additional access control. Edit permission currently permits downloading; direct file editing is not implemented.

## 8. Security Features

- Werkzeug password hashing.
- Session-based authentication.
- Document ownership verification.
- Read/edit sharing permissions.
- Owner-only document deletion.
- Unauthorized access checks.
- File extension validation.
- Secure filename handling.
- Administrator-restricted audit logs.
- Activity logging.

## 9. Automated Testing

TrustVault uses pytest for automated testing.

Run tests using:

```bash
python -m pytest -v
```

The current test suite contains six tests:

1. Application import test.
2. Dashboard authentication test.
3. Unauthorized document download test.
4. Unauthorized document deletion test.
5. Unauthorized document sharing test.
6. Administrator-only audit log access test.

**Latest recorded result: 6 passed.**

## 10. Deployment

Live application:

https://trustvault-xfv8.onrender.com

Source code:

https://github.com/ruthsmiley02/TrustVault

Deployment requires appropriate environment variables and persistent storage configuration.

## 11. Known Limitations

- JSON files are currently used instead of a relational database.
- Audit logs are not tamper-proof.
- Edit permission currently allows downloading rather than modifying document contents.
- Additional production security measures are required.
- Persistent storage must be configured appropriately for deployment.

## 12. Future Enhancements

- Database integration.
- Two-factor authentication.
- Email notifications.
- Advanced file encryption.
- Malware scanning.
- Improved administrator dashboard.
- Cloud-based document storage.
- Tamper-resistant audit logging.
- Direct document editing with appropriate permissions.

## 13. Conclusion

TrustVault provides a secure foundation for document storage and sharing through authentication, ownership checks, access permissions, file validation, and audit logging.

Automated security tests verify important access-control restrictions. The project can be extended with database integration and additional production security measures.