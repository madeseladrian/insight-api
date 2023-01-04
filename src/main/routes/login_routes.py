from fastapi import APIRouter, Depends, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from ...presentation.params import (
    LoginControllerRequest,
    SignUpControllerRequest
)
from ..factories.controllers import (
    login_controller_factory,
    signup_controller_factory
)


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

@router.post(
    '/login/',
    status_code=status.HTTP_200_OK
)
def login(request: OAuth2PasswordRequestForm = Depends()):
    controller = login_controller_factory()
    http_response = controller.handle(LoginControllerRequest(
        email=request.username,
        password=request.password
    ))
    return {**http_response, 'token_type': 'bearer'}
