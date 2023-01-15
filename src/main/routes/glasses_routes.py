from fastapi import APIRouter, Depends, status

# from ...presentation.params import AddGlassesControllerRequest

from ..adapters import route_response_adapter
from ..docs import glasses_responses
from ..factories.controllers import add_glasses_controller_factory
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
    # http_response = controller.handle(AddGlassesControllerRequest(
    #     url_image=request['url_image'],
    #     glasses_id=request['glasses_id'],
    #     user_id='token',
    #     model=request['model'],
    #     format=request['format'],
    #     gender=request['gender'],
    #     public=request['public'],
    #     category=request['category'],
    #     frame_color=request['frame_color'],
    #     lens_color=request['lens_color'],
    #     size_lens=request['size_lens'],
    #     size_bridge=request['size_bridge'],
    #     height_frame=request['height_frame'],
    #     size_temples=request['size_temples'],
    #     price=request['price'],
    #     additional_info=request['additional_info']
    # ))
    return route_response_adapter(http_response)
