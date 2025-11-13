from fastapi import Depends
from sqlalchemy.orm import Session

from random import randrange
from sqlalchemy import Uuid
from src.database import get_db
from src.players.models import Player
from .models import BankAccount
from .schemas import AccountTypes, BaseBankAccount

def create_account_number():
    number = randrange(start=10**10, stop=10**11-1)
    return number


def create_acc(acc_type: str, db:Session):
    new_acc = BankAccount(
        account_number = create_account_number(),
        acc_type = acc_type,
        )
    try: 
        db.add(new_acc)
    except Exception as e:
        db.rollback()
        print(e)
        create_acc(acc_type=acc_type, db=db)
    db.commit()
    

    return new_acc