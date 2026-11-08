# TrustVault – Development Prompts

## Introduction

This document records the AI-assisted prompts and development guidance used during the development, testing, and improvement of the TrustVault project.

The entries below summarize the development requests and discussions. They are paraphrased summaries, not necessarily exact word-for-word prompts.

## Prompt 1 – Project Development

**Date:** 07-11-2026

**Prompt summary:**

"Help me develop a secure file storage and management system using Python and Flask."

**Purpose:**

To develop the basic Flask application structure and implement the main project functionality.

## Prompt 2 – User Authentication

**Date:** 07-11-2026

**Prompt summary:**

"Implement user registration and login functionality using Flask, with secure password hashing."

**Purpose:**

To provide user authentication and protect user credentials using Werkzeug password hashing.

## Prompt 3 – File Upload Security

**Date:** 07-11-2026

**Prompt summary:**

"Add secure file upload functionality with allowed file extensions, secure filenames, and a maximum upload size of 5 MB."

**Purpose:**

To validate uploaded documents and restrict file types and file sizes.

## Prompt 4 – Document Authorization

**Date:** 07-11-2026

**Prompt summary:**

"Implement document ownership checks and access permissions so users cannot access documents without authorization."

**Purpose:**

To prevent unauthorized document access and enforce document ownership restrictions.

## Prompt 5 – Document Sharing and Revocation

**Date:** 07-11-2026

**Prompt summary:**

"Implement document sharing functionality that allows document owners to grant read or edit permissions and revoke access."

**Purpose:**

To provide controlled document sharing and permission management.

## Prompt 6 – Audit Logging

**Date:** 07-11-2026

**Prompt summary:**

"Implement JSON-based audit logging to record registration, successful login, failed login, file upload, file download, unauthorized access attempts, sharing, revocation, and logout."

**Purpose:**

To maintain records of important application activities and security-related events.

## Prompt 7 – Dashboard and Document Search

**Date:** 08-11-2026

**Prompt summary:**

"Create a Flask dashboard with document search and filters for filename, owner, category, and upload date."

**Purpose:**

To improve document organization and help users find documents using multiple search criteria.

## Prompt 8 – Document Deletion

**Date:** 08-11-2026

**Prompt summary:**

"Implement document deletion with an ownership check so that only the document owner can delete a document."

**Purpose:**

To prevent unauthorized document deletion and record deletion activities in audit logs.

## Prompt 9 – Automated Security Testing

**Date:** 08-11-2026

**Prompt summary:**

"Help me create pytest tests to verify authentication, unauthorized document downloads, unauthorized deletion, unauthorized sharing, and administrator-only audit log access."

**Purpose:**

To verify important application security controls using automated tests.

## Prompt 10 – Security Threat Analysis

**Date:** 09-11-2026

**Prompt summary:**

"Prepare a security threat analysis for TrustVault, including potential threats, implemented protections, limitations, and future security improvements."

**Purpose:**

To document security risks and identify improvements required for stronger application security.

## Conclusion

AI-assisted development guidance was used to understand Flask functionality, improve application security, implement document management features, and create automated tests.

The generated suggestions were reviewed and tested during project development. The final implementation and its limitations are documented in the project files.