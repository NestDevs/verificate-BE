from fastapi import APIRouter, Depends
from src.controller.auth_control import assign_verifier
from src.utils.auth import verify_user
from src.schema.users_model import User

router = APIRouter()
#assign verifier
@router.post("/verifier")
async def _assign_verifier(user:dict,current_user:User=Depends(verify_user)):
     return await assign_verifier(user,current_user)


