from ....presentation.contracts import Controller
from ....presentation.controllers import SignUpController

from ...usecases import (
    make_db_add_account,
    make_db_authentication,
    make_signup_validation
)

def signup_controller_factory() -> Controller:
    return SignUpController(
        add_account=make_db_add_account(),
        authentication=make_db_authentication(),
        validation=make_signup_validation()
    )
