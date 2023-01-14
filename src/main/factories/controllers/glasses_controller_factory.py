from ....presentation.contracts import Controller
from ....presentation.controllers import AddGlassesController

from ...usecases import make_add_glasses_validation, make_db_add_glasses
from ..decorators import log_controller_decorator_factory


@log_controller_decorator_factory
def add_glasses_controller_factory() -> Controller:
    return AddGlassesController(
        add_glasses=make_db_add_glasses(),
        validation=make_add_glasses_validation()
    )
