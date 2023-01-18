import cv2
from cvzone.FaceMeshModule import FaceMeshDetector
from fastapi import HTTPException, status
from google.api_core.client_options import ClientOptions
import googleapiclient.discovery
import mediapipe as mp
import numpy as np


# Make predictions of the models in AI Platform
def predict_json(project, region, model, instances, version=None):
    """Send json data to a deployed model for prediction.

    Args:
        project (str): project where the Cloud ML Engine Model is deployed.
        region (str): regional endpoint to use; set to None for ml.googleapis.com
        model (str): model name.
        instances ([Mapping[str: Any]]): Keys should be the names of Tensors
            your deployed model expects as inputs. Values should be datatypes
            convertible to Tensors, or (potentially nested) lists of datatypes
            convertible to tensors.
        version: str, version of the model to target.
    Returns:
        Mapping[str: any]: dictionary of prediction results defined by the
            model.
    """
    # Create the ML Engine service object.
    # To authenticate set the environment variable
    # GOOGLE_APPLICATION_CREDENTIALS=<path_to_service_account_file>
    prefix = "{}-ml".format(region) if region else "ml"
    api_endpoint = "https://{}.googleapis.com".format(prefix)
    client_options = ClientOptions(api_endpoint=api_endpoint)
    service = googleapiclient.discovery.build(
        'ml', 'v1', client_options=client_options)
    name = 'projects/{}/models/{}'.format(project, model)

    if version is not None:
        name += '/versions/{}'.format(version)

    response = service.projects().predict(
        name=name,
        body={'instances': instances}
    ).execute()

    if 'error' in response:
        raise RuntimeError(response['error'])

    return response['predictions']

def convert_bytes_to_opencv(image: bytes):
    # Transforming 'bytes' in 'array'
    image_array = np.frombuffer(image, dtype=np.uint8)

    # Convert the image to OpenCV format
    return cv2.imdecode(image_array, -1)

def convert_to_bytes(image):
    _, encoded_image = cv2.imencode('.jpg', image)
    return encoded_image.tobytes()

def number_of_faces(image: bytes):
    image = convert_bytes_to_opencv(image)

    # Detector
    detector = FaceMeshDetector(maxFaces=10)
    _, faces = detector.findFaceMesh(image, draw=False)

    number_of_faces = len(faces)

    return number_of_faces

def mesh_points_image(image):
    # Face Mesh
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh(
        max_num_faces=1,
        refine_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    )

    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Facial landmarks
    result = face_mesh.process(rgb_image)

    if result.multi_face_landmarks:
        mesh_points = [
            np.multiply(
                [p.x, p.y],
                [image.shape[1], image.shape[0]]
            ).astype(int) for p in result.multi_face_landmarks[0].landmark
        ]
        mesh_points = np.array(mesh_points)
        return mesh_points

def radius_eyes(image):
    # Left Iris
    left_iris = [474, 475, 476, 477]
    # Right Iris
    right_iris = [469, 470, 471, 472]

    mesh_points = mesh_points_image(image)
    mesh_points = np.array(mesh_points)

    _, left_radius = cv2.minEnclosingCircle(mesh_points[left_iris])
    _, right_radius = cv2.minEnclosingCircle(mesh_points[right_iris])

    return left_radius, right_radius

def location_eyes(image: bytes):
    image = convert_bytes_to_opencv(image)

    # Left Iris
    left_iris = [474, 475, 476, 477]
    # Right Iris
    right_iris = [469, 470, 471, 472]

    mesh_points = mesh_points_image(image)
    mesh_points = np.array(mesh_points)

    (l_cx, l_cy), _ = cv2.minEnclosingCircle(mesh_points[left_iris])
    (r_cx, r_cy), _ = cv2.minEnclosingCircle(mesh_points[right_iris])

    center_left = np.array([l_cx, l_cy], dtype=np.int32).tolist()
    center_right = np.array([r_cx, r_cy], dtype=np.int32).tolist()

    return center_left, center_right

def distance_between_landmark_points_x(point1, point2, image: bytes):
    image = convert_bytes_to_opencv(image)

    # Eye Radius Factor
    left_radius, right_radius = radius_eyes(image)

    # detector
    detector = FaceMeshDetector(maxFaces=1)
    image, faces = detector.findFaceMesh(image, draw=False)

    if faces:
        face = faces[0]
        face[point1][1] = face[point2][1]

        pointLeft = tuple(face[point1])
        pointRight = tuple(face[point2])

        # Calculate the line segment distance between two points w, Equivalent to finding the distance by Pythagorean theorem
        w, _ = detector.findDistance(pointRight, pointLeft)  # Return line segment distance and line segment information ( Coordinates of two end points and midpoint )

        correction_factor = 0.57
        real_distance = (w * 23.4) / (left_radius + right_radius)
        real_distance = round(real_distance * correction_factor, 1)

        return real_distance

def distance_between_landmark_points_y(point1, point2, image: bytes):
    image = convert_bytes_to_opencv(image)

    # Eye Radius Factor
    left_radius, right_radius = radius_eyes(image)

    # detector
    detector = FaceMeshDetector(maxFaces=1)
    image, faces = detector.findFaceMesh(image, draw=False)

    if faces:
        face = faces[0]
        face[point1][0] = face[point2][0]

        pointLeft = tuple(face[point1])
        pointRight = tuple(face[point2])

        # Calculate the line segment distance between two points w, Equivalent to finding the distance by Pythagorean theorem
        w, _ = detector.findDistance(pointRight, pointLeft)  # Return line segment distance and line segment information ( Coordinates of two end points and midpoint )

        correction_factor = 0.57
        real_distance = (w * 23.4) / (left_radius + right_radius)
        real_distance = round(real_distance * correction_factor, 1)

        return real_distance

def distance_between_points(point1, point2, image: bytes):
    image = convert_bytes_to_opencv(image)

    # Eye Radius Factor
    left_radius, right_radius = radius_eyes(image)

    # Detector
    detector = FaceMeshDetector(maxFaces=1)
    image, faces = detector.findFaceMesh(image, draw=False)

    if faces:
        pointLeft = tuple(point1)
        pointRight = tuple(point2)

        # Calculate the line segment distance between two points w, Equivalent to finding the distance by Pythagorean theorem
        w, _ = detector.findDistance(pointRight, pointLeft)  # Return line segment distance and line segment information ( Coordinates of two end points and midpoint )

        correction_factor = 0.55
        real_distance = (w * 23.4) / (left_radius + right_radius)
        real_distance = round(real_distance * correction_factor, 1)

        return real_distance

def feature(faces, name_feature: str, feature):
    if faces == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Face not found"
        )

    elif faces == 1:
        return {name_feature: feature}

    elif faces > 1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Many faces found"
        )

    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Internal Server Error"
    )
