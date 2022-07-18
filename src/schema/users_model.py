from datetime import datetime, timezone

from pydantic import BaseModel, EmailStr, Field

from src.schema.questions_model import Level


class User(BaseModel):
    """
    Model to hold  user data.
    """

    name: str = Field(min_length=10)
    password: str = Field(min_length=7)
    email: EmailStr
    linked_in: str = Field(min_length=8)
    skill: list[str]
    level: Level
    created_at: str = str(datetime.now(timezone.utc))


class User_login(BaseModel):
    """
    Model to collect user login details.
    """

    email: EmailStr
    password: str


class Verifier(BaseModel):
    """
    Model to hold backend verifier data.
    """

    email: EmailStr
    password: str = Field(min_length=7)
    is_admin: bool = True
