from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def check_rules(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')

        contain_a_leader = False
        experienced = 0
        for crew_member in self.crew:
            if crew_member.rank in (Rank.COMMANDER, Rank.CAPTAIN):
                contain_a_leader = True
            if crew_member.years_experience >= 5:
                experienced += 1
            if not crew_member.is_active:
                raise ValueError("All crew members must be active")

        if not contain_a_leader:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365 and experienced * 2 < len(self.crew):
            raise ValueError(
                "Long missions need 50% experienced crew (5+ years)"
            )

        return self


BAR: str = "=" * 41

if __name__ == "__main__":
    print("Space Mission Crew Validation")
    print(BAR)

    crew_members_list: list[CrewMember] = [
        CrewMember(
            member_id="CM001", name="Zaphod Beeblebrox",
            rank=Rank.COMMANDER, age=42,
            specialization="Galactic Presidency", years_experience=20,
        ),
        CrewMember(
            member_id="CM002", name="Arthur Dent",
            rank=Rank.LIEUTENANT, age=38,
            specialization="Emergency Tea Brewing", years_experience=10,
        ),
        CrewMember(
            member_id="CM003", name="Ford Prefect",
            rank=Rank.OFFICER, age=35,
            specialization="Field Research", years_experience=8,
        ),
    ]
    space_mission = SpaceMission(
        mission_id="M42_MAGRATHEA",
        mission_name="The Answer to Everything",
        destination="Magrathea",
        launch_date=datetime(2042, 10, 12, 4, 2),
        duration_days=900,
        budget_millions=4242.0,
        crew=crew_members_list,
    )
    print("Valid mission created:")
    print(f"Mission: {space_mission.mission_name}")
    print(f"ID: {space_mission.mission_id}")
    print(f"Destination: {space_mission.destination}")
    print(f"Duration: {space_mission.duration_days} days")
    print(f"Budget: ${space_mission.budget_millions}M")
    print(f"Crew size: {len(space_mission.crew)}")
    print("Crew members:")
    for member in space_mission.crew:
        print(f"- {member.name} ({member.rank.value}) - "
              f"{member.specialization}")

    print()
    print(BAR)

    try:
        one_crew_member: list[CrewMember] = [
            CrewMember(
                member_id="CM042",
                name="Marvin",
                rank=Rank.OFFICER,
                age=30,
                specialization="Chronic Depression",
                years_experience=4,
            )
        ]
        SpaceMission(
            mission_id="M42_MOON",
            mission_name="Paranoid Android Run",
            destination="Moon",
            launch_date=datetime(2042, 9, 1, 12, 0),
            duration_days=120,
            budget_millions=42.0,
            crew=one_crew_member,
        )
    except ValidationError as e:
        print("Expected validation error:")
        msg = e.errors()[0]["msg"]
        print(msg.replace("Value error, ", ""))
