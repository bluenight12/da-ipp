# 성별 및 연령 인식 모듈

* 이 코드는 OpenVINO와 OpenCV를 사용하여 얼굴 감지 및 성별 및 연령 예측을 수행합니다. 이 모듈은 두 개의 주요 클래스로 구성되어 있습니다: FaceDetection과 AgeGenderPrediction.

## FaceDetection 클래스
* FaceDetection 클래스는 얼굴 감지를 담당합니다. 이 클래스는 OpenVINO 모델을 사용하여 이미지에서 얼굴을 감지하고, 감지된 얼굴을 잘라내는 기능을 제공합니다.

### 메소드
* __init__: 이 메소드는 클래스의 인스턴스를 초기화합니다. 모델 파일의 경로와 사용할 디바이스를 입력으로 받아, 해당 모델을 로드하고 컴파일합니다.
* preprocess_image: 이 메소드는 입력 이미지를 모델이 처리할 수 있는 형태로 전처리합니다. 이미지를 모델의 입력 크기에 맞게 크기를 조정합니다.
* detect_faces: 이 메소드는 전처리된 이미지에서 얼굴을 감지합니다. 감지된 얼굴의 위치 정보를 반환합니다.
* crop_faces: 이 메소드는 감지된 얼굴을 이미지에서 잘라내어 반환합니다. 감지된 얼굴의 위치 정보를 사용하여 원본 이미지에서 얼굴 부분을 잘라냅니다.
* run: 이 메소드는 이미지를 입력으로 받아, 감지된 얼굴 이미지들을 반환합니다. 입력 이미지를 전처리하고, 얼굴을 감지한 후, 감지된 얼굴을 잘라내어 반환합니다.

## AgeGenderPrediction 클래스
* AgeGenderPrediction 클래스는 성별 및 연령 예측을 담당합니다. 이 클래스는 OpenVINO 모델을 사용하여 감지된 얼굴의 성별과 연령을 예측합니다.

### 메소드
* __init__:  이 메소드는 클래스의 인스턴스를 초기화합니다. 모델 파일의 경로와 사용할 디바이스를 입력으로 받아, 해당 모델을 로드하고 컴파일합니다.
* preprocess_image: 이 메소드는 입력 이미지를 모델이 처리할 수 있는 형태로 전처리합니다. 이미지를 모델의 입력 크기에 맞게 크기를 조정하고, 필요한 경우 색상 공간을 변환합니다.
* predict_age_gender: 이 메소드는 전처리된 이미지에서 성별과 연령을 예측합니다. 예측된 성별과 연령 정보를 반환합니다.
* run: 이 메소드는 감지된 얼굴 이미지들을 받아 각각의 연령과 성별을 예측합니다. 각 얼굴 이미지를 전처리하고, 연령과 성별을 예측하여 리스트에 추가합니다. 최종적으로 연령과 성별 정보를 담은 두 개의 리스트를 반환합니다.

## 사용 방법
* 이 모듈을 사용하려면 먼저 FaceDetection 클래스를 사용하여 이미지에서 얼굴을 감지하고 잘라내야 합니다. 그런 다음 AgeGenderPrediction 클래스를 사용하여 각 얼굴의 성별과 연령을 예측할 수 있습니다.

```
face_detector = FaceDetection(model_xml="path_to_face_detection_model.xml", model_bin="path_to_face_detection_model.bin")
age_gender_predictor = AgeGenderPrediction(model_xml="path_to_age_gender_model.xml", model_bin="path_to_age_gender_model.bin")

image = cv2.imread("path_to_image.jpg")
faces = face_detector.run(image)
ages, genders = age_gender_predictor.run(faces)
print(ages)
print(genders)

```

## 참고자료

* 사용 모델
	* https://github.com/openvinotoolkit/open_model_zoo/tree/master/models/intel/age-gender-recognition-retail-0013
	* https://github.com/openvinotoolkit/open_model_zoo/tree/master/models/intel/face-detection-retail-0005
* OPENVINO: https://docs.openvino.ai/2023.3/documentation.html

