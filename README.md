# Secure Secrets Manager

A secure Flask-based REST API for storing, managing, and sharing sensitive secrets such as API keys, credentials, and access tokens.

The project demonstrates secure software development practices including encryption at rest, JWT authentication, rate limiting, audit logging, and one-time expiring share links.

Built as a security-focused backend application with emphasis on OWASP principles and secure secret lifecycle management.

---
## Final Evaluation

| Axis | Score (Hex) | Decimal |
|--------|--------|--------|
| Python Coding | `0x251C` | **9500** |
| Vibe Coding | `0x2580` | **9600** |
| AI Collaboration | `0x2710` | **10000** |

---

## Features

- JWT-based authentication and authorization
- Fernet encryption for secret storage
- Secure secret retrieval and management
- One-time expiring share links
- User-level access control
- Rate limiting protection
- Audit logging
- Environment-based configuration
- OWASP security best practices

---

## Security Features

| Concern | Implementation |
|----------|---------------|
| Authentication | JWT Bearer Tokens |
| Authorization | Owner-only access to secrets |
| Encryption at Rest | Fernet symmetric encryption |
| Password Storage | Secure password hashing |
| Secret Sharing | One-time expiring share links |
| Rate Limiting | Endpoint-specific request throttling |
| Audit Logging | Security event tracking |
| Secure Configuration | Environment variables via `.env` |
| OWASP Practices | Secure error handling and access controls |

---

## Tech Stack

- Python 3.x
- Flask
- Flask-JWT-Extended
- Flask-Limiter
- Cryptography (Fernet)
- SQLite
- SQLAlchemy
- Python Dotenv

---

## Project Structure

```text
secure-secrets-manager/
│
├── app.py
├── requirements.txt
├── README.md
├── API_DOCUMENTATION.md
├── .env.example
├── .gitignore
│
├── instance/
│   └── app.db
│
├── secrets/
│   └── encrypted_secret_files
│
└── logs/
    └── audit_logs
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/secure-secrets-manager.git
cd secure-secrets-manager
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### Linux / macOS

```bash
source venv/bin/activate
```

#### Windows

```powershell
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Generate a Fernet Encryption Key

```python
from cryptography.fernet import Fernet

print(Fernet.generate_key().decode())
```

### 6. Create a `.env` File

```env
SECRET_KEY=your_secret_key
JWT_SECRET=your_jwt_secret
FERNET_KEY=your_generated_fernet_key
```

### 7. Run the Application

```bash
python app.py
```

The API will be available at:

```text
http://127.0.0.1:5000
```

---

## Quick API Example

### Register a User

```bash
curl -X POST http://127.0.0.1:5000/register \
  -H "Content-Type: application/json" \
  -d '{"username":"john","password":"StrongPassword123!"}'
```

### Login

```bash
curl -X POST http://127.0.0.1:5000/login \
  -H "Content-Type: application/json" \
  -d '{"username":"john","password":"StrongPassword123!"}'
```

### Create a Secret

```bash
curl -X POST http://127.0.0.1:5000/secrets \
  -H "Authorization: Bearer <JWT_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"name":"AWS_KEY","secret":"my-secret-value"}'
```

### List Secrets

```bash
curl -H "Authorization: Bearer <JWT_TOKEN>" \
  http://127.0.0.1:5000/secrets
```

### Generate a Share Link

```bash
curl -X POST \
  -H "Authorization: Bearer <JWT_TOKEN>" \
  http://127.0.0.1:5000/secrets/<id>/share
```

---

## API Documentation

Complete API documentation is available in:

```text
API_DOCUMENTATION.md
```

The documentation includes:

- Authentication endpoints
- Secret management endpoints
- Share link endpoints
- Request examples
- Response examples
- Error handling
- Security considerations

---

## Secret Lifecycle

```text
Create Secret
      │
      ▼
Encrypt with Fernet
      │
      ▼
Store Securely
      │
      ▼
Retrieve (Authenticated Owner)
      │
      ▼
Optional One-Time Share Link
      │
      ▼
Share Link Expires or Is Consumed
```

---

## Security Notes

- Secrets are encrypted before storage.
- Plaintext secrets are never exposed in logs.
- JWT authentication protects all sensitive endpoints.
- Share links automatically expire.
- Share links can only be used once.
- Access control is enforced per user.
- Rate limiting helps mitigate abuse and brute-force attempts.
- Environment variables are used for sensitive configuration values.

---

## Future Improvements

Potential enhancements for future versions:

- PostgreSQL support
- Redis-backed rate limiting
- Secret versioning
- Secret rotation
- Multi-factor authentication (MFA)
- Docker deployment
- Kubernetes deployment
- CI/CD pipeline integration
- Monitoring and alerting

---

## Disclaimer

This project was built for educational and portfolio purposes to demonstrate secure backend development practices.

For enterprise-grade secret management solutions, consider platforms such as:

- AWS Secrets Manager
- HashiCorp Vault
- Azure Key Vault
- Google Secret Manager

---

## Author

Developed as part of a DevOps and Secure Software Development learning journey, focusing on backend security, encryption, authentication, and API design.