from typing import Tuple
from faker import Faker
from tempfile import SpooledTemporaryFile

from src.data.contracts.db.glasses import AddImageStorage


faker = Faker()

class AddImageStorageSpy(AddImageStorage):
    image: SpooledTemporaryFile
    image_type: str
    url_image: str = faker.url()
    glasses_id: str = faker.uuid4()

    def add_image(self, image: SpooledTemporaryFile, image_type: str) -> Tuple[str, str]:
        self.image = image
        self.image_type = image_type
        return self.url_image, self.glasses_id
