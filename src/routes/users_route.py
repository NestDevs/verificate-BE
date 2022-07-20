from fastapi import APIRouter, Depends

from src.controller.users_controls import (
    login,
    register,
    set_result,
    verifier_login,
)
from src.schema.users_model import (
    TestResult,
    User,
    UserLogin,
    Verifier,
)
from src.utils.auth import (
    verify_user,
    verify_user2,
)

router = APIRouter()


# Test taker Register
@router.post("/register", tags=["users"])
async def sign_up(new_user: User):
    """
        {
      "user": {
        "first_name": "stringstri",
        "last_name": "stringstri",
        "password": "$2b$12$oztJC2l.LI211RghgA7y1O7kP/Zpc.K1m2kXRx2v8hZXFS0Ai3HXu",
        "email": "ussdeer@example.com",
        "linked_in": "https://atila.ca",
        "results": {
          "java": [
            {
              "level": "BEGINNER",
              "test_result": "FAILED",
              "score": 0
            }
          ]
        },
        "created_at": "2022-07-19 17:40:53.057852+00:00"
      },
      "user_id": "62d6ecfab917caa7fe8aa528",
      "success": true,
      "message": "User created successfully",
      "status": 200
    }
    """
    return await register(new_user)


# Test taker login
@router.post("/login", tags=["users"])
async def sign_in(details: UserLogin):
    return await login(details)


# Get test taker profile
@router.get("/profile", tags=["users"])
async def user_profile(current_user=Depends(verify_user)):
    return current_user


# category
@router.post("/profile/{email}/{category}")
async def test_category(email, category, test_results: TestResult):
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
