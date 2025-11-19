from typing import Optional

from pydantic import BaseModel
from sqlmodel import SQLModel, Field


class StudentData(BaseModel):
    student_roll: int
    student_name : str
    student_class : str
    student_contact: int
    student_address: str


class Student(SQLModel, table=True):
    model_config = {"protected_namespace":()}

    __tablename__ = "student_master"

    id: int | None = Field(default=None, primary_key=True)
    student_roll: str  = Field(default=None, unique=True, index=True)
    student_name : str = Field(default=None)
    student_class : str = Field(default=None)
    student_contact: Optional[str] = None
    student_address: Optional[str] = None

    description: Optional[str] = None
    # description: str | None



class AddStudentData(SQLModel):
    model_config = {"protected_namespace":()}

    student_roll: str | None = None
    student_name: str | None = None
    student_class: str | None = None

    class config:
        from_attributes=True


class ReadStudentData(SQLModel):
    model_config = {"protected_namespace":()}

    id : int
    student_roll: str | None = None
    student_name: str | None = None
    student_class: str | None = None

    class config:
        from_attributes=True


class UpdateStudentData(SQLModel):
    model_config = {"protected_namespace":{}}

    student_name: str | None = None
    student_class: str | None = None
    student_contact: str | None = None
    student_address: str | None = None
    description: Optional[str] = None

    class config:
        from_attributes=True










