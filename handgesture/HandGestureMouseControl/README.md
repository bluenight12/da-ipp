# Hand Gesture Mouse Control

이 프로젝트는 웹캠을 통해 손동작을 인식하고, 그에 따라 마우스를 제어하는 기능을 제공합니다.

## 필요한 라이브러리

- cv2
- numpy
- time
- mediapipe
- pyautogui

## 사용법

1. 먼저, `model/gesture_recognizer.task`와 같은 경로에 손동작 인식 모델을 저장해야 합니다.
2. 다음으로, `HandGestureMouseControl` 클래스의 인스턴스를 생성합니다. 이때, 인식 모델의 경로를 매개변수로 전달해야 합니다.
3. 마지막으로, `run` 메서드를 호출하여 손동작 인식을 시작합니다.

```python
from hand_gesture_mouse_control import HandGestureMouseControl

model_path = 'model/gesture_recognizer.task'
controller = HandGestureMouseControl(model_path)
controller.run()
```
## 참고 자료
* MediaPipe Hands
	* https://developers.google.com/mediapipe/solutions/vision/gesture_recognizer/python#live-stream_1
	* https://developers.google.com/mediapipe/solutions/vision/gesture_recognizer/index#models
* PyAutoGUI
	* https://pyautogui.readthedocs.io/en/latest/mouse.html

## 주의사항
* 이 코드는 웹캠이 필요합니다. 웹캠이 연결되어 있지 않거나 다른 프로그램에서 사용 중인 경우, 코드가 제대로 작동하지 않을 수 있습니다.
* pyautogui 라이브러리는 GUI 자동화를 위한 것으로, 마우스와 키보드를 제어합니다. 따라서 이 코드를 실행할 때는 컴퓨터가 마우스와 키보드 입력을 받을 수 있는 상태여야 합니다.
