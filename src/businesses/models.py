import uuid
from sqlalchemy import Column, DateTime, Float, String, ForeignKey, Uuid
from sqlalchemy.orm import relationship
from src.database import Base



class Business(Base):
    __tablename__ = "businesses"

    id = Column(Uuid(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    business_name = Column(String(20), nullable=False, unique=True)
    #bank_account_id = Column(Uuid, ForeignKey("bank_accounts.id", ondelete="CASCADE"))
    payroll = Column(String, nullable=False, index=True)
    # this will be a 1 to many relationship, from one business to many players
    #payment = Column(Uuid, ForeignKey("players.id"))

    owner = relationship("Player", back_populates="business_info")    

    #bank_account = relationship("BankAccount", back_populates="player", foreign_keys=[bank_account_id])

    #job_info = relationship("Employee", back_populates="business")

    
'''
class Employee(Base):
    __tablename__ = "employees"

    id = Column(Uuid(as_uuid=True), primary_key=True,index=True,  default=uuid.uuid4)
    roll = Column(String(10), nullable=False, index=True)
    salary = Column(Float)
    wage_type = Column(String(10))
    player_id = Column(Uuid, ForeignKey("players.id", ondelete="CASCADE"))
    business_id = Column(Uuid, ForeignKey("businesses.id", ondelete="CASCADE"))
    
    player = relationship("Player", back_populates="job_info",foreign_keys=[player_id])
    business = relationship("Business", back_populates="job_info", foreign_keys=[business_id])
    
'''    