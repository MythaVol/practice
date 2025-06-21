from fastapi import FastAPI
from pydantic import BaseModel

class Student(BaseModel):
    isu: int
    name: str
    surname: str

student_list: Student =[
    {"isu": 409564, "name":"Ivan", "surname": "Ivanov"},
    {"isu": 403940, "name":"Grisha", "surname": "Kulebyakin"}
]


app = FastAPI()


@app.get("/students")
def home()-> list[Student]:
    return student_list


@app.post("/students/add")
def add(student: Student):
    student_list.append(student)
    return student_list