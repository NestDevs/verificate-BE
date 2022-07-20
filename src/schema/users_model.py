from datetime import datetime, timezone
from enum import Enum

from pydantic import BaseModel, EmailStr, Field, HttpUrl
from src.schema.questions_model import Category

class Levels(str, Enum):
    """enum for skill level"""

    BEGINNER = "BEGINNER"
    INTERMEDIATE = "INTERMEDIATE"
    ADVANCED = "ADVANCED"


class Result(str, Enum):
    """enum for test status"""

    FAILED = "FAILED"
    PASSED = "PASSED"


class TestResult(BaseModel):
    """
    to hold eaxh categories test results
    """
    user_id: str
    category:Category
    level: Levels
    test_result: Result
    score: float = 0.0


class User(BaseModel):
    """
    Model to hold  user data.
    """

    first_name: str = Field(min_length=3)
    last_name: str = Field(min_length=3)
    password: str = Field(min_length=7)
    email: EmailStr
    linked_in: HttpUrl
    results: dict[str, list[TestResult]] = None
    created_at: str = str(datetime.now(timezone.utc))

class UserAccess(User):
    """Model to assign access to user"""
    is_verifier: bool = False
    is_admin: bool = False
class UserLogin(BaseModel):
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
