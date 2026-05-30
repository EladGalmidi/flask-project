# Secure Secrets Manager

## Features

- Encrypted secret storage
- JWT authentication
- One-time share links
- Expiring tokens
- Rate limiting
- Audit logging
- OWASP security practices

---

## Installation

### 1. Clone repository

```bash
git clone https://github.com/yourusername/secure-secrets-manager.git
cd secure-secrets-manager
```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate virtual environment

Linux/macOS:

```bash
source venv/bin/activate
```

Windows:

```powershell
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Generate Fernet key

```python
from cryptography.fernet import Fernet
print(Fernet.generate_key().decode())
```

### 6. Create .env

```env
SECRET_KEY=your_secret
JWT_SECRET=your_jwt_secret
FERNET_KEY=your_generated_key
```

### 7. Run application

```bash
python app.py
```

---

## API Examples

### Register

```http
POST /register
```

Body:

```json
{
  "username": "elad",
  "password": "StrongPassword123!"
}
```

---

### Login

```http
POST /login
```

---

### Store Secret

```http
POST /secrets
Authorization: Bearer <TOKEN>
```

---

## Security Notes

- Secrets are encrypted using Fernet
- Passwords are hashed
- Secrets are never logged
- Rate limiting enabled
- Share links expire automatically
- One-time token usage enforced