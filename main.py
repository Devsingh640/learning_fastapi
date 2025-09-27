from fastapi import FastAPI

app = FastAPI()


"""
Implement CRUD
"""


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
@app.post("/create-student")
def create_student():
    return "student created"

# READ
@app.get("/fetch-students")
def fetch_students():
    return student_data

@app.get("/fetch-student-by-roll-no/{rn}")
def fetch_student_by_roll_no(rn):
    print(rn)
    return student_data[rn]

# UPDATE
@app.put("/update-student")
def update_student():
    return "student updated"

@app.delete("delete-student")
def delete_student():
    return "student deleted"







