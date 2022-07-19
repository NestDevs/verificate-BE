from datetime import datetime, timedelta, timezone

from fastapi import Depends, HTTPException, security, status
from jose import JWTError, jwt
from passlib.context import CryptContext

from src.config.settings import settings
from src.utils.functions import model

oauth2_scheme = security.OAuth2PasswordBearer(tokenUrl="login")
hasher = CryptContext(schemes=["bcrypt"], deprecated=["auto"])


def hashed(password: str):
    hasher.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return hasher.verify(plain_password, hashed_password)


def create_access_token(data: dict):
    to_encode = data.copy()
    expires_at = datetime.now(timezone.utc) + timedelta(settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode["exp"] = expires_at

    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def create_access_token2(data: dict):
    to_encode = data.copy()
    expires_at = datetime.now(timezone.utc) + timedelta(settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode["exp"] = expires_at

    return jwt.encode(to_encode, settings.SECRET_KEY2, algorithm=settings.ALGORITHM)


async def verify_access_token(token: str, exeption_error):
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )

        user_mail: str = payload.get("email")

        # verify if the user exists in the database
        user_exist = await model.findOne({"email": user_mail}, "users_collection", {"password": 0})

        if user_exist is None:
            raise exeption_error
        return user_exist
    except JWTError as e:
        raise exeption_error from e


async def verify_access_token2(token: str, exeption_error):
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY2,
            algorithms=[settings.ALGORITHM],
        )

        user_mail: str = payload.get("email")

        # verify if the user exists in the database
        user_exist = await model.findOne({"email": user_mail}, "users_collection", {"password": 0})

        if user_exist is None:
            raise exeption_error
        return user_exist
    except JWTError as e:
        raise exeption_error from e


async def verify_user(token: str = Depends(oauth2_scheme)):
    exeption_error = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        headers={"WWW-Authenticate": "Bearer"},
    )
    return await verify_access_token(token, exeption_error)


async def verify_user2(token: str = Depends(oauth2_scheme)):
    exeption_error = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        headers={"WWW-Authenticate": "Bearer"},
    )
    return await verify_access_token2(token, exeption_error)
