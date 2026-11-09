# TrustVault – AI Development Prompts and Usage Record

## 1. Introduction

This document records the AI-assisted prompts and development guidance used while developing, testing, debugging, and documenting TrustVault – Secure File Storage and Management System.

The prompts below are paraphrased summaries of the actual development discussions, not necessarily exact word-for-word prompts.

AI-generated suggestions were reviewed and adapted during implementation. The application was tested locally and on Render. Not every suggested feature was implemented completely; known limitations are documented honestly.

## 2. Development Prompt Records

### Prompt 1 – Project Development

**Date:** 07-11-2026

**Prompt summary:**

"Help me develop a secure file storage and management system using Python and Flask."

**AI output:**

Provided guidance for the Flask application structure, routes, templates, file handling, authentication, and document management.

**Problem or limitation identified:**

The initial project structure alone did not provide a complete secure application. Authentication, ownership checks, role-based authorization, and validation needed to be implemented and tested separately.

**Action taken:**

Developed the application incrementally and added authentication, document management, access control, and security tests.

**Fix commit:**

No single corrective commit for the overall project structure is identified. Refer to the repository's development history:

https://github.com/ruthsmiley02/TrustVault/commits/main

### Prompt 2 – User Authentication

**Date:** 07-11-2026

**Prompt summary:**

"Implement user registration and login functionality using Flask, with secure password hashing."

**AI output:**

Provided Flask registration and login guidance using Werkzeug password hashing and session-based authentication.

**Problem or limitation identified:**

Authentication alone does not ensure that users can access only their own documents. Each protected document operation also requires authorization checks.

**Action taken:**

Used password hashing and session checks and added authorization checks to protected document operations. Authentication and access restrictions were covered by automated tests.

**Fix commit:**

No separate authentication correction commit is identified in the available development record. See:

https://github.com/ruthsmiley02/TrustVault/commits/main

### Prompt 3 – File Upload Security

**Date:** 07-11-2026

**Prompt summary:**

"Add secure file upload functionality with allowed file extensions, secure filenames, and a maximum upload size of 5 MB."

**AI output:**

Provided upload validation guidance using allowed extensions, file-size restrictions, and Werkzeug's secure filename handling.

**Problem or limitation identified:**

Uploaded filenames and file extensions cannot be trusted without server-side validation. Upload restrictions must be enforced by the application rather than relying only on the browser interface.

**Action taken:**

Implemented server-side extension and size validation and secure filename handling. The configured maximum upload size is 5 MB.

**Fix commit:**

No specific corrective commit is identified for this entry. See:

https://github.com/ruthsmiley02/TrustVault/commits/main

### Prompt 4 – Document Authorization and Access Control

**Date:** 07-11-2026

**Prompt summary:**

"Implement document ownership checks and access permissions so users cannot access documents without authorization."

**AI output:**

Provided guidance for checking document ownership, shared permissions, and user roles before allowing document operations.

**Problem or limitation identified:**

A logged-in user must not automatically receive access to every document. Access must be checked for the particular document and the requesting user. Viewer permissions must also prevent unauthorized management operations.

**Action taken:**

Implemented server-side ownership and permission checks. Added tests for unauthorized document downloads, deletion, and sharing. Manually checked viewer restrictions on the deployed application.

**Fix commit:**

No exact corrective commit for the original authorization implementation is identified in the available record. Related test and development history:

https://github.com/ruthsmiley02/TrustVault/commits/main

### Prompt 5 – Document Sharing and Revocation

**Date:** 07-11-2026

**Prompt summary:**

"Implement document sharing functionality that allows document owners to grant read or edit permissions and revoke access."

**AI output:**

Provided guidance for granting permissions to named users and revoking previously granted access.

**Problem or limitation identified:**

A shared user must lose access after the owner revokes permission. The edit permission must not be described as full document editing when the application does not implement actual document modification.

**Action taken:**

Tested sharing a document with the viewer account, accessing the shared document, revoking access, and checking that the viewer could no longer access it. Documented that actual document editing is not implemented.

**Fix commit:**

No separate corrective commit for the sharing workflow is identified. See:

https://github.com/ruthsmiley02/TrustVault/commits/main

### Prompt 6 – Audit Logging and Administrative Access

**Date:** 07-11-2026

**Prompt summary:**

"Implement JSON-based audit logging to record registration, successful login, failed login, file upload, file download, unauthorized access attempts, sharing, revocation, and logout."

**AI output:**

Provided guidance for recording application events in a JSON audit log and restricting audit-log access to administrators.

**Problem or limitation identified:**

A JSON audit file can be modified by someone with sufficient access to the application storage. JSON-based logging does not by itself provide tamper-proof audit records.

**Action taken:**

Implemented application event logging and administrator-only audit-log access. Security tests include checking that a normal user cannot access the administrator audit-log route. The limitation of mutable JSON audit records is documented rather than claiming tamper-proof logging.

**Fix commit:**

No specific audit-log correction commit is identified in the available record. See:

https://github.com/ruthsmiley02/TrustVault/commits/main

### Prompt 7 – Dashboard and Document Search

**Date:** 08-11-2026

**Prompt summary:**

"Create a Flask dashboard with document search and filters for filename, owner, category, and upload date."

**AI output:**

Provided guidance for displaying documents and implementing search and filtering on the dashboard.

**Problem or limitation identified:**

Search functionality must be checked against the actual implemented filters. A search field should not be described as supporting every filter unless each one has been verified.

**Action taken:**

Integrated document search into the dashboard. The implemented search behavior should be described according to the filters actually present in the application.

**Fix commit:**

No exact corrective commit for the search implementation is identified in the available record. See:

https://github.com/ruthsmiley02/TrustVault/commits/main

### Prompt 8 – Document Deletion

**Date:** 08-11-2026

**Prompt summary:**

"Implement document deletion with an ownership check so that only the document owner can delete a document."

**AI output:**

Provided guidance for document deletion and server-side ownership verification.

**Problem or limitation identified:**

A delete operation must not rely only on hiding the delete button. The server must verify that the requesting user owns the document.

**Action taken:**

Used server-side ownership checks and included unauthorized deletion checks in the automated security tests.

**Fix commit:**

No separate corrective commit for the deletion implementation is identified in the available record. See:

https://github.com/ruthsmiley02/TrustVault/commits/main

### Prompt 9 – Automated Security Testing

**Date:** 08-11-2026

**Prompt summary:**

"Help me create pytest tests to verify authentication, unauthorized document downloads, unauthorized deletion, unauthorized sharing, and administrator-only audit log access."

**AI output:**

Provided guidance for pytest test cases covering authentication and role-based document authorization.

**Problem or limitation identified:**

Testing only successful operations is insufficient. The application must also reject unauthorized operations, including cross-user access and restricted viewer actions.

**Action taken:**

Created and ran automated security tests. The latest reported test result during development was 11 passed. The tests cover important authorization restrictions. Some manual scenarios, such as actual sharing and revocation, were also checked separately.

**Fix commit:**

Test documentation was updated in commit `272b9b4`:

https://github.com/ruthsmiley02/TrustVault/commit/272b9b4

### Prompt 10 – Security Threat Analysis

**Date:** 09-11-2026

**Prompt summary:**

"Prepare a security threat analysis for TrustVault, including potential threats, implemented protections, limitations, and future security improvements."

**AI output:**

Provided guidance for identifying threats involving authentication, unauthorized access, file uploads, document sharing, audit records, and deployment.

**Problem or limitation identified:**

A threat analysis must distinguish implemented protections from proposed improvements. It would be misleading to claim that mutable JSON audit logs are tamper-proof or that unimplemented document editing is available.

**Action taken:**

Prepared `THREATS.md` to describe relevant threats, existing protections, known limitations, and possible future improvements.

**Fix commit:**

No separate corrective commit for the threat-analysis document is identified in the available record. See:

https://github.com/ruthsmiley02/TrustVault/commits/main

### Prompt 11 – Render Viewer Account Configuration

**Date:** 09-11-2026

**Prompt summary:**

"Help me fix the viewer account setup on Render using environment variables and verify that the viewer account is created with the correct role."

**AI output:**

Provided guidance for reading viewer credentials from Render environment variables, creating or updating the viewer account, and checking the saved role and password hash.

**Problem identified:**

The viewer account was not being configured correctly because the Render environment variable setup was incorrect. The username had been entered as an environment variable key instead of being supplied as the value of the expected username variable.

**Action taken:**

Corrected the Render environment variable configuration and updated the viewer setup code. Added diagnostic checks that report whether the username and password variables are set and whether the viewer account is configured correctly. Verified that the viewer could log in and that viewer restrictions worked.

**Related commits:**

- `c77ca66` – Fix Render viewer account setup:
  https://github.com/ruthsmiley02/TrustVault/commit/c77ca66
- `8a31e8d` – Check viewer environment variables:
  https://github.com/ruthsmiley02/TrustVault/commit/8a31e8d

### Prompt 12 – README and Test Documentation

**Date:** 09-11-2026

**Prompt summary:**

"Update the README documentation to reflect the latest automated security test count and test descriptions."

**AI output:**

Provided guidance for updating the test documentation to match the latest reported test results.

**Problem identified:**

The README contained an outdated test count and needed to reflect the more recent test suite.

**Action taken:**

Updated the README test documentation and pushed the change to GitHub.

**Fix commit:**

`272b9b4` – Update README test documentation:

https://github.com/ruthsmiley02/TrustVault/commit/272b9b4

## 3. Reused Prompts, Instructions, and Context Files

During development, previous project requirements and implementation details were reused to maintain consistency.

The following project files were used as development context or documentation references where relevant:

- `README.md` – project overview, setup, features, and limitations.
- `THREATS.md` – security threats, existing protections, and limitations.
- `API_DOCUMENTATION.md` – application routes and API documentation.
- `PROMPTS.md` – record of AI-assisted development discussions.
- `tests/test_security.py` – automated security test cases.
- `.env.example` – example environment variable names without actual secrets.

Previously discussed requirements were reused when improving authentication, authorization, document sharing, viewer restrictions, audit logging, and deployment.

## 4. Responsible Use of AI

AI was used as a development assistant for understanding Flask, writing and reviewing code, debugging configuration issues, preparing tests, and improving documentation.

Generated suggestions were not treated as automatically correct. They were reviewed, adapted, and tested during development.

Known limitations were retained in the documentation instead of claiming that every requested feature was fully implemented.

## 5. Conclusion

AI-assisted development helped with the implementation, testing, debugging, and documentation of TrustVault.

The development process included both successful implementation work and correction of configuration and documentation issues. The project was tested locally and deployed to Render.

The final project documentation identifies unfinished features and security limitations, including the lack of actual document editing and tamper-proof audit logging.