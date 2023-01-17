from ....presentation.contracts import Controller
from ....presentation.controllers import DeleteGlassesController

from ...usecases import make_delete_glasses_validation, make_db_delete_glasses
from ..decorators import log_controller_decorator_factory


@log_controller_decorator_factory
def delete_glasses_controller_factory() -> Controller:
    return DeleteGlassesController(
        delete_glasses=make_db_delete_glasses(),
        validation=make_delete_glasses_validation()
    )
