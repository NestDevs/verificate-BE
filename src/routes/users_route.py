from fastapi import APIRouter, Depends

from src.controller.users_controls import (
    login, 
    register, 
    set_result, 
    verifier_login
    )
from src.schema.users_model import (
    Test_results, 
    User, 
    User_login, 
    Verifier
    )
from src.utils.auth import (
    verify_user, 
    verify_user2
    )

router = APIRouter()


# Test taker Register
@router.post("/register", tags=["users"])
async def sign_up(new_user: User):
    return await register(new_user)


# Test taker login
@router.post("/login", tags=["users"])
async def sign_in(details: User_login):
    return await login(details)


# Get test taker profile
@router.get("/profile", tags=["users"])
async def user_profile(current_user=Depends(verify_user)):
    return current_user


# category
@router.post("/profile/{email}/{category}")
async def test_category(email, category, test_results: Test_results):
    test_results.email = email
    return set_result(category, test_results)


# admin login
@router.post("/admin/login", tags=["users"])
async def admin_login(details: Verifier):
    return await verifier_login(details)


# Rout for page where admin uploads questions
@router.get("/admin", tags=["users"])
async def admin_profile(current_user=Depends(verify_user2)):
    return current_user
