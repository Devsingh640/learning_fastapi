import time

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.middleware.cors import CORSMiddleware

from src.packages.routes.router import init_routes

app = FastAPI()

init_routes(app)

template = Jinja2Templates(directory="templates")


# @app.get("/", response_class=HTMLResponse)
# def index():
#     return "hello world"

#
# app.add_middleware( CORSMiddleware(
#                                     allow_origins= ["*"],
#                                     allow_methods=["*"],
#                                     allow_headers=["*"]
#                     ))

@app.middleware("http")
async def calculate_and_print_request_processing_time(request:Request, call_next):
    # update_log_handler()
    start = time.perf_counter()
    response = await call_next(request)
    end = time.perf_counter()
    process_time = end - start
    # print(process_time)
    response.headers["ABC"] = f"{process_time}"
    return response


@app.get("/", response_class=HTMLResponse)
def index(request:Request):
    context={
        "request": request,
        "title": "TITLE",
        "user": "VISHAL",
        "status": "Active"
    }
    return template.TemplateResponse("index.html", context=context)







