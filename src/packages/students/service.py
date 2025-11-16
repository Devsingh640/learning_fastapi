from starlette.responses import JSONResponse

from src.packages.students.dal import StudentDal
from src.packages.students.model import Student, ReadStudentData
from fastapi.encoders import jsonable_encoder
from fastapi import Request

class StudentService:
    def __init__(self, student_dal: StudentDal):
        self.student_dal = student_dal

    def create(self, new_students):
        try:
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
        except Exception as error:
            print("Unexpected Error : ", str(error))


    def get_all(self, request_model: Request, page:int, limit:int):
        try:
            data, total_records= self.student_dal.get_all(request_model, page, limit)

            if data:
                # data = [Student, Student, Student, Student, Student, Student]
                response_data = [ReadStudentData.model_dump(el) for el in data]
                # response_data = [{}, {}, {}, {}, {}, {}]
                return JSONResponse({
                    "message": "data found",
                    "data": jsonable_encoder(response_data),
                    "total_records":total_records,
                    "total_pages": total_records,
                    "status": True
                },
                    status_code=200)
            else:
                return JSONResponse({
                    "message": "no data found",
                    "data": [],
                    "total_records": total_records,
                    "total_pages": total_records,
                    "status": True
                },
                    status_code=200)
        except Exception as error:
            print("Unexpected Error : ", str(error))


    def get_by_id(self, r_id: int):
        try:
            data= self.student_dal.get_by_id(r_id)
            if not data:
                return JSONResponse({
                    "message": "no record found",
                    "data": None,
                    "status": False
                },
                    status_code=200)
            else:
                response_data = ReadStudentData.model_dump(data)
                return JSONResponse({
                    "message": "record found",
                    "data": jsonable_encoder(response_data),
                    "status": True
                },
                    status_code=200)
        except Exception as error:
            print("Unexpected Error : ", str(error))

    def update_by_id(self, r_id: int, body):
        try:
            status, data = self.student_dal.update_by_id(r_id, body)
            if not status:
                return JSONResponse({
                    "message": "no record found",
                    "data": None,
                    "status": False
                },
                    status_code=200)
            else:
                response_data = ReadStudentData.model_dump(data)
                return JSONResponse({
                    "message": "record deleted",
                    "data": jsonable_encoder(response_data),
                    "status": True
                },
                    status_code=200)
        except Exception as error:
            print("Unexpected Error : ", str(error))

    def delete_by_id(self, r_id: int):
        try:
            status, data= self.student_dal.delete_by_id(r_id)
            if not status:
                return JSONResponse({
                    "message": "no record found",
                    "data": None,
                    "status": False
                },
                    status_code=200)
            else:
                response_data = ReadStudentData.model_dump(data)
                return JSONResponse({
                    "message": "record deleted",
                    "data": jsonable_encoder(response_data),
                    "status": True
                },
                    status_code=200)
        except Exception as error:
            print("Unexpected Error : ", str(error))







