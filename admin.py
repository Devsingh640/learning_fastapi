from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from starlette_admin.contrib.sqlmodel import Admin, ModelView
from src.packages.utilities.pos_db import engine
from src.packages.students.model import Student
from src.packages.todo.model import Todo
from src.packages.user.model import User


admin = Admin(engine,
              title="Todo Application")


class StudentView(ModelView):
    pass

class TodoView(ModelView):
    pass

class UserView(ModelView):
    pass

def init_admin(app: FastAPI):
    app.mount("/static", StaticFiles(directory="static"), name="static")

    admin.add_view(StudentView(Student, label="Students"))
    admin.add_view(TodoView(Todo, label="Todo"))
    admin.add_view(UserView(User, label="User"))

    admin.mount_to(app)



