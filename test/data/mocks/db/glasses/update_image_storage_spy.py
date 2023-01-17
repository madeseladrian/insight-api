from faker import Faker

from src.data.contracts.db.glasses import UpdateImageStorage
from src.data.params import UpdateImageRepositoryParams


faker = Faker()

class UpdateImageStorageSpy(UpdateImageStorage):
    params: UpdateImageRepositoryParams

    def update_image(self, params: UpdateImageRepositoryParams) -> None:
        self.params = params
