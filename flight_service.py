import csv
from typing import Dict, Optional
from models import Flight
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

flights_dict: Dict[int, Flight] = {}


def add_flight(flight: Flight) -> Flight:
    ##TODO imp


def get_flight(flight_id: int) -> Optional[Flight]:
    ##TODO imp


def load_flights() -> None:
    csv_file_path = "app/flights_raw_data.csv"  ##TODO export this to a config file

    with open(csv_file_path, mode="r") as file:
        reader = csv.DictReader(file)
        for (row) in (reader):  ##TODO ask what is the expected behavior if there are more then one flight per flight id
            flight_id = row["Flight ID"]
            flights_dict[flight_id] = Flight(
                id=flight_id,
                arrival=datetime.strptime(row["Arrival"], "%H:%M").time(),
                departure=datetime.strptime(row["Departure"], "%H:%M").time(),
                success=row["Success"],
            )


def update_flights() -> None:
    logger.info("Updating daily flights status")
    successful_flights_counter = 0
    sorted_flights = sorted(flights_dict.items(), key=lambda item: item[1]["arrival"])

    for flight_id, flight in sorted_flights:
        if (
            successful_flights_counter < 20
            and flight["arrival"] - flight["departure"] >= 180
        ):
            flight["success"] = "success"
            successful_flights_counter += 1
        else:
            flight["success"] = "failure"

        flights_dict[flight_id] = flight
