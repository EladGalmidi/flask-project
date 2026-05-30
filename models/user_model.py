from utils.file_storage import (
    read_json_file,
    write_json_file
)

USERS_FILE = "secrets_data/users.json"


def create_user(user_data):
    users = read_json_file(USERS_FILE)
    users.append(user_data)
    write_json_file(USERS_FILE, users)


def get_user_by_username(username):
    users = read_json_file(USERS_FILE)

    for user in users:
        if user["username"] == username:
            return user

    return None