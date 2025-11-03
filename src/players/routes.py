from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from src.database import get_db
from src.auth.models import User
from src.players.models import Player
from src.players.schemas import PlayerResponse


router = APIRouter(prefix="/players", tags=["players"])



@router.get("/name/{name}", response_model=PlayerResponse)
async def get_player_by_name(name: str, db: Session = Depends(get_db)):

    # get the user id for the name in the request
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
async def delete_player_by_name(name: str, db: Session = Depends(get_db)):
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