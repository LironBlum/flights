import logging
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.flight_service import Flight, add_flight, get_flight, get_all_flights

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/add_flight/", status_code=201)
def create(flight: dict):
    added_flight = add_flight(flight)
    return added_flight


@router.get("/get_flight/{flight_id}")
def get(flight_id: str):
    flight: Flight = get_flight(flight_id)
    if not flight:
        raise HTTPException(status_code=404, detail="Flight not found")
    return flight


@router.get("/get_flight/")
def get_all():
    flights: Flight = get_all_flights()
    return JSONResponse(content={"flights": flights})
