from inspect import isabstract
import pytest
from unittest.mock import patch

from src.domain.features import UpdateGlasses
from src.domain.params import UpdateGlassesParams


class TestUpdateGlasses:
    def test_1_should_UpdateGlasses_is_an_abstract_class(self):
        assert isabstract(UpdateGlasses)

    @patch.multiple(UpdateGlasses, __abstractmethods__=set())
    def test_2_should_UpdateGlasses_raise_a_NotImplementedError_if_not_implemented(self):
        params = UpdateGlassesParams(glasses_id='any_id', data={'any_key': 'any_value'})
        update_glasses = UpdateGlasses()

        with pytest.raises(NotImplementedError, match='Should implement method: update'):
            update_glasses.update(params)
