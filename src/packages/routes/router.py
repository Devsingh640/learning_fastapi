from fastapi import FastAPI
from src.packages.students.controller import student_router
from src.packages.subjects.controller import subject_router

def init_routes(app: FastAPI):
    app.include_router(student_router, prefix="/students")
    app.include_router(subject_router, prefix="/subjects")


