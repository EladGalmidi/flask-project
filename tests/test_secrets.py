def test_secret_creation(client):
    # 1. יוצרים קודם כל את המשתמש במערכת
    client.post("/register", json={
        "username": "secret_user",
        "password": "password123"
    })
    
    # 2. מבצעים התחברות (Login) כדי לקבל את הטוקן החוקי מהשרת
    login_response = client.post("/login", json={
        "username": "secret_user",
        "password": "password123"
    })
    
    # 3. שולפים את הטוקן מתוך ה-JSON (משתמשים ב-.get בשביל הגנה)
    token = login_response.json.get("token")
    
    # 4. עכשיו כשיש לנו טוקן אמיתי ולא None, הבקשה ליצירת הסוד תעבוד:
    response = client.post(
        "/secrets",
        json={
            "name": "AWS_KEY",
            "secret": "super-secret"
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )
    
    # 5. בדיקה שהסוד נוצר בהצלחה
    assert response.status_code == 201