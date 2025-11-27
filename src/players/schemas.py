from typing import Any
from pydantic import BaseModel, UUID4, EmailStr

from src.auth.schemas import UserBase
from src.banking.schemas import BankAccountResponse 

class BasePlayer(BaseModel):
    pass


class PlayerCreate(BasePlayer):
    user_name: str | None
    user_email: EmailStr | None

class BusinessForPlayer(BaseModel):
    business_name: str
    payroll: str | Any

class PlayerResponse(BasePlayer):
    id: UUID4
    user_info: UserBase 
    bank_account: BankAccountResponse   
    business: list[ BusinessForPlayer ]
    class Config: 
        from_attributes = True


    

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
