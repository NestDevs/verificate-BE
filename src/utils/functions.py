from __future__ import annotations

from datetime import datetime, timezone

from bson.objectid import ObjectId

from src.config.database import database


class Model:
    """Functions for interacting and querying the database"""

    # generic function to get one data from a collection
    @classmethod
    def findone(cls, query=None, collection="", exeptions=None):
        if query is None:
            query = {}
        if exeptions is None:
            exeptions = {}
        return database.get_collection(collection).find_one(query, exeptions)

    # generic function to get many/all data from a collection
    @classmethod
    def findall(cls, query=None, collection="", exeptions=None):
        if query is None:
            query = {}
        if exeptions is None:
            exeptions = {}
        return database.get_collection(collection).find(query, exeptions).to_list(None)

    # generic function to create data
    @classmethod
    def create(cls, newdata=None, collection=""):
        if newdata is None:
            newdata = {}
        newdata["_id"] = str(ObjectId())
        return database.get_collection(collection).insert_one(newdata)

    # generic function to create data
    @classmethod
    def createmany(cls, newdata=None, collection=""):
        if newdata is None:
            newdata = []
        return database.get_collection(collection).insert_many(newdata)

    # generic function to update data
    @classmethod
    def update(cls, item_id, newdata=None, collection=""):
        if newdata is None:
            newdata = {}
        newdata["updated_at"] = str(datetime.now(timezone.utc))
        return database.get_collection(collection).update_one(
            {"_id": item_id},
            {"$set": newdata},
        )

    # generic function to delete data
    @classmethod
    def delete(cls, item_id, collection=""):
        return database.get_collection(collection).delete_one({"_id": item_id})


model = Model()
