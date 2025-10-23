from typing import Any
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session


from src.auth.models import User
from src.database import get_db
from src.players.models import Player
from src.banking.services import auto_create_bank_account




def auto_create_player(user_name, user_email, 
                  db: Session) -> bool | int:
    '''create a player with a bank account when a user is created, returns account number if 
    crated and Faise if not'''
    user = db.query(User).filter(User.email == user_email or 
                                 User.user_name == user_name).first()
    if not user: 
        raise HTTPException(status_code=404, 
                            detail=f"user {user_name} not found")
    user_id = user.id
    new_player = Player(user_id = user_id)
    db.add(new_player)
    db.commit()
    db.refresh(new_player)
    player = db.query(Player).filter(Player.user_id == user_id).first()
    if not player:
        return False
    account_number = auto_create_bank_account(player_id=player.id, type="player", db=db)
    return account_number