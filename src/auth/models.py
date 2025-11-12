# this file contains the database models for the authentication system
import datetime as dt
import uuid
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.types import Uuid
from sqlalchemy.orm import relationship
from src.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Uuid(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(DateTime, default=dt.datetime.now(dt.timezone.utc))
    bio = Column(String(255), null=True)
    #TODO add an option for a profile pic
    profile = Column(String(255), null=True)
    
    player_id = Column(Uuid, ForeignKey("players.id"), nullable=True)
    
    player = relationship("Player", back_populates="user_info", cascade="all, delete-orphan", foreign_keys=[player_id])
