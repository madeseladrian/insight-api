from faker import Faker

from src.domain.params import AddGlassesParams

faker = Faker()

def mock_add_glasses_params() -> AddGlassesParams:
    return AddGlassesParams(
        user_id=faker.uuid4(),
        glasses_id=faker.uuid4(),
        url_image=faker.image_url(),
        model=faker.word(),
        format=faker.word(),
        gender=faker.word(),
        public=faker.word(),
        category=faker.word(),
        frame_color=faker.word(),
        lens_color=faker.word(),
        size_lens=0.0,
        size_bridge=0.0,
        height_frame=0.0,
        size_temples=0.0,
        price=0.0,
        additional_info=faker.sentence(),
    )
