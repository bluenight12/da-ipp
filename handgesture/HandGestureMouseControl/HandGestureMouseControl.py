import cv2
import numpy as np
import time
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import pyautogui



class HandGestureMouseControl:
    def __init__(self, model_path):
        pyautogui.FAILSAFE = False
        # MediaPipe Hands model setup
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils  # Drawing helpers
        # Hand landmark extraction object creation
        self.hands = self.mp_hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self.BaseOptions = mp.tasks.BaseOptions
        self.GestureRecognizer = mp.tasks.vision.GestureRecognizer
        self.GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
        #self.GestureRecognizerResult = mp.tasks.vision.GestureRecognizerResult
        self.VisionRunningMode = mp.tasks.vision.RunningMode
        self.count = 0

        self.options = self.GestureRecognizerOptions(
            base_options=self.BaseOptions(model_asset_path=model_path),
            running_mode=self.VisionRunningMode.LIVE_STREAM,
            result_callback=self.control_mouse)

    def control_mouse(self, result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
        click = False
        for gesture in result.gestures:
            # print(gesture)
            if 'Victory' in str(gesture):
                print("click")
                click = True
            if 'Pointing_Up' in str(gesture) and self.count == 0:
                print("move")

        for landmarks in result.hand_landmarks:
            landmark = landmarks[8]
            x = landmark.x
            y = landmark.y
            if (x != 0) and (y != 0) and self.count == 0:
                if click:
                    pyautogui.click(int(1680*x), int(1050*y))
                else:
                    pyautogui.moveTo(int(1680*x), int(1050*y))
                self.count += 1
        if self.count != 0:
            self.count = (self.count+1) % 3

    def run(self, video=0):
        with self.GestureRecognizer.create_from_options(self.options) as recognizer:
            cap = cv2.VideoCapture(video)
            frame_count = 0

            while True:

                ret, img = cap.read()
                img = cv2.flip(img, 1)

                # Convert the color space from BGR to RGB
                img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                # Create a MediaPipe Image object
                mp_image = mp.Image(
                    image_format=mp.ImageFormat.SRGB, data=img_rgb)

                frame_timestamp_ms = frame_count * 1000

                recognizer.recognize_async(mp_image, frame_timestamp_ms)

                img = cv2.resize(img, (1680, 1050))

                cv2.imshow('MediaPipe Hands', img)

            # Handle key press for quitting (q)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                frame_count += 1

            # Release resources
            cap.release()
            cv2.destroyAllWindows()

## 사용법
a = HandGestureMouseControl(model_path)
model_path = 'model/gesture_recognizer.task'
GestureRecognizerResult = mp.tasks.vision.GestureRecognizerResult
a.run()
