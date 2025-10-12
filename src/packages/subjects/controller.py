from typing import List

from fastapi import APIRouter

from src.packages.subjects.model import SubjectData
from src.packages.utilities.api_response_model import ApiResponseModel

subject_router = APIRouter()

subjects: List[SubjectData] = []


# helper
def check_if_roll_no_exists(roll_no: int):
    for i, student in enumerate(subjects):
        if student.student_roll == roll_no:
            return True, i
        else:
            continue
    return False, None



@subject_router.post("/", response_model=ApiResponseModel[List[SubjectData]])
def create_student(student_data: SubjectData):
    try:
        exists, i = check_if_roll_no_exists(student_data.student_roll)
        if not exists:
            subjects.append(student_data)
            return ApiResponseModel(message="created successfully", data=[student_data], status=True)
        else:
            return ApiResponseModel(message="record already exists", data=None, status=False)
    except Exception as error:
        return ApiResponseModel(message=str(error), data=None, status=False)


@subject_router.get("/", response_model=ApiResponseModel[List[SubjectData]])
def fetch_students():
    try:
        if len(subjects) <= 0:
            return ApiResponseModel(message="data not found", data=[], status=False)
        else:
            return ApiResponseModel(message="data found", data=subjects, status=True)
    except Exception as error:
        return ApiResponseModel(message=str(error), data=None, status=False)


@subject_router.get("/{rid}", response_model=ApiResponseModel[List[SubjectData]])
def fetch_student_by_roll_no(rid: int):
    try:
        exists, i = check_if_roll_no_exists(rid)
        if not exists:
            return ApiResponseModel(message="data not found", data=None, status=False)
        else:
            ApiResponseModel(message="data found", data=[subjects[i]], status=True)
    except Exception as error:
        return ApiResponseModel(message=str(error), data=None, status=False)


@subject_router.put("/{rid}", response_model=ApiResponseModel[List[SubjectData]])
def update_student(rid:int, student_data: SubjectData):
    try:
        exists, i = check_if_roll_no_exists(rid)
        if not exists:
            return ApiResponseModel(message="data not found", data=None, status=False)
        else:
            if rid == student_data.student_roll:
                subjects[i] = student_data
                ApiResponseModel(message="data updated", data=[subjects[i]], status=True)
            else:
                return ApiResponseModel(message="record already exists", data=None, status=False)

    except Exception as error:
        return ApiResponseModel(message=str(error), data=None, status=False)


@subject_router.delete("/{rid}", response_model=ApiResponseModel[List[SubjectData]])
def delete_student(rid:int):
    try:
        exists, i = check_if_roll_no_exists(rid)
        if not exists:
            return ApiResponseModel(message="data not found", data=None, status=False)
        else:
            deleted_student = subjects.pop(i)
            ApiResponseModel(message="data deleted", data=[deleted_student], status=True)
    except Exception as error:
        return ApiResponseModel(message=str(error), data=None, status=False)

