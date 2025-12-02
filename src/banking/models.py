import uuid
import datetime as dt
from sqlalchemy import Column, String, Integer,Float, ForeignKey, DateTime
from sqlalchemy.types import Uuid
from sqlalchemy.orm import relationship
from src.database import Base



class BankAccount(Base):
    __tablename__ = "bank_accounts"

    id = Column(Uuid(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    account_number = Column(Integer, nullable=False, index=True)
    acc_type = Column(String)
    current_balance = Column(Float, default=30)

    player = relationship("Player", back_populates="bank_account")

class Transaction(Base):
    __tablename__ = "transactions"
#    A transaction table, must provide amount, from_acc and to_acc
    id = Column(Uuid(as_uuid=True), primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    from_acc = Column(Uuid, ForeignKey("bank_accounts.id"))
    to_acc = Column(Uuid, ForeignKey("bank_accounts.id"))
    made_at = Column(DateTime, default=dt.datetime.now(dt.timezone.utc))