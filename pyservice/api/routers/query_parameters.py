from fastapi import FastAPI, APIRouter
from services.process_query_parameters import calculate_days
router = APIRouter()

@router.get("/query_param")
async def process_parameters(name : str, dob : str):
    result = calculate_days(dob)
    return {"Days" : result.days }