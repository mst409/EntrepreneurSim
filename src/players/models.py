import uuid
from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.types import Uuid

from src.database import Base


players_businesses = Table(
    "owners",
    Base.metadata,
    Column("player_id", Uuid, ForeignKey("players.id"), primary_key=True),
    Column("business_id", Uuid, ForeignKey("businesses.id"), primary_key=True),
)


class Player(Base):
    __tablename__ = "players"

    id = Column(Uuid(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    # user_name = Column(String(15), nullable=True)
    user_id = Column(Uuid, ForeignKey("users.id", ondelete="CASCADE"), nullable=True)
    bank_account_id = Column(Uuid, ForeignKey("bank_accounts.id"), nullable=True)

    user_info = relationship(
        "User", back_populates="player", uselist=False, foreign_keys=[user_id]
    )

    bank_account = relationship(
        "BankAccount", back_populates="player", foreign_keys=[bank_account_id]
    )

    business = relationship(
        "Business", secondary=players_businesses, back_populates="owner"
    )
    employer = relationship("Employee", back_populates="player")
