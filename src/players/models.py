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
    # TODO change the column type to uuid
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=dt.datetime.now(dt.timezone.utc))
    # bank_account = Column(Integer, ForeignKey("bank_accounts.id"), nullable=False)

    user_info = relationship("User", back_populates="player")
    buisness = relationship("Business", back_populates="owner")


class Employee(Base):
    __tablename__ = "employees"
    id = Column(Uuid(as_uuid=True), primary_key=True, index=True)
