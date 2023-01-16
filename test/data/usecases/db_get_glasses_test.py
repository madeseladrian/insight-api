from faker import Faker
from typing import Tuple

from src.domain.params import GetGlassesParams
from src.data.usecases import DbGetGlasses

from ..mocks.db.glasses import GetGlassesRepositorySpy


class TestDbAddGlasses:
    # SetUp
    faker = Faker()
    params = GetGlassesParams(id=faker.uuid4())

    SutTypes = Tuple[
        DbGetGlasses,
        GetGlassesRepositorySpy
    ]

    def make_sut(self) -> SutTypes:
        get_glasses_repository_spy = GetGlassesRepositorySpy()
        sut = DbGetGlasses(
            get_glasses_repository=get_glasses_repository_spy
        )
        return (
            sut,
            get_glasses_repository_spy
        )

    def test_1_should_call_GetGlassesRepository_with_correct_values(self):
        sut, get_glasses_repository_spy = self.make_sut()
        sut.get(self.params)

        assert get_glasses_repository_spy.params == self.params
