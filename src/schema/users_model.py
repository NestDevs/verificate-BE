from datetime import datetime, timezone

from pydantic import BaseModel, EmailStr, Field, HttpUrl

from src.schema.questions_model import Level


class Skills(BaseModel):
    """
    models to hold list of users skills
    """

    skill: list[str] | None = None


class User(BaseModel):
    """
    Model to hold  user data.
    """

    first_name: str = Field(min_length=10)
    last_name: str = Field(min_length=10)
    password: str = Field(min_length=7)
    email: EmailStr
    linked_in: HttpUrl
    skill: Skills
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
