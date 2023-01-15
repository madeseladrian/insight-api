from typing import BinaryIO, TypedDict


class AddImageParams(TypedDict):
    content_type: str
    glasses_id: str
    image: BinaryIO

class AddImageResult(TypedDict):
    glasses_id: str
    url_image: str
