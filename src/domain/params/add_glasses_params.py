from typing import TypedDict


class AddGlassesParams(TypedDict):
    user_id: str
    glasses_id: str
    uid_image: str
    model: str
    format: str
    gender: str
    public: str
    category: str
    frame_color: str
    lens_color: str
    size_lens: float
    size_bridge: float
    height_frame: float
    size_temples: float
    price: float
    additional_info: str

AddGlassesResult = bool
