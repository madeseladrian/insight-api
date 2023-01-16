from inspect import isabstract
import pytest
from unittest.mock import patch

from src.domain.features import GetGlasses
from src.domain.params import GetGlassesParams


class TestGetGlasses:
    def test_1_should_GetGlasses_is_an_abstract_class(self):
        assert isabstract(GetGlasses)

    @patch.multiple(GetGlasses, __abstractmethods__=set())
    def test_2_should_GetGlasses_raise_a_NotImplementedError_if_not_implemented(self):
        params = GetGlassesParams(id='any_id')
        get_glasses = GetGlasses()

        with pytest.raises(NotImplementedError, match='Should implement method: get'):
            get_glasses.get(user_id=params)
