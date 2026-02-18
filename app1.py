from fastapi.responses import HTMLResponse
from fastapi import FastAPI
import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

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


templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"),
name="static")

@app.get("/hello/{name}", response_class=HTMLResponse)
async def hello(request: Request, name:str):
    return templates.TemplateResponse("hello.html", {"request": request, "name": name})








if __name__ == "__main__":
    uvicorn.run("app1:app", host="127.0.0.1", port=8001, reload=True)

