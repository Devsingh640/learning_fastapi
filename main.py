from fastapi import FastAPI

from src.packages.routes.router import init_routes

app = FastAPI()

init_routes(app)


@app.get("/")
def index():
    return "hello world"







