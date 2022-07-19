from fastapi import APIRouter
from src.controller.certificate_controls import get_certificates, create_certificate

router = APIRouter()
#create certificates
@router.post("/")
async def _create_certificate(user_id):
    return await create_certificate(user_id)

#get all for a usercertificates
@router.get("/{user_id}")
async def _get_certificates(user_id):
    return await get_certificates(user_id)
