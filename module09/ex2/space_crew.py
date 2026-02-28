from enum import Enum
from typing import List
from pydantic import BaseModel, Field, model_validator
from datetime import datetime


class Rank(Enum):
    CADET = "cadet"
    OFFICIER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime = Field(...)
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission(self):
        unactive = [c for c in self.crew if c.is_active is False]
        if self.mission_id.startswith("M") is False:
            raise ValueError("Mission ID must start with M")
        elif has_cc(self.crew) is False:
            raise ValueError("Must have at least one Commander or Captain")
        elif self.duration_days > 365:
            crew = [
                c for c in self.crew if c.years_experience >= 5
            ]
            if len(crew) < len(self.crew) / 2:
                raise ValueError(
                        "Long missions (> 365 days) require at least 50%"
                        "experienced crew"
                    )
        elif len(unactive) != 0:
            raise ValueError("All crew members must be active")
        return self


def has_cc(crew: List[CrewMember]) -> bool:
    for c in crew:
        if c.rank == Rank.COMMANDER or c.rank == Rank.CAPTAIN:
            return True
    return False


def valid() -> None:

    mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime(2026, 8, 15, 10, 0),
        duration_days=900,
        crew=[
            CrewMember(
                member_id="C001",
                name="Sarah Connor",
                rank=Rank.COMMANDER,
                age=40,
                specialization="Mission Command",
                years_experience=15
            ),
            CrewMember(
                member_id="C002",
                name="John Smith",
                rank=Rank.LIEUTENANT,
                age=35,
                specialization="Navigation",
                years_experience=10
            ),
            CrewMember(
                member_id="C003",
                name="Alice Johnson",
                rank=Rank.OFFICIER,
                age=32,
                specialization="Engineering",
                years_experience=8
            )
        ],
        mission_status="planned",
        budget_millions=2500.0
    )

    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(f"- {member.name} ({member.rank.value}) - "
              f"{member.specialization}")
    print("")


def unvalid() -> None:
    print("Expected validation error:")
    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2026, 8, 15, 10, 0),
            duration_days=900,
            crew=[
                CrewMember(
                    member_id="C001",
                    name="Sarah Connor",
                    rank=Rank.CADET,
                    age=40,
                    specialization="Mission Command",
                    years_experience=15
                ),
                CrewMember(
                    member_id="C002",
                    name="John Smith",
                    rank=Rank.LIEUTENANT,
                    age=35,
                    specialization="Navigation",
                    years_experience=10
                ),
                CrewMember(
                    member_id="C003",
                    name="Alice Johnson",
                    rank=Rank.OFFICIER,
                    age=32,
                    specialization="Engineering",
                    years_experience=8
                )
            ],
            mission_status="planned",
            budget_millions=2500.0
        )

        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for member in mission.crew:
            print(f"- {member.name} ({member.rank.value}) - "
                  f"{member.specialization}")
        print("")
    except ValueError as e:
        print(f"{e.errors()[0]["msg"]}")


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    valid()
    print("=========================================")
    unvalid()


main()
