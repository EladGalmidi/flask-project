def test_invalid_share_token(client):

    response = client.get(
        "/share/invalid-token"
    )

    assert response.status_code == 404