from fastapi import APIRouter, Depends, status, UploadFile
import uuid

from ...presentation.params import (
    AddImageControllerRequest,
    UpdateImageControllerRequest
)
from ..adapters import route_response_adapter
from ..docs import glasses_responses
from ..factories.controllers import (
    add_image_controller_factory,
    update_image_controller_factory
)
from ..models import ImageResponseModel
from ..middlewares import auth


router = APIRouter(
    tags=['Image'],
    prefix='/image'
)

@router.post(
    '/',
    responses=glasses_responses,
    status_code=status.HTTP_200_OK,
    response_model=ImageResponseModel
)
def add_image(image: UploadFile, user_id: str = Depends(auth)):
    controller = add_image_controller_factory()
    http_response = controller.handle(AddImageControllerRequest(
        image=image.file,
        glasses_id=str(uuid.uuid4()),
        content_type=image.content_type
    ))
    adapter = route_response_adapter(http_response)
    body = adapter.get('body')
    return {**body, 'token_type': 'bearer'}


@router.put(
    '/',
    responses=glasses_responses,
    status_code=status.HTTP_204_NO_CONTENT
)
def update_image(glasses_id: str, image: UploadFile, user_id: str = Depends(auth)):
    controller = update_image_controller_factory()
    http_response = controller.handle(UpdateImageControllerRequest(
        image=image.file,
        glasses_id=glasses_id,
        content_type=image.content_type
    ))
    route_response_adapter(http_response)
