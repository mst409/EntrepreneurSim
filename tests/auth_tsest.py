from fastapi.testclient import TestClient


def test_create_user(client: TestClient):
    # test creating a new user
    response = client.post("/auth/signup", json={
        "user_name": "testuser",
        "email": "user@example.com",
        "password": "testpassword"
    })
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def create_email_already_registerd(client: TestClient):
    '''test creating a user with a diffrent username and email 
    that is already taken'''

    client.post("/auth/signup", json={
        "user_name": "testuser",
        "email": "user@example.com",
        "password": "testpassword"
    })

    response = client.post("/auth/signup", json={
        "user_name": "testuser2",
        "email": "user@example.com",
        "password": "testpassword"
    })
    assert response.status_code == 400
    assert response.json() == {"detail": "Email already registered"}

    # TODO test the new player that is auto generated
    # TODO test the players bank account
    