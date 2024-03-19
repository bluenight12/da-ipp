import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import pynput

# HandGestureMouseControl 클래스 정의


class HandGestureMouseControl:
    # 초기화 메서드
    def __init__(self, model_path):
        # pyautogui의 안전 모드를 끕니다.
        # pyautogui.FAILSAFE = False
        # MediaPipe의 손 모듈을 불러옵니다.
        self.mp_hands = mp.solutions.hands
        # MediaPipe의 그리기 유틸리티를 불러옵니다.
        self.mp_drawing = mp.solutions.drawing_utils
        self.hands = self.mp_hands.Hands(               # 손 인식 객체를 생성합니다.
            max_num_hands=1,                            # 최대 손의 개수를 1로 설정합니다.
            # 최소 탐지 신뢰도를 0.5로 설정합니다.
            min_detection_confidence=0.5,
            # 최소 추적 신뢰도를 0.5로 설정합니다.
            min_tracking_confidence=0.5
        )
        self.BaseOptions = mp.tasks.BaseOptions
        self.GestureRecognizer = mp.tasks.vision.GestureRecognizer
        self.GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
        self.VisionRunningMode = mp.tasks.vision.RunningMode
        self.count = 0
        self.frame_count = 0
        self.click_count = 0
        self.options = self.GestureRecognizerOptions(
            base_options=self.BaseOptions(model_asset_path=model_path),
            running_mode=self.VisionRunningMode.IMAGE)
        self.recognizer = self.GestureRecognizer.create_from_options(
            self.options)
        self.mouse_drag = pynput.mouse.Controller()
        self.mouse_button = pynput.mouse.Button
    # 마우스 제어 메서드
    def control_mouse(self, result: mp.tasks.vision.GestureRecognizerResult, output_image: mp.Image):
        click = False
        

        for gesture in result.gestures:                         # 각 제스처에 대해
            #print(gesture)
            if 'Closed_Fist' in str(gesture) and self.click_count == 0:                   # 만약 제스처가 'Closed_Fist'라면 클릭을 True로 설정합니다.
                print("click")
                click = True

        for landmarks in result.hand_landmarks:                 # 각 랜드마크에 대해
            landmark = landmarks[5]                             # 5번째 랜드마크(검지 손가락 맨밑마디)를 가져옵니다.
            print(landmark)
            x = landmark.x                                      # 각 x,y 좌표를 가져옵니다.
            y = landmark.y
            if (x != 0) and (y != 0) and self.count == 0:       # 만약 x와 y가 0이 아니고 count가 0이라면
                if click and self.click_count == 0:                                       # 만약 클릭이 True라면 
                    self.mouse_drag.press(self.mouse_button.left)           # 해당 위치에서 클릭합니다.                                                                         
                    self.click_count += 1
                    self.mouse_drag.release(self.mouse_button.left)
                else: 
                    self.mouse_drag.position=(int(1440*x), int(2480*y))  # 마우스를 해당 위치로 이동합니다.

        if self.click_count !=0:
            self.click_count = (self.click_count+1)% 30
   
    # 실행 메서드
    def run(self, image):
        img = cv2.flip(image, 1)                                                # 이미지를 좌우 반전합니다.
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)                          # 이미지의 색상 공간을 BGR에서 RGB로 변환합니다.
        mp_image = mp.Image(                                                    # MediaPipe Image 객체를 생성합니다.
            image_format=mp.ImageFormat.SRGB, data=img_rgb)

        if self.frame_count == 0:                                               # 만약 frame_count가 0이라면
            gesture_recognition_result = self.recognizer.recognize(mp_image)    # 제스처 인식 결과를 가져옵니다.
            self.control_mouse(gesture_recognition_result, mp_image)            # 마우스 제어 메서드를 호출합니다.
        # self.frame_count = (self.frame_count+1) % 3                             # frame_count를 1 증가시키고 3으로 나눈 나머지를 저장합니다.

        # 만약 화면 크기에 맞춰서 조정하라면 img값을 리턴받아서 화면에 출력하도록함
        # img = cv2.resize(img, (1680, 1050))
        # return img


# 사용예제
model_path = 'model/gesture_recognizer.task'        # 모델 경로를 설정합니다.
a = HandGestureMouseControl(model_path)             # HandGestureMouseControl 객체를 생성합니다.

cap = cv2.VideoCapture(0)                           # 카메라를 엽니다.


while True:

    ret, image = cap.read()                         # 카메라에서 이미지를 읽어옵니다.
    a.run(image)
    cv2.imshow('MediaPipe Hands', image)            # 이미지를 화면에 표시합니다.
    # cv2.namedWindow("a")

    if cv2.waitKey(1) & 0xFF == ord('q'):           # 만약 'q' 키가 눌리면 루프를 종료합니다.
        break

cap.release()                                       # 카메라를 해제합니다.
cv2.destroyAllWindows()                             # 모든 창을 닫습니다.
