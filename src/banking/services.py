from fastapi import Depends
from sqlalchemy.orm import Session

from random import randrange

from sqlalchemy import Uuid
from src.database import get_db
from .models import BankAccount
from .schemas import AccountTypes, BaseBankAccount

def create_account_number():
    number = randrange(start=10**10, stop=10**11-1)
    return number


def auto_create_bank_account(player_id, type: str, db: Session) -> bool | int:
    '''Creates a new bank account for player or business, returns account number if created and false if 
    player id already has an account'''
    account_number = create_account_number()
    new_account: BaseBankAccount = BankAccount(player = player_id, 
                              account_number = account_number,
                              type=type)
    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    return account_number

