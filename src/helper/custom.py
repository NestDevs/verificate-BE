from __future__ import annotations

from bson.objectid import ObjectId


class PyObjectId(ObjectId):
    """mongodb objectid validator"""

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        if not ObjectId.is_valid(value):
            raise ValueError("Invalid objectid")
        return str(ObjectId(value))

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")
