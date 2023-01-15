from faker import Faker
from io import BytesIO

from src.domain.params import AddImageParams


faker = Faker()

def mock_add_image_params() -> AddImageParams:
    return AddImageParams(
        content_type=faker.word(),
        glasses_id=faker.uuid4(),
        image=BytesIO()
    )
