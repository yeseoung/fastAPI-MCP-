from pydantic import BaseModel

class student_Response(BaseModel): # DTO // DATA TO OBJECT
    student_id : int
    name : str
    grade : int
    major : str