from typing import Any
from pydantic import BaseModel, Field, UUID4
import uuid
from src.players.schemas import PlayerBuisnessResponse


class BaseBusiness(BaseModel):
    business_name:str = Field(max_length=20)


class BusinessCreate(BaseBusiness):
    owner_name: str

class BusinessResponse(BaseBusiness):
    # TODO add the owner name to the response model
    id: UUID4
    owner: PlayerBuisnessResponse

    class Config:
        from_attributes = True