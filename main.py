from fastapi import FastAPI
from pydantic import BaseModel
from typing import TypeVar, Generic, Optional, List

app = FastAPI()


"""
Implement CRUD
"""

T = TypeVar("T")

class StudentData(BaseModel):
    student_roll: int
    student_name : str
    student_class : str
    student_contact: int
    student_address: str

class ApiResponseModel(BaseModel, Generic[T]):
    message: str
    data: Optional[T] = None
    status: bool



students=[] # list of objects (dictionaries)


@app.get("/")
def index():
    return "hello world"


@app.post("/students")
def create_student(student_data: StudentData):
    try:
        students.append(student_data)
        return {"message": f"created successfully",
                "data": student_data,
                "status": True
                }
    except Exception as error:
        # return {
        #     "message" : str(error),
        #     "data" : None,
        #     "status": False
        # }
        return ApiResponseModel(message=str(error), data=None, status=False)


@app.get("/students", response_model=ApiResponseModel[List[StudentData]])
def fetch_students():
    try:
        if len(students) <= 0:
            # return {"message": "not found",
            #         "data": None,
            #         "status": False
            #         }
            return ApiResponseModel(message="not found", data=[], status=False)
        else:
            # return {"message": "record found",
            #     "data": students,
            #     "status": True
            #     }
            return ApiResponseModel(message="not found", data=students, status=False)
    except Exception as error:
        # return {
        #     "message": str(error),
        #     "data": None,
        #     "status": False
        # }
        return ApiResponseModel(message=str(error), data=None, status=False)


@app.get("/students/{rid}")
def fetch_student_by_roll_no(rid: int):
    try:
        if rid < 0 or rid >= len(students):
            return {"message": "not found",
                "data": None,
                "status": False
                }
        else:
            return {"message": "record found",
                "data": students[rid],
                "status": True
                }
    except Exception as error:
        # return {
        #     "message": str(error),
        #     "data": None,
        #     "status": False
        # }
        return ApiResponseModel(message=str(error), data=None, status=False)


@app.put("/students/{rid}")
def update_student(rid:int, student_data: StudentData):
    try:
        if rid < 0 or rid >= len(students):
            return {"message": "not found",
                    "data":None,
                    "status":False}
        else:
            students[rid] = student_data
            return {"message": f"student with roll no. {rid} updated",
                    "data": student_data,
                    "status": True
                    }
    except Exception as error:
        # return {
        #     "message": str(error),
        #     "data": None,
        #     "status": False
        # }
        return ApiResponseModel(message=str(error), data=None, status=False)


@app.delete("/students/{rid}")
def delete_student(rid:int):
    try:
        if rid < 0 or rid >= len(students):
            return {"message": "not found",
                    "data":None,
                    "status":False}
        else:
            deleted_student = students.pop(rid)
            return {"message": f"student with roll no. {rid} deleted",
                    "data": deleted_student,
                    "status": True
                    }
    except Exception as error:
        # return {
        #     "message" : str(error),
        #     "data" : None,
        #     "status": False
        # }
        return ApiResponseModel(message=str(error), data=None, status=False)







