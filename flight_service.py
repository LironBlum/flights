import csv
from typing import Dict, Optional
from app.models import Flight
from datetime import timedelta
import logging

logger = logging.getLogger(__name__)

flights_dict: Dict[str, Flight] = {}


def add_flight(flight: Dict) -> Dict[int, Flight]:  ##TODO add user input validation
    logger.info(f"Adding new flight: {flight}")
    flight_id = flight["Flight_id"]
    flights_dict[flight_id] = Flight.from_dict(flight)
    update_flights()
    return {flight_id: flights_dict[flight_id]}


def get_flight(flight_id: str) -> Optional[Flight]:
    logger.info(f"Getting flight with id: {flight_id}")
    return flights_dict.get(flight_id)


def get_all_flights() -> Dict[str, Flight]:
    logger.info("Getting all flights")
    return [(flight_id, flight.to_dict()) for flight_id, flight in flights_dict.items()]


def load_flights() -> None:
    logger.info("Loading flights data from csv file to memory")
    csv_file_path = "app/flights_raw_data.csv"  ##TODO export this to a config file

    with open(csv_file_path, mode="r") as file:
        reader = csv.DictReader(file)
        for (
            row
        ) in (
            reader
        ):  ##TODO ask what is the expected behavior if there are more then one flight per flight id
            flight_id = row["Flight ID"]
            flights_dict[flight_id] = Flight.from_dict(row)


def update_flights() -> None:
    logger.info("Updating daily flights status")
    successful_flights_counter = 0
    global flights_dict
    sorted_flights = sorted(flights_dict.items(), key=lambda item: item[1].arrival)
    min_flight_duration = timedelta(minutes=180)  ##TODO export this to a config file

    sorted_flights_dict = {}

    for flight_id, flight in sorted_flights:
        if (
            successful_flights_counter < 20  ##TODO export this to a config file
            and flight.arrival - flight.departure >= min_flight_duration
        ):
            flight.success = "success"
            successful_flights_counter += 1
        else:
            flight.success = "failure"

        sorted_flights_dict[flight_id] = flight

    flights_dict = sorted_flights_dict
