from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session


from src.auth.models import User
from src.players.models import Player
from src.database import get_db




def auto_create_player(user_name, user_email, 
                  db: Session) -> bool:
    '''create a player when a user is created'''
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
    return True