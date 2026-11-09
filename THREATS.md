# TrustVault – Security Threat Analysis

## 1. Introduction

TrustVault is a Flask-based secure file storage and management application. It allows authenticated users to upload, download, share, and manage documents with role-based and document-level access permissions.

This document identifies potential security threats, describes the security measures implemented in the application, records known limitations, and recommends future improvements.

## 2. Identified Security Threats

### 2.1 Unauthorized Access

**Threat:**

An unauthorized person may attempt to access another user's account, dashboard, or protected documents.

**Protection implemented:**

- Login authentication is required to access protected application pages.
- Flask sessions are used to maintain authentication status.
- Document ownership and sharing permissions are checked before allowing access.
- Administrator-only functionality is protected using role-based authorization.

**Known limitation:**

Further security testing is required to cover every possible unauthorized access scenario.

### 2.2 Password Theft

**Threat:**

Passwords may be exposed if they are stored as plain text or handled insecurely.

**Protection implemented:**

- Passwords are hashed using Werkzeug security functions.
- Password verification uses secure password-checking functions.
- Plain-text passwords are not stored in user records.

**Known limitation:**

Additional protections such as password reset security, account lockout, and multi-factor authentication can be introduced in future versions.

### 2.3 Malicious File Uploads

**Threat:**

Users may upload harmful files, unexpected file types, or excessively large files.

**Protection implemented:**

- Allowed file extensions are restricted to PDF, DOCX, JPG, JPEG, and PNG.
- Secure filenames are generated using Werkzeug's `secure_filename()`.
- The maximum upload size is limited to 5 MB.
- Server-side validation is performed before accepting uploads.

**Known limitation:**

Extension validation alone cannot guarantee that an uploaded file is safe. File-content verification and malware scanning are recommended future improvements.

### 2.4 Unauthorized Document Download

**Threat:**

A user may attempt to download another user's private document without permission.

**Protection implemented:**

- Document ownership is checked before allowing downloads.
- Users with valid read or edit sharing permissions can download shared documents.
- Unauthorized download attempts are recorded in audit logs.

**Known limitation:**

Additional testing is recommended for different document-sharing and permission combinations.

### 2.5 Session Security

**Threat:**

An attacker may attempt to misuse a logged-in user's session.

**Protection implemented:**

- Flask sessions are used for authentication.
- A secret key is used to protect session data.
- Sessions are cleared during logout.
- Protected routes require authentication.

**Known limitation:**

Production deployment should use a strong environment-provided secret key, HTTPS, and secure session-cookie settings such as `Secure`, `HttpOnly`, and `SameSite`.

### 2.6 Audit Log Tampering

**Threat:**

An attacker or unauthorized person may attempt to modify or delete audit-log records to hide application activities.

**Protection implemented:**

- Important application activities are recorded in JSON audit logs.
- Access to the audit-log page is restricted to administrators.
- Unauthorized access attempts are recorded where supported by the application.

**Known limitation:**

JSON audit logs are not tamper-proof. A person with sufficient access to the stored files may modify or delete records.

Future versions should use centralized logging, restricted append-only storage, or cryptographically protected audit records.

### 2.7 Unauthorized Document Deletion

**Threat:**

A user may attempt to delete a document owned by another user.

**Protection implemented:**

- Only the document owner is permitted to delete an owned document.
- Server-side ownership checks are performed before deletion.
- Unauthorized deletion attempts are recorded in audit logs.

**Known limitation:**

Additional testing should cover deletion attempts involving different user roles and document-sharing states.

### 2.8 Unauthorized Document Sharing

**Threat:**

A user may attempt to share another user's document or modify permissions without authorization.

**Protection implemented:**

- Only the document owner can grant sharing permissions.
- Named users can receive read or edit permission selections.
- Owners can revoke previously granted access.
- Unauthorized sharing attempts are restricted and recorded in audit logs.

**Known limitation:**

The edit permission selection does not currently provide actual document editing. Shared edit access currently permits downloading, and direct document modification is not implemented.

### 2.9 Path Traversal

**Threat:**

An attacker may attempt to access files outside the permitted upload directory by manipulating filenames or file paths.

**Protection implemented:**

- Uploaded filenames are processed using Werkzeug's secure filename handling.
- File access is restricted through the application's configured upload directory and document-access logic.

**Known limitation:**

Secure filename handling alone does not guarantee complete path-traversal protection. Additional path validation and security testing should be performed for every file-access operation.

### 2.10 Unauthorized Audit Log Access

**Threat:**

Ordinary users may attempt to view sensitive application activity, document access records, and user-related information.

**Protection implemented:**

- The audit-log route is protected by administrator authorization.
- Normal users are not permitted to access administrator-only audit information.
- Automated security tests check unauthorized audit-log access.

**Known limitation:**

Additional tests should be performed for every administrative route and sensitive information endpoint.

## 3. Security Testing

Automated security tests using pytest were developed to verify important application security controls.

The latest reported test result during development was:

**11 tests passed.**

The security test coverage includes:

1. Application import and initialization.
2. Authentication requirements for protected pages.
3. Unauthorized document download restrictions.
4. Unauthorized document deletion restrictions.
5. Unauthorized document sharing restrictions.
6. Administrator-only audit-log access.
7. Viewer restrictions on document uploads.
8. Viewer restrictions on unshared document downloads.
9. Viewer restrictions on deletion and sharing.
10. Access denial after shared permission is revoked.
11. Additional cross-user and role-based access restrictions.

Manual testing was also performed on the deployed application.

The following scenarios were checked:

- Administrator login.
- Viewer login.
- Viewer dashboard restrictions.
- Owner sharing a document with the viewer.
- Viewer accessing and downloading a shared document.
- Owner revoking the viewer's access.
- Viewer losing access after revocation.

**Testing limitation:**

Automated and manual tests do not prove that every possible security vulnerability has been eliminated. Additional security testing is recommended.

## 4. Security Improvements Recommended

The following improvements are recommended for future versions:

- Add CSRF protection to application forms.
- Add file-content validation and malware scanning.
- Configure secure session-cookie settings.
- Ensure production uses a strong environment-provided secret key.
- Disable Flask debug mode in production.
- Use HTTPS for all application communication.
- Use a production-ready web server.
- Protect stored files and application data using appropriate access permissions.
- Consider migrating JSON storage to a relational database.
- Implement tamper-resistant audit logging.
- Add additional automated authorization and permission tests.
- Implement actual document editing for shared edit permissions.
- Introduce stronger backup and recovery mechanisms.

## 5. Known Project Limitations

The current version of TrustVault has the following limitations:

1. JSON files are used for application data storage instead of a relational database.
2. JSON audit logs are not tamper-proof.
3. File extension validation does not guarantee uploaded files are free from malware.
4. Shared edit permission does not currently support actual document editing.
5. Additional production security protections, including CSRF protection and secure cookie configuration, are recommended.
6. Further testing is required to establish complete coverage of every search filter and authorization scenario.
7. Deployment on temporary or free hosting storage may require additional persistent storage and backup configuration.

These limitations are documented honestly so that implemented functionality is not confused with proposed future improvements.

## 6. Conclusion

TrustVault implements important security measures, including password hashing, user authentication, document ownership checks, role-based authorization, file-upload validation, document-sharing permissions, access revocation, administrator-restricted audit logs, and activity logging.

Automated security tests and manual deployment checks help verify important application security controls.

However, additional improvements are required before using the application in a production environment. These include tamper-resistant audit logging, stronger file validation, actual document editing, and additional security testing.

TrustVault demonstrates the practical implementation of secure file management concepts while clearly identifying its current limitations and future security improvements.