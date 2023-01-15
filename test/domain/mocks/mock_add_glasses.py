from faker import Faker

from src.domain.params import AddGlassesParams


faker = Faker()

def mock_add_glasses_params() -> AddGlassesParams:
    return AddGlassesParams(
        url_image=faker.url(),
        glasses_id=faker.uuid4(),
        user_id=faker.uuid4(),
        model=faker.word(),
        format=faker.word(),
        gender=faker.word(),
        public=faker.word(),
        category=faker.word(),
        frame_color=faker.word(),
        lens_color=faker.word(),
        size_lens=0.0,
        size_bridge=0.1,
        height_frame=0.2,
        size_temples=0.3,
        price=0.4,
        additional_info=faker.sentence(),
    )
