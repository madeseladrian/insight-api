from faker import Faker
from typing import Optional

from src.data.contracts.db.account import LoadAccountByTokenRepository
from src.data.params import LoadAccountByTokenRepositoryResult


faker = Faker()

class LoadAccountByTokenRepositorySpy(LoadAccountByTokenRepository):
    token: str
    result: Optional[LoadAccountByTokenRepositoryResult] = LoadAccountByTokenRepositoryResult(id=faker.uuid4())

    def load_by_token(self, token: str) -> Optional[LoadAccountByTokenRepositoryResult]:
        self.token = token
        return self.result
