from typing import TypedDict


class AddGlassesParams(TypedDict):
    uidImage: str
    model: str
    format: str
    gender: str
    public: str
    category: str
    frameColor: str
    lensColor: str
    sizeLens: float
    sizeBridge: float
    heightFrame: float
    sizeTemples: float
    price: float
    additionalInfo: str

AddGlassesResult = bool
