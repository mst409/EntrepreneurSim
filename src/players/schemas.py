import datetime
from typing import Any, List
from pydantic import BaseModel, Field, UUID4, EmailStr

from src.auth.schemas import UserBase
from src.banking.schemas import BankAccountResponse
from src.businesses.schemas import BusinessResponse


class BasePlayer(BaseModel):
    pass


class PlayerCreate(BasePlayer):
    user_name: str | None
    user_email: EmailStr | None


class PlayerBusinessResponse(BasePlayer):
    id: UUID4
    user_name: str | None
    created_at: datetime.datetime

    class Config:
        from_attributes = True


class Owner(BaseModel):
    # player_id: str
    business: BusinessResponse

    class Config:
        from_attributes = True


class BusinessPlayerResponse(BaseModel):
    id: UUID4
    business_name: str
    # PayRoll: str


class PlayerResponse(BasePlayer):
    id: UUID4
    user_info: UserBase
    bank_account: BankAccountResponse
    business: List[BusinessResponse]

    class Config:
        from_attributes = True


class BusinessWithPlayer(BaseModel):
    business_name: str
    owner: PlayerResponse


class EmployeeBase(BaseModel):
    roll: str
    salary: float
    # make an enum for wage_types
    wage_type: str


class EmployeeCreate(EmployeeBase):
    player_id: UUID4
    business_id: UUID4


class EmployeeResponse(EmployeeBase):
    pass
