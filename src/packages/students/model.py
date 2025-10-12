from pydantic import BaseModel

class StudentData(BaseModel):
    student_roll: int
    student_name : str
    student_class : str
    student_contact: int
    student_address: str
