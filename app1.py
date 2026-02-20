from fastapi.responses import HTMLResponse
from fastapi import FastAPI, File, UploadFile
import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
import shutil   
from fastapi import Form


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
app = FastAPI()
@app.post("/cookie/")
def create_cookie():
    content = {"message": "cookie set"}
    response = JSONResponse(content=content)
    response.set_cookie(key="username", value="admin")
    return response


@app.get("/readcookie/")
async def read_cookie(username: str = Cookie(None)):
    return {"username": username}



if __name__ == "__main__":
    uvicorn.run("app1:app", host="127.0.0.1", port=8001, reload=True)

