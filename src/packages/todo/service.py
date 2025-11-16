from starlette.responses import JSONResponse

from fastapi.encoders import jsonable_encoder
from fastapi import Request

from src.packages.todo.dal import TodoDal
from src.packages.todo.model import Todo


class TodoService:
    def __init__(self, todo_dal: TodoDal):
        self.todo_dal = todo_dal

    def create(self, new_todo, todo: Todo):
        try:
            new_todo_data_to_save =  [Todo.model_validate(todo) for todo in new_todo]


            response = self.todo_dal.add(new_todo_data_to_save)

            if response:
                response_data =  [Todo(**inserted_todo.model_dump()) for inserted_todo in response]

                return JSONResponse({
                    "message" : "Todo created successfully",
                    "data": jsonable_encoder(response_data),
                    "status" : True
                },
                status_code=200)

            else:
                return JSONResponse({
                    "message" : "Todo not created successfully",
                    "data": None,
                    "status": False
                },
                status_code=200)
        except Exception as error:
            print("Unexpected Error : ", str(error))


    def get_all(self, request_model: Request, page:int, limit:int):
        try:
            data, total_records= self.todo_dal.get_all(request_model, page, limit)

            if data:
                response_data = [Todo.model_dump(el) for el in data]
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
            data= self.todo_dal.get_by_id(r_id)
            if not data:
                return JSONResponse({
                    "message": "no record found",
                    "data": None,
                    "status": False
                },
                    status_code=200)
            else:
                response_data = Todo.model_dump(data)
                return JSONResponse({
                    "message": "record found",
                    "data": jsonable_encoder(response_data),
                    "status": True
                },
                    status_code=200)
        except Exception as error:
            print("Unexpected Error : ", str(error))

    def update_by_id(self, todo_id: int, body):
        try:
            status, data = self.todo_dal.update_by_id(todo_id, body)
            if not status:
                return JSONResponse({
                    "message": "no record found",
                    "data": None,
                    "status": False
                },
                    status_code=200)
            else:
                response_data = Todo.model_dump(data)
                return JSONResponse({
                    "message": "record deleted",
                    "data": jsonable_encoder(response_data),
                    "status": True
                },
                    status_code=200)
        except Exception as error:
            print("Unexpected Error : ", str(error))

    def delete_by_id(self, todo_id: int):
        try:
            status, data= self.todo_dal.delete_by_id(todo_id)
            if not status:
                return JSONResponse({
                    "message": "no record found",
                    "data": None,
                    "status": False
                },
                    status_code=200)
            else:
                response_data = Todo.model_dump(data)
                return JSONResponse({
                    "message": "record deleted",
                    "data": jsonable_encoder(response_data),
                    "status": True
                },
                    status_code=200)
        except Exception as error:
            print("Unexpected Error : ", str(error))