from fastapi.testclient import TestClient


def test_get_test(client: TestClient):
    res = client.get("/auth/test")
    assert res.status_code in (200, 404)