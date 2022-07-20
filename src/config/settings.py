from __future__ import annotations

import os

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    """Class to hold application config values.""" 

    PROJECT_NAME = "Verificate"
    MONGO_SERVER = os.getenv("MONGO_SERVER")
    SECRET_KEY = os.getenv("SECRET_KEY")
    WEB3_PROVIDER_URL = os.getenv("WEB3_PROVIDER_URL")
    CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")
    OWNER_ACCOUNT = os.getenv("OWNER_ACCOUNT")
    OWNER_ACCOUNT_PRIVATE_KEY = os.getenv("OWNER_ACCOUNT_PRIVATE_KEY")
    SECRET_KEY2 = os.getenv("SECRET_KEY2")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 200


settings = Settings()
