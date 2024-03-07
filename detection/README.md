# 성별 및 연령 인식 모듈

* 이 코드는 OpenVINO와 OpenCV를 사용하여 얼굴 감지 및 성별 및 연령 예측을 수행합니다. 이 모듈은 두 개의 주요 클래스로 구성되어 있습니다: FaceDetection과 AgeGenderPrediction.

## FaceDetection 클래스
* FaceDetection 클래스는 얼굴 감지를 담당합니다. 이 클래스는 OpenVINO 모델을 사용하여 이미지에서 얼굴을 감지하고, 감지된 얼굴을 잘라내는 기능을 제공합니다.

### 메소드
* __init__: 모델 파일의 경로와 사용할 디바이스를 입력으로 받아 초기화합니다.
* preprocess_image: 이미지를 모델 입력에 맞게 전처리합니다.
* detect_faces: 전처리된 이미지에서 얼굴을 감지합니다.
* crop_faces: 감지된 얼굴을 이미지에서 잘라냅니다.
## AgeGenderPrediction 클래스
* AgeGenderPrediction 클래스는 성별 및 연령 예측을 담당합니다. 이 클래스는 OpenVINO 모델을 사용하여 감지된 얼굴의 성별과 연령을 예측합니다.

### 메소드
* __init__: 모델 파일의 경로와 사용할 디바이스를 입력으로 받아 초기화합니다.
* preprocess_image: 이미지를 모델 입력에 맞게 전처리합니다.
* predict_age_gender: 전처리된 이미지에서 성별과 연령을 예측합니다.
## 사용 방법
* 이 모듈을 사용하려면 먼저 FaceDetection 클래스를 사용하여 이미지에서 얼굴을 감지하고 잘라내야 합니다. 그런 다음 AgeGenderPrediction 클래스를 사용하여 각 얼굴의 성별과 연령을 예측할 수 있습니다.

'''
face_detector = FaceDetection(model_xml="path_to_face_detection_model.xml", model_bin="path_to_face_detection_model.bin")
age_gender_predictor = AgeGenderPrediction(model_xml="path_to_age_gender_model.xml", model_bin="path_to_age_gender_model.bin")

image = cv2.imread("path_to_image.jpg")
processed_image = face_detector.preprocess_image(image)
faces = face_detector.detect_faces(processed_image)

for face in faces:
    processed_face = age_gender_predictor.preprocess_image(face)
    age, gender = age_gender_predictor.predict_age_gender(processed_face)
    print(f"Detected {gender} face, age {age}")
'''
