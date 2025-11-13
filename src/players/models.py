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
    user_name = Column(String(15), nullable=True)
    user_id = Column(Uuid, ForeignKey("users.id", ondelete="CASCADE"), nullable=True)
    bank_account_id = Column(Uuid, ForeignKey("bank_accounts.id"), nullable=True)

    

    bank_account = relationship("BankAccount", back_populates="player", foreign_keys=[bank_account_id])

    user_info = relationship("User", back_populates="player", uselist=False, foreign_keys=[user_id])