from typing import Optional
from fastapi import FastAPI, Path
import uvicorn
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "name": "John",
        "age": 25,
        "class": 12
    },

    2: {
        "name": "Abrahm",
        "age": 25,
        "class": 11
    },
    3: {
        "name": "Johny",
        "age": 22,
        "class": 10
    },
    4: {
        "name": "Walton",
        "age": 20,
        "class": 9
    },
}

class Student(BaseModel):
    name: str
    age: int
    batch: int

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    batch: Optional[int] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

###########################Path Parameter################################
@app.get("/get-student/{student_id}")
def get_students_by_id(student_id: int):  ## path params should match the variable name in path and argument
    return students[student_id]

###########################Query Parameter################################

@app.get("/get-by-name")
def get_student(name: str):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}

################Combining Query and Path Parameters################################

@app.get("/get-student-id-name/{student_id}")
def get_students(student_id: int, name: str):
    
    if students[student_id]["name"] == name:
        return students[student_id]
    return {"Data": "Not found"}

################ Create Student - Post Method ################################

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student already exists"}
    
    students[student_id] = student
    return students[student_id]

################ Update Student - Put Method ################################
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    
    if student.name:
        students[student_id]["name"] = student.name
    if student.age:
        students[student_id]["age"] = student.age
    if student.batch:
        students[student_id]["batch"] = student.batch

    return students[student_id]


################ Delete Student - Delete Method ################################

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    
    del students[student_id]
    return {"Message": "Student deleted successfully"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

