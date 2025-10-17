import datetime
from pydantic import BaseModel, Field, UUID4, EmailStr



class BasePlayer(BaseModel):
    pass

class PlayerCreate(BasePlayer):
    user_name: str | None
    user_email: EmailStr | None

class PlayerResponse(BasePlayer):
    id: UUID4
    user_id: int | UUID4
    user_name: str
    created_at: datetime.datetime