from ....presentation.contracts import Controller
from ....presentation.controllers import UpdateImageController

from ...usecases import make_update_image_validation, make_db_update_image
from ..decorators import log_controller_decorator_factory


@log_controller_decorator_factory
def update_image_controller_factory() -> Controller:
    return UpdateImageController(
        update_image=make_db_update_image(),
        validation=make_update_image_validation()
    )
