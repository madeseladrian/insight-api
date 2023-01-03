from faker import Faker
import uuid

from src.domain.params import AddAccountParams


faker = Faker()

def mock_add_account_params() -> AddAccountParams:
    return AddAccountParams(
        id=str(uuid.uuid4()),
        name=faker.name(),
        email=faker.email(),
        password=faker.password()
    )
