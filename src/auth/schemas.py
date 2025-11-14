# this file contains the pydantic models for the authentication system

from pydantic import BaseModel, EmailStr, Field

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class UserBase(BaseModel):
    name: str
    email: EmailStr 
    bio: str | None = Field(max_length=255) 
    profile: str | None = Field(max_length=255) 

    class Config:
        from_attributes = True


class CreateUser(UserBase):
    password: str
    
class UserResponse(UserBase):
    pass
