# this file contains the database models for the authentication system
import datetime as dt
import uuid
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.types import Uuid
from src.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Uuid(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    user_name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(DateTime, default=dt.datetime.now(dt.timezone.utc))
