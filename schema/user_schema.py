from pydantic import BaseModel
from pydantic import BaseModel, EmailStr, field_validator
from typing import Annotated
from pydantic import constr



class UserCreate(BaseModel):
    firstname: Annotated[str, constr(min_length=2, max_length=30)]
    lastname: Annotated[str, constr(min_length=2, max_length=30)]
    phone: Annotated[str, constr(pattern=r'^\d{10}$')]
    address: Annotated[str, constr(min_length=5)]
    email: EmailStr
    password: Annotated[str, constr(min_length=8)]
    confirm_password: str

    @field_validator('firstname', 'lastname')
    @classmethod
    def names_must_be_alpha(cls, v, info):
        if not v.isalpha():
            raise ValueError(f"{info.field_name.capitalize()} must contain only letters")
        return v
    @field_validator('confirm_password')
    @classmethod
    def passwords_match(cls, v, values):
        if 'password' in values.data and v != values.data['password']:
            raise ValueError('Passwords do not match')
        return v
    @field_validator('phone')
    @classmethod
    def validate_phone(cls, v):
        if not v.isdigit():
            raise ValueError("Phone number must contain only digits")
        if not v.isdigit() or len(v) != 10:
            raise ValueError("Phone number must be exactly 10 digits")
        return v

class Token(BaseModel):
    access_token: str
    token_type: str

class UserOut(BaseModel):
    id: int
    firstname: str
    lastname: str
    email: EmailStr
    phone:int

    class Config:
        orm_mode = True
class LoginRequest(BaseModel):
    email: EmailStr
    password: Annotated[str, constr(min_length=8)]

class ForgotPassword(BaseModel):
    email: EmailStr

