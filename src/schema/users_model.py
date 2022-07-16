from datetime import datetime, timezone

from pydantic import BaseModel, EmailStr, Field
from .questions_model import Level

from pydantic import BaseModel

class user(BaseModel):

    name: str = Field(min_length=10)
    password: str = Field(min_length=7)
    email: EmailStr
    linked_in:str = Field(min_length=8)
    skill:list[str]
    level:Level
    created_at: str = str(datetime.now(timezone.utc))


class verifier(BaseModel):
    email: EmailStr
    password: str = Field(min_length=7)
    is_admin: bool= True

