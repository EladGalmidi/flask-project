def test_register(client):
    response = client.post("/register", json={
        "username": "test",
        "password": "password123"
    })

    assert response.status_code == 201
