from typing import Tuple

from src.domain.features import AddGlasses
from src.data.usecases import DbAddGlasses

from ...domain.mocks import mock_add_glasses_params
from ..mocks.db.glasses import AddGlassesRepositorySpy


class TestDbAddSurvey:
    # SetUp
    params = mock_add_glasses_params()

    SutTypes = Tuple[
        AddGlasses,
        AddGlassesRepositorySpy
    ]

    def make_sut(self) -> SutTypes:
        add_glasses_repository_spy = AddGlassesRepositorySpy()
        sut = DbAddGlasses(
            add_glasses_repository=add_glasses_repository_spy
        )
        return (
            sut,
            add_glasses_repository_spy
        )

    def test_1_should_call_AddGlassesRepository_with_correct_email(self):
        sut, add_glasses_repository_spy = self.make_sut()
        sut.add(self.params)

        assert add_glasses_repository_spy.data == self.params
