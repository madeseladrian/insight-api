from faker import Faker
from typing import Tuple

from src.domain.params import DeleteGlassesParams
from src.data.usecases import DbDeleteGlasses

from ..mocks.db.glasses import DeleteGlassesRepositorySpy


class TestDbAddGlasses:
    # SetUp
    faker = Faker()
    params = DeleteGlassesParams(glass_id=faker.uuid4())

    SutTypes = Tuple[
        DbDeleteGlasses,
        DeleteGlassesRepositorySpy
    ]

    def make_sut(self) -> SutTypes:
        delete_glasses_repository_spy = DeleteGlassesRepositorySpy()
        sut = DbDeleteGlasses(
            delete_glasses_repository=delete_glasses_repository_spy
        )
        return (
            sut,
            delete_glasses_repository_spy
        )

    def test_1_should_call_DeleteGlassesRepository_with_correct_values(self):
        sut, delete_glasses_repository_spy = self.make_sut()
        sut.delete(self.params)

        assert delete_glasses_repository_spy.params == self.params

    def test_2_should_return_None_on_success(self):
        sut, _ = self.make_sut()
        params = sut.delete(self.params)

        assert params is None
