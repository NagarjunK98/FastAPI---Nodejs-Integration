from fastapi import APIRouter, responses
from .routers import query_parameters

router = APIRouter()

router.include_router(
    query_parameters.router,
    prefix="/query-params",
    tags=["display"],
    responses = {404: {"description": "API not found"}},
)
