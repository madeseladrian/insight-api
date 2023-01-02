from faker import Faker

from src.data.contracts.db.account import LoadAccountByEmailRepository
from src.data.params import LoadAccountByEmailRepositoryResult


faker = Faker()

class LoadAccountByEmailRepositorySpy(LoadAccountByEmailRepository):
    email: str
    result: LoadAccountByEmailRepositoryResult = LoadAccountByEmailRepositoryResult(
      id=faker.uuid4(),
      name=faker.name(),
      password=faker.password()
    )

    def load_by_email(self, email: str) -> LoadAccountByEmailRepositoryResult:
        self.email = email
        return self.result
