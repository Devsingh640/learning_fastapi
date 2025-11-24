from typing import List, Annotated

from fastapi import APIRouter, Depends, Query, Request, Form

from src.packages.user.dal import UserDal
from src.packages.user.model import AddUserData, UpdateUserData
from src.packages.user.service import UserService
from src.packages.utilities.pos_db import get_session

user_router = APIRouter()

def get_user_service(session = Depends(get_session)) -> UserService :
    return UserService(UserDal(session))


#CRUD operations

# signup endpoint
@user_router.post("/signup")
def signup_user(user_id: Annotated[str, Form()],
                user_name: Annotated[str, Form()],
                email: Annotated[str, Form()],
                status: Annotated[bool, Form()],
                description: Annotated[str, Form()],
                password: Annotated[str, Form()],
                user_service = Depends(get_user_service)):


        user_data =  {
                        "user_id":user_id,
                        "user_name":user_name,
                        "email":email,
                        "status":status,
                        "description":description,
                        "password":password,
                      }

        return user_service.create2(user_data)

# login endpoint
@user_router.post("/login")
def user_login(email: Annotated[str, Form()],
               password: Annotated[str, Form()],
               user_service = Depends(get_user_service)):
    return user_service.login(email=email, password=password)

@user_router.post("/")
def new_create_user(user_data: AddUserData | List[AddUserData],
                   user_service = Depends(get_user_service)):

        if isinstance(user_data, AddUserData):
            user_data = [user_data]

        return user_service.create(user_data)

# Read user instance
@user_router.get("/")
def new_get_users(request_model: Request,
                  page: int = Query(default=1),
                  limit: int = Query(default=10),
                  user_service = Depends(get_user_service)
                  ):
    return user_service.get_all(request_model, page, limit)

# Read user instance by user ID
@user_router.get("/id/{user_id}")
def new_get_user_by_id(user_id: int, user_service = Depends(get_user_service)):
    return user_service.get_user_by_id(user_id)

# Update user instance by user id
@user_router.put("/id/{user_id}")
def new_update_user_by_id(user_data: UpdateUserData, user_id : int, user_service = Depends(get_user_service)):
    return user_service.update_by_id(user_id, body = user_data)

# Delete user instance by user id
@user_router.delete("/id/{user_id}")
def new_delete_user_by_id(user_id : int, user_service = Depends(get_user_service)):
    return user_service.delete_by_id(user_id)


# Read user instance by user_name
@user_router.get("/name/{user_name}")
def new_get_user_by_name(user_name: str, user_service = Depends(get_user_service)):
    return user_service.get_user_by_name(user_name)

# Update user instance by user name
@user_router.put("/name/{user_name}")
def new_update_user_by_name(user_data: UpdateUserData, user_name : str, user_service = Depends(get_user_service)):
    return user_service.update_by_name(user_name, body = user_data)

# Delete user instance by user name
@user_router.delete("/name/{user_name}")
def new_delete_user_by_name(user_name : str, user_service = Depends(get_user_service)):
    return user_service.delete_by_name(user_name)


# Read user instance by user_email
@user_router.get("/email/{email}")
def new_get_user_by_email(email: str, user_service = Depends(get_user_service)):
    return user_service.get_user_by_email(email)

# Update user instance by user email
@user_router.put("/email/{email}")
def new_update_user_by_email(user_data: UpdateUserData, email : str, user_service = Depends(get_user_service)):
    return user_service.update_by_email(email, body = user_data)

# Delete user instance by user email
@user_router.delete("/email/{email}")
def new_delete_user_by_email(email : str, user_service = Depends(get_user_service)):
    return user_service.delete_by_email(email)


