from typing import List

from fastapi import APIRouter, Depends, Query, Request

from src.packages.user.dal import UserDal
from src.packages.user.model import UserData, AddUserData, UpdateUserData
from src.packages.user.service import UserService
from src.packages.utilities.api_response_model import ApiResponseModel
from src.packages.utilities.pos_db import get_session

user_router = APIRouter()

users: List[UserData] = []

# Since we have 3 unique values in the data set by which we can applied CRUD operation. Which are user_id, user_name, email

# check by user_id
def check_if_user_id_exists(user_id: int):
    for i, user in enumerate(users):
        if user.user_id == user_id:
            return True, i
        else:
            continue
    return False, None

#check by user_name
def check_if_user_name_exists(user_name: str):
    for i, user in enumerate(users):
        if user.user_name == user_name:
            return True, i
        else:
            continue
    return False, None

#check by user_email
def check_if_user_email_exists(email: str):
    for i, user in enumerate(users):
        if user.email == email:
            return True, i
        else:
            continue
    return False, None

def get_user_service(session = Depends(get_session)) -> UserService :
    return UserService(UserDal(session))


#CRUD operations
#C-create user instance
@user_router.post("/u1")
def new_create_user(user_data: AddUserData | List[AddUserData],
                   user_service = Depends(get_user_service)):

        if isinstance(user_data, AddUserData):
            user_data = [user_data]

        return user_service.create(user_data)

# Read user instance
@user_router.get("/u1")
def new_get_users(request_model: Request,
                  page: int = Query(default=1),
                  limit: int = Query(default=10),
                  user_service = Depends(get_user_service)
                  ):
    return user_service.get_all(request_model, page, limit)

# Read user instance by user ID
@user_router.get("/u1/id/{user_id}")
def new_get_user_by_id(user_id: int, user_service = Depends(get_user_service)):
    return user_service.get_user_by_id(user_id)

# Update user instance by user id
@user_router.put("/u1/id/{user_id}")
def new_update_user_by_id(user_data: UpdateUserData, user_id : int, user_service = Depends(get_user_service)):
    return user_service.update_by_id(user_id, body = user_data)

# Delete user instance by user id
@user_router.delete("/u1/id/{user_id}")
def new_delete_user_by_id(user_id : int, user_service = Depends(get_user_service)):
    return user_service.delete_by_id(user_id)



# Read user instance by user_name
@user_router.get("/u1/name/{user_name}")
def new_get_user_by_name(user_name: str, user_service = Depends(get_user_service)):
    return user_service.get_user_by_name(user_name)

# Update user instance by user name
@user_router.put("/u1/name/{user_name}")
def new_update_user_by_name(user_data: UpdateUserData, user_name : str, user_service = Depends(get_user_service)):
    return user_service.update_by_name(user_name, body = user_data)

# Delete user instance by user name
@user_router.delete("/u1/name/{user_name}")
def new_delete_user_by_name(user_name : str, user_service = Depends(get_user_service)):
    return user_service.delete_by_name(user_name)


# Read user instance by user_email
@user_router.get("/u1/email/{email}")
def new_get_user_by_email(email: str, user_service = Depends(get_user_service)):
    return user_service.get_user_by_email(email)

# Update user instance by user email
@user_router.put("/u1/email/{email}")
def new_update_user_by_email(user_data: UpdateUserData, email : str, user_service = Depends(get_user_service)):
    return user_service.update_by_email(email, body = user_data)

# Delete user instance by user email
@user_router.delete("/u1/email/{email}")
def new_delete_user_by_email(email : str, user_service = Depends(get_user_service)):
    return user_service.delete_by_email(email)



# CRUD operations on list of user

# create list of user
@user_router.post("/", response_model=ApiResponseModel[List[UserData]])
def create_user(user_data: UserData):
    try:
        exits, i = check_if_user_id_exists(user_data.user_id)
        if not exits:
            users.append(user_data)
            return ApiResponseModel(message = "User created successfully!", data = [user_data], status = True)
        else:
            return ApiResponseModel(message = "User already exists!", data = None, status = False)
    except Exception as error:
        return ApiResponseModel(message = str(error), data = None, status = False)


# Read list of user
@user_router.get("/", response_model=ApiResponseModel[List[UserData]])
def fetch_users():
    try:
        if len(users) <= 0:
            return ApiResponseModel(message = "No users found!", data = [], status = False)
        else:
            return ApiResponseModel(message = "Users found!", data = [users], status = True)

    except Exception as error:
        return ApiResponseModel(message = str(error), data = None, status = False)


# Read list of user by id
@user_router.get("/id/{user_id}", response_model=ApiResponseModel[List[UserData]])
def fetch_users_by_user_id(user_id : int):
    try:
        exits, i = check_if_user_id_exists(user_id)
        if not exits:
            return ApiResponseModel(message = "No users found!", data = None, status = False)
        else:
            return ApiResponseModel(message = "Users found!", data = [users[i]], status = True)
    except Exception as error:
        return ApiResponseModel(message = str(error), data = None, status = False)


# Update list of user by id
@user_router.put("/id/{user_id}", response_model=ApiResponseModel[List[UserData]])
def update_user(user_id : int, user_data: UserData):
    try:
        exits, i = check_if_user_id_exists(user_id)
        if not exits:
            return ApiResponseModel(message = "No users found!", data = None, status = False)
        else:
            if user_id == user_data.user_id:
                users[i] = user_data
                return ApiResponseModel(message = "Users data updated!", data = [users[i]], status = True)
            else:
                return ApiResponseModel(message = "User data already exits!", data = None, status = False)
    except Exception as error:
        return ApiResponseModel(message = str(error), data = None, status = False)


# Delete list of user by id
@user_router.delete("/id/{user_id}", response_model=ApiResponseModel[List[UserData]])
def delete_user(user_id : int):
    try:
        exits, i = check_if_user_id_exists(user_id)
        if not exits:
            return ApiResponseModel(message = "No users data found!", data = None, status = False)
        else:
            deleted_user = users.pop(i)
            return ApiResponseModel(message = "Users data deleted!", data = [deleted_user], status = True)

    except Exception as error:
        return ApiResponseModel(message = str(error), data = None, status = False)



# Assuming list of user_name multiple
# Read list of user by name
@user_router.get("/name/{user_name}", response_model=ApiResponseModel[List[UserData]])
def fetch_users_by_user_name(user_name : str):
    try:
        exits, i = check_if_user_name_exists(user_name)
        if not exits:
            return ApiResponseModel(message = "No users name found!", data = None, status = False)
        else:
            return ApiResponseModel(message = "Users name found!", data = [users[i]], status = True)
    except Exception as error:
        return ApiResponseModel(message = str(error), data = None, status = False)


# Update list of user by name
@user_router.put("/name/{user_name}", response_model=ApiResponseModel[List[UserData]])
def update_user_name(user_name: str, user_data: UserData):
    try:
        exits, i = check_if_user_name_exists(user_name)
        if not exits:
            return ApiResponseModel(message="No users found!", data=None, status=False)
        else:
            if user_name == user_data.user_name:
                users[i] = user_data
                return ApiResponseModel(message="Users data updated!", data=[users[i]], status=True)
            else:
                return ApiResponseModel(message="User data already exits!", data=None, status=False)
    except Exception as error:
        return ApiResponseModel(message=str(error), data=None, status=False)


# Delete list of user by name
@user_router.delete("/name/{user_name}", response_model=ApiResponseModel[List[UserData]])
def delete_user_name(user_name: str):
    try:
        exits, i = check_if_user_name_exists(user_name)
        if not exits:
            return ApiResponseModel(message="No users data found!", data=None, status=False)
        else:
            deleted_user = users.pop(i)
            return ApiResponseModel(message="Users data deleted!", data=[deleted_user], status=True)

    except Exception as error:
        return ApiResponseModel(message=str(error), data=None, status=False)


# Assuming list of user email multiple
# Read list of user by email
@user_router.get("/email/{email}", response_model=ApiResponseModel[List[UserData]])
def fetch_users_by_email(email : str):
    try:
        exits, i = check_if_user_email_exists(email)
        if not exits:
            return ApiResponseModel(message = "No users name found!", data = None, status = False)
        else:
            return ApiResponseModel(message = "Users name found!", data = [users[i]], status = True)
    except Exception as error:
        return ApiResponseModel(message = str(error), data = None, status = False)


# Update list of user by email
@user_router.put("/email/{email}", response_model=ApiResponseModel[List[UserData]])
def update_email(email: str, user_data: UserData):
    try:
        exits, i = check_if_user_email_exists(email)
        if not exits:
            return ApiResponseModel(message="No users found!", data=None, status=False)
        else:
            if email == user_data.email:
                users[i] = user_data
                return ApiResponseModel(message="Users data updated!", data=[users[i]], status=True)
            else:
                return ApiResponseModel(message="User data already exits!", data=None, status=False)
    except Exception as error:
        return ApiResponseModel(message=str(error), data=None, status=False)


# Delete list of user by email
@user_router.delete("/email/{email}", response_model=ApiResponseModel[List[UserData]])
def delete_email(email: str):
    try:
        exits, i = check_if_user_email_exists(email)
        if not exits:
            return ApiResponseModel(message="No users data found!", data=None, status=False)
        else:
            deleted_user = users.pop(i)
            return ApiResponseModel(message="Users data deleted!", data=[deleted_user], status=True)

    except Exception as error:
        return ApiResponseModel(message=str(error), data=None, status=False)


