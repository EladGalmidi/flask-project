from cryptography.fernet import Fernet
from config import Config

fernet = Fernet(Config.FERNET_KEY.encode())


def encrypt_secret(secret_value: str) -> str:
    """
    Encrypt secret value using Fernet symmetric encryption.
    """
    encrypted = fernet.encrypt(secret_value.encode())
    return encrypted.decode()


def decrypt_secret(encrypted_secret: str) -> str:
    """
    Decrypt encrypted secret.
    """
    decrypted = fernet.decrypt(encrypted_secret.encode())
    return decrypted.decode()