import base64
from fastapi import APIRouter, Depends, File, status
from google.cloud import vision
import numpy as np
import os

from ..middlewares import auth
from .schemas import (
    BetweenEyebrowns,
    BetweenMouthChin,
    BetweenNoseMouth,
    Gender,
    LeftEye,
    LeftEyebrownHeight,
    LeftEyebrownThickness,
    LeftIris,
    LowerLipThickness,
    RightEye,
    RightIris,
    RightEyebrownHeight,
    RightEyebrownThickness,
    NoseHeight,
    NoseWidth,
    MouthWidth,
    PupillaryDistance,
    Shape,
    UpperLipThickness
)
from .ai_predictions import (
    convert_bytes_to_opencv,
    convert_to_bytes,
    distance_between_landmark_points_x,
    distance_between_landmark_points_y,
    distance_between_points,
    feature,
    location_eyes,
    number_of_faces,
    predict_json
)

router = APIRouter(
  prefix="/face",
  tags=['Face']
)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'google_vision_credentials.json'

# Projects
project = 'insight-api-374021'

# Region
region = 'us-central1'

# Versions
version_v1 = 'v1'

# Face Annotations - Google Cloud
client = vision.ImageAnnotatorClient()


@router.post("/gender", status_code=status.HTTP_201_CREATED, response_model=Gender)
def gender(image: bytes = File(), user_id: str = Depends(auth)):
    # Transforming 'bytes' to OpenCV format
    image_cv = convert_bytes_to_opencv(image)

    # Get the face annotations
    google_vision = vision.Image(content=image)
    response = client.face_detection(image=google_vision)

    # Number of faces annotations
    faceAnnotation = response.face_annotations

    # Points
    points = faceAnnotation[0].bounding_poly.vertices

    # Image resized
    image_resized = image_cv[points[0].y:points[2].y, points[0].x:points[2].x]
    image = convert_to_bytes(image_resized)

    request_data = [{'image_bytes': {'b64': base64.b64encode(image).decode()}, 'key': ''}]

    # Response model
    model_name = 'gender'
    gender = predict_json(project, region, model_name, request_data, version_v1)

    # Gender Predictions
    labels = ['F', 'M']
    predictions_gender = labels[np.argmax(gender[0]['scores'])]

    return {'gender': predictions_gender}

@router.post("/shape", status_code=status.HTTP_201_CREATED, response_model=Shape)
def shape(image: bytes = File(), user_id: str = Depends(auth)):
    image_cv = convert_bytes_to_opencv(image)

    # Get the face annotations
    google_vision = vision.Image(content=image)
    response = client.face_detection(image=google_vision)

    # Number of faces annotations
    faceAnnotation = response.face_annotations

    # Points
    points = faceAnnotation[0].bounding_poly.vertices

    # Image resized
    image_resized = image_cv[points[0].y:points[2].y, points[0].x:points[2].x]
    image = convert_to_bytes(image_resized)

    request_data = [{'image_bytes': {'b64': base64.b64encode(image).decode()}, 'key': ''}]

    # Response model
    model_name = 'shape'
    shape = predict_json(project, region, model_name, request_data, version_v1)

    # Shape Predictions
    labels = shape[0]['labels']
    predictions_shape = labels[np.argmax(shape[0]['scores'])]

    return {'shape': predictions_shape}

@router.post("/leftEye", status_code=status.HTTP_201_CREATED, response_model=LeftEye)
def left_eye(image: bytes = File(), user_id: str = Depends(auth)):
    faces = number_of_faces(image)

    left_eye = distance_between_landmark_points_x(
        point1=33, point2=133, image=image
    )

    return feature(faces=faces, name_feature='left_eye', feature=left_eye)

@router.post("/leftIris", status_code=status.HTTP_201_CREATED, response_model=LeftIris)
def left_iris(image: bytes = File(), user_id: str = Depends(auth)):
    faces = number_of_faces(image)

    left_iris = 11.7

    return feature(faces=faces, name_feature='left_iris', feature=left_iris)

@router.post("/leftEyebrowHeight", status_code=status.HTTP_201_CREATED, response_model=LeftEyebrownHeight)
def left_eyebrown_height(image: bytes = File(), user_id: str = Depends(auth)):
    faces = number_of_faces(image)

    left_eyebrown_height = distance_between_landmark_points_y(
        point1=222, point2=65, image=image
    )

    return feature(faces=faces, name_feature='left_eyebrown_height', feature=left_eyebrown_height)

@router.post("/leftEyebrowThickness", status_code=status.HTTP_201_CREATED, response_model=LeftEyebrownThickness)
def left_eyebrown_thickness(image: bytes = File(), user_id: str = Depends(auth)):
    faces = number_of_faces(image)

    left_eyebrown_thickness = distance_between_landmark_points_y(
        point1=65, point2=66, image=image
    )

    return feature(faces=faces, name_feature='left_eyebrown_thickness', feature=left_eyebrown_thickness)

@router.post("/rightEye", status_code=status.HTTP_201_CREATED, response_model=RightEye)
def right_eye(image: bytes = File(), user_id: str = Depends(auth)):
    faces = number_of_faces(image)

    right_eye = distance_between_landmark_points_x(
        point1=362, point2=263, image=image
    )

    return feature(faces=faces, name_feature='right_eye', feature=right_eye)

@router.post("/rightIris", status_code=status.HTTP_201_CREATED, response_model=RightIris)
def right_iris(image: bytes = File(), user_id: str = Depends(auth)):
    faces = number_of_faces(image)

    right_iris = 11.7

    return feature(faces=faces, name_feature='right_iris', feature=right_iris)

@router.post("/rightEyebrownHeight", status_code=status.HTTP_201_CREATED, response_model=RightEyebrownHeight)
def right_eyebrown_height(image: bytes = File(), user_id: str = Depends(auth)):
    faces = number_of_faces(image)

    right_eyebrown_height = distance_between_landmark_points_y(
        point1=258, point2=295, image=image
    )

    return feature(faces=faces, name_feature='right_eyebrown_height', feature=right_eyebrown_height)

@router.post("/rightEyebrownThickness", status_code=status.HTTP_201_CREATED, response_model=RightEyebrownThickness)
def right_eyebrown_thickness(image: bytes = File(), user_id: str = Depends(auth)):
    faces = number_of_faces(image)

    right_eyebrown_thickness = distance_between_landmark_points_y(
        point1=295, point2=296, image=image
    )

    return feature(faces=faces, name_feature='right_eyebrown_thickness', feature=right_eyebrown_thickness)

@router.post("/betweenEyebrowns", status_code=status.HTTP_201_CREATED, response_model=BetweenEyebrowns)
def between_eyebrowns(image: bytes = File(), user_id: str = Depends(auth)):
    faces = number_of_faces(image)

    between_eyebrowns = distance_between_landmark_points_x(
        point1=55, point2=285, image=image
    )

    return feature(faces=faces, name_feature='between_eyebrowns', feature=between_eyebrowns)

@router.post("/noseHeight", status_code=status.HTTP_201_CREATED, response_model=NoseHeight)
def nose_height(image: bytes = File(), user_id: str = Depends(auth)):
    faces = number_of_faces(image)

    nose_height = distance_between_landmark_points_y(
        point1=168, point2=2, image=image
    )

    return feature(faces=faces, name_feature='nose_height', feature=nose_height)

@router.post("/noseWidth", status_code=status.HTTP_201_CREATED, response_model=NoseWidth)
def nose_width(image: bytes = File(), user_id: str = Depends(auth)):
    faces = number_of_faces(image)

    nose_width = distance_between_landmark_points_x(
        point1=115, point2=344, image=image
    )

    return feature(faces=faces, name_feature='nose_width', feature=nose_width)

@router.post("/betweenNoseMouth", status_code=status.HTTP_201_CREATED, response_model=BetweenNoseMouth)
def between_nose_mouth(image: bytes = File(), user_id: str = Depends(auth)):
    faces = number_of_faces(image)

    between_nose_mouth = distance_between_landmark_points_y(
        point1=2, point2=0, image=image
    )

    return feature(faces=faces, name_feature='between_nose_mouth', feature=between_nose_mouth)

@router.post("/mouthWidth", status_code=status.HTTP_201_CREATED, response_model=MouthWidth)
def mouth_width(image: bytes = File(), user_id: str = Depends(auth)):
    faces = number_of_faces(image)

    mouth_width = distance_between_landmark_points_x(
        point1=61, point2=291, image=image
    )

    return feature(faces=faces, name_feature='mouth_width', feature=mouth_width)

@router.post("/upperlipThickness", status_code=status.HTTP_201_CREATED, response_model=UpperLipThickness)
def upper_lip_thickness(image: bytes = File(), user_id: str = Depends(auth)):
    faces = number_of_faces(image)

    upper_lip_thickness = distance_between_landmark_points_y(
        point1=0, point2=13, image=image
    )

    return feature(faces=faces, name_feature='upper_lip_thickness', feature=upper_lip_thickness)

@router.post("/lowerlipThickness", status_code=status.HTTP_201_CREATED, response_model=LowerLipThickness)
def lower_lip_thickness(image: bytes = File(), user_id: str = Depends(auth)):
    faces = number_of_faces(image)

    lower_lip_thickness = distance_between_landmark_points_y(
        point1=14, point2=17, image=image
    )

    return feature(faces=faces, name_feature='lower_lip_thickness', feature=lower_lip_thickness)

@router.post("/betweenMouthChin", status_code=status.HTTP_201_CREATED, response_model=BetweenMouthChin)
def between_mouth_chin(image: bytes = File(), user_id: str = Depends(auth)):
    faces = number_of_faces(image)

    between_mouth_chin = distance_between_landmark_points_y(
        point1=17, point2=152, image=image
    )

    return feature(faces=faces, name_feature='between_mouth_chin', feature=between_mouth_chin)

@router.post("/pupillaryDistance", status_code=status.HTTP_201_CREATED, response_model=PupillaryDistance)
def pupillary_distance(image: bytes = File(), user_id: str = Depends(auth)):
    faces = number_of_faces(image)

    center_left, center_right = location_eyes(image)
    pupillary_distance = distance_between_points(
        point1=center_left, point2=center_right, image=image
    )

    return feature(faces=faces, name_feature='pupillary_distance', feature=pupillary_distance)
