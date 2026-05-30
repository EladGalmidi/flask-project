import json
import os
from threading import Lock

storage_lock = Lock()


def read_json_file(path):
    if not os.path.exists(path):
        return []

    with storage_lock:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)


def write_json_file(path, data):
    # --- תוסיף את שתי השורות האלו כדי לייצר את התיקייה אוטומטית אם היא חסרה ---
    dirname = os.path.dirname(path)
    if dirname:
        os.makedirs(dirname, exist_ok=True)
        
    with storage_lock:
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4) # או איך שכתוב אצלך המשך הפונקציה