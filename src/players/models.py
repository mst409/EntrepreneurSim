import uuid
import datetime as dt
from sqlalchemy import Column, String, Integer,Float, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.types import Uuid

from src.database import Base

players_businesses = Table(
    'owners',
    Base.metadata,
    Column("id", primary_key=True),
    Column("player_id", ForeignKey("players.id")),
    Column("business", ForeignKey("businesses.id")),
)

class Player(Base):
    __tablename__ = "players"

    id = Column(Uuid(as_uuid=True), primary_key=True, 
                index=True, default=uuid.uuid4)
    #user_name = Column(String(15), nullable=True)
    user_id = Column(Uuid, ForeignKey("users.id", ondelete="CASCADE"), nullable=True)
    bank_account_id = Column(Uuid, ForeignKey("bank_accounts.id"), nullable=True)

    user_info = relationship("User", back_populates="player", uselist=False, foreign_keys=[user_id])

    bank_account = relationship("BankAccount", back_populates="player", foreign_keys=[bank_account_id])
    
    # business: Mapped[list["Business"]] = relationship(secondary=players_businesses, back_populates="owner")
    employer = relationship("Employee", back_populates="player")

# class Owners(Base):
#     __tablename__ = "owners"

#     id = Column(Uuid(as_uuid=True), primary_key=True, 
#                 index=True, default=uuid.uuid4)

#     player_id = Column(Uuid, ForeignKey("players.id", ondelete="CASCADE"))
#     business_id = Column(Uuid, ForeignKey("businesses.id", ondelete="CASCADE"))

#     player = relationship("Player", back_populates="business", foreign_keys=[player_id])

#     business = relationship("Business", back_populates="owner", foreign_keys=[business_id])
