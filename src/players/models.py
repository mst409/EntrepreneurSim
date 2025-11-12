import uuid
import datetime as dt
from sqlalchemy import Column, String, Integer,Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.types import Uuid

from src.database import Base


class Player(Base):
    __tablename__ = "players"

    id = Column(Uuid(as_uuid=True), primary_key=True, 
                index=True, default=uuid.uuid4)
    name = Column(String(15))
    bank_account_id = Column(Integer, ForeignKey("bank_accounts.id"), nullable=False)
    job = Column(ForeignKey("employees.id", ondelete="CASCADE"))
    
    
    user_info = relationship("User", back_populates="player_id")
    bank_account = relationship("bank_accounts", back_populates="player", foreign_keys=[bank_account_id])