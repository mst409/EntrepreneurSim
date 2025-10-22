# this file contains the database models for the authentication system
import datetime as dt
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from src.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(DateTime, default=dt.datetime.now(dt.timezone.utc))

    player = relationship("Player", back_populates="user_info", cascade="all, delete-orphan")