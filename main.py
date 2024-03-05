from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

# http://127.0.0.1:8000/docs
# python -m uvicorn myapi:app --reload
app = FastAPI()


students = {
    1: {
        "name": "jone",
        "age": 17,
        "class": "student 12",
    }
}


class Student(BaseModel):
    name: str
    age: int
    year: str


class updatedStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[str] = None
    year: Optional[str] = None


@app.get("/")
def index():
    return {"name": "First database"}


@app.get("/get-student/{student_id}")
def get_student(
    student_id: int = Path(..., description="the id is student", gt=0, lt=3)
):
    return students[student_id]


@app.get("/get-student-by-name/{student_id}")
def get_student(*, student_id: int, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"data": " not found"}


@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"error": "Student exists already"}

    students[student_id] = student
    return students[student_id]


@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: updatedStudent):
    if student_id not in students:
        return {"error": "Student does not exist"}
    if student.name != None:
        students[student_id].name = student.name
    if student.age != None:
        students[student_id].age = student.age
    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]

    


@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"error": "student dose not exist"}

    del students[student_id]
    return {"message": "student delete successfully"}
