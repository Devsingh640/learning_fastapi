from starlette.responses import JSONResponse

from src.packages.students.dal import StudentDal
from src.packages.students.model import Student, ReadStudentData
from fastapi.encoders import jsonable_encoder

class StudentService:
    def __init__(self, student_dal: StudentDal):
        self.student_dal = student_dal


    def create(self, new_students):

        new_student_data_to_save =  [Student.model_validate(student) for student in new_students]

        # new_student_data_to_save = []
        # for student in new_students:
        #     new_student_data_to_save.append(Student.model_validate(student))

        response = self.student_dal.add(new_student_data_to_save)

        if response:
            response_data =  [ReadStudentData(**inserted_student.model_dump()) for inserted_student in response]

            # response_data = []
            # for inserted_student in response:
            #     dict_data = inserted_student.model_dump()
            #     response_data.append(ReadStudentData(**dict_data))


            return JSONResponse({
                "message" : "student created successfully",
                "data": jsonable_encoder(response_data),
                "status" : True
            },
            status_code=200)

        else:
            return JSONResponse({
                "message" : "student not created successfully",
                "data": None,
                "status": False
            },
            status_code=200)










