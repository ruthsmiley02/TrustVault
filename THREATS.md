# TrustVault – Security Threat Analysis

## 1. Introduction

TrustVault is a Flask-based file storage and management application. This document describes potential security threats and the security measures implemented in the project.

## 2. Identified Security Threats

### 2.1 Unauthorized Access
**Threat:** An unauthorized person may attempt to access another user's account or documents.

**Protection implemented:**
- Login authentication is required.
- User sessions are used to maintain login status.
- Document ownership is checked before downloading files.

### 2.2 Password Theft
**Threat:** Passwords may be exposed if stored as plain text.

**Protection implemented:**
- Passwords are hashed using Werkzeug security functions.
- Password verification uses secure password-checking functions.

### 2.3 Malicious File Uploads
**Threat:** Users may upload files containing harmful content or unexpected file types.

**Protection implemented:**
- Allowed file extensions are restricted to PDF, DOCX, JPG, JPEG, and PNG.
- Secure filenames are used.
- The maximum upload size is limited to 5 MB.

**Limitation:** Extension validation alone cannot guarantee that a file is safe. Additional file-content and malware scanning can be added in future versions.

### 2.4 Unauthorized Document Download
**Threat:** A user may try to download another user's private document.

**Protection implemented:**
- The application checks document ownership before allowing downloads.
- Unauthorized download attempts are recorded in audit logs.

### 2.5 Session Security
**Threat:** An attacker may attempt to misuse a logged-in user's session.

**Protection implemented:**
- Flask sessions are used for authentication.
- A secret key is used to protect session data.

**Limitation:** Production deployment should use a strong environment-provided secret key and secure cookie settings.

### 2.6 Audit Log Tampering
**Threat:** Someone may attempt to modify or delete audit log records.

**Protection implemented:**
- Important user activities are recorded in JSON audit logs.
- Access to the audit log page is restricted to administrators.

**Limitation:** Local JSON logs are not tamper-proof. Stronger protection can be added using protected storage or centralized logging.

## 3. Additional Security Improvements

The following improvements are recommended for future versions:

- Add CSRF protection to forms.
- Add file-content validation and malware scanning.
- Use secure session cookie settings.
- Remove the default development secret key.
- Disable debug mode in production.
- Use a production-ready web server.
- Protect stored data with suitable access permissions.

## 4. Conclusion

TrustVault implements basic security measures such as password hashing, authentication, file validation, ownership checks, role-based audit log access, and activity logging. Further security improvements are necessary before using the application in a real production environment.