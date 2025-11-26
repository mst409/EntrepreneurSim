from enum import Enum
from pydantic import BaseModel, Field, UUID4

from src.players.models import Owners


class PayRoll(str, Enum):
    first = ("00",)
    fifteenth = "15"


class Owner(BaseModel):
    # business_id: BaseBusiness
    # player_id: UUID4

    class Config:
        from_attributes = True


class BaseBusiness(BaseModel):
    business_name: str = Field(max_length=20)
    payroll: PayRoll


class BusinessCreate(BaseBusiness):
    owner_name: str


class BusinessResponse(BaseBusiness):
    # TODO add the owner name to the response model
    id: UUID4
    owner: Owner

    class Config:
        from_attributes = True
