from typing import Any
from fastapi import Depends, HTTPException
from sqlalchemy import Uuid
from sqlalchemy.orm import Session
from src.auth.models import User
from src.banking.models import BankAccount
from src.database import get_db
from src.players.models import Player
from src.banking.services import create_acc




def auto_create_player(user: User, db: Session) -> bool | int:
    '''create a player with a bank account when a user is created, returns account number if crated and False if not'''
    # create new player
    new_player = Player(user_info = user)
    # create new bank account 
    new_acc = create_acc(acc_type="player", db=db)
    # link the new account to the new player via the "bank account" relationship in the player model
    new_player.bank_account = new_acc
    db.add(new_player)
   
    
    #new_player.bank_account = account

    db.commit()
    return True