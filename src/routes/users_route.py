from fastapi import APIRouter
from src.controller.users_controls import (register,)
from ..schema.users_model import user,verifier

router = APIRouter()


@router.post("/register",tags=["users"])
async def sign_up(new_user:user):
    return await register(new_user)