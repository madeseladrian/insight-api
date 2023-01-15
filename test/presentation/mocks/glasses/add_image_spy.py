from faker import Faker

from src.domain.features import AddImage
from src.domain.params import AddImageParams, AddImageResult


faker = Faker()

class AddImageSpy(AddImage):
    params: AddImageParams
    glasses_id: str = faker.uuid4()
    url_image: str = faker.url()

    def add_image(self, params: AddImageParams) -> AddImageResult:
        self.params = params
        return AddImageResult(
            glasses_id=self.glasses_id,
            url_image=self.url_image
        )
