from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from src.database import get_db
from src.auth.models import User
from src.players.models import Player

from src.players.views import PlayerView
from src.players.schemas import PlayerResponse


router = APIRouter(prefix="/players", tags=["players"])


@router.get("/name/{name}", response_model=PlayerResponse)
async def get_player_by_name(name: str, db: Session = Depends(get_db)):
    # this is using a view instead of joining on each query
    player = (
        db.query(Player)
        .join(PlayerView, PlayerView.player_id == Player.id)
        .filter(PlayerView.name == name)
        .first()
    )
    if not player:
        raise HTTPException(detail=f"Player {name} not found", status_code=404)
    return player


@router.delete("/delete/{name}", response_model=dict[str, str])
async def delete_player_by_name(name: str, db: Session = Depends(get_db)):
    # delete player (not user) my name
    player: Player = (
        db.query(Player).join(Player.user_info).filter(User.name == name).first()
    )
    db.delete(player)
    db.commit()

    return {"message": f"player '{player.id}' deleted"}  # pyright: ignore[reportOptionalMemberAccess]
