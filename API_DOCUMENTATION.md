# Secure Secrets Manager - API Documentation

## Overview

Secure Secrets Manager is a Flask-based secure API for storing, retrieving, and sharing encrypted secrets such as API keys and credentials.

Features:
- User authentication (JWT)
- Encrypted secret storage (Fernet)
- One-time expiring share links
- Access control per user
- Rate limiting
- Audit logging

---

## Authentication

All protected endpoints require JWT authentication.

### Header


Authorization: Bearer <JWT_TOKEN>


Token is received from `/login`.

---

# Register User

## POST `/register`

Create a new user.

### Request
```json
{
  "username": "john",
  "password": "StrongPassword123!"
}
Response
{
  "message": "User registered successfully"
}
Errors
400 → user already exists / missing fields
Login User
POST /login

Authenticate user and receive JWT token.

Request
{
  "username": "john",
  "password": "StrongPassword123!"
}
Response
{
  "token": "jwt-token-here"
}
Errors
401 → invalid credentials
Create Secret
POST /secrets

Store encrypted secret.

Headers
Authorization: Bearer <JWT_TOKEN>
Request
{
  "name": "AWS_KEY",
  "secret": "my-secret-value",
  "description": "AWS production key",
  "tags": ["aws", "prod"]
}
Response
{
  "message": "Secret stored successfully",
  "secret_id": "uuid"
}
Errors
401 → unauthorized
400 → invalid payload
List Secrets
GET /secrets

Get all secrets for the logged-in user.

Headers
Authorization: Bearer <JWT_TOKEN>
Response
[
  {
    "id": "uuid",
    "name": "AWS_KEY",
    "description": "AWS production key",
    "tags": ["aws"]
  }
]
Get Secret
GET /secrets/<id>

Retrieve decrypted secret (owner only).

Headers
Authorization: Bearer <JWT_TOKEN>
Response
{
  "id": "uuid",
  "name": "AWS_KEY",
  "secret": "decrypted-value"
}
Errors
403 → forbidden
404 → not found
🗑 Delete Secret
DELETE /secrets/<id>

Delete a secret.

Response
{
  "message": "Secret deleted"
}
Errors
403 → forbidden
404 → not found
Update Secret Metadata
PUT /secrets/<id>

Update name, description, and tags.

Request
{
  "name": "NEW_NAME",
  "description": "Updated description",
  "tags": ["prod", "updated"]
}
Response
{
  "message": "Secret updated"
}
Create Share Link
POST /secrets/<id>/share

Generate a one-time expiring share link.

Response
{
  "share_link": "/share/<token>"
}
Rules
Expires after 15 minutes
Can be used only once
Errors
403 → forbidden
404 → not found
Access Shared Secret
GET /share/<token>

Access secret using share token.

Response
{
  "secret": "decrypted-value"
}
Errors
403 → expired or already used
404 → invalid token
Error Responses
401 Unauthorized
{
  "error": "Missing authorization header"
}
403 Forbidden
{
  "error": "Forbidden"
}
404 Not Found
{
  "error": "Secret not found"
}