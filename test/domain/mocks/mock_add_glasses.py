from faker import Faker
from src.domain.params import AddGlassesParams
from src.data.params import AddGlassesRepositoryParams
from tempfile import SpooledTemporaryFile


faker = Faker()

params = AddGlassesParams(
    user_id=faker.uuid4(),
    image=SpooledTemporaryFile(max_size=10),
    image_type='image/jpeg',
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

def mock_add_glasses_params() -> AddGlassesParams:
    return params

def mock_add_glasses_repository_params(url_image: str, glasses_id: str) -> AddGlassesRepositoryParams:
    return AddGlassesRepositoryParams(
        url_image=url_image,
        glasses_id=glasses_id,
        user_id=params['user_id'],
        model=params['model'],
        format=params['format'],
        gender=params['gender'],
        public=params['public'],
        category=params['category'],
        frame_color=params['frame_color'],
        lens_color=params['lens_color'],
        size_lens=params['size_lens'],
        size_bridge=params['size_bridge'],
        height_frame=params['height_frame'],
        size_temples=params['size_temples'],
        price=params['price'],
        additional_info=params['additional_info']
    )
