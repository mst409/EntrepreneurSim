import datetime
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session


from src.auth.schemas import User
from src.banking.models import BankAccount

def test_create_user(client: TestClient, db_session: Session):
    # test creating a new user
    response = client.post("/auth/signup", json={
        "user_name": "testuser",
        "email": "user@example.com",
        "password": "testpassword"
    })
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

'''
    add this after the player models are added to the main
    # get the auto created player form the api
    response = client.get("/players/name/testuser")
    # test the status code
    assert response.status_code == 200

    # get the response as JSON
    get_user_response = response.json()

    # check for the id, created_at and user_info fields 
    assert isinstance(get_user_response["id"], str)
    assert isinstance(get_user_response["created_at"], str)
    # check if the players username is the created user_name
    assert get_user_response["user_info"]["user_name"] == "testuser"
    assert isinstance(get_user_response["user_info"], dict)

    # get the BankAccount obj from the db
    bank_account = db_session.query(BankAccount).first()
    
    # check for the BankAccount obj
    assert isinstance(bank_account, BankAccount)

    # check if the bank_account-player foreigen key points to the player id
    assert str(bank_account.player_info.id) == get_user_response["id"]
'''



def test_email_already_registered(client: TestClient):
    '''test creating a user with a different username and email 
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