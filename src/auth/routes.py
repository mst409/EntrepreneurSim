import datetime as dt
from datetime import timedelta
from typing import Annotated
from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from src.players.services import auto_create_player
from src.auth.schemas import CreateUser, Token
from src.database import get_db
from src.auth.services import authenticate_user, create_access_token, get_password_hash
from src.auth.models import User

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/signup")
async def signup(user: CreateUser, db=Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = User(
        name = user.name,
        email = user.email,
        hashed_password = get_password_hash(user.password),
        created_at = dt.datetime.now(dt.timezone.utc)
        )
    
    db.add(new_user)
    db.commit()
    auto_create_player(user=new_user, db=db)
    return {"message": "User created successfully"}


@router.post("/token", response_model=Token)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db=Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(data={"sub": user.user_name}, expires_delta=access_token_expires)

    return Token(access_token=access_token, token_type="bearer")
