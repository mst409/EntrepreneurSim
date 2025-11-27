from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from src.businesses.models import Business
from src.businesses.schemas import BusinessResponse
from src.banking.schemas import BankAccountResponse
from src.auth.models import User
from src.players.models import Player
from src.players.schemas import PlayerResponse


router = APIRouter(prefix="/players", tags=["players"])


@router.get("/name/{name}", response_model=PlayerResponse)
async def get_player_by_name(name: str, db: Session = Depends(get_db)):
    player = db.query(Player).join(Player.user_info).filter(User.name == name).first()

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
