# 1번 초기화면에서 화면을 터치할 때
# Client Server 방식
# detection/age-gender를 통해 나이 성별을 가져오고 옷 뿌릴 준비
import os
import cv2
import time
import sqlite3

from detection import age_gender
from Voice import recognize_text_module
from Voice import translate_korean_to_english
from Voice import clothes_extractor
from ACGPN import run, generate_image


photo = run.RUN()
con = sqlite3.connect('cloth.db')
cur = con.cursor()

def first_step():
    face_detector = age_gender.FaceDetection(model_xml='detection/model/face-detection-retail-0005/face-detection-retail-0005.xml',
                                             model_bin='detection/model/face-detection-retail-0005/face-detection-retail-0005.bin')

    age_gender_predictor = age_gender.AgeGenderPrediction(model_xml='detection/model/age-gender-recognition-retail-0013/age-gender-recognition-retail-0013.xml',
                                                          model_bin='detection/model/age-gender-recognition-retail-0013/age-gender-recognition-retail-0013.bin')
    
    count = 0
    tmp = ''
    gen = photo.take_photo()
    while 1:
        i = next(gen)
        # flaged = yield
        yield i
        #crop image
        faces = face_detector.run(i)
        #predict age, gender
        age = ''
        gender = ''
        try:
            age, gender = age_gender_predictor.run(faces)

        except ValueError as e:
            raise ValueError("Image is empty") from e

        except cv2.error as e:
            print(e)
        
        finally:
            if age is not None:
                count += 1
                if count >= 5:
                    count = 0
                    yield age, gender



        
#   print('for end')
    

# # 2번 모드 선택 [1(옷 바로 선택) 2(음성)]
def second_step():
    get_option = ''
    # if get_option == 1:
    #     third_by_one_step()
    if get_option == 2:
        print("3-2로 이동")


# # 3-1번 옷 바로 선택
# def third_by_one_step():
#     do_nothing = ''
# # 옷 선택 UI 띄워주기


# # 3-2번 음성 ( 옷 뿌려주고 )
def third_by_two_step():
    # 바로 음성을 받음 (추후에 count혹은 사용자가 버튼을 누르도록)
    yield recognize_text_module.recognize_and_save_text(output_file=f'{os.path.dirname(os.path.realpath(__file__))}/Voice/text.txt')
    # pip install googletrans==4.0.0rc1
    yield translate_korean_to_english.translate_korean_to_english(
        input_file=f'{os.path.dirname(os.path.realpath(__file__))}/Voice/text.txt', 
        output_file=f'{os.path.dirname(os.path.realpath(__file__))}/Voice/english.txt')
    # 안에 정제 해야할 Value가 많음
    yield clothes_extractor.extract_clothes(f"{os.path.dirname(os.path.realpath(__file__))}/Voice/english.txt",
                                       f"{os.path.dirname(os.path.realpath(__file__))}/Voice/clothes.txt")
    


#third_by_two_step()

# Voice/recognize text module

# # 3-3 사진 선택하기
# def third_by_third_step():
#     # DB에서 받아온 5개 정도 보여주고 제스처 넣어서 선택할 수 있게 하기
#     f"{os.path.dirname(os.path.realpath(__file__))}/Voice/clothes.txt"
#     cur.execute('SELECT * FROM cloth')
#     print(cur.fetchmany(4))
#     # UI + HandGesture

# # 4번 카메라에서 사진 가져오기(인식해서 사진찍는 타이밍 정하게 하기)
# def fourth_step():
#     photo.take_photo()

def forth_step(flaged):
    gen = photo.take_photo(flaged)
    while 1:
        next(gen)
        i = gen.send(flaged)
        flaged = yield
        yield i


# # 5번 4번에서 찍은 사진 의류 합성 시키기
def fifth_step():
    yield 0
    photo.get_cloth_mask()
    yield 33
    photo.get_image()
    yield 66
    photo.run_test()
    yield 100
    #photo.set_background()
# # 배경 넣기 전까지 단계를 해서 사진 생성

# # 6번 배경 텍스트로 합성하기
def sixth_step():
    yield recognize_text_module.recognize_and_save_text(output_file=f'{os.path.dirname(os.path.realpath(__file__))}/voice_image/text.txt')
    # pip install googletrans==4.0.0rc1
    yield translate_korean_to_english.translate_korean_to_english(
        input_file=f'{os.path.dirname(os.path.realpath(__file__))}/voice_image/text.txt', 
        output_file=f'{os.path.dirname(os.path.realpath(__file__))}/voice_image/bck_eng.txt')

# # 배경 합성한 사진 마무리 짓고 QR코드로 옷 사진 주기
# # 마찬가지로 recognize text module

def seventh_step(value: str):
    yield 0
    host = '61.108.166.15'
    port = 22
    username = 'team004'
    password = 'busan@123'
    # voice_image에서 값 가져오기
    prompt = value + ', landscape, 8k, best quality, high quality, realistic, high resolution,  masterpiece'
    command = '/datasets/team004/text2image/run.sh' + ' ' + prompt  # Make sure the script is executable
    remote_file_path = '/datasets/team004/text2image/result.png'  # The path where 'result.png' is saved on the remote machine
    local_file_path = './ACGPN/Data_preprocessing/test_background/background.png'  # Where to save 'result.png' locally
    generate_image.execute_remote_command_and_download_file(host, port, username, password, command, remote_file_path, local_file_path)
    yield 50
    photo.set_background()
    yield 100
