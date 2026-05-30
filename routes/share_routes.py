import uuid
from datetime import datetime, timedelta

from flask import Blueprint, jsonify, request

from models.secret_model import get_secret
from utils.file_storage import (
    read_json_file,
    write_json_file
)
from utils.encryption import decrypt_secret

share_bp = Blueprint("share", __name__)

SHARE_FILE = "secrets_data/share_tokens.json"


@share_bp.route("/secrets/<secret_id>/share", methods=["POST"])
def create_share_link(secret_id):
    token = str(uuid.uuid4())

    share_tokens = read_json_file(SHARE_FILE)

    share_tokens.append({
        "token": token,
        "secret_id": secret_id,
        "expires_at": (
            datetime.utcnow() +
            timedelta(minutes=15)
        ).isoformat(),
        "used": False
    })

    write_json_file(SHARE_FILE, share_tokens)

    return jsonify({
        "share_link": f"/share/{token}"
    })


@share_bp.route("/share/<token>", methods=["GET"])
def access_shared_secret(token):
    share_tokens = read_json_file(SHARE_FILE)

    for share in share_tokens:
        if share["token"] == token:

            if share["used"]:
                return jsonify({
                    "error": "Token already used"
                }), 403

            if datetime.utcnow() > datetime.fromisoformat(
                share["expires_at"]
            ):
                return jsonify({
                    "error": "Token expired"
                }), 403

            secret = get_secret(share["secret_id"])

            share["used"] = True

            write_json_file(
                SHARE_FILE,
                share_tokens
            )

            return jsonify({
                "secret": decrypt_secret(
                    secret["secret"]
                )
            })

    return jsonify({
        "error": "Invalid token"
    }), 404