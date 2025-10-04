from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


"""
Implement CRUD
"""


class StudentData(BaseModel):
    student_name : str
    student_class : str
    student_contact: int
    student_address: str


students=[] # list of objects (dictionaries)


@app.get("/")
def index():
    return "hello world"


@app.post("/create-student", response_model=StudentData)
def create_student(student_data: StudentData):
    try:
        students.append(student_data)
        return {"message": f"created successfully",
                "data": student_data,
                "status": True
                }
    except Exception as error:
        return {
            "message" : str(error),
            "data" : None,
            "status": False
        }


@app.get("/fetch-students", response_model=StudentData)
def fetch_students():
    try:
        if len(students) <= 0:
            return {"message": "not found",
                    "data": None,
                    "status": False
                    }
        else:
            return {"message": "record found",
                "data": students,
                "status": True
                }
    except Exception as error:
        return {
            "message": str(error),
            "data": None,
            "status": False
        }


@app.get("/fetch-student-by-roll-no/{rid}")
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
        return {
            "message": str(error),
            "data": None,
            "status": False
        }


@app.put("/update-student/{rid}")
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
        return {
            "message": str(error),
            "data": None,
            "status": False
        }


@app.delete("/delete-student/{rid}")
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
        return {
            "message" : str(error),
            "data" : None,
            "status": False
        }







