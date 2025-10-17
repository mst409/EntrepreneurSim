import uuid
import datetime as dt
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.types import Uuid

from src.database import Base


class Player(Base):
    __tablename__ = "players"

    id = Column(Uuid(as_uuid=True), primary_key=True, 
                index=True, default=uuid.uuid4)
    # TODO change the column type to uuid
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=dt.datetime.now(dt.timezone.utc))