# Hand Gesture Mouse Control

이 파이썬 스크립트는 MediaPipe와 pyautogui를 사용하여 웹캠 피드에서 손동작을 감지하고, 이를 사용하여 마우스를 제어합니다.

## 필요한 라이브러리

- cv2
- mediapipe
- pynput

pip를 사용하여 설치할 수 있습니다:
```
pip install opencv-python
pip install mediapipe
pip install pynput
```

## 사용법

* 먼저, 모델 경로를 사용하여 HandGestureMouseControl 클래스를 초기화합니다:
```
hand_detector = HandGestureMouseControl(model_path='model_path')
```
* 그런 다음, 웹캠 피드를 시작하고 손동작 감지를 수행합니다:
```
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("입력이 없습니다.")
        break

    hand_detector.run(frame)

    cv2.imshow('Webcam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```
이렇게 하면 감지된 손동작에 따라 마우스가 제어되며, 웹캠 피드가 창에 표시됩니다. 'q’를 누르면 스크립트가 중지됩니다.

## 참고 자료
* MediaPipe Hands
	* https://developers.google.com/mediapipe/solutions/vision/gesture_recognizer/python#live-stream_1
	* https://developers.google.com/mediapipe/solutions/vision/gesture_recognizer/index#models


## 주의사항
* 이 코드는 웹캠이 필요합니다. 웹캠이 연결되어 있지 않거나 다른 프로그램에서 사용 중인 경우, 코드가 제대로 작동하지 않을 수 있습니다.

