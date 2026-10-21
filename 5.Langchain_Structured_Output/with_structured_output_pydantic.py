from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

  name: str = 'nitin'
  age: Optional[int] = None
  email: EmailStr
  cgpa: float = Field(gt=0, lt=10, default=5, description='a decimal value representing cgpa of a student')

new_student = {'age':32, 'email':'abc@gmail.com', 'cgpa':'9.5'} # dictionary bnai

student = Student(**new_student)

student_dict = dict(student)

print(student_dict['age'])

student_json = student.model_dump()