from __future__ import annotations

import os

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    """Class to hold application config values."""

    PROJECT_NAME = "Verificate"
    MONGO_SERVER = os.getenv("MONGO_SERVER")
    #SECRET_KEY = os.getenv("SECRET_KEY")


settings = Settings()
