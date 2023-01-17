from inspect import isabstract
from io import BytesIO
import pytest
from unittest.mock import patch

from src.domain.features import UpdateImage
from src.domain.params import UpdateImageParams


class TestUpdateImage:
    def test_1_should_UpdateImage_is_an_abstract_class(self):
        assert isabstract(UpdateImage)

    @patch.multiple(UpdateImage, __abstractmethods__=set())
    def test_2_should_UpdateImage_raise_a_NotImplementedError_if_not_implemented(self):
        params = UpdateImageParams(
            image=BytesIO(),
            glasses_id='any_id',
            content_type='any_type'
        )
        update_image = UpdateImage()

        with pytest.raises(NotImplementedError, match='Should implement method: update_image'):
            update_image.update_image(params)
