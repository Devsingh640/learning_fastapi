from typing import List

from src.packages.students.model import Student


class StudentDal:

    def __init__(self, session):
        self.session = session

    # can do single insert and bulk insert
    def add(self, new_students: List[Student]):
        try:
            # new_students = [s1 , s2, s3]
            for student in new_students:
                self.session.add(student)

            self.session.commit()

            for student in new_students:
                self.session.refresh(student)

        except Exception as error:
            self.session.rollback()
            print("Unexpected Error Occured: ", str(error))









    def get_all(self):
        pass

    def get_by_id(self, r_id: int):
        pass

    def update(self, r_id: int, body: dict):
        pass

    def delete(self, r_id: int):
        pass