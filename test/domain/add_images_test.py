from inspect import isabstract
from io import BytesIO
import pytest
from unittest.mock import patch

from src.domain.features import AddImage
from src.domain.params import AddImageParams


class TestAddAccount:
    def test_1_should_AddImage_is_an_abstract_class(self):
        assert isabstract(AddImage)

    @patch.multiple(AddImage, __abstractmethods__=set())
    def test_2_should_AddImage_raise_a_NotImplementedError_if_not_implemented(self):
        params = AddImageParams(
            image=BytesIO(),
            glasses_id='any_id'
        )
        add_images = AddImage()

        with pytest.raises(NotImplementedError, match='Should implement method: add_image'):
            add_images.add_image(params)
