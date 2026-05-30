from utils.file_storage import (
    read_json_file,
    write_json_file
)

SHARE_FILE = "secrets_data/share_tokens.json"


def save_share_token(token_data):
    tokens = read_json_file(SHARE_FILE)

    tokens.append(token_data)

    write_json_file(
        SHARE_FILE,
        tokens
    )


def get_all_share_tokens():
    return read_json_file(
        SHARE_FILE
    )


def update_share_tokens(tokens):
    write_json_file(
        SHARE_FILE,
        tokens
    )