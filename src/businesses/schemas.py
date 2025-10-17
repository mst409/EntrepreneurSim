from typing import Any
from pydantic import BaseModel, Field, UUID4

from src.auth.schemas import User


class BaseBusiness(BaseModel):
    business_name:str = Field(max_length=20)


class BusinessCreate(BaseBusiness):
    owner_name: str
    # owenr_id: int | None = Field(default=None)

class BusinessResponse(BaseBusiness):
    # TODO add the owner name to the response model
    owenr: int | UUID4
    id: UUID4