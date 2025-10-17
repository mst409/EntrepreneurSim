from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.auth.models import User
from src.database import get_db
from src.players.models import Player
from .schemas import BusinessCreate, BusinessResponse
from .models import Business


router = APIRouter(prefix="/buisnesses", tags=["buisnesses"])


@router.post("/create", response_model=dict[str, str])
def create_bisness(body: BusinessCreate, db: Session = Depends(get_db)):

    # check if buisness name already exsits
    if db.query(Business).filter(Business.business_name == body.business_name).first():
        raise HTTPException(status_code=409, 
                            detail=f"Buissnes with name '{body.owner_name}' already found")
    # get owner id
    owner = db.query(User).filter(User.user_name == body.owner_name).first()
    if not owner:
        raise HTTPException(status_code=404, 
                            detail=f"User with name '{body.owner_name}' not found")
    
    new_buisiness = Business(**body.model_dump(exclude={"owner_name"}))
    new_buisiness.owner = owner.id
    db.add(new_buisiness)
    db.commit()
    db.refresh(new_buisiness)

    return {"message": f'Buisness "{body.business_name}" created'}

@router.get("/all")
def get_all_buisness(db: Session = Depends(get_db)):
    all_buisness = db.query(Business, Player, User).join(Business).all()
    return all_buisness