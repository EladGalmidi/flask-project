import jwt
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config


def hash_password(password):
    return generate_password_hash(password)


def verify_password(password, hashed):
    return check_password_hash(hashed, password)


def generate_token(username):
    payload = {
        "username": username,
        "exp": datetime.utcnow() + timedelta(hours=1)
    }

    return jwt.encode(payload, Config.JWT_SECRET, algorithm="HS256")


def decode_token(token):
    return jwt.decode(
        token,
        Config.JWT_SECRET,
        algorithms=["HS256"]
    )