import cv2
import mediapipe as mp
import pyautogui  # for mouse control
import time

pyautogui.FAILSAFE = False

# MediaPipe Hands model setup
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils  # Drawing helpers

# Hand landmark extraction object creation
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Webcam capture initialization
cap = cv2.VideoCapture(0)

index_finger_tip = None
middle_finger_tip = None
count = 0
while True:
    start_time = time.time()
    # Read frame from webcam
    ret, img = cap.read()

    # Convert image to RGB format
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.flip(img, 1)
    # Process the image with MediaPipe Hands model
    results = hands.process(img)
    # x, y = pyautogui.position()
    # Extract and visualize landmarks (if desired)
    tem_x = 0
    tem_y = 0

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw landmarks and connections
            # mp_drawing.draw_landmarks(
            #     img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get the tip of the index and middle fingers
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
            tem_x = index_finger_tip.x
            tem_y = index_finger_tip.y
            # If both fingers are raised, click at the last known position of the index fingert
            # if index_finger_tip and middle_finger_tip:
            #     pyautogui.click(x=index_finger_tip.x, y=index_finger_tip.y)
    if (tem_x != 0) and (tem_y != 0) and count == 0:
        pyautogui.moveTo(1680*tem_x, 1050*tem_y)
        count += 1
    if count != 0:
        count = (count+1) % 3
       
    end_time = time.time()
    fps = 1 / (end_time - start_time)
    cv2.putText(img, "FPS: {:.2f}".format(fps), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    # Display the resulting image
    img = cv2.resize(img, dsize=(1680, 1050))
    cv2.imshow('MediaPipe Hands', img)

    # Handle key press for quitting (q)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
