from fastapi.responses import HTMLResponse
from fastapi import FastAPI, File, UploadFile, HTTPException
import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
import shutil   
from fastapi import Form
from typing import List
from pydantic import BaseModel, Field
from typing import Tuple
app = FastAPI()

# @app.get("/hello/", response_class=HTMLResponse)
# async def hello():
#     ret = """
#     <html>
#         <body>
#             <h2>Hello Madhukumar Gopal!</h2>
#         </body>
#     </html>
#      """
#     return ret



# templates = Jinja2Templates(directory="templates")

# @app.get("/hello/", response_class=HTMLResponse)
# async def hello(request: Request):
#     return templates.TemplateResponse("hello.html", {"request": request})


# templates = Jinja2Templates(directory="templates")

# app.mount("/static", StaticFiles(directory="static"),
# name="static")

# @app.get("/hello/{name}", response_class=HTMLResponse)
# async def hello(request: Request, name:str):
#     return templates.TemplateResponse("hello.html", {"request": request, "name": name})

templates = Jinja2Templates(directory="templates")
# @app.get("/login/", response_class=HTMLResponse)
# async def login(request: Request):
#     return templates.TemplateResponse("login.html",{"request": request})

# @app.post("/submit")
# async def submit(request: Request):
#     form = await request.form()
#     username = form.get("nm")
#     password = form.get("pwd")
#     if username == "madhu" and password == "madhu":
#         return templates.TemplateResponse("submit.html", {"request": request})
#     else:
#         return templates.TemplateResponse("login.html", {"request": request})

# @app.post("/submit")
# async def submit(nm:str = Form(...),pwd:str = Form(...)):
#     print(f"Submit called with nm={nm}")
#     return {"username":nm}
  
# @app.get("/upload/", response_class=HTMLResponse)
# async def upload(request: Request):
#     return templates.TemplateResponse("uploadfile.html",{"request": request})


# @app.post("/upload/")
# async def create_upload_file(file: UploadFile = File(...)):
#     with open("destination.png", "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)
#     return {"filename": file.filename}



from fastapi import FastAPI, Cookie
from fastapi.responses import JSONResponse
# app = FastAPI()
# @app.post("/cookie/")
# def create_cookie():
#     content = {"message": "cookie set"}
#     response = JSONResponse(content=content)
#     response.set_cookie(key="username", value="admin", max_age=20, httponly=True, secure=True)
#     return response


# @app.get("/readcookie/")
# async def read_cookie(username: str = Cookie(None)):
#     return {"username": username}

# app = FastAPI()
# class student(BaseModel):
#     id: int
#     name :str = Field(None, title="name of student", max_length=10)
#     marks: List[int] = []
#     percent_marks: float
# class percent(BaseModel):
#     id:int
#     name :str = Field(None, title="name of student", max_length=10)
#     percent_marks: float
# @app.post("/marks", response_model=percent)
# async def get_percent(s1:student):
#     s1.percent_marks=sum(s1.marks)/2
    # return s1

# app = FastAPI()
# @app.get("/rspheader/")
# def set_rsp_headers():
#     content = {"message": "Hello World"}
#     headers = {"X-Web-Framework": "FastAPI", "Content-Language": "en-US"}
#     return JSONResponse(content=content, headers=headers)

# app = FastAPI()
# class supplier(BaseModel):
#     supplierID:int
#     supplierName:str
# class product(BaseModel):
#     productID:int
#     prodname:str
#     price:int
#     supp:supplier
# class customer(BaseModel):
#     custID:int
#     custname:str
#     prod:Tuple[product]

# @app.post('/invoice')
# async def getInvoice(c1:customer):
#     return c1   



data = []
class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str  


@app.post("/book")
def add_book(book: Book):
    data.append(book.dict())
    return data


@app.get("/list")
def get_books():
    return data 

@app.get("/book/{id}")
def get_book(id: int):
    for book in data:
        if book["id"] == id:
            return book
    return {"message": "Book not found"} 


@app.put("/book/{id}")
def update_book(id: int, book: Book):
    for index, existing_book in enumerate(data):
        if existing_book["id"] == id:
            data[index] = book.dict()
            return data[index]

@app.delete("/book/{id}", status_code=204)
def delete_book(id: int):
    for index, book in enumerate(data):
        if book["id"] == id:
            data.pop(index)
            return

    raise HTTPException(status_code=404, detail="Book not found")





if __name__ == "__main__":
    uvicorn.run("app1:app", host="127.0.0.1", port=8001, reload=True)

