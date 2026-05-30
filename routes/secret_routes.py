from flask import Blueprint, request, jsonify
from models.secret_model import (
    save_secret,
    get_secret,
    delete_secret,
    update_secret,
    get_user_secrets,
    generate_secret_id
)
from utils.encryption import (
    encrypt_secret,
    decrypt_secret
)
from utils.auth import decode_token
from utils.validators import validate_secret_payload
from utils.audit_logger import audit_event

secret_bp = Blueprint("secrets", __name__)


def get_authenticated_user():
    auth_header = request.headers.get("Authorization")

    if not auth_header:
        return None

    token = auth_header.split(" ")[1]

    payload = decode_token(token)

    return payload["username"]


@secret_bp.route("/secrets", methods=["POST"])
def create_secret():
    user = get_authenticated_user()

    if not user:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json

    valid, error = validate_secret_payload(data)
    if not valid:
        return jsonify({
            "error": "Invalid payload"
        }), 400

    secret = {
        "id": generate_secret_id(),
        "owner": user,
        "name": data["name"],
        "description": data.get("description", ""),
        "tags": data.get("tags", []),
        "secret": encrypt_secret(data["secret"])
    }

    save_secret(secret)

    audit_event(
        f"Secret created by user {user}"
    )

    return jsonify({
        "message": "Secret stored successfully",
        "secret_id": secret["id"]
    }), 201


@secret_bp.route("/secrets/<secret_id>", methods=["GET"])
def retrieve_secret(secret_id):
    user = get_authenticated_user()

    secret = get_secret(secret_id)

    if not secret:
        return jsonify({
            "error": "Secret not found"
        }), 404

    if secret["owner"] != user:
        return jsonify({
            "error": "Forbidden"
        }), 403

    return jsonify({
        "id": secret["id"],
        "name": secret["name"],
        "secret": decrypt_secret(secret["secret"])
    })


@secret_bp.route("/secrets", methods=["GET"])
def list_secrets():
    user = get_authenticated_user()

    secrets = get_user_secrets(user)

    sanitized = []

    for s in secrets:
        sanitized.append({
            "id": s["id"],
            "name": s["name"],
            "description": s["description"],
            "tags": s["tags"]
        })

    return jsonify(sanitized)


@secret_bp.route("/secrets/<secret_id>", methods=["DELETE"])
def remove_secret(secret_id):
    user = get_authenticated_user()

    secret = get_secret(secret_id)

    if not secret:
        return jsonify({
            "error": "Secret not found"
        }), 404

    if secret["owner"] != user:
        return jsonify({
            "error": "Forbidden"
        }), 403

    delete_secret(secret_id)

    audit_event(
        f"Secret deleted by user {user}"
    )

    return jsonify({
        "message": "Secret deleted"
    })


@secret_bp.route("/secrets/<secret_id>", methods=["PUT"])
def update_secret_metadata(secret_id):
    user = get_authenticated_user()

    secret = get_secret(secret_id)

    if secret["owner"] != user:
        return jsonify({
            "error": "Forbidden"
        }), 403

    data = request.json

    update_secret(secret_id, {
        "description": data.get("description", ""),
        "tags": data.get("tags", [])
    })

    return jsonify({
        "message": "Secret updated"
    })

    update_secret(secret_id, {

    "name": data.get(
        "name",
        secret["name"]
    ),

    "description": data.get(
        "description",
        secret["description"]
    ),

    "tags": data.get(
        "tags",
        secret["tags"]
    )
})