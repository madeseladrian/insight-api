from fastapi import APIRouter, Depends, status

from ...presentation.params import GetGlassesControllerRequest

from ..adapters import route_response_adapter
from ..docs import glasses_responses
from ..factories.controllers import (
    add_glasses_controller_factory,
    get_glasses_controller_factory
)
from ..middlewares import auth
from ..params import AddGlassesRequest


router = APIRouter(
    tags=['Glasses'],
    prefix='/glasses'
)

@router.post(
    '/',
    responses=glasses_responses,
    status_code=status.HTTP_204_NO_CONTENT
)
def add_glasses(request: AddGlassesRequest, user_id: str = Depends(auth)):
    controller_params = {**request}
    controller_params.update({'user_id': user_id})

    controller = add_glasses_controller_factory()
    http_response = controller.handle(controller_params)
    return route_response_adapter(http_response)

@router.get(
    '/',
    responses=glasses_responses,
    status_code=status.HTTP_200_OK
)
def get_glasses(user_id: str = Depends(auth)):
    controller = get_glasses_controller_factory()
    http_response = controller.handle(
        GetGlassesControllerRequest(id=user_id)
    )
    adapter = route_response_adapter(http_response)
    body = adapter.get('body')
    return {**body, 'token_type': 'bearer'}
