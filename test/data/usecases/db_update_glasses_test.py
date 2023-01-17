from typing import Dict, Tuple

from src.data.usecases import DbUpdateGlasses

from ..mocks.db.glasses import UpdateGlassesRepositorySpy


class TestDbAddGlasses:

    params: Dict = {'any_key': 'any_value'}

    SutTypes = Tuple[
        DbUpdateGlasses,
        UpdateGlassesRepositorySpy
    ]

    def make_sut(self) -> SutTypes:
        update_glasses_repository_spy = UpdateGlassesRepositorySpy()
        sut = DbUpdateGlasses(
            update_glasses_repository=update_glasses_repository_spy
        )
        return (
            sut,
            update_glasses_repository_spy
        )

    def test_1_should_call_UpdateGlassesRepository_with_correct_values(self):
        sut, update_glasses_repository_spy = self.make_sut()
        sut.update(self.params)

        assert update_glasses_repository_spy.data == self.params

    def test_2_should_return_None_if_UpdateGlassesRepository_update_data(self):
        sut, _ = self.make_sut()
        update = sut.update(self.params)

        assert update is None
