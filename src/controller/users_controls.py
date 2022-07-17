from fastapi.encoders import jsonable_encoder
from src.utils.functions import model
from ..schema.users_model import user
from ..utils.auth import hash
    
async def register(User):
    try:
        User=user()
        mail= User.email
        check= await model.findone(mail,"questions")
        if check is not None:
            return {"error: ": "user already exists"}
        User.password = hash(User.password)
        foo= await model.create(jasonable_encoder(User), "questions")

        return (f"user with email {foo.email} created successfully")

    except Exception as error:
        return error