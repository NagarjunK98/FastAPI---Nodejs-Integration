from fastapi import FastAPI
from api import api

app = FastAPI()

app.include_router(
    api.router,
    prefix="/v1/api",
    tags=["api"],
    responses= {404 : {"description": "Not Found"}}

)