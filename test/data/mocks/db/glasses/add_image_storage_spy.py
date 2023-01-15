from faker import Faker

from src.data.contracts.db.glasses import AddImageStorage
from src.data.params import AddImageRepositoryParams, AddImageRepositoryResult

faker = Faker()

class AddImageStorageSpy(AddImageStorage):
    params: AddImageRepositoryParams
    url_image: str = faker.url()
    glasses_id: str = faker.uuid4()

    def add_image(self, params: AddImageRepositoryParams) -> AddImageRepositoryResult:
        self.params = params
        return AddImageRepositoryResult(
            glasses_id=self.glasses_id,
            url_image=self.url_image
        )
