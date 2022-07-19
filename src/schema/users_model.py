from datetime import datetime, timezone

from pydantic import BaseModel, EmailStr, Field, HttpUrl


class Levels(BaseModel):
    """
    true boolean if beginer exam is passed.
    """

    BEGINNER: bool = False
    INTERMEDIATE: bool = False
    ADVANCED: bool = False


class Test_results(BaseModel):
    """
    to hold eaxh categories test results
    """

    email: EmailStr
    category: Levels


class User(BaseModel):
    """
    Model to hold  user data.
    """

    first_name: str = Field(min_length=10)
    last_name: str = Field(min_length=10)
    password: str = Field(min_length=7)
    email: EmailStr
    linked_in: HttpUrl
    results: Test_results | None = None
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
