from fastapi import APIRouter, Depends, status

from ...presentation.params import AddGlassesControllerRequest

from ..adapters import route_response_adapter
from ..docs import glasses_responses
from ..factories.controllers import add_glasses_controller_factory
from ..middlewares import auth


router = APIRouter(
    tags=['Glasses'],
    prefix='/glasses'
)

@router.post(
    '/',
    responses=glasses_responses,
    status_code=status.HTTP_204_NO_CONTENT
)
def add_glasses(request: AddGlassesControllerRequest, user_id: str = Depends(auth)):
    controller = add_glasses_controller_factory()
    http_response = controller.handle(request)
    return route_response_adapter(http_response)
