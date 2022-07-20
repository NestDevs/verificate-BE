from fastapi import APIRouter, Depends
from src.controller.certificate_controls import get_certificates, create_certificate
from src.utils.auth import verify_user
from src.schema.users_model import User

router = APIRouter()
#create certificates
@router.post("/")
async def _create_certificate(certificate_data:dict,current_user:User= Depends(verify_user)):
    return await create_certificate(certificate_data,current_user)

#get all for a usercertificates
@router.get("/")
async def _get_certificates(current_user:User= Depends(verify_user)):
    return await get_certificates(current_user)
