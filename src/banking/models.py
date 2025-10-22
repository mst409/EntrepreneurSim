import uuid
import datetime as dt
from sqlalchemy import Column, String, Integer,Float, ForeignKey, DateTime
from sqlalchemy.types import Uuid
from sqlalchemy.orm import relationship
from src.database import Base

class BankAccount(Base):
    __tablename__ = "bank_accounts"

    id = Column(Uuid(as_uuid=True), primary_key=True, index=True)
    player = Column(Uuid, ForeignKey("players.id"))
    capital = Column(Float, nullable=False, default=30.00)
    account_number = Column(Integer, nullable=False, index=True)
    type = Column(String)

    player_info = relationship("Player")


class Transaction(Base):
    __tablename__ = "transactions"
    '''A trasaction table, must provide ammount, from_acc and to_acc'''
    id = Column(Uuid(as_uuid=True), primary_key=True, index=True)
    ammount = Column(Float, nullable=False)
    from_acc = Column(Uuid, ForeignKey("players.id"))
    to_acc = Column(Uuid, ForeignKey("businesses.id"))
    made_at = Column(DateTime, default=dt.datetime.now(dt.timezone.utc))