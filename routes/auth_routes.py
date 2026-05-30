from flask import Blueprint, request, jsonify
from utils.auth import (
    hash_password,
    verify_password,
    generate_token
)
from models.user_model import (
    create_user,
    get_user_by_username
)
from utils.rate_limiter import limiter

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
@limiter.limit("5 per minute")
def register():
    data = request.json

    if get_user_by_username(data["username"]):
        return jsonify({
            "error": "User already exists"
        }), 400

    create_user({
        "username": data["username"],
        "password": hash_password(data["password"])
    })

    return jsonify({
        "message": "User registered successfully"
    }), 201


@auth_bp.route("/login", methods=["POST"])
@limiter.limit("10 per minute")
def login():
    data = request.json

    user = get_user_by_username(data["username"])

    if not user:
        return jsonify({
            "error": "Invalid credentials"
        }), 401

    if not verify_password(
        data["password"],
        user["password"]
    ):
        return jsonify({
            "error": "Invalid credentials"
        }), 401

    token = generate_token(user["username"])

    return jsonify({
        "token": token
    })