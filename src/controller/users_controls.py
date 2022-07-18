import json

from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder

from src.schema.users_model import User, User_login
from src.utils.auth import create_access_token, hashed, verify_password
from src.utils.functions import model


async def register(user):
    """
    Register a user to collection.

    returns
    -------
    User email on success.
    """
    try:
        user = User().dict()
        check = await model.findone({"email": user["email"]}, "users_collection")
        if check is not None:
            return {"error: ": "user already exists"}
        user["password"] = hashed(user["password"])
        create_user = await model.create(jsonable_encoder(user), "users_collection")

        return (
            json.dumps(
                {
                    "user": user,
                    "success": True,
                    "message": "User created successfully",
                    "status": 200,
                },
            ),
            f"user {create_user.email} created succesfully",
        )

    except Exception:
        # return f"failed with error: {error}"
        raise HTTPException(status_code=500, detail="server error") from HTTPException(status_code=500)


async def login(load: User_login):
    """
    Login a test taker.

    returns
    -------
    access token and user mail.
    """
    try:
        user_exists = await model.findone({"email": load.email}, "users_collection")
        if not user_exists:
            return json.dumps(
                {
                    "success": False,
                    "message": "email or password does not match",
                    "status": 404,
                },
            )
        password_verified = verify_password(load.password, user_exists["pasword"])
        if not password_verified:
            return json.dumps(
                {
                    "success": False,
                    "message": "email or password does not match",
                    "status": 404,
                },
            )
        access_token = create_access_token(data={"email": user_exists["email"]})

        return (
            f"{load.email} logged in successfully",
            {
                "access_token": f"Bearer {access_token}",
                "email": user_exists["email"],
                "status": 200,
            },
        )
    except Exception:
        # return f"failed with error: {error}"
        raise HTTPException(status_code=500, detail="server error") from HTTPException(status_code=500)
