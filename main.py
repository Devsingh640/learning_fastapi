import time

from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.middleware.cors import CORSMiddleware
import gc

from src.configuration.configuration import settings
from src.packages.routes.router import init_routes
from src.packages.utilities.pos_db import create_db_tables, close_session
from admin import init_admin
template = Jinja2Templates(directory="templates")


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        init_routes(app)
        init_admin(app)

        create_db_tables()
    except Exception as error:
        print(str(error))
    finally:
        close_session()
        gc.collect()

    yield


app = FastAPI(lifespan=lifespan,
              title=settings.APPLICATION_SWAGGER_TITLE,
              description=settings.APPLICATION_SWAGGER_DESCRIPTION,
              summary=settings.APPLICATION_SWAGGER_SUMMARY,
              version=settings.APPLICATION_SWAGGER_VERSION,
              docs_url=settings.APPLICATION_SWAGGER_DOCUMENTATION_URL)


@app.middleware("http")
async def calculate_and_print_request_processing_time(request:Request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    end = time.perf_counter()
    process_time = end - start
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
    return template.TemplateResponse("index1.html", context=context)








