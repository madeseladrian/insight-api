from faker import Faker

from src.data.contracts.db.glasses import DeleteImageStorage
from src.data.params import DeleteImageRepositoryParams


faker = Faker()

class DeleteImageStorageSpy(DeleteImageStorage):
    params: DeleteImageRepositoryParams

    def delete_image(self, params: DeleteImageRepositoryParams) -> None:
        self.params = params
