from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from enum import Enum

class Roles(str, Enum):
    ADMIN = 'Administrator'
    STUDENT = 'Student'
    TEACHER = 'Teacher'


class UserPublic(BaseModel):
    id: str
    email: EmailStr
    role: Roles


class UserCreate(UserPublic):
    password: str
    
    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    id: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: str | None

    class Config:
        from_attributes = True