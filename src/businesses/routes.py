from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.auth.models import User
from src.database import get_db
from src.players.models import Player
from .schemas import BusinessCreate, BusinessResponse
from .models import Business


router = APIRouter(prefix="/businesses", tags=["businesses"])


@router.post("/create", response_model=dict[str, str])
async def create_business(body: BusinessCreate, db: Session = Depends(get_db)):

    # check if business name already exists
    if db.query(Business).filter(Business.business_name == body.business_name).first():
        raise HTTPException(status_code=409, 
                            detail=f"Business with name '{body.owner_name}' already found")
    # get owner player object
    owner = db.query(Player).join(Player.user_info).filter(User.name == body.owner_name).first()
    if not owner:
        raise HTTPException(detail=f"Player {body.owner_name} not found, to create a business you must have a player", status_code=404)
    
    
    new_business = Business(**body.model_dump(exclude={"owner_name"}))
    db.add(new_business)
    db.commit()
    db.refresh(new_business)

    return {"message": f'Business "{body.business_name}" created'}

@router.get("/all", response_model=list[BusinessResponse])
async def get_all_business(db: Session = Depends(get_db)):
    all_business = db.query(Business).all()
    return all_business