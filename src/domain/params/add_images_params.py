from typing import BinaryIO, TypedDict


class AddImagesParams(TypedDict):
    image: BinaryIO
    glasses_id: str
