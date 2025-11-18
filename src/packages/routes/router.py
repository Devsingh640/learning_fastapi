from fastapi import FastAPI
from src.packages.students.controller import student_router
from src.packages.subjects.controller import subject_router
from src.packages.user.controller import user_router
# from src.packages.todo.controller import todo_router

def init_routes(app: FastAPI):
    app.include_router(student_router, prefix="/students", tags=["Students"])
    app.include_router(subject_router, prefix="/subjects", tags=["Subjects"])
    app.include_router(user_router, prefix="/user", tags=["User"])
    # app.include_router(todo_router, prefix="/todo", tags=["todo"])

