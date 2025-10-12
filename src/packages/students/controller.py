from typing import List

from fastapi import APIRouter

from src.packages.students.model import StudentData
from src.packages.utilities.api_response_model import ApiResponseModel

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


@student_router.get("/dummy-student")
def dummy_student():
    return "hello"


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
        exists, i = check_if_roll_no_exists(rid)
        if not exists:
            return ApiResponseModel(message="data not found", data=None, status=False)
        else:
            deleted_student = students.pop(i)
            ApiResponseModel(message="data deleted", data=[deleted_student], status=True)
    except Exception as error:
        return ApiResponseModel(message=str(error), data=None, status=False)

