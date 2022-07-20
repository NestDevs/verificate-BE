from typing import Optional
from datetime import datetime, timezone
from enum import Enum
from pydantic import BaseModel, Field


class Level(str, Enum):
    """Enum for test skill levels"""

    BEGINNER = "BEGINNER"
    INTERMEDIATE = "INTERMEDIATE"
    ADVANCED = "ADVANCED"
class Category(str, Enum):
    """Enum for test categories"""

    GENERAL = "GENERAL"
    REACT = "REACT"
    ANGULAR = "ANGULAR"
    VUE = "VUE"
    NODE = "NODE"
    FLASK = "FLASK"
    DJANGO = "DJANGO"
    PYTHON = "PYTHON"
    JAVA = "JAVA"
    C = "C"
    CPP = "CPP"
    C_SHARP = "C#"
    GO = "GO"
    RUBY = "RUBY"
    PHP = "PHP"
    SWIFT = "SWIFT"
    KOTLIN = "KOTLIN"
    HASKELL = "HASKELL"
    JAVASCRIPT = "JAVASCRIPT"
    TYPESCRIPT = "TYPESCRIPT"
    RUST = "RUST"
    FLUTER = "FLUTER"
    HTML = "HTML"
    CSS = "CSS"
    SQL = "SQL"
    MYSQL = "MYSQL"
    POSTGRESQL = "POSTGRESQL"
    MONGODB = "MONGODB"
    REDIS = "REDIS"
    ELASTIC = "ELASTIC"
    SASS = "SASS"
    LESS = "LESS"
    STYLUS = "STYLUS"
    COFFEE = "COFFEE"
    LUA = "LUA"
    LARAVEL = "LARAVEL"

class Option(BaseModel):
    """Model for test options"""
    a:str
    b:str
    c:str
    d:str
class Question(BaseModel):
    """Base model to hold question meta data."""

    test_name: str = Field(min_length=5)
    skill_level: Level
    question:str
    options: Option
    answer: str
    mark:float
    duration: float
    category:Category
    set_by: str
    uploaded_at: str = str(datetime.now(timezone.utc))
    

    class Config:
        """question model configuration."""

        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "test_name": "verificate_B1_React",
                "skill_level": "BEGNNER",
                "question": "What is the correct way to write a for loop in JavaScript?",
                "options": {
                    "a": "for (let i = 0; i < 10; i++)",
                    "b": "for (let i = 10; i > 0; i--)",
                    "c": "for (let i = 0; i <= 10; i++)",
                    "d": "for (let i = 10; i >= 0; i--)",
                },
                "duration":2,#in minutes per question
                "set_by": "xdbr44596fldkejksfA1",
                "uploaded_at": "2022-04-22 22:38:33.075643",
            },
        }

class UpdateQuestion(BaseModel):
    """
    Base model to hold question data.
    """
    test_name: Optional[str] = Field(min_length=5)
    question:Optional[str]
    options: Optional[Option]
    answer: Optional[str]
    mark:float
    duration: Optional[float]
    category:Optional[Category]
   