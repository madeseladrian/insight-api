from dataclasses import dataclass
from email_validator import validate_email


@dataclass
class EmailValidatorAdapter:

    def is_valid(self, email: str) -> None:
        validate_email(email=email, check_deliverability=True)
