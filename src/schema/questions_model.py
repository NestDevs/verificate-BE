from datetime import datetime, timezone
from enum import Enum

from pydantic import BaseModel, Field


class Level(str, Enum):
    """Enum for test skill levels"""

    BEGINNER = "BEGINNER"
    INTERMEDIATE = "INTERMEDIATE"
    ADVANCED = "ADVANCED"


class Question(BaseModel):
    """Base model to hold question data."""

    test_name: str = Field(min_length=5)
    skill_level: Level
    set_by: str
    uploaded_at: str = str(datetime.now(timezone.utc))

    class Config:
        """question model configuration."""

        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "test_name": "verificate_B1",
                "skill_level": "BEGNNER",
                "set_by": "xdbr44596fldkejksfA1",
                "uploaded_at": "2022-04-22 22:38:33.075643",
            },
        }
