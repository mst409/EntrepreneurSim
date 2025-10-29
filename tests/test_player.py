from urllib import response
from fastapi.testclient import TestClient
from pydantic import UUID4
from sqlalchemy.orm import Session

from src.players.schemas import PlayerCreate, PlayerResponse
from src.players.models import Player
from src.auth.models import User
from src.auth.schemas import CreateUser


testuser = {
    "user_name":"testuser",
    "email": "test@user.com",
    "password": "testpassword"
}


def test_search_player_by_name(client: TestClient):
    '''Test searching a player by name after createing it'''
    reaponae = client.post("auth/signup", json={
        **testuser
    })
    
    assert reaponae.status_code == 200
    
    response = client.get(f"players/name/{testuser['user_name']}")
    player_info = response.json()

    assert response.status_code == 200
    assert isinstance(player_info['id'], str)


def test_delete_user_by_name(client: TestClient):
    post_user = client.post("auth/signup", json={
        **testuser
    })
    
    assert post_user.status_code == 200
    
    response = client.delete(f"players/delete/{testuser['user_name']}")
    assert response.status_code == 200

    response = client.get(f"players/name/{testuser['user_name']}")
    assert response.status_code == 404



