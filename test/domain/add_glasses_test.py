from inspect import isabstract
import pytest
from unittest.mock import patch

from src.domain.features import AddGlasses
from src.domain.params import AddGlassesParams


class TestAddAccount:
    def test_1_should_AddAccount_is_an_abstract_class(self):
        assert isabstract(AddGlasses)

    @patch.multiple(AddGlasses, __abstractmethods__=set())
    def test_2_should_AddGlasses_raise_a_NotImplementedError_if_not_implemented(self):
        params = AddGlassesParams(
          uid_image='any_uid',
          model='any_model',
          format='any_format',
          gender='any_gender',
          public='any_public',
          category='any_category',
          frame_color='any_color',
          lens_color='any_color',
          size_bridge=0.0,
          height_frame=0.0,
          size_temples=0.0,
          price=0.0,
          additional_info='any_info'
        )
        add_glasses = AddGlasses()

        with pytest.raises(NotImplementedError, match='Should implement method: add'):
            add_glasses.add(data=params)
