from sqlalchemy.orm import Session
from src.auth.models import User
from src.players.models import Player
from src.banking.services import create_acc
from src.players.schemas import PlayerResponse



def auto_create_player(user: User, db: Session) -> PlayerResponse:
    '''Create a player provided a user object, return a new_player obj if created'''

    # create new player
    new_player = Player(user_info = user)
    # create new bank account 
    new_acc = create_acc(acc_type="player", db=db)
    # link the new account to the new player via the "bank account" relationship in the player model
    new_player.bank_account = new_acc
    db.add(new_player)
    db.commit()
    return new_player 