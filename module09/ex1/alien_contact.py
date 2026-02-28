from enum import Enum
from pydantic import BaseModel, Field, model_validator
from datetime import datetime
from typing import Optional


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime = Field(...)
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def validate_rules(self):
        if self.contact_id.startswith("AC") is False:
            raise ValueError("contact_id should start with AC")
        elif (self.contact_type == ContactType.PHYSICAL and
                self.is_verified is False):
            raise ValueError("Physical contact reports must be verified")
        elif (self.contact_type == ContactType.TELEPATHIC and
                self.witness_count < 3):
            raise ValueError(
                                "Telepathic contact requires at least "
                                "3 witnesses")
        elif self.signal_strength > 7.0 and self.message_received is False:
            raise ValueError(
                            "Strong signals (> 7.0) should include received"
                            "messages")
        return self

def valid() -> None:
    print("Valid contact report")
    contact = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime(2026, 2, 28, 22, 30),
        location="Area 51, Nevada",
        contact_type=ContactType.RADIO,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
        is_verified=True,
    )

    print(
        f"ID: {contact.contact_id}\n"
        f"Type: {contact.contact_type.value}\n"
        f"Location: {contact.location}\n"
        f"Signal: {contact.signal_strength}/10\n"
        f"Duration: {contact.duration_minutes} minutes\n"
        f"Witnesses: {contact.witness_count}\n"
        f"Message: '{contact.message_received}'\n"
        f"Verified: {'Yes' if contact.is_verified else 'No'}\n"
    )


def unvalid() -> None:
    print("Expected validation error:")
    try:
        contact = AlienContact(
                contact_id="AC_2024_001",
                timestamp=datetime(2026, 2, 28, 22, 30),
                location="Area 51, Nevada",
                contact_type=ContactType.TELEPATHIC,
                signal_strength=8.5,
                duration_minutes=45,
                witness_count=1,
                message_received="Greetings from Zeta Reticuli",
                is_verified=True,
            )
        print(
                f"ID: {contact.contact_id}\n"
                f"Type: {contact.contact_type.value}\n"
                f"Location: {contact.location}\n"
                f"Signal: {contact.signal_strength}/10\n"
                f"Duration: {contact.duration_minutes} minutes\n"
                f"Witnesses: {contact.witness_count}\n"
                f"Message: '{contact.message_received}'\n"
                f"Verified: {'Yes' if contact.is_verified else 'No'}\n"
            )
    except ValueError as e:
        print(f"{e.errors()[0]["msg"]}")


def main():
    print("Alien Contact Log Validation")
    print("======================================")
    valid()
    print("======================================")
    unvalid()

main()
