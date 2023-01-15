from pydantic import BaseModel


class ImageResponseModel(BaseModel):
    glasses_id: str
    url_image: str
