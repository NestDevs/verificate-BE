from __future__ import annotations

import motor.motor_asyncio

from src.config.settings import settings

# create connection
client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGO_SERVER)

#  create database
database = client["verificate"]
users_collection = database.get_collection("users")
user_results_collection = database.get_collection("user_result")
verifiers_collection = database.get_collection("verifiers")
