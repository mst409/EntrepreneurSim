# this file contains the pydantic models for the authentication system

from pydantic import BaseModel, EmailStr, Field

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class CreateUser(BaseModel):
    user_name: str
    email: EmailStr
    password: str = Field(..., min_length=8)
    bio: str = Field(max_length=255) 
    profile: str = Field(max_length=255) 
class User(BaseModel):
    user_name: str
    email: str | None = None

    class Config:
        from_attributes = True