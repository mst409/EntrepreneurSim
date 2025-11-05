from sqlalchemy.orm import Session

from random import choice
from .models import BankAccount
from .schemas import BaseBankAccount

def create_account_number() -> int:
    number = choice(range(10**9, 10**10))
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

