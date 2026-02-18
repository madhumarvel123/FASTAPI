from fastapi import FastAPI, Path, Query, Body
import uvicorn
from typing import List
from pydantic import BaseModel, Field

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello kartheek reddy"}

@app.get("/hello/{name}")
async def hello(name: str = Path(...,min_length=2, max_length=10)):
    return {"message": f"Hello {name}"} 

@app.get("/hello")
def hello(name: str):
    return {"message": f"Hi {name}"}


@app.get("/hello/{name}/{age}")
async def hello(name: str, age: int = Path(...,ge=1, le=100), percentage: float = Query(...,ge=0, le=100)):
    return {"message": f"Hello {name} you are {age} years old and your percentage is {percentage}"}


class Student(BaseModel):
     id:int
     name:str = Field(...,min_length=2, max_length=10)
     subjects:List[str] = Field(None,min_items=1, max_items=5)  


@app.post("/students/")
async def create_student(s1: Student):
    return s1


@app.post("/professors/")
async def create_professor(assistant_name:str = Body(...),rank:int = Body(...)):
    return {"message": f"Hello {assistant_name} you are {rank} years old"}



@app.post("/students/{college}")
async def student_data(college: str, age: int, student: Student):
    retval = {"college": college, "age": age, **student.dict()}
    return retval




if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)





