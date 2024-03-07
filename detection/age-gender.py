import openvino as ov
import cv2
from typing import Tuple
import os
import sys
import numpy as np
import ipywidgets as widgets


class FaceDetection:
    def __init__(self, model_xml, model_bin, device="CPU"):
        self.model_xml = model_xml
        self.model_bin = model_bin
        
        self.core = ov.Core()
        self.device = widgets.Dropdown(
            options=self.core.available_devices + ["AUTO"],
            value='AUTO',
            description='Device:',
            disabled=False,
        )
        self.model = self.core.read_model(model= self.model_xml)
        self.compiled_model = self.core.compile_model(model=self.model, device_name=self.device.value)
        self.input_keys = self.compiled_model.input(0)
        self.output_keys = self.compiled_model.output(0)
        self.height, self.width = list(self.input_keys.shape)[2:]
        # print(self.output_keys)
        # print(self.input_keys)
        # print(self.height)
        

    def preprocess_image(self, image):
        # 얼굴 감지 전처리 코드 추가
        resized_image = cv2.resize(image, (self.width, self.height))

        input_image = np.expand_dims(resized_image.transpose(2, 0, 1), 0)
        return input_image

    def detect_faces(self, processed_image):
        # Perform inference on the processed image
        results = self.compiled_model([processed_image])[self.output_keys]
        # Extract the results
        # print(results)
        results = np.squeeze(results, (0, 1))
        results = results[~np.all(results == 0, axis=1)]
        return results

    def crop_faces(bgr_image, results, threshold=0.6):
        
        # Fetch image shapes to calculate ratio
        (real_y, real_x) = bgr_image.shape[:2]

        # Find the boxes ratio
        results = results[:, :]
        # Store the cropped faces
        cropped_faces = []
        # Iterate through non-zero boxes
        for box in results:
            # Pick confidence factor from last place in array
            conf = box[2]
            if conf > threshold:
                # Convert float to int and multiply corner position of each box by x and y ratio
                (x_min, y_min, x_max, y_max) = [
                    int(corner_position * real_y) if idx % 2 
                    else int(corner_position * real_x)
                    for idx, corner_position in enumerate(box[3:])
                ]
                
                # Crop the face from the image
                cropped_face = bgr_image[y_min:y_max, x_min:x_max]
                cropped_faces.append(cropped_face)
                
        return cropped_faces

class AgeGenderPrediction:
    def __init__(self, model_xml, model_bin, device="CPU"):
        self.model_xml = model_xml
        self.model_bin = model_bin
        
        self.core = ov.Core()
        self.device = widgets.Dropdown(
            options=self.core.available_devices + ["AUTO"],
            value='AUTO',
            description='Device:',
            disabled=False,
        )
        self.model = self.core.read_model(model= self.model_xml)
        self.compiled_model = self.core.compile_model(model=self.model, device_name=self.device.value)
        self.input_keys = self.compiled_model.input(0)
        self.age_output_key = self.compiled_model.output(0)
        self.gender_output_key = self.compiled_model.output(1)
        self.height, self.width = list(self.input_keys.shape)[2:]
        
        
    def preprocess_image(self, image):
        # 이미지 전처리 코드 추가
        resized_image = cv2.resize(image, (self.width, self.height))
        input_image = np.expand_dims(resized_image.transpose(2, 0, 1), 0)
        return input_image

    def predict_age_gender(self, processed_image):
        # Perform inference on the processed image
        results = self.compiled_model([processed_image])
        # Extract the results
       
        age = results[self.age_output_key][0][0][0][0] * 100  # The model outputs age in the range [0, 1], multiply by 100 for years
        gender = results[self.gender_output_key]  # The model outputs gender as a probability of being male
       
        return age, 'Male' if gender[0,0,0,0] < gender[0,1,0,0] else 'Female'


# 사용 예시
face_detection = FaceDetection(model_xml='model/face-detection-retail-0005/face-detection-retail-0005.xml', model_bin='model/face-detection-retail-0005/face-detection-retail-0005..bin')
# age_gender_prediction = AgeGenderPrediction(model_xml='model/age-gender-recognition-retail-0013/age-gender-recognition-retail-0013.xml', model_bin='model/age-gender-recognition-retail-0013/age-gender-recognition-retail-0013.bin')

# 각 클래스의 메서드 호출
face_image = cv2.imread('assets/test1.jpg') # 이미지 데이터
processed_face_image = face_detection.preprocess_image(face_image)
face_boxes = face_detection.detect_faces(processed_face_image)
pose = face_boxes[0]
# print(pose)

pose = FaceDetection.crop_faces(face_image, face_boxes)

age_gender_prediction = AgeGenderPrediction(model_xml='model/age-gender-recognition-retail-0013/age-gender-recognition-retail-0013.xml', model_bin='model/age-gender-recognition-retail-0013/age-gender-recognition-retail-0013.bin')


for i, face in enumerate(pose):
    processed_face_image = age_gender_prediction.preprocess_image(face)
    age, gender = age_gender_prediction.predict_age_gender(processed_face_image)
    print(f"Face {i+1}: Age - {age}, Gender - {gender}")




for i, face in enumerate(pose):
    cv2.imshow(f"Face {i+1}", face)

cv2.waitKey(0)
cv2.destroyAllWindows()


# age_gender_image = cv2.imread('images.jpeg') # 이미지 데이터
# processed_age_gender_image = age_gender_prediction.preprocess_image(age_gender_image)
# age, gender = age_gender_prediction.predict_age_gender(processed_age_gender_image)