from ....presentation.contracts import Controller
from ....presentation.controllers import UpdateGlassesController

from ...usecases import make_update_glasses_validation, make_db_update_glasses
from ..decorators import log_controller_decorator_factory


@log_controller_decorator_factory
def update_glasses_controller_factory() -> Controller:
    return UpdateGlassesController(
        update_glasses=make_db_update_glasses(),
        validation=make_update_glasses_validation()
    )
