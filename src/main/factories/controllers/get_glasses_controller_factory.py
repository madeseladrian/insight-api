from ....presentation.contracts import Controller
from ....presentation.controllers import GetGlassesController

from ...usecases import make_get_glasses_validation, make_db_get_glasses
from ..decorators import log_controller_decorator_factory


@log_controller_decorator_factory
def get_glasses_controller_factory() -> Controller:
    return GetGlassesController(
        get_glasses=make_db_get_glasses(),
        validation=make_get_glasses_validation()
    )
