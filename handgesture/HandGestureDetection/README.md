# OpenVINO를 이용한 손동작 감지
이 파이썬 스크립트는 OpenVINO 툴킷을 사용하여 웹캠 피드에서 손동작 감지를 수행합니다.

## 의존성
스크립트는 다음 라이브러리를 필요로 합니다:

* OpenVINO
* OpenCV
* NumPy
* ipywidgets

pip를 사용하여 설치할 수 있습니다:
```
pip install openvino
pip install opencv-python
pip install numpy
pip install ipywidgets
```

## 사용법

* 먼저, 모델 XML과 BIN 파일의 경로를 사용하여 HandDetection 클래스를 초기화합니다:

### Python
```
hand_detector = HandDetection(model_xml='model/model.xml', model_bin='model/model.bin')
```
* 그런다음 그런 다음, 웹캠 피드를 시작하고 손동작 감지를 수행합니다:
```
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("입력이 없습니다.")
        break

    label, confidence = hand_detector.run(frame)
    if confidence > 50:
        print(label, confidence)

    cv2.imshow('Webcam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

```
* 이렇게 하면 감지된 손동작과 그 신뢰도 수준이 계속해서 콘솔에 출력되며, 웹캠 피드가 창에 표시됩니다. 'q’를 누르면 스크립트가 중지됩니다.

# 참고

* HandDetection 클래스는 사전 훈련된 모델을 사용하여 손동작을 감지합니다. 모델은 OpenVINO와 호환되어야 하며 손동작을 감지할 수 있어야 합니다. 모델의 입력은 이미지이며, 출력은 감지된 객체의 경계 상자와 레이블이어야 합니다.

