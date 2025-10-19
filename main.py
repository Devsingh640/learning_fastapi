from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from src.packages.routes.router import init_routes

app = FastAPI()

init_routes(app)

template = Jinja2Templates(directory="templates")


# @app.get("/", response_class=HTMLResponse)
# def index():
#     return "hello world"

@app.get("/", response_class=HTMLResponse)
def index(request:Request):
    context={
        "request": request,
        "title": "TITLE",
        "user": "VISHAL",
        "status": "Active"
    }
    return template.TemplateResponse("index.html", context=context)







