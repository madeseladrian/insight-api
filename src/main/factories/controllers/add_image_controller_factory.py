from ....presentation.contracts import Controller
from ....presentation.controllers import AddImageController

from ...usecases import make_add_image_validation, make_db_add_image
from ..decorators import log_controller_decorator_factory


@log_controller_decorator_factory
def add_image_controller_factory() -> Controller:
    return AddImageController(
        add_image=make_db_add_image(),
        validation=make_add_image_validation()
    )
