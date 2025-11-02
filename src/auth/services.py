from fastapi.security import OAuth2PasswordBearer
import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from .models import User as user_table

SECRET_KEY = "b7ab9c1f2c5b9c727e1bbc891dfd39d30c6cab740b9c541aec41f10c5cc364af"
ALGORITHM = "HS256"


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def authenticate_user(db, email: str, password: str):
    user = db.query(user_table).filter(user_table.email == email).first()
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    #! "encode" is not a known attribute of jwt 
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
