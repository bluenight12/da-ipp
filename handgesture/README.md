# 손동작 인식을 이용한 마우스 컨트롤
이 프로젝트는 MediaPipe와 OpenCV를 사용하여 웹캠에서 손동작을 인식하고, 인식된 손동작을 이용하여 마우스를 제어하는 Python 코드입니다.

## 필요한 라이브러리
OpenCV
MediaPipe
PyAutoGUI
time
## 설치 방법
```
pip install opencv-python
pip install mediapipe
pip install pyautogui
```

## 사용 방법
* Python 파일을 실행합니다.
* 웹캠이 켜지면, 손을 웹캠 앞에 가져다 놓습니다.
* 인식된 손의 동작에 따라 마우스가 제어됩니다.
## 코드 설명
* pyautogui.FAILSAFE = False: PyAutoGUI의 Failsafe 모드를 비활성화합니다. Failsafe 모드가 활성화된 경우, 마우스를 화면의 모서리로 이동시키면 PyAutoGUI의 함수가 예외를 발생시킵니다.
* mp_hands.Hands(...): MediaPipe Hands 모델을 초기화합니다. max_num_hands는 감지할 수 있는 최대 손의 수를, min_detection_confidence와 min_tracking_confidence는 감지 및 추적의 최소 신뢰도를 설정합니다.
* cv2.VideoCapture(0): 웹캠을 사용하여 비디오 캡처를 시작합니다.
* while True: ...: 웹캠에서 프레임을 계속 읽어옵니다. 각 프레임에서 손동작을 인식하고, 인식된 손동작을 이용하여 마우스를 제어합니다.
* cv2.imshow('MediaPipe Hands', img): 인식된 손동작과 함께 이미지를 화면에 표시합니다.
* if cv2.waitKey(1) & 0xFF == ord('q'): break: ‘q’ 키를 누르면 루프에서 빠져나옵니다.
* cap.release(), cv2.destroyAllWindows(): 모든 리소스를 해제하고 창을 닫습니다.
## 주의 사항
* 웹캠이 필요합니다.
* 손동작 인식은 조명, 배경, 손의 위치 등에 따라 정확도가 달라질 수 있습니다.
* 손동작 인식이 잘 되지 않는 경우, 웹캠의 위치를 조정하거나 다른 조명을 시도해 보세요.
* 이 코드는 기본적인 손동작 인식과 마우스 제어를 구현한 것이며, 실제 응용 프로그램에서는 추가적인 처리가 필요할 수 있습니다. 예를 들어, 인식된 손동작에 따라 특정 작업을 수행하도록 코드를 확장할 수 있습니다. 또한, MediaPipe는 사용자 정의 손동작 인식기를 만들 수 있는 기능도 제공하므로, 필요에 따라 자신만의 손동작 인식 모델을 학습시킬 수도 있습니다.
## 참고 자료
* MediaPipe Hands
* OpenCV
* PyAutoGUI
