from pydantic import BaseModel, Field, ValidationError
from typing import Optional
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime = Field(...)
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(None, max_length=200)


def valid() -> None:
    print("Space Station Data Validation")
    print("========================================")
    valid = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime(2026, 2, 28, 12, 0),
        is_operational=True,
        notes="Regular maintenance completed.",
    )

    print(
        f"Valid station created:\nID: {valid.station_id}\n"
        f"Name: {valid.name}\nCrew: {valid.crew_size} people\n"
        f"Power: {valid.power_level}%\nOxygen: {valid.oxygen_level}%\n"
        f"Status:{"Operational" if valid.is_operational else
                                "Non-operational"}\n"
    )


def unvalid() -> None:
    try:
        valid = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=60,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2026, 2, 28, 12, 0),
            is_operational=True,
            notes="Regular maintenance completed.",
        )

        print(
            f"Valid station created:\nID: {valid.station_id}\n"
            f"Name: {valid.name}\nCrew: {valid.crew_size} people\n"
            f"Power: {valid.power_level}%\nOxygen: {valid.oxygen_level}%\n"
            f"Status:{"Operational" if valid.is_operational else
                                    "Non-operational"}\n"
        )
    except ValidationError as e:
        print("Expected validation error:")
        print(f"{e.errors()[0]["msg"]}")


def main() -> None:
    valid()
    unvalid()


main()
