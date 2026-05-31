# Secure Secrets Manager API Documentation

## Overview

Secure Secrets Manager is a secure REST API built with Flask for storing, managing, and sharing encrypted secrets such as API keys, credentials, and access tokens.

### Features

- JWT-based authentication
- Encrypted secret storage using Fernet
- User-level access control
- One-time expiring share links
- Rate limiting protection
- Audit logging

---

## Base URL

During local development:

```text
http://127.0.0.1:5000
```

---

## Authentication

Protected endpoints require a valid JWT token.

Include the following header with authenticated requests:

```http
Authorization: Bearer <JWT_TOKEN>
```

JWT tokens are issued through the `/login` endpoint.

---

## Error Format

All errors are returned as JSON:

```json
{
  "error": "Short error description"
}
```

---

# Authentication Endpoints

## POST `/register`

Create a new user account.

### Authentication

None

### Request Body

```json
{
  "username": "john",
  "password": "StrongPassword123!"
}
```

### Success Response

**201 Created**

```json
{
  "message": "User registered successfully"
}
```

### Possible Errors

| Status | Description |
|----------|-------------|
| 400 | Missing required fields |
| 409 | User already exists |

### Example

```bash
curl -X POST http://127.0.0.1:5000/register \
  -H "Content-Type: application/json" \
  -d '{"username":"john","password":"StrongPassword123!"}'
```

---

## POST `/login`

Authenticate a user and receive a JWT token.

### Authentication

None

### Request Body

```json
{
  "username": "john",
  "password": "StrongPassword123!"
}
```

### Success Response

**200 OK**

```json
{
  "token": "<jwt-token>"
}
```

### Possible Errors

| Status | Description |
|----------|-------------|
| 401 | Invalid credentials |

### Example

```bash
curl -X POST http://127.0.0.1:5000/login \
  -H "Content-Type: application/json" \
  -d '{"username":"john","password":"StrongPassword123!"}'
```

---

# Secret Management

## POST `/secrets`

Create and securely store an encrypted secret.

### Authentication

Required

### Request Body

```json
{
  "name": "AWS_KEY",
  "secret": "my-secret-value",
  "description": "AWS production key",
  "tags": ["aws", "prod"]
}
```

### Success Response

**201 Created**

```json
{
  "message": "Secret stored successfully",
  "secret_id": "uuid"
}
```

### Possible Errors

| Status | Description |
|----------|-------------|
| 400 | Invalid request payload |
| 401 | Unauthorized |

### Example

```bash
curl -X POST http://127.0.0.1:5000/secrets \
  -H "Authorization: Bearer <JWT_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"name":"AWS_KEY","secret":"my-secret-value"}'
```

---

## GET `/secrets`

Retrieve all secrets belonging to the authenticated user.

### Authentication

Required

### Success Response

```json
[
  {
    "id": "uuid",
    "name": "AWS_KEY",
    "description": "AWS production key",
    "tags": ["aws"]
  }
]
```

### Example

```bash
curl -H "Authorization: Bearer <JWT_TOKEN>" \
  http://127.0.0.1:5000/secrets
```

---

## GET `/secrets/<id>`

Retrieve a specific secret and decrypt its value.

### Authentication

Required (Owner only)

### Success Response

```json
{
  "id": "uuid",
  "name": "AWS_KEY",
  "secret": "decrypted-value"
}
```

### Possible Errors

| Status | Description |
|----------|-------------|
| 403 | Access denied |
| 404 | Secret not found |

### Example

```bash
curl -H "Authorization: Bearer <JWT_TOKEN>" \
  http://127.0.0.1:5000/secrets/<id>
```

---

## PUT `/secrets/<id>`

Update secret metadata.

### Authentication

Required (Owner only)

### Request Body

```json
{
  "name": "NEW_NAME",
  "description": "Updated description",
  "tags": ["prod", "updated"]
}
```

### Success Response

```json
{
  "message": "Secret updated"
}
```

### Possible Errors

| Status | Description |
|----------|-------------|
| 400 | Invalid request |
| 403 | Access denied |
| 404 | Secret not found |

### Example

```bash
curl -X PUT http://127.0.0.1:5000/secrets/<id> \
  -H "Authorization: Bearer <JWT_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"name":"NEW_NAME"}'
```

---

## DELETE `/secrets/<id>`

Delete a secret.

### Authentication

Required (Owner only)

### Success Response

```json
{
  "message": "Secret deleted"
}
```

### Possible Errors

| Status | Description |
|----------|-------------|
| 403 | Access denied |
| 404 | Secret not found |

### Example

```bash
curl -X DELETE \
  -H "Authorization: Bearer <JWT_TOKEN>" \
  http://127.0.0.1:5000/secrets/<id>
```

---

# Secret Sharing

## POST `/secrets/<id>/share`

Generate a one-time share link for a secret.

### Authentication

Required (Owner only)

### Success Response

```json
{
  "share_link": "/share/<token>"
}
```

### Share Rules

- Valid for 15 minutes
- Can be used only once
- Automatically expires after usage

### Possible Errors

| Status | Description |
|----------|-------------|
| 403 | Access denied |
| 404 | Secret not found |

### Example

```bash
curl -X POST \
  -H "Authorization: Bearer <JWT_TOKEN>" \
  http://127.0.0.1:5000/secrets/<id>/share
```

---

## GET `/share/<token>`

Access a secret using a share token.

### Authentication

Not required

### Success Response

```json
{
  "secret": "decrypted-value"
}
```

### Possible Errors

| Status | Description |
|----------|-------------|
| 403 | Token expired or already used |
| 404 | Invalid token |

### Example

```bash
curl http://127.0.0.1:5000/share/<token>
```

---

# Common Error Responses

## 401 Unauthorized

```json
{
  "error": "Missing authorization header"
}
```

---

## 403 Forbidden

```json
{
  "error": "Forbidden"
}
```

---

## 404 Not Found

```json
{
  "error": "Secret not found"
}
```

---

## Security Notes

- Secrets are encrypted before storage using Fernet symmetric encryption.
- Users can access only their own secrets.
- Share links are single-use and automatically expire.
- JWT tokens are required for all protected endpoints.
- Audit logging records access and management operations.
- Rate limiting helps mitigate brute-force and abuse attempts.