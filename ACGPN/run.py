import numpy as np
from PIL import Image
import os
import sys
import time
import cv2
from .predict_pose import generate_pose_keypoints
import test
from .U_2_Net import u2net_load
from .U_2_Net import u2net_run

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from detection import age_gender


##################################################################################################
# 배경과 사람을 합친 이미지를 return 할지는 통합중에 고민 해봐야 할 문제이고 테스팅은 jupyter notebook 에서 해주세요#
##################################################################################################


class RUN:

    def __init__(self):
        self.u2net = u2net_load.model(model_name='u2net')
        
    def take_photo(self):
        cap = cv2.VideoCapture(0)
        
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        while 1:
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.transpose(frame)
            frame = cv2.flip(frame, 1)

            key = cv2.waitKey(33)
            if len(frame.shape) != 3 or frame.shape[2] != 3:
            # 이미지가 3채널(RGB)을 가지고 있는지 확인합니다.
                continue
            if frame.size == 0 or frame is None:
                continue

            yield frame

            if key == ord('q'): break
            # elif key == ord('s'):
            #     cv2.imwrite(f'{os.getcwd()}/detection/predict.png', frame)
            # elif key == ord('a'): 
            #     cv2.imwrite(f'{os.path.dirname(__file__)}/inputs/img/img001.png', frame)
                
        cv2.destroyAllWindows()
        
    
    #Cloth mask
    def get_cloth_mask(self):
        #cloth name은 일단 고정(매개변수로 받아도 됨)
        self.cloth_name = 'cloth001.png'
        
        #cloth 폴더 안에 사진을 하나만 둔다면 제일 나은 선택 count로 ++ 해 나가도 마지막을 인식하기 때문에 cloth name과 같이 바꿔 주면 됨
        # ex) f'cloth00{count}.png'
        cloth_path = os.path.join(
            'ACGPN/inputs/cloth', sorted(os.listdir('ACGPN/inputs/cloth'))[-1])

        
        cloth = Image.open(cloth_path)

        cloth = cloth.resize((192, 256), Image.BICUBIC).convert('RGB')
        cloth.save(os.path.join('ACGPN/Data_preprocessing/test_color', self.cloth_name))
        # 마스킹 작업
        u2net_run.infer(self.u2net, 'ACGPN/Data_preprocessing/test_color',
                        'ACGPN/Data_preprocessing/test_edge')

        # Image.open(f'Data_preprocessing/test_edge/{self.cloth_name}')

    def get_image(self):
        
        self.img_name = 'img001.png'
        
        # VRAM이 적어서 CUDA 불가능 
        # os.environ['CUDA_VISIBLE_DEVICES'] = '0'
        img_path = os.path.join('ACGPN/inputs/img', sorted(os.listdir('ACGPN/inputs/img'))[-1])
        img = Image.open(img_path)
        img = img.resize((192, 256), Image.BICUBIC)
        
        # cv2의 resize 알고리즘과 차이 없음
        # LANCZ0S4와 AREA 둘다 테스트 완료
        # image_cv = cv2.resize(cv2.cvtColor(cv2.imread(img_path),cv2.COLOR_BGR2RGB), (192, 256), cv2.INTER_LANCZOS4)

        # test_img 폴더에 (192, 256) 사이즈로 자른 파일 저장
        img_path = os.path.join('ACGPN/Data_preprocessing/test_img', self.img_name)
        img.save(img_path)

        # test_img 폴더에 있는 사진을 마스킹
        u2net_run.infer(self.u2net, 'ACGPN/Data_preprocessing/test_img', 'ACGPN/Data_preprocessing/test_mask')

        # bash로 할 때 옮길지 그대로 갈지 고민해봐야 할 문제(안 옮길 가능성 높음)
        # 사람을 부위별로 나눠서 라벨링 후 이미지로 저장
        os.system("python ACGPN/Self-Correction-Human-Parsing-for-ACGPN/simple_extractor.py --dataset 'lip' --model-restore 'ACGPN/lip_final.pth' --input-dir 'ACGPN/Data_preprocessing/test_img' --output-dir 'ACGPN/Data_preprocessing/test_label'")

        pose_path = os.path.join('ACGPN/Data_preprocessing/test_pose',
                                self.img_name.replace('.png', '_keypoints.json'))
        
        # 사람의 포즈를 따서 좌표로 변환시켜줌
        # json 파일 형식으로 Export
        generate_pose_keypoints(img_path, pose_path)

    def run_test(self):
        # test_pairs.txt 안에 사진과 의류 정보가 들어가기 때문에 삭제 후 재생성
        os.system('rm -rf ACGPN/Data_preprocessing/test_pairs.txt')
        with open('ACGPN/Data_preprocessing/test_pairs.txt', 'w') as f:
            f.write(f'{self.img_name} {self.cloth_name}')

        # 마찬가지로 bash로 나눌지 고민            
        os.system('python ACGPN/test.py')

    def set_background(self):
        # 나중에 매개 변수로 만들어진 background의 매개 변수를 가져오든지 원래 가지고 있던 배경(찍은 사진)을 다시 넣어줘도 됨
        bg = cv2.cvtColor(cv2.imread(os.path.join('ACGPN/Data_preprocessing/test_background', sorted(os.listdir('ACGPN/Data_preprocessing/test_background'))[-1])), cv2.COLOR_BGR2RGB)
        
        # test.py를 돌리고 나온 결과물을 가져오기
        result = cv2.cvtColor(cv2.imread(os.path.join('ACGPN/results/test/try-on', sorted(os.listdir('ACGPN/results/test/try-on'))[-1])), cv2.COLOR_BGR2RGB)

        # background의 부분을 비워야 하기 때문에(픽셀을 0으로) 마스킹 된 데이터를 불러옴
        bg_remove = cv2.imread('ACGPN/Data_preprocessing/test_mask/img001.png', cv2.IMREAD_GRAYSCALE)
        bg = cv2.resize(bg, dsize=(result.shape[1], result.shape[0]))

        # u2net에서 이진화 처리를 안하기 때문에 이진화 처리 후 결과물 배경을 흰색으로 처리(재마스킹 하기 위해서)
        ret, self.thresh = cv2.threshold(bg_remove, 100, 255, cv2.THRESH_BINARY)
        result[self.thresh == 0] = 255

        # 해당 result 파일을 final 폴더에 넣고 한번 더 마스킹 작업(원래 작업했던 부분에서 잘리거나 한 부분이 있기 때문에)
        cv2.imwrite('ACGPN/results/test/final/img001.png', cv2.cvtColor(result,cv2.COLOR_RGB2BGR))
        u2net_run.infer(self.u2net, 'ACGPN/results/test/final', 'ACGPN/Data_preprocessing/test_mask')

        # result 파일에서 마스킹 작업된 파일을 가져온 뒤에 이진화
        bg_remove = cv2.imread('ACGPN/Data_preprocessing/test_mask/img001.png', cv2.IMREAD_GRAYSCALE)
        ret, self.thresh = cv2.threshold(bg_remove, 100, 255, cv2.THRESH_BINARY)
        
        # thresh에 흰색 부분은 사람이 들어갈 자리기에 배경 부분의 그 곳을 검은색으로 만들어줌(더하기 연산을 수월하게 하기 위해서)
        bg[self.thresh >= 2] = 0
        new_image = bg + result

        cv2.imwrite('ACGPN/results/img001.png', cv2.cvtColor(new_image, cv2.COLOR_RGB2BGR))
        # cv2.imshow('Final result', cv2.cvtColor(new_image, cv2.COLOR_RGB2BGR))
        # cv2.waitKey()
        # cv2.destroyAllWindows()

    def test(self):
        '''
        test는 test용 임시 함수니까 막 써도 상관 없음
        '''
        # 192 x 256 으로 변환한 사진을 마스킹해서 저장
        # u2net_run.infer(self.u2net, 'Data_preprocessing/test_img', 'Data_preprocessing/test_mask')
        
        # 마스킹 된 데이터를 토대로 
        # img = cv2.imread(f'Data_preprocessing/test_mask/img001.png', cv2.IMREAD_GRAYSCALE)
        # r_img_path = os.path.join('Data_preprocessing/test_img', sorted(os.listdir('Data_preprocessing/test_img'))[-1])
        # self.r_img = cv2.cvtColor(cv2.imread(r_img_path), cv2.COLOR_BGR2RGB)
        # ret, self.thresh = cv2.threshold(img, 230, 255, cv2.THRESH_BINARY)
        #k = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        #dst = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, None)
        # self.r_img[img <= 2] = 255
        # cv2.imwrite('Data_preprocessing/test_img/img001.png', cv2.cvtColor(self.r_img, cv2.COLOR_RGB2BGR))
        # 사진 띄우고 싶으면 아래 코드 주석 해제
        #fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(20, 7))
        #ax[0].imshow(img, cmap='gray')
        #ax[1].imshow(self.r_img)
        #ax[2].imshow(thresh, cmap='gray')
        #plt.show()        

'''
class RUN:

    def __init__(self):
        self.u2net = u2net_load.model(model_name='u2netp')
 
    #Cloth mask
    def get_cloth_mask(self):
        #u2net = u2net_load.model(model_name = 'u2netp')
        #cloth_name = f'cloth_{int(time.time())}.png'
        self.cloth_name = 'cloth001.png'

        cloth_path = os.path.join(
            'inputs/cloth', sorted(os.listdir('inputs/cloth'))[-1])
        cloth = Image.open(cloth_path)
        cloth = cloth.resize((192, 256), Image.BICUBIC).convert('RGB')
        cloth.save(os.path.join('Data_preprocessing/test_color', self.cloth_name))
        u2net_run.infer(self.u2net, 'Data_preprocessing/test_color',
                        'Data_preprocessing/test_edge')

        Image.open(f'Data_preprocessing/test_edge/{self.cloth_name}')

    def get_image(self):
        #img_name = f'img_{int(time.time())}.png'
        self.img_name = 'img001.png'

        img_path = os.path.join('inputs/img', sorted(os.listdir('inputs/img'))[-1])
        img = Image.open(img_path)
        img = img.resize((192, 256), Image.BICUBIC)
        print(type(img))
        img_path = os.path.join('Data_preprocessing/test_img', self.img_name)
        img.save(img_path)
        u2net_run.infer(self.u2net, 'Data_preprocessing/test_img', 'Data_preprocessing/test_mask')
        os.system("python Self-Correction-Human-Parsing-for-ACGPN/simple_extractor.py --dataset 'lip' --model-restore 'lip_final.pth' --input-dir 'Data_preprocessing/test_img' --output-dir 'Data_preprocessing/test_label'")

        pose_path = os.path.join('Data_preprocessing/test_pose',
                                self.img_name.replace('.png', '_keypoints.json'))
        generate_pose_keypoints(img_path, pose_path)

    def run_test(self):
        os.system('rm -rf Data_preprocessing/test_pairs.txt')
        with open('Data_preprocessing/test_pairs.txt', 'w') as f:
            f.write(f'{self.img_name} {self.cloth_name}')
        test.main()
        output_grid = np.concatenate([
            np.array(Image.open(f'Data_preprocessing/test_img/{self.img_name}')),
            np.array(Image.open(f'Data_preprocessing/test_color/{self.cloth_name}')),
            np.array(Image.open(f'results/test/try-on/{self.img_name}'))
        ], axis=1)

        image_grid = Image.fromarray(output_grid)
        
        cv2.imshow('image', cv2.cvtColor(output_grid, cv2.COLOR_RGB2BGR))
        if cv2.waitKey() & 0xff == 27:
            cv2.destroyAllWindows()

'''
# run = RUN()

# run.get_cloth_mask()
# run.get_image()
# run.run_test()
# run.set_background()


# u2net = u2net_load.model(model_name = 'u2netp')
#cloth_name = f'cloth_{int(time.time())}.png'
# cloth_name = 'cloth001.png'

# cloth_path = os.path.join(
#     'inputs/cloth', sorted(os.listdir('inputs/cloth'))[-1])
# cloth = Image.open(cloth_path)
# cloth = cloth.resize((192, 256), Image.BICUBIC).convert('RGB')
# cloth.save(os.path.join('Data_preprocessing/test_color', cloth_name))
# os.system('export CUDA_VISIBLE_DEVICES=""')
# u2net_run.infer(u2net, 'Data_preprocessing/test_color',
#                 'Data_preprocessing/test_edge')

# Image.open(f'Data_preprocessing/test_edge/{cloth_name}')

# img_name = f'img_{int(time.time())}.png'
# img_name = 'img001.png'

# img_path = os.path.join('inputs/img', sorted(os.listdir('inputs/img'))[-1])
# img = Image.open(img_path)
# img = img.resize((192, 256), Image.BICUBIC)

# img_path = os.path.join('Data_preprocessing/test_img', img_name)
# img.save(img_path)
# #os.system('export CUDA_VISIBLE_DEVICES="0"')
# os.system("python Self-Correction-Human-Parsing-for-ACGPN/simple_extractor.py --dataset 'lip' --model-restore 'lip_final.pth' --input-dir 'Data_preprocessing/test_img' --output-dir 'Data_preprocessing/test_label'")

# pose_path = os.path.join('Data_preprocessing/test_pose',
#                          img_name.replace('.png', '_keypoints.json'))
# generate_pose_keypoints(img_path, pose_path)

# os.system('rm -rf Data_preprocessing/test_pairs.txt')
# with open('Data_preprocessing/test_pairs.txt', 'w') as f:
#     f.write(f'{img_name} {cloth_name}')
# os.system('python test.py')
# output_grid = np.concatenate([
#     np.array(Image.open(f'Data_preprocessing/test_img/{img_name}')),
#     np.array(Image.open(f'Data_preprocessing/test_color/{cloth_name}')),
#     np.array(Image.open(f'results/test/try-on/{img_name}'))
# ], axis=1)

# image_grid = Image.fromarray(output_grid)

# image_grid