import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet

# טעינת משתני סביבה מקובץ .env אם הוא קיים
load_dotenv()

class Config:
    # 1. מפתח סודי כללי של פלאסק
    SECRET_KEY = os.getenv("SECRET_KEY") or "super-secret-flask-key"

    # 2. הגדרת JWT Secret חסינה לטסטים
    JWT_SECRET = os.getenv("JWT_SECRET") or "test_jwt_secret_key_12345"

    # 3. הגדרת Fernet Key חסינה לשגיאות (בודקת אורך תקין של 44 תווים)
    _key = os.getenv("FERNET_KEY")
    if _key and len(_key) == 44:
        FERNET_KEY = _key
    else:
        FERNET_KEY = Fernet.generate_key().decode()

    # 4. ביטול הגבלת הקצב בזמן בדיקות/פיתוח כדי למנוע את האזהרה של הלימיטר
    RATELIMIT_ENABLED = False


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False