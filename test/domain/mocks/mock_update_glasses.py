from faker import Faker

from src.domain.params import UpdateGlassesParams


faker = Faker()

def mock_update_glasses_params() -> UpdateGlassesParams:
    return UpdateGlassesParams(
        glasses_id=faker.uuid4(),
        data={'model': faker.word()}
    )
