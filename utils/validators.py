def validate_secret_payload(data):

    if "name" not in data:
        return False, "Missing name"

    if "secret" not in data:
        return False, "Missing secret"

    if len(data["name"]) > 100:
        return False, "Name too long"

    if len(data["secret"]) > 10000:
        return False, "Secret too large"

    if len(data.get("description", "")) > 500:
        return False, "Description too long"

    if len(data.get("tags", [])) > 20:
        return False, "Too many tags"

    return True, None