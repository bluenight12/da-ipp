import cv2
import mediapipe as mp
import math

# 카메라 내부 파라미터 설정 (임의로 설정)
PIXEL_TO_CM = 0.2  # 픽셀을 cm로 변환하기 위한 비율


def calculate_distance(point1, point2):
    # 두 점 간의 유클리디안 거리를 계산합니다.
    distance = math.sqrt((point2[0] - point1[0]) **
                         2 + (point2[1] - point1[1])**2)
    return distance * PIXEL_TO_CM  # 픽셀 값을 cm로 변환하여 반환합니다.


def apply_weight(distance, value):
    # 거리에 따른 가중치를 적용합니다.
    if distance <= 50:  # 예시: 거리가 50cm 이하일 때는 가중치를 1로 유지합니다.
        return value * 1
    elif 50 < distance <= 100:  # 거리가 50cm 초과 100cm 이하일 때는 가중치를 1.1로 설정합니다.
        return value * 1.1
    else:  # 거리가 100cm 이상일 때는 가중치를 1.2로 설정합니다.
        return value * 1.2


def main():
    # MediaPipe의 Holistic 모델을 로드합니다.
    mp_holistic = mp.solutions.holistic

    # 웹캠을 연결합니다. 기본 웹캠을 사용할 경우 0을 입력합니다.
    cap = cv2.VideoCapture(0)

    # Holistic 모델을 초기화합니다.
    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        while cap.isOpened():
            # 웹캠에서 프레임을 읽어옵니다.
            ret, frame = cap.read()
            if not ret:
                print("프레임을 읽을 수 없습니다.")
                break

            # 읽어온 프레임을 RGB로 변환합니다.
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Holistic 모델을 통해 프레임을 처리합니다.
            results = holistic.process(frame_rgb)

            # 거리를 계산합니다.
            shoulder_distance = None
            body_height = None
            if results.pose_landmarks:
                left_shoulder = (int(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_SHOULDER].x * frame.shape[1]),
                                 int(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_SHOULDER].y * frame.shape[0]))
                right_shoulder = (int(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_SHOULDER].x * frame.shape[1]),
                                  int(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_SHOULDER].y * frame.shape[0]))
                shoulder_distance = calculate_distance(
                    left_shoulder, right_shoulder)

                head = (int(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.NOSE].x * frame.shape[1]),
                        int(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.NOSE].y * frame.shape[0]))
                left_ankle = (int(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_ANKLE].x * frame.shape[1]),
                              int(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_ANKLE].y * frame.shape[0]))
                right_ankle = (int(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_ANKLE].x * frame.shape[1]),
                               int(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_ANKLE].y * frame.shape[0]))
                body_height = calculate_distance(head, left_ankle) if calculate_distance(
                    head, left_ankle) > calculate_distance(head, right_ankle) else calculate_distance(head, right_ankle)

            # 거리에 따라 가중치를 적용합니다.
            if shoulder_distance is not None:
                shoulder_distance = apply_weight(
                    shoulder_distance, shoulder_distance)
            if body_height is not None:
                body_height = apply_weight(body_height, body_height)

            # 스켈레톤 데이터를 그립니다.
            if results.pose_landmarks:
                mp_drawing = mp.solutions.drawing_utils
                mp_drawing.draw_landmarks(
                    frame, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)

            # 처리된 프레임을 화면에 표시합니다.
            if shoulder_distance is not None:
                cv2.putText(frame, f"Shoulder Distance: {shoulder_distance:.2f} cm", (
                    20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            if body_height is not None:
                cv2.putText(frame, f"Body Height: {body_height:.2f} cm", (
                    20, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('MediaPipe Holistic', frame)

            # 'q' 키를 누르면 루프를 종료합니다.
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # 사용이 끝난 자원을 해제합니다.
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
