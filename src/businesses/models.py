import uuid
from sqlalchemy import Column, Integer, String, ForeignKey, Uuid
from sqlalchemy.orm import relationship
from src.database import Base

class Business(Base):
    __tablename__ = "businesses"

    id = Column(Uuid(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    # TODO #3 cheng to UUID4 after the user id is changed
    owner_id = Column(Uuid, ForeignKey("users.id", ondelete="CASCADE"))
    business_name = Column(String(20), nullable=False, unique=True)
    # bank_account = Column(Uuid, ForeignKey("bank_accounts.id"))

    owner = relationship("User",back_populates="business")