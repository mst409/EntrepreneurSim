from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from pydantic import UUID4
from sqlalchemy.orm import Session


from src.database import get_db
from src.auth.models import User
from src.auth.schemas import UserResponse
from src.players.models import Player
from src.players.schemas import PlayerCreate, PlayerResponse
from src.players.services import auto_create_player


router = APIRouter(prefix="/players", tags=["players"])



@router.get("/name/{name}", response_model=PlayerResponse)
async def get_player_by_name(name: str, db: Session = Depends(get_db)):
    player = db.query(Player).join(Player.user_info).filter(User.name == name).first()
    return player




@router.delete("/delete/{name}", response_model=dict[str, str])
async def delete_player_by_name(name: str, db: Session = Depends(get_db)):
    #delete player (not user) my name
    player: Player = db.query(Player).join(Player.user_info).filter(User.name == name).first()
    db.delete(player)
    db.commit()

    return {"message": f"player '{player.id}' deleted"} # pyright: ignore[reportOptionalMemberAccess]