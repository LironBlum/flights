import logging
from fastapi import APIRouter, HTTPException
from app.flight_service import Flight, add_flight, get_flight

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/add_flight/")
def create_flight(flight: dict) -> Flight:
    addedFlight: Flight = add_flight(flight)
    return addedFlight


@router.get("/get_flight/{flight_id}")
def get_flight(flight_id: int) -> Flight:
    flight: Flight = get_flight(flight_id)
    if not flight:
        raise HTTPException(status_code=404, detail="Flight not found")
    return flight
