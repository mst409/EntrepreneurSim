import datetime
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


class PlayerResponse(BasePlayer):
    id: UUID4
    user_info: UserBase 
    bank_account: BankAccountResponse   
    business_info: BusinessResponse
    class Config: 
        from_attributes = True