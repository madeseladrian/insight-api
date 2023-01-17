from typing import BinaryIO, TypedDict


class UpdateImageParams(TypedDict):
    content_type: str
    glasses_id: str
    image: BinaryIO
