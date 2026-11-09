# TrustVault – API and Route Documentation

## 1. Project Overview

TrustVault is a secure document storage and management application developed using Python and Flask.

The application uses Flask routes to handle authentication, document uploads, downloads, sharing, deletion, and audit logging.

## 2. Authentication

TrustVault uses session-based authentication.

- Users must log in before accessing protected routes.
- Passwords are stored as secure hashes using Werkzeug.
- User roles are stored in the session after successful login.
- Unauthorized users are redirected to the login or dashboard page.

## 3. User Roles

| Role | Permissions |
|---|---|
| Administrator | Access administrator audit logs and normal document features |
| Document Owner (`user`) | Upload, download, share, revoke access, and delete owned documents |
| Viewer | Download documents shared with them; cannot upload, share, revoke, or delete |

**Note:** In the current implementation, document owners use the account role `user`. Ownership is determined by the document's `owner` field.

## 4. Application Routes

### 4.1 Registration

**Endpoint:** `/register`  
**Methods:** GET, POST  
**Authorization:** Public

**Purpose:**
- Displays the registration form.
- Creates a new user account.
- Validates username and password.
- Hashes the password before storing it.
- Assigns the default `user` role.

### 4.2 Login

**Endpoint:** `/login`  
**Methods:** GET, POST  
**Authorization:** Public

**Purpose:**
- Displays the login form.
- Validates user credentials.
- Creates an authenticated session.
- Stores username and role in the session.
- Records successful and failed login attempts.

### 4.3 Dashboard

**Endpoint:** `/dashboard`  
**Methods:** GET  
**Authorization:** Authenticated users

**Purpose:**
- Displays the user's dashboard.
- Shows documents owned by the user and documents shared with them.
- Supports document search and filtering by:
  - Filename
  - Document owner
  - Category
  - Upload date
- Hides owner-only controls from viewers.

### 4.4 Upload Document

**Endpoint:** `/upload`  
**Methods:** GET, POST  
**Authorization:** Authenticated document owners; viewers are denied.

**Purpose:**
- Displays the upload form.
- Accepts supported document files.
- Validates file extensions and file size.
- Stores uploaded files securely.
- Records upload activity in the audit log.

### 4.5 Download Document

**Endpoint:** `/download/<document_id>`  
**Methods:** GET  
**Authorization:** Document owner or user with `read` or `edit` sharing permission.

**Purpose:**
- Checks document ownership and sharing permissions.
- Prevents unauthorized downloads.
- Records successful and unauthorized download attempts.

### 4.6 Share Document

**Endpoint:** `/share/<document_id>`  
**Methods:** POST  
**Authorization:** Document owner only; viewers are denied.

**Purpose:**
- Allows an owner to share a document with another registered user.
- Supports `read` and `edit` permission values.
- Records sharing activity.

### 4.7 Revoke Document Access

**Endpoint:** `/revoke/<document_id>`  
**Methods:** POST  
**Authorization:** Document owner only; viewers are denied.

**Purpose:**
- Removes a user's sharing permission.
- Prevents further access after revocation.
- Records access revocation in the audit log.

### 4.8 Delete Document

**Endpoint:** `/delete/<document_id>`  
**Methods:** POST  
**Authorization:** Document owner only; viewers are denied.

**Purpose:**
- Checks document ownership.
- Deletes the stored file and document metadata.
- Records deletion activity.
- Prevents unauthorized deletion.

### 4.9 Audit Logs

**Endpoint:** `/audit-logs`  
**Methods:** GET  
**Authorization:** Administrator only

**Purpose:**
- Displays recorded application activities.
- Shows login, upload, download, sharing, revocation, and deletion events.
- Restricts audit log access to administrators.

### 4.10 Logout

**Endpoint:** `/logout`  
**Methods:** GET  
**Authorization:** Authenticated users

**Purpose:**
- Clears the current user session.
- Records logout activity.
- Redirects the user to the login page.

## 5. Document Permissions

| Permission | Supported behavior |
|---|---|
| Owner | Manage and share owned documents |
| Read | View document details and download the document |
| Edit | Currently permits downloading, like read permission |

**Implementation limitation:** Direct editing of document contents is not currently implemented. The `edit` permission is stored, but it does not provide an actual document-editing operation.

## 6. Security Measures

- Password hashing using Werkzeug.
- Session-based authentication.
- Role-based access restrictions.
- Document ownership verification.
- Per-document sharing permissions.
- Secure filename handling.
- File extension validation.
- Maximum upload size of 5 MB.
- Unauthorized action logging.
- Administrator-only audit log access.

## 7. Data Storage

TrustVault currently uses JSON files for data storage.

| File | Purpose |
|---|---|
| `users.json` | User accounts and password hashes |
| `documents.json` | Document metadata and sharing permissions |
| `audit_logs.json` | Application activity records |

Uploaded documents are stored in the `uploads/` directory.

## 8. Automated Testing

Automated security tests are maintained in:

`tests/test_security.py`

The tests cover:

- Application initialization.
- Authentication requirements.
- Unauthorized document downloads.
- Unauthorized document deletion.
- Unauthorized document sharing.
- Administrator-only audit log access.
- Viewer upload restrictions.
- Viewer download restrictions.
- Viewer deletion restrictions.
- Viewer sharing restrictions.
- Download prevention after access revocation.

**Latest test result: 11 tests passed.**

## 9. Limitations and Future Improvements

- Implement actual document editing.
- Add a persistent database such as MySQL or PostgreSQL.
- Improve audit log integrity and tamper resistance.
- Add stronger session security.
- Add automated deployment initialization and demo data.
- Add more integration and security tests.

## 10. Conclusion

TrustVault provides a Flask-based document management system with authentication, role restrictions, document sharing, access revocation, file validation, and activity monitoring. Its security tests help verify that users cannot perform unauthorized document operations.