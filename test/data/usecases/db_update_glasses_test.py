from typing import Tuple

from src.data.usecases import DbUpdateGlasses

from ..mocks.db.glasses import UpdateGlassesRepositorySpy


class TestDbAddGlasses:

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
        sut.update({})

        assert update_glasses_repository_spy.data == {}
