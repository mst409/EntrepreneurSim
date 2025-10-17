from fastapi import Depends
from sqlalchemy.orm import Session


from sqlalchemy import Uuid
from database import get_db
from .models import BankAccount
from .schemas import AccountTypes, BaseBankAccount




def create_player_bank_account(player_id: Uuid, db: Session = Depends(get_db)):
    '''Creates a new bank acoount FOR PLAYER, returns true if created and false if 
    player id already has an account'''
    if db.query(BankAccount).filter(BankAccount.player == player_id 
                                    and BankAccount.type == 'player'):
        return False
    new_account = BankAccount(player = player_id, type=AccountTypes.Player)
    db.add(new_account)
    db.commit()
    db.refresh(new_account)


    return True

def create_buisness_bank_account(player_id: Uuid, db: Session = Depends(get_db)):
    '''Creates a new bank acoount FOR BUISNESS, returns true if created and false if 
    player id already has an account'''
    if db.query(BankAccount).filter(BankAccount.player == player_id 
                                    and BankAccount.type == 'buisness'):
        return False
    new_account = BankAccount(player = player_id, type=AccountTypes.Buisness)
    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    return True