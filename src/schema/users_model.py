from datetime import datetime, timezone
from enum import Enum

from pydantic import BaseModel, EmailStr, Field, HttpUrl

class Levels(str, Enum):
    """ enum for skill level """

    BEGINNER = "BEGINNER"
    INTERMEDIATE = "INTERMEDIATE"
    ADVANCED = "ADVANCED"
    
class Result(str, Enum):
    """ enum for test status"""
    
    FAILED = "FAILED"
    PASSED = "PASSED"

class Test_results(BaseModel):
    """
    to hold eaxh categories test results
    """

    level: Levels
    test_result: Result
    score: int = 0

class Test(BaseModel):
    """ Model for the tests """
    
    language: list[Test_results]

class User(BaseModel):
    """
    Model to hold  user data.
    """

    first_name: str = Field(min_length=10)
    last_name: str = Field(min_length=10)
    password: str = Field(min_length=7)
    email: EmailStr
    linked_in: HttpUrl
    results: dict[str, Test_results]
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
