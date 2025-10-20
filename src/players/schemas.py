import datetime
from pydantic import BaseModel, Field, UUID4, EmailStr

from src.auth.schemas import User



class BasePlayer(BaseModel):
    pass

class PlayerCreate(BasePlayer):
    user_name: str | None
    user_email: EmailStr | None

class PlayerBuisnessResponse(BasePlayer):
    id: UUID4
    created_at: datetime.datetime

    class Config: 
        from_attributes = True


class PlayerResponse(BasePlayer):
    id: UUID4
    created_at: datetime.datetime
    user_info: User

    class Config: 
        from_attributes = True