from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Flight:
    departure: datetime
    arrival: datetime
    success: Optional[str] = None

    @classmethod
    def from_dict(cls, data: dict):
        today = datetime.today().date()

        departure_time = datetime.combine(
            today, datetime.strptime(data["Departure"], "%H:%M").time()
        )
        arrival_time = datetime.combine(
            today, datetime.strptime(data["Arrival"], "%H:%M").time()
        )
        success = data.get("Success")

        return cls(departure=departure_time, arrival=arrival_time, success=success)

    def to_dict(self):
        return {
            "Departure": self.departure.strftime("%H:%M"),
            "Arrival": self.arrival.strftime("%H:%M"),
        }
