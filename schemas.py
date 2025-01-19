from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str
    age: int
    gender: str
    email: EmailStr  # Ensures valid email
    city: str
    interests: str




from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    name: str
    age: int
    gender: str
    email: EmailStr
    city: str
    interests: str

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    email: Optional[EmailStr] = None
    city: Optional[str] = None
    interests: Optional[str] = None
