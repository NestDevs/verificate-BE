# controller for changing roles(assigning verifiers) and admins 

from src.utils.functions import Model

# assign verifier
async def assign_verifier(user,current_user):
    # check if the user exist
    try:
        user_id = user["user_id"]
        # current user is admin
        is_admin = current_user["is_admin"]
        if not is_admin:
            return {
                "success":False,
                "message":"Forbidden access",
                "status":403
            }
        user_exist = await Model.findone({"_id":user_id},"users_collection")
        if user_exist is None:
            return {
                "success":False,
                "message":"User does not exist",
                "status":404
            }
        updated_user = await Model.update(user_id,{"is_verifier":True},"users_collection")
        print(updated_user)
        return {
            "success":True,
            "message":f"User {user_id} is now a verifier",
            "status":201
        }
    except Exception as error:
        return {
            "success":False,
            "message":f"Error occured during assigning user a verififer : {error}",
            "status":500
        }
