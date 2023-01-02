from fastapi import APIRouter, status

from ...presentation.params import SignUpControllerRequest
from ..factories.controllers import signup_controller_factory


router = APIRouter(
    tags=['Login']
)

@router.post(
    '/signup/',
    status_code=status.HTTP_200_OK,
)
def create_user(request: SignUpControllerRequest):
    controller = signup_controller_factory()
    http_response = controller.handle(request)
    return {**http_response, 'token_type': 'bearer'}
