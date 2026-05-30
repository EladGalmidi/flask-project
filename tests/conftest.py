import os
import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

@pytest.fixture(autouse=True)
def clean_storage():
    """מנקה את קבצי הנתונים הזמניים לפני כל טסט בנפרד"""
    # נתיב מלא לקובץ
    file_path = os.path.join('secrets_data', 'users.json')

    if os.path.exists(file_path):
        try:
            os.remove(file_path)
        except OSError:
            pass
    yield