from fastapi import FastAPI
from pydantic import BaseModel
from typing import TypeVar, Generic, Optional, List

app = FastAPI(title="Student & Subject CRUD API")


T = TypeVar("T")


class ApiResponseModel(BaseModel, Generic[T]):
    message: str
    data: Optional[T] = None
    status: bool



class SubjectData(BaseModel):
    subject_id: int
    subject_name: str
    subject_status: bool
    subject_description: str
    min_pass_marks: int



class StudentMarks(BaseModel):
    Math: int
    Math2: int
    Physic1: int
    Physic2: int


class StudentData(BaseModel):
    student_roll: int
    student_name: str
    student_class: str
    student_contact: int
    student_address: str
    student_marks: StudentMarks



students: List[StudentData] = []
subjects: List[SubjectData] = []



def check_if_roll_no_exists(roll_no: int):
    for i, student in enumerate(students):
        if student.student_roll == roll_no:
            return True, i
    return False, None


def check_if_subject_exists(sub_id: int):
    for i, subject in enumerate(subjects):
        if subject.subject_id == sub_id:
            return True, i
    return False, None



@app.get("/")
def index():
    return {"message": "Student & Subject CRUD "}



# STUDENT CRUD

@app.post("/students", response_model=ApiResponseModel[List[StudentData]])
def create_student(student_data: StudentData):
    try:
        exists, _ = check_if_roll_no_exists(student_data.student_roll)
        if exists:
            return ApiResponseModel(message="Student already exists", status=False)
        students.append(student_data)
        return ApiResponseModel(message="Student created successfully", data=[student_data], status=True)
    except Exception as error:
        return ApiResponseModel(message=str(error), status=False)


@app.get("/students", response_model=ApiResponseModel[List[StudentData]])
def fetch_students():
    try:
        if not students:
            return ApiResponseModel(message="No students found", data=[], status=False)
        return ApiResponseModel(message="Students fetched successfully", data=students, status=True)
    except Exception as error:
        return ApiResponseModel(message=str(error), status=False)


@app.get("/students/{rid}", response_model=ApiResponseModel[List[StudentData]])
def fetch_student_by_roll_no(rid: int):
    try:
        exists, i = check_if_roll_no_exists(rid)
        if not exists:
            return ApiResponseModel(message="Student not found", status=False)
        return ApiResponseModel(message="Student found", data=[students[i]], status=True)
    except Exception as error:
        return ApiResponseModel(message=str(error), status=False)


@app.put("/students/{rid}", response_model=ApiResponseModel[List[StudentData]])
def update_student(rid: int, student_data: StudentData):
    try:
        exists, i = check_if_roll_no_exists(rid)
        if not exists:
            return ApiResponseModel(message="Student not found", status=False)
        if rid != student_data.student_roll:
            return ApiResponseModel(message="Roll number mismatch", status=False)
        students[i] = student_data
        return ApiResponseModel(message="Student updated successfully", data=[students[i]], status=True)
    except Exception as error:
        return ApiResponseModel(message=str(error), status=False)


@app.delete("/students/{rid}", response_model=ApiResponseModel[List[StudentData]])
def delete_student(rid: int):
    try:
        exists, i = check_if_roll_no_exists(rid)
        if not exists:
            return ApiResponseModel(message="Student not found", status=False)
        deleted_student = students.pop(i)
        return ApiResponseModel(message="Student deleted successfully", data=[deleted_student], status=True)
    except Exception as error:
        return ApiResponseModel(message=str(error), status=False)


# SUBJECT CRUD

@app.post("/subjects", response_model=ApiResponseModel[List[SubjectData]])
def create_subject(subject_data: SubjectData):
    try:
        exists, _ = check_if_subject_exists(subject_data.subject_id)
        if exists:
            return ApiResponseModel(message="Subject already exists", status=False)
        subjects.append(subject_data)
        return ApiResponseModel(message="Subject created successfully", data=[subject_data], status=True)
    except Exception as error:
        return ApiResponseModel(message=str(error), status=False)


@app.get("/subjects", response_model=ApiResponseModel[List[SubjectData]])
def fetch_subjects():
    try:
        if not subjects:
            return ApiResponseModel(message="No subjects found", data=[], status=False)
        return ApiResponseModel(message="Subjects fetched successfully", data=subjects, status=True)
    except Exception as error:
        return ApiResponseModel(message=str(error), status=False)


@app.get("/subjects/{sid}", response_model=ApiResponseModel[List[SubjectData]])
def fetch_subject_by_id(sid: int):
    try:
        exists, i = check_if_subject_exists(sid)
        if not exists:
            return ApiResponseModel(message="Subject not found", status=False)
        return ApiResponseModel(message="Subject found", data=[subjects[i]], status=True)
    except Exception as error:
        return ApiResponseModel(message=str(error), status=False)


@app.put("/subjects/{sid}", response_model=ApiResponseModel[List[SubjectData]])
def update_subject(sid: int, subject_data: SubjectData):
    try:
        exists, i = check_if_subject_exists(sid)
        if not exists:
            return ApiResponseModel(message="Subject not found", status=False)
        if sid != subject_data.subject_id:
            return ApiResponseModel(message="Subject ID mismatch", status=False)
        subjects[i] = subject_data
        return ApiResponseModel(message="Subject updated successfully", data=[subjects[i]], status=True)
    except Exception as error:
        return ApiResponseModel(message=str(error), status=False)


@app.delete("/subjects/{sid}", response_model=ApiResponseModel[List[SubjectData]])
def delete_subject(sid: int):
    try:
        exists, i = check_if_subject_exists(sid)
        if not exists:
            return ApiResponseModel(message="Subject not found", status=False)
        deleted_subject = subjects.pop(i)
        return ApiResponseModel(message="Subject deleted successfully", data=[deleted_subject], status=True)
    except Exception as error:
        return ApiResponseModel(message=str(error), status=False)
