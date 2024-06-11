from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from enum import Enum

class Roles(str, Enum):
    ADMIN = 'admin'
    STUDENT = 'student'
    TEACHER = 'teacher'


class UserPublic(BaseModel):
    email: EmailStr
    firstName: str
    lastName: str
    role: Roles


class UserCreate(UserPublic):
    password: str
    
    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: str | None

    class Config:
        from_attributes = True

class FrontendData(BaseModel):
    token: Token
    user: UserPublic