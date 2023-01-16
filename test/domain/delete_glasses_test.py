from inspect import isabstract
import pytest
from unittest.mock import patch

from src.domain.features import DeleteGlasses
from src.domain.params import DeleteGlassesParams


class TestDeleteGlasses:
    def test_1_should_DeleteGlasses_is_an_abstract_class(self):
        assert isabstract(DeleteGlasses)

    @patch.multiple(DeleteGlasses, __abstractmethods__=set())
    def test_2_should_DeleteGlasses_raise_a_NotImplementedError_if_not_implemented(self):
        params = DeleteGlassesParams(glass_id='any_id')
        delete_glasses = DeleteGlasses()

        with pytest.raises(NotImplementedError, match='Should implement method: delete'):
            delete_glasses.delete(params)
