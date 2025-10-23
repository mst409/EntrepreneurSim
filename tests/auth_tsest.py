from fastapi.testclient import TestClient


def test_create_user(client: TestClient):
    res = client.post("/auth/signup", json={
  "user_name": "testuser",
  "email": "user@example.com",
  "password": "testpassword"
})
    assert res.status_code == 200

def test_get_new_player(client: TestClient):
    response = client.get("/players/name/testuser")
    assert response.status_code == 200