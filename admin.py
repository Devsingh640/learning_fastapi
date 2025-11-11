from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from starlette_admin.contrib.sqlmodel import Admin, ModelView
from src.packages.utilities.pos_db import engine
from src.packages.students.model import Student



admin = Admin(engine,
              title="Todo Application")


class StudentView(ModelView):
    pass

def init_admin(app: FastAPI):
    app.mount("/static", StaticFiles(directory="static"), name="static")

    admin.add_view(StudentView(Student, label="Students"))

    admin.mount_to(app)



