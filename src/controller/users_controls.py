# import json
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder

from src.helper.response import ResponseModel
from src.schema.users_model import User_login, Verifier
from src.utils.auth import create_access_token, create_access_token2, hashed, verify_password
from src.utils.functions import model


async def register(user):
    """
    Register a user to collection.

    returns
    -------
    User email on success.
    """
    try:
        check = await model.findone(
            {"email": user.email},
            "users",
        )
        if check is not None:
            return {"error: ": "user already exists"}
        user.password = hashed(user.password)
        create_user = await model.create(
            jsonable_encoder(user),
            "users",
        )
        print(create_user)
        return {
            "user": create_user.inserted_id,
            "success": True,
            "message": "User created successfully",
            "status": 200,
        }
    except Exception as error:
        print(error)
        raise HTTPException(
            status_code=500,
            detail="server error",
        ) from error


async def login(load: User_login):
    """
    Login a test taker.

    returns
    -------
    access token and user mail.
    """
    try:
        user_exists = await model.findone(
            {"email": load.email},
            "users",
        )
        print(user_exists)
        if not user_exists:
            return {
                "success": False,
                "message": "email or password does not match",
                "status": 404,
            }

        password_verified = verify_password(
            load.password,
            user_exists["password"],
        )
        print(password_verified)
        if not password_verified:
            return {
                "success": False,
                "message": "email or password does not match",
                "status": 404,
            }
        access_token = create_access_token(
            data={
                "email": user_exists["email"],
            },
        )
        return (
            f"{load.email} logged in successfully",
            {
                "access_token": f"Bearer {access_token}",
                "email": user_exists["email"],
                "status": 200,
            },
        )
    except Exception as error:
        print(error)
        raise HTTPException(
            status_code=500,
            detail="server error",
        ) from error


async def verifier_login(verifier: Verifier):
    """
    Login for an admin to upload questions
    """
    try:
        admin = await model.findone(
            {"email": verifier.email},
            "verifiers",
        )
        if not admin:
            return (
                {
                    "success": False,
                    "message": "Not an Admin",
                    "status": 404,
                },
            )
        password_verified = verify_password(
            verifier.password,
            admin["password"],
        )
        if not password_verified:
            return (
                {
                    "success": False,
                    "message": "Not an Admin",
                    "status": 404,
                },
            )
        access_token = create_access_token2(
            data={"email": admin["email"]},
        )
        return (
            f"{verifier.email} logged in successfully",
            {
                "access_token": f"Bearer {access_token}",
                "email": admin["email"],
                "status": 200,
            },
        )
    except Exception as error:
        print(error)
        raise HTTPException(
            status_code=500,
            detail="server error",
        ) from error


async def set_result(category_name, test_results):
    """
    if passed set the level to true.
    """
    result = {
        f"{category_name}": f"{test_results}",
    }
    await model.create(result, "user_result")
    return ResponseModel.success(message="success")
