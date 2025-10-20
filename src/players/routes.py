from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from pydantic import UUID4
from sqlalchemy.orm import Session


from src.database import get_db
from src.auth.models import User
from src.players.models import Player
from src.players.schemas import PlayerCreate, PlayerResponse


router = APIRouter(prefix="/players", tags=["players"])


@router.post("/create", response_model=dict[str,  str])
def create_player(body: PlayerCreate, 
                  db: Session = Depends(get_db)):
    player = db.query(User).filter(User.user_name == body.user_name
                                   or User.email == body.user_email).first()
    if not player:
        raise HTTPException(status_code=404, 
                            detail=f"user with name '{body.user_name}' or email '{body.user_email}' not found")
    new_palyer = Player(user_id = player.id)
    db.add(new_palyer)
    db.commit()
    db.refresh(new_palyer)

    return {"message": "new player created"}


@router.get("/name/{name}", response_model=PlayerResponse)
def get_player_by_name(name: str, db: Session = Depends(get_db)):

    # get the user id for the name if the request
    user = db.query(User).filter(User.user_name == name).first()
    if not user: 
        raise HTTPException(status_code=404, 
                            detail=f"player with name '{name}' not found")
    
    # get the player obj with the id
    player = db.query(Player).filter(Player.user_id == user.id).first()
    if not player:
        raise HTTPException(status_code=404,
                            detail=f'player with name "{name}" not found')
    # TODO #2 find how to get all the data in one query with a join

    return player


@router.delete("/delete/{name}", response_model=dict[str, str])
def delete_player_by_name(name: str, db: Session = Depends(get_db)):
        # get the user id for the name if the request
    user = db.query(User).filter(User.user_name == name).first()
    if not user: 
        raise HTTPException(status_code=404, 
                            detail=f"player with name '{name}' not found")
    
    # get the player obj with the id
    player = db.query(Player).filter(Player.user_id == user.id).first()
    if not player:
        raise HTTPException(status_code=404,
                            detail=f'player with name "{name}" not found')
    
    db.delete(player)
    db.commit()

    return {"message": f"player '{player.id}' deleted"}