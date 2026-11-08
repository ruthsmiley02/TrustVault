# TrustVault – Security Threat Analysis

## 1. Introduction

TrustVault is a Flask-based file storage and management application. It allows authenticated users to upload, download, share, and manage documents with access permissions.

This document describes potential security threats, implemented security measures, known limitations, and recommended improvements.

## 2. Identified Security Threats

### 2.1 Unauthorized Access

**Threat:** An unauthorized person may attempt to access another user's account or protected documents.

**Protection implemented:**
- Login authentication is required to access protected pages.
- User sessions are used to maintain login status.
- Document ownership and sharing permissions are checked before allowing access.

### 2.2 Password Theft

**Threat:** Passwords may be exposed if stored as plain text.

**Protection implemented:**
- Passwords are hashed using Werkzeug security functions.
- Password verification uses secure password-checking functions.
- Plain-text passwords are not stored in the user records.

### 2.3 Malicious File Uploads

**Threat:** Users may upload files containing harmful content or unexpected file types.

**Protection implemented:**
- Allowed file extensions are restricted to PDF, DOCX, JPG, JPEG, and PNG.
- Secure filenames are used.
- The maximum upload size is limited to 5 MB.

**Limitation:** Extension validation alone cannot guarantee that a file is safe. Additional file-content validation and malware scanning can be added in future versions.

### 2.4 Unauthorized Document Download

**Threat:** A user may try to download another user's private document without permission.

**Protection implemented:**
- The application checks document ownership before allowing downloads.
- Users with read or edit permission can download shared documents.
- Unauthorized download attempts are recorded in audit logs.

### 2.5 Session Security

**Threat:** An attacker may attempt to misuse a logged-in user's session.

**Protection implemented:**
- Flask sessions are used for authentication.
- A secret key is used to protect session data.
- Sessions are cleared during logout.

**Limitation:** Production deployment should use a strong environment-provided secret key and secure cookie settings.

### 2.6 Audit Log Tampering

**Threat:** Someone may attempt to modify or delete audit log records.

**Protection implemented:**
- Important user activities are recorded in JSON audit logs.
- Access to the audit log page is restricted to administrators.
- Unauthorized access attempts are recorded.

**Limitation:** Local JSON logs are not tamper-proof. Stronger protection can be added using protected storage or centralized logging.

### 2.7 Unauthorized Document Deletion

**Threat:** A user may attempt to delete a document owned by another user.

**Protection implemented:**
- Only the document owner can delete a document.
- The application checks document ownership before deletion.
- Unauthorized deletion attempts are recorded in audit logs.

### 2.8 Unauthorized Document Sharing

**Threat:** A user may attempt to share another user's document without permission.

**Protection implemented:**
- Only the document owner can grant sharing permissions.
- Users can be assigned read or edit permissions.
- Unauthorized sharing attempts are recorded in audit logs.

### 2.9 Path Traversal

**Threat:** An attacker may attempt to access files outside the permitted upload directory by manipulating filenames or file paths.

**Protection implemented:**
- Secure filenames are generated during file uploads.
- Stored filenames are validated before accessing files.
- File downloads are restricted to the configured upload directory.

### 2.10 Unauthorized Audit Log Access

**Threat:** Ordinary users may attempt to view sensitive document activity and user records.

**Protection implemented:**
- The audit log route is protected by administrator authorization.
- Normal users are redirected when they attempt to access the audit log page.

## 3. Security Testing

Automated security tests using pytest verify the following:

1. Application imports successfully.
2. Dashboard authentication is required.
3. Unauthorized document downloads are blocked.
4. Unauthorized document deletion is blocked.
5. Unauthorized document sharing is blocked.
6. Normal users cannot access administrator audit logs.

All six current automated tests passed during testing.

## 4. Additional Security Improvements

The following improvements are recommended for future versions:

- Add CSRF protection to forms.
- Add file-content validation and malware scanning.
- Use secure session cookie settings.
- Remove the default development secret key.
- Disable debug mode in production.
- Use a production-ready web server.
- Protect stored data with suitable access permissions.
- Consider migrating JSON storage to a database.
- Implement tamper-resistant audit logging.
- Add automated tests for additional authentication and permission scenarios.

## 5. Known Limitations

- JSON files are currently used for data storage instead of a relational database.
- Audit logs are stored in JSON files and are not tamper-proof.
- File extension validation does not guarantee that uploaded files are free from malware.
- Production deployment requires secure secret-key configuration.
- Additional protections such as CSRF protection and stronger production file-storage controls are needed.

## 6. Conclusion

TrustVault implements important security measures such as password hashing, authentication, file validation, document ownership checks, sharing permissions, administrator-restricted audit logs, and activity logging.

Automated security tests help verify important access-control restrictions. Further improvements are necessary before using the application in a real production environment.