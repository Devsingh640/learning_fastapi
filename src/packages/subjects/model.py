from pydantic import BaseModel

class SubjectData(BaseModel):
    subject_name: str
    description : str
    subject_id : str
    subject_status: bool
    min_passing_marks: int