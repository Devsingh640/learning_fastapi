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


student_data = {
    "1234":     {"student_roll_no": "1234",
                "student_name": "raja",
                "student_class" : "s3",
                "student_contact": "1234567890"},

    "4321": {"student_roll_no": "4321",
             "student_name": "sumit",
             "student_class": "s2",
             "student_contact": "0987654321"}
}




@app.get("/")
def index():
    return "hello world"

# CREATE
@app.post("/create-student", response_model=StudentData)
def create_student(studentData: StudentData):
    students.append(studentData)
    print(students)     # print the original data structure
    print(students[0]) # print the ist element from the student data
    return studentData

@app.get("/fetch-students", response_model=StudentData)
def fetch_students():


    return students

@app.get("/fetch-student-by-roll-no/{rn}")
def fetch_student_by_roll_no(rn: int, response_model = StudentData):
    print(rn)
    print(type(rn))

    # if else condition
    if rn < 0 or rn >= len(students):
        pass
    else:
        return students[rn]


    return student_data.get("rn", {"student_roll_no": "4321",
             "student_name": "sumit",
             "student_class": "s2",
             "student_contact": "0987654321"})

# UPDATE
@app.put("/update-student/{rn}")
def update_student(rn):
    print(rn)

    updated_dict = {"student_roll_no": rn,
                "student_name": "vijay",
                "student_class" : "s6",
                "student_contact": "8765432345"}

    student_data.update({rn:updated_dict})

    return f"student with roll no. {rn} updated"

@app.delete("/delete-student/{rn}")
def delete_student(rn):
    print(rn)
    student_data.pop(str(rn))
    return f"student with roll no. {rn} deleted"







