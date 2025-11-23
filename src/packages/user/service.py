
from starlette.responses import JSONResponse
import jwt
from src.packages.user.dal import UserDal
from src.packages.user.model import User, ReadUserData
from fastapi.encoders import jsonable_encoder
from fastapi import Request
from datetime import timedelta, datetime, timezone


class UserService:
    def __init__(self, user_dal: UserDal):
        self.user_dal = user_dal

    def create2(self, new_user):
        try:

            my_user = User.model_validate(new_user)
            my_user.get_hash_password()

            response = self.user_dal.add2(my_user)

            if response:
                response_data =  [ReadUserData(**inserted_user.model_dump()) for inserted_user in response]

                return JSONResponse({
                    "message" : "user created successfully",
                    "data": jsonable_encoder(response_data),
                    "status" : True
                },
                status_code=200)

            else:
                return JSONResponse({
                    "message" : "user not created successfully",
                    "data": None,
                    "status": False
                },
                status_code=200)
        except Exception as error:
            print("Unexpected Error : ", str(error))

    def create(self, new_users):
        try:
            # new_user_data_to_save =  [User.model_validate(user) for user in new_users]

            new_user_data_to_save = []
            for user in new_users:
                my_user = User.model_validate(user)
                my_user.get_hash_password()

                new_user_data_to_save.append(my_user)

            response = self.user_dal.add(new_user_data_to_save)

            if response:
                response_data =  [ReadUserData(**inserted_user.model_dump()) for inserted_user in response]

                # response_data = []
                # for inserted_user in response:
                #     dict_data = inserted_user.model_dump()
                #     response_data.append(ReadUserData(**dict_data))


                return JSONResponse({
                    "message" : "user created successfully",
                    "data": jsonable_encoder(response_data),
                    "status" : True
                },
                status_code=200)

            else:
                return JSONResponse({
                    "message" : "user not created successfully",
                    "data": None,
                    "status": False
                },
                status_code=200)
        except Exception as error:
            print("Unexpected Error : ", str(error))


    def get_all(self, request_model: Request, page:int, limit:int):
        try:
            data, total_records= self.user_dal.get_all(request_model, page, limit)

            if data:
                # data = [User, User, User, User, User, User]
                response_data = [ReadUserData.model_dump(el) for el in data]
                # response_data = [{}, {}, {}, {}, {}, {}]
                return JSONResponse({
                    "message": "data found",
                    "data": jsonable_encoder(response_data),
                    "total_records":total_records,
                    "total_pages": total_records,
                    "status": True
                },
                    status_code=200)
            else:
                return JSONResponse({
                    "message": "no data found",
                    "data": [],
                    "total_records": total_records,
                    "total_pages": total_records,
                    "status": True
                },
                    status_code=200)
        except Exception as error:
            print("Unexpected Error : ", str(error))


    def get_by_id(self, r_id: int):
        try:
            data= self.user_dal.get_by_id(r_id)
            if not data:
                return JSONResponse({
                    "message": "no record found",
                    "data": None,
                    "status": False
                },
                    status_code=200)
            else:
                response_data = ReadUserData.model_dump(data)
                return JSONResponse({
                    "message": "record found",
                    "data": jsonable_encoder(response_data),
                    "status": True
                },
                    status_code=200)
        except Exception as error:
            print("Unexpected Error : ", str(error))

    def update_by_id(self, r_id: int, body):
        try:
            status, data = self.user_dal.update_by_id(r_id, body)
            if not status:
                return JSONResponse({
                    "message": "no record found",
                    "data": None,
                    "status": False
                },
                    status_code=200)
            else:
                response_data = ReadUserData.model_dump(data)
                return JSONResponse({
                    "message": "record deleted",
                    "data": jsonable_encoder(response_data),
                    "status": True
                },
                    status_code=200)
        except Exception as error:
            print("Unexpected Error : ", str(error))

    def delete_by_id(self, r_id: int):
        try:
            status, data= self.user_dal.delete_by_id(r_id)
            if not status:
                return JSONResponse({
                    "message": "no record found",
                    "data": None,
                    "status": False
                },
                    status_code=200)
            else:
                response_data = ReadUserData.model_dump(data)
                return JSONResponse({
                    "message": "record deleted",
                    "data": jsonable_encoder(response_data),
                    "status": True
                },
                    status_code=200)
        except Exception as error:
            print("Unexpected Error : ", str(error))


    def create_jwt_access_token(self, data: dict, expiration_time:timedelta, secret_key:str):
        data_copy = {}
        algorithm = "HS256"

        if expiration_time:
            expire = datetime.now(timezone.utc) + expiration_time
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=10)

        data_copy.update({"exp": expire})

        return jwt.encode(data_copy, secret_key, algorithm=algorithm)



    def login(self, email="", password=""):
        jwt_token_expiration_time_in_hours = timedelta(hours=12)
        jwt_token_expiration_time_in_minutes = timedelta(minutes=5)
        jwt_token_expiration_time_in_seconds = timedelta(seconds=5)

        jwt_secret_key = "aserfghujkuytrertyuikmnbvfdftyuikmnbvcxsrtyujbvcxsedrtyuikmnbvcdfghj"

        user = self.user_dal.login_user(email, password)

        if not user:
            return JSONResponse({
                "message": "invalid creds",
                "data": None,
                "status": False
            },
                status_code=401)
        else:
            response_data = user.model_dump()

            # token will be generated here
            jwt_token = self.create_jwt_access_token(response_data, jwt_token_expiration_time_in_seconds, jwt_secret_key)

            print(jwt_token)
            print(type(jwt_token))

            return JSONResponse({
                "message": "login success",
                "data": jsonable_encoder(response_data),
                "token": jwt_token,
                "status": True
            },
                status_code=200)









