from typing import List
from fastapi import APIRouter, Depends, Query, Request
from src.packages.todo.dal import TodoDal
from src.packages.todo.service import TodoService
from src.packages.todo.model import AddTodoData, UpdateTodoData
from src.packages.utilities.pos_db import get_session

todo_router = APIRouter()


def get_todo_service(session=Depends(get_session)) -> TodoService:
    return TodoService(TodoDal(session))


# CREATE
@todo_router.post("/t1")
def new_create_todo(todo_data: AddTodoData | List[AddTodoData],
                todo_service = Depends(get_todo_service)):
    if isinstance(todo_data, AddTodoData):
        todo_data = [todo_data]

    return todo_service.create(todo_data)


# GET ALL
@todo_router.get("/t1")
def new_get_todos(request_model: Request,
                  page: int = Query(1),
                  limit: int = Query(10),
                   todo_service = Depends(get_todo_service)):

    return todo_service.get_all(request_model, page, limit)


# GET BY ID
@todo_router.get("/t1/{todo_id}")
def new_get_todo_by_id(
    todo_id: str,
    todo_service = Depends(get_todo_service)):

    return todo_service.get_by_id(todo_id)


# UPDATE
@todo_router.put("/t1/{todo_id}")
def new_update_todo_by_id(
    todo_data: UpdateTodoData,
    todo_id: str,
    todo_service = Depends(get_todo_service)):

    return todo_service.update_by_id(todo_id, body=todo_data)


# DELETE
@todo_router.delete("/t1/{todo_id}")
def new_delete_todo_by_id(
    todo_id: str,
    todo_service = Depends(get_todo_service)):

    return todo_service.delete_by_id(todo_id)
