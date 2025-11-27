from enum import Enum
from pydantic import BaseModel, Field, UUID4

from src.players.schemas import PlayerResponse

class PayRoll(str, Enum):
    first = ("00",)
    fifteenth = "15"

class BaseBusiness(BaseModel):
    business_name: str = Field(max_length=20)
    payroll: PayRoll


class BusinessCreate(BaseBusiness):
    owner_name: str


class BusinessResponse(BaseBusiness):
    # TODO #14 add the owner name to the response model
    id: UUID4
    owner: list[PlayerResponse]
    class Config:
        from_attributes = True
