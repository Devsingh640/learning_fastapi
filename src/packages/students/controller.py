from typing import List

from fastapi import APIRouter, Depends, Query, Request

from src.packages.students.dal import StudentDal
from src.packages.students.model import StudentData, AddStudentData, UpdateStudentData
from src.packages.students.service import StudentService
from src.packages.utilities.api_response_model import ApiResponseModel
from src.packages.utilities.pos_db import get_session

student_router = APIRouter()

students: List[StudentData] = []


# helper
def check_if_roll_no_exists(roll_no: int):
    for i, student in enumerate(students):
        if student.student_roll == roll_no:
            return True, i
        else:
            continue
    return False, None

def get_student_service(session = Depends(get_session)) -> StudentService :
    return StudentService(StudentDal(session))



@student_router.post("/s1")
def new_create_student(student_data: AddStudentData | List[AddStudentData],
                   student_service = Depends(get_student_service)):

        if isinstance(student_data, AddStudentData):
            student_data = [student_data]

        return student_service.create(student_data)


@student_router.get("/s1")
def new_get_students(request_model: Request,
                    page: int = Query(default=1),
                    limit: int = Query(default=10),
                    student_service = Depends(get_student_service)
                     ):
    return student_service.get_all(request_model, page, limit)

@student_router.get("/s1/{r_id}")
def new_get_student_by_id(r_id : int,
                          student_service = Depends(get_student_service)):
    return student_service.get_by_id(r_id)

@student_router.put("/s1/{r_id}")
def new_update_student_by_id(student_data:UpdateStudentData,
                             r_id : int,
                          student_service = Depends(get_student_service)):
    return student_service.update_by_id(r_id, body=student_data)

@student_router.delete("/s1/{r_id}")
def new_delete_student_by_id(r_id : int,
                          student_service = Depends(get_student_service)):
    return student_service.delete_by_id(r_id)



@student_router.post("/", response_model=ApiResponseModel[List[StudentData]])
def create_student(student_data: StudentData):
    try:
        exists, i = check_if_roll_no_exists(student_data.student_roll)
        if not exists:
            students.append(student_data)
            return ApiResponseModel(message="created successfully", data=[student_data], status=True)
        else:
            return ApiResponseModel(message="record already exists", data=None, status=False)
    except Exception as error:
        return ApiResponseModel(message=str(error), data=None, status=False)


@student_router.get("/", response_model=ApiResponseModel[List[StudentData]])
def fetch_students():
    try:
        if len(students) <= 0:
            return ApiResponseModel(message="data not found", data=[], status=False)
        else:
            return ApiResponseModel(message="data found", data=students, status=True)
    except Exception as error:
        return ApiResponseModel(message=str(error), data=None, status=False)


@student_router.get("/{rid}", response_model=ApiResponseModel[List[StudentData]])
def fetch_student_by_roll_no(rid: int):
    try:
        exists, i = check_if_roll_no_exists(rid)
        if not exists:
            return ApiResponseModel(message="data not found", data=None, status=False)
        else:
            ApiResponseModel(message="data found", data=[students[i]], status=True)
    except Exception as error:
        return ApiResponseModel(message=str(error), data=None, status=False)


@student_router.put("/{rid}", response_model=ApiResponseModel[List[StudentData]])
def update_student(rid:int, student_data: StudentData):
    try:
        exists, i = check_if_roll_no_exists(rid)
        if not exists:
            return ApiResponseModel(message="data not found", data=None, status=False)
        else:
            if rid == student_data.student_roll:
                students[i] = student_data
                ApiResponseModel(message="data updated", data=[students[i]], status=True)
            else:
                return ApiResponseModel(message="record already exists", data=None, status=False)

    except Exception as error:
        return ApiResponseModel(message=str(error), data=None, status=False)


@student_router.delete("/{rid}", response_model=ApiResponseModel[List[StudentData]])
def delete_student(rid:int):
    try:
        # cal start time
        exists, i = check_if_roll_no_exists(rid)
        if not exists:
            return ApiResponseModel(message="data not found", data=None, status=False)
        else:
            deleted_student = students.pop(i)
            ApiResponseModel(message="data deleted", data=[deleted_student], status=True)
        # end time cal

        # final time = end time - start time
        print("")
    except Exception as error:
        return ApiResponseModel(message=str(error), data=None, status=False)

