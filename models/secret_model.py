import uuid
from utils.file_storage import (
    read_json_file,
    write_json_file
)

SECRETS_FILE = "secrets_data/secrets.json"


def save_secret(secret):
    secrets = read_json_file(SECRETS_FILE)
    secrets.append(secret)
    write_json_file(SECRETS_FILE, secrets)


def get_secret(secret_id):
    secrets = read_json_file(SECRETS_FILE)

    for secret in secrets:
        if secret["id"] == secret_id:
            return secret

    return None


def delete_secret(secret_id):
    secrets = read_json_file(SECRETS_FILE)

    secrets = [
        s for s in secrets
        if s["id"] != secret_id
    ]

    write_json_file(SECRETS_FILE, secrets)


def update_secret(secret_id, updated_data):
    secrets = read_json_file(SECRETS_FILE)

    for secret in secrets:
        if secret["id"] == secret_id:
            secret.update(updated_data)

    write_json_file(SECRETS_FILE, secrets)


def get_user_secrets(username):
    secrets = read_json_file(SECRETS_FILE)

    return [
        s for s in secrets
        if s["owner"] == username
    ]


def generate_secret_id():
    return str(uuid.uuid4())