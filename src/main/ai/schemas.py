from pydantic import BaseModel


class Age(BaseModel):
    age: int

    class Config:
        orm_mode = True

class Gender(BaseModel):
    gender: str

    class Config:
        orm_mode = True

class Shape(BaseModel):
    shape: str

    class Config:
        orm_mode = True

class LeftEye(BaseModel):
    left_eye: float

    class Config:
        orm_mode = True

class LeftIris(BaseModel):
    left_eye: float

    class Config:
        orm_mode = True

class LeftEyebrownHeight(BaseModel):
    left_eyebrown_height: float

    class Config:
        orm_mode = True

class LeftEyebrownThickness(BaseModel):
    left_eyebrown_thickness: float

    class Config:
        orm_mode = True

class RightEye(BaseModel):
    right_eye: float

    class Config:
        orm_mode = True

class RightIris(BaseModel):
    right_iris: float

    class Config:
        orm_mode = True

class RightEyebrownHeight(BaseModel):
    right_eyebrown_height: float

    class Config:
        orm_mode = True

class RightEyebrownThickness(BaseModel):
    right_eyebrown_thickness: float

    class Config:
        orm_mode = True

class BetweenEyebrowns(BaseModel):
    between_eyebrowns: float

    class Config:
        orm_mode = True

class NoseHeight(BaseModel):
    nose_height: float

    class Config:
        orm_mode = True

class NoseWidth(BaseModel):
    nose_width: float

    class Config:
        orm_mode = True

class BetweenNoseMouth(BaseModel):
    between_nose_mouth: float

    class Config:
        orm_mode = True

class MouthWidth(BaseModel):
    mouth_width: float

    class Config:
        orm_mode = True

class UpperLipThickness(BaseModel):
    upper_lip_thickness: float

    class Config:
        orm_mode = True

class LowerLipThickness(BaseModel):
    lower_lip_thickness: float

    class Config:
        orm_mode = True

class BetweenMouthChin(BaseModel):
    between_mouth_chin: float

    class Config:
        orm_mode = True

class PupillaryDistance(BaseModel):
    pupillary_distance: float

    class Config:
        orm_mode = True
