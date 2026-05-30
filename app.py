from flask import Flask
from config import Config

from routes.auth_routes import auth_bp
from routes.secret_routes import secret_bp
from routes.share_routes import share_bp

from utils.rate_limiter import limiter

app = Flask(__name__)

import os

if os.getenv("FLASK_ENV") == "production":

    app.config.from_object(
        "config.ProductionConfig"
    )

else:

    app.config.from_object(
        "config.DevelopmentConfig"
    )

limiter.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(secret_bp)
app.register_blueprint(share_bp)


@app.route("/")
def health_check():
    return {
        "status": "Secure Secrets Manager Running"
    }


if __name__ == "__main__":
    app.run(debug=False)

from utils.security_headers import (
    add_security_headers
)

@app.after_request
def apply_headers(response):

    return add_security_headers(
        response
    )