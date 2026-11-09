# TrustVault – Secure File Storage and Management System

## 1. Project Overview

TrustVault is a web-based secure file storage and management application developed using Python and Flask.

It allows users to register, log in, upload, download, organize, search, share, and manage documents with access permissions.

The application includes document ownership verification, per-document read and edit permissions, administrator-only audit logs, and automated security tests.

## 2. Features

### User Authentication
- User registration and login.
- Secure password hashing using Werkzeug.
- Session-based authentication.
- Logout functionality.
- Role-based access control.

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
├── API_DOCUMENTATION.md
├── THREATS.md
├── PROMPTS.md
├── .env.example
├── .gitignore
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
├── uploads/
│
└── tests/
    └── test_security.py
```

**Note:** The `data/` and `uploads/` directories are used for application data and uploaded documents. Private data and uploaded files should not be committed to the public repository.

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
python -m venv .venv
```

### Step 4: Activate the Virtual Environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Configure Environment Variables

Configure the secret key and the administrator and viewer account credentials using the environment variables required by the application.

The `.env.example` file provides the configuration template. Do not commit real passwords or secret keys to GitHub.

For deployment, configure the required environment variables in the hosting provider's environment settings.

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

Maximum upload size: **5 MB**.

The application uses secure filename handling and file extension validation.

## 7. Document Permission Management

TrustVault uses three account roles and additional per-document permissions.

| User type | Permission |
|---|---|
| Administrator (`admin`) | Access administrator audit logs and normal document features |
| Document Owner (`user`) | Manage, download, share, revoke, and delete owned documents |
| Viewer (`viewer`) | Download documents shared with them; cannot upload, share, revoke, or delete |

Per-document sharing permissions:

| Permission | Supported behavior |
|---|---|
| Owner | Manage and share owned documents |
| Read | View document details and download the document |
| Edit | Currently permits downloading, like read permission |

**Implementation limitation:** The current application stores the `edit` permission, but actual document-content editing is not implemented.

## 8. Security Features

- Werkzeug password hashing.
- Session-based authentication.
- Role-based access restrictions.
- Document ownership verification.
- Per-document read/edit sharing permissions.
- Owner-only document deletion.
- Unauthorized access checks.
- File extension validation.
- Secure filename handling.
- Administrator-restricted audit logs.
- Activity logging.

**Security limitation:** Audit records are stored in JSON files and are not tamper-proof.

## 9. Automated Testing

TrustVault uses pytest for automated testing.

Run tests using:

```bash
python -m pytest -v
```

The current test suite contains 11 tests covering:

1. Application import.
2. Dashboard authentication.
3. Unauthorized document download.
4. Unauthorized document deletion.
5. Unauthorized document sharing.
6. Administrator-only audit log access.
7. Viewer upload restriction.
8. Viewer access restriction.
9. Viewer deletion restriction.
10. Viewer sharing restriction.
11. Revoked viewer access restriction.

**Latest recorded test result: 11 passed.**

## 10. Deployment

**Live application:**

https://trustvault-xfv8.onrender.com

**Source code:**

https://github.com/ruthsmiley02/TrustVault

The deployed application requires the appropriate environment variables and suitable storage configuration.

**Deployment note:** Confirm that uploaded files and JSON data are stored persistently. Temporary or ephemeral hosting storage may not retain data across service restarts or redeployments.

## 11. Demo Account Credentials

The challenge requires one demo account for each role.

| Role | Username | Password |
|---|---|---|
| Administrator | `tvadmin` | Add dedicated demo password |
| Document Owner | Add owner username | Add dedicated demo password |
| Viewer | `tvviewer` | Add dedicated demo password |

**Important:** Replace the placeholders with working, dedicated demonstration credentials before submission. Do not publish personal passwords, production secrets, or your environment-variable values.

## 12. Known Limitations

- JSON files are currently used instead of a relational database.
- Audit logs are not tamper-proof.
- Edit permission currently allows downloading rather than modifying document contents.
- Additional production security measures are required.
- Persistent storage must be configured appropriately for deployment.
- Additional integration and security tests would improve coverage.

## 13. Future Enhancements

- Database integration using MySQL or PostgreSQL.
- Two-factor authentication.
- Email notifications.
- Advanced file encryption.
- Malware scanning.
- Improved administrator dashboard.
- Cloud-based document storage.
- Tamper-resistant audit logging.
- Direct document editing with appropriate permissions.

## 14. Conclusion

TrustVault provides a Flask-based document management system with authentication, role-based access restrictions, document sharing, access revocation, file validation, and activity monitoring.

Automated security tests verify important access-control restrictions. The project can be extended with database integration and additional production security measures.# TrustVault – Secure File Storage and Management System

## 1. Project Overview

TrustVault is a web-based secure file storage and management application developed using Python and Flask.

It allows users to register, log in, upload, download, organize, search, share, and manage documents with access permissions.

The application includes document ownership verification, per-document read and edit permissions, administrator-only audit logs, and automated security tests.

## 2. Features

### User Authentication
- User registration and login.
- Secure password hashing using Werkzeug.
- Session-based authentication.
- Logout functionality.
- Role-based access control.

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
├── API_DOCUMENTATION.md
├── THREATS.md
├── PROMPTS.md
├── .env.example
├── .gitignore
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
├── uploads/
│
└── tests/
    └── test_security.py
```

**Note:** The `data/` and `uploads/` directories are used for application data and uploaded documents. Private data and uploaded files should not be committed to the public repository.

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
python -m venv .venv
```

### Step 4: Activate the Virtual Environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Configure Environment Variables

Configure the secret key and the administrator and viewer account credentials using the environment variables required by the application.

The `.env.example` file provides the configuration template. Do not commit real passwords or secret keys to GitHub.

For deployment, configure the required environment variables in the hosting provider's environment settings.

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

Maximum upload size: **5 MB**.

The application uses secure filename handling and file extension validation.

## 7. Document Permission Management

TrustVault uses three account roles and additional per-document permissions.

| User type | Permission |
|---|---|
| Administrator (`admin`) | Access administrator audit logs and normal document features |
| Document Owner (`user`) | Manage, download, share, revoke, and delete owned documents |
| Viewer (`viewer`) | Download documents shared with them; cannot upload, share, revoke, or delete |

Per-document sharing permissions:

| Permission | Supported behavior |
|---|---|
| Owner | Manage and share owned documents |
| Read | View document details and download the document |
| Edit | Currently permits downloading, like read permission |

**Implementation limitation:** The current application stores the `edit` permission, but actual document-content editing is not implemented.

## 8. Security Features

- Werkzeug password hashing.
- Session-based authentication.
- Role-based access restrictions.
- Document ownership verification.
- Per-document read/edit sharing permissions.
- Owner-only document deletion.
- Unauthorized access checks.
- File extension validation.
- Secure filename handling.
- Administrator-restricted audit logs.
- Activity logging.

**Security limitation:** Audit records are stored in JSON files and are not tamper-proof.

## 9. Automated Testing

TrustVault uses pytest for automated testing.

Run tests using:

```bash
python -m pytest -v
```

The current test suite contains 11 tests covering:

1. Application import.
2. Dashboard authentication.
3. Unauthorized document download.
4. Unauthorized document deletion.
5. Unauthorized document sharing.
6. Administrator-only audit log access.
7. Viewer upload restriction.
8. Viewer access restriction.
9. Viewer deletion restriction.
10. Viewer sharing restriction.
11. Revoked viewer access restriction.

**Latest recorded test result: 11 passed.**

## 10. Deployment

**Live application:**

https://trustvault-xfv8.onrender.com

**Source code:**

https://github.com/ruthsmiley02/TrustVault

The deployed application requires the appropriate environment variables and suitable storage configuration.

**Deployment note:** Confirm that uploaded files and JSON data are stored persistently. Temporary or ephemeral hosting storage may not retain data across service restarts or redeployments.

## 11. Demo Account Credentials

The following accounts are provided for testing the different user roles in TrustVault.

| Role | Username | Password |
|---|---|---|
| Administrator | `tvadmin` | Ruthsmiley@2902 |
| Document Owner | `tvowner` | 123456789 |
| Viewer | `tvviewer` | tvviewer@123|

**Note:** Demo passwords are configured separately through environment variables or account registration. Use dedicated demonstration passwords and do not publish private credentials or application secret keys.

## 12. Known Limitations

- JSON files are currently used instead of a relational database.
- Audit logs are not tamper-proof.
- Edit permission currently allows downloading rather than modifying document contents.
- Additional production security measures are required.
- Persistent storage must be configured appropriately for deployment.
- Additional integration and security tests would improve coverage.

## 13. Future Enhancements

- Database integration using MySQL or PostgreSQL.
- Two-factor authentication.
- Email notifications.
- Advanced file encryption.
- Malware scanning.
- Improved administrator dashboard.
- Cloud-based document storage.
- Tamper-resistant audit logging.
- Direct document editing with appropriate permissions.

## 14. Conclusion

TrustVault provides a Flask-based document management system with authentication, role-based access restrictions, document sharing, access revocation, file validation, and activity monitoring.

Automated security tests verify important access-control restrictions. The project can be extended with database integration and additional production security measures.