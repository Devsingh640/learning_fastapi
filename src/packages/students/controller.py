from typing import List

from fastapi import APIRouter, Depends, Query, Request

from src.packages.students.dal import StudentDal
from src.packages.students.model import AddStudentData, UpdateStudentData
from src.packages.students.service import StudentService
from src.packages.utilities.pos_db import get_session

student_router = APIRouter()

def get_student_service(session = Depends(get_session)) -> StudentService :
    return StudentService(StudentDal(session))


@student_router.post("/")
def new_create_student(student_data: AddStudentData | List[AddStudentData],
                   student_service = Depends(get_student_service)):

        if isinstance(student_data, AddStudentData):
            student_data = [student_data]

        return student_service.create(student_data)


@student_router.get("/")
def new_get_students(request_model: Request,
                    page: int = Query(default=1),
                    limit: int = Query(default=10),
                    student_service = Depends(get_student_service)
                     ):
    return student_service.get_all(request_model, page, limit)

@student_router.get("/{r_id}")
def new_get_student_by_id(r_id : int,
                          student_service = Depends(get_student_service)):
    return student_service.get_by_id(r_id)

@student_router.put("/{r_id}")
def new_update_student_by_id(student_data:UpdateStudentData,
                             r_id : int,
                          student_service = Depends(get_student_service)):
    return student_service.update_by_id(r_id, body=student_data)

@student_router.delete("/{r_id}")
def new_delete_student_by_id(r_id : int,
                          student_service = Depends(get_student_service)):
    return student_service.delete_by_id(r_id)