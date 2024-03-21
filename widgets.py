import os
import sys
import random
import time
import sqlite3
import requests
import math
import multiprocessing
import qrcode

# from PyQt6 import QtWidgets, uic
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget, QProgressBar
from PySide6.QtCore import QFile, QIODevice, QObject, Qt, QThread, QTimer, Signal, Slot
from PySide6.QtGui import QPalette, QImage, QPixmap
import pygame

from ui.mainwindow_ui import Ui_MainWindow
from ui.second_window_ui import Ui_Second_Window
from ui.third_window_ui import Ui_Third_Window
# from ui.third3_window_ui import Ui_Third3_Window
from ui.forth_window_ui import Ui_Forth_Window
from ui.fifth_window_ui import Ui_Fifth_Window
from ui.sixth_window_ui import Ui_Sixth_Window
from ui.seventh_window_ui import Ui_Seventh_Window

from voice_image import text2background_image_fin as tif

import cv2
import main
import numpy as np
import mediapipe as mp


class Camera(QThread):

    updateSignal = Signal(QImage)
    updateText = Signal(float, str)
    updateCount = Signal(str)

    def __init__(self, parent=None):
        super().__init__()
        self.flag = 0
        self.value = 0
        self.photo_time = 0
        self.current_time = time.time()
        self.p_flag = False
        self.mp_holistic = mp.solutions.holistic
        self.holistic = self.mp_holistic.Holistic(
            min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.sound_flag = False
        pygame.mixer.init()
        self.countdown = pygame.mixer.Sound("countdown.mp3")
        self.shutter = pygame.mixer.Sound("shutter.mpga")

    def run(self):
        gen = main.first_step()
        while 1:
            i = next(gen)
            # print(f"{self.photo_time}포토타임 {self.p_flag}플래그")
            # terminate를 쓰면 뒤에서 계속 돌아감
            if self.flag == 1:
                break
            if isinstance(i, tuple) and widget.currentIndex() == 0:
                if self.value == 0:
                    self.updateText.emit(i[0], i[1])
            if isinstance(i, np.ndarray):
                i = cv2.resize(i, dsize=(600, 800),
                               interpolation=cv2.INTER_LANCZOS4)
                i = cv2.flip(i, 1)
                if self.value == 1 and self.p_flag is False:
                    i = self.get_skeleton(i)
                image = QImage(i, i.shape[1], i.shape[0],
                               i.strides[0], QImage.Format.Format_BGR888)
                if self.p_flag is False:
                    self.updateSignal.emit(image)
                    

    def get_skeleton(self, image: np.ndarray):

        frame_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.holistic.process(frame_rgb)

        if results.pose_landmarks:
            right_hand = (int(results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.LEFT_PINKY].x * image.shape[1]),
                          int(results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.LEFT_PINKY].y * image.shape[0]))
            left_hand = (int(results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.RIGHT_PINKY].x * image.shape[1]),
                         int(results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.RIGHT_PINKY].y * image.shape[0]))

            right_elbow = int(
                results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.LEFT_ELBOW].y * image.shape[0])
            left_elbow = int(
                results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.RIGHT_ELBOW].y * image.shape[0])

            left_shoulder = int(
                results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.LEFT_SHOULDER].x * image.shape[1])
            right_shoulder = int(
                results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.RIGHT_SHOULDER].x * image.shape[1])
            left = 150
            right = 450
            image = cv2.line(image, (left, 200), (left, 600), (0, 255, 0), 1)
            image = cv2.line(image, (right, 200), (right, 600), (0, 0, 255), 1)

            if 0 < left_hand[0] < left and right < right_hand[0] < 600 and right_elbow < right_hand[1] and left_elbow < left_hand[1]:
                if self.photo_time == 0:
                    self.photo_time = time.time()
                    if self.sound_flag is False:
                        self.countdown.play()
                        self.sound_flag = True
                elif time.time() - self.photo_time > 3:
                    cv2.imwrite('ACGPN/inputs/img/img001.png', image)
                    self.shutter.play()
                    self.updateCount.emit('찰칵')
                    self.p_flag = True
                    self.photo_time = 0
                elif time.time() - self.photo_time >= 0:
                    self.updateCount.emit(
                        str(math.ceil(3 - (time.time() - self.photo_time))))
            else:
                self.updateCount.emit('포즈를 취해주세요')
                self.photo_time = 0
                if self.sound_flag is True:
                    self.countdown.stop()
                    self.sound_flag = False
                    

        return image
        # if results.pose_landmarks:
        #     mp_drawing = mp.solutions.drawing_utils
        #     mp_drawing.draw_landmarks(
        #         image, results.pose_landmarks, self.mp_holistic.POSE_CONNECTIONS)

    def setting(self, value):
        self.value = value

    def kill(self):
        self.flag = 1
        self.holistic.close()

    def take_photo(self):
        self.photo_time = time.time()

    def reset_photo(self):
        self.p_flag = False


class Get_Voice(QThread):
    updateString = Signal(str)

    def __init__(self, parent=None):
        super().__init__()

    def second_run(self):
        # 리스트 한번이라도 받았으면 넘어가기 키 X
        for i in main.third_by_two_step():
            if isinstance(i, list):
                self.updateString.emit(''.join(i))
                break
            elif isinstance(i, str):
                self.updateString.emit(i)
        second.on_Finished()

    def sixth_run(self):
        for i in main.sixth_step():
            if isinstance(i, list):
                self.updateString.emit(''.join(i))
                break
            elif isinstance(i, str):
                self.updateString.emit(i)
        sixth.on_Finished()


class MainWindow(QMainWindow, Ui_MainWindow):
    value_changed = Signal(int)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # self.label.setAlignment(
        #     Qt.AlignmentFlag.AlignHCenter
        #     | Qt.AlignmentFlag.AlignVCenter
        # )

        self.go_second.clicked.connect(self.onSecondSelect)
        self.go_third.clicked.connect(self.onThirdSelect)
        self.thread = Camera()
        self.thread.setting(0)
        # self.thread.finished.connect(self.onFinished)
        self.thread.start()
        self.thread.updateSignal.connect(self.update_label)
        self.thread.updateText.connect(self.update_text)

    def onSecondSelect(self):
        # self.pushButton.setEnabled(False)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        print('Go Second')

    def onThirdSelect(self):
        # self.pushButton.setEnabled(False)
        widget.setCurrentIndex(widget.currentIndex() + 2)
        third.genderFlag = True
        third.recommend_cloth()
        print('Go Third')

    @Slot(QImage)
    def update_label(self, image):
        self.camera.setPixmap(QPixmap.fromImage(image))

    @Slot(float, str)
    def update_text(self, age, gender):
        third.gender = gender
        third.age = age
        print(gender, age)
        # self.label_2.setText(f'age = {round(age)}, gender = {gender}')


class Second_Window(QWidget, Ui_Second_Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.start.clicked.connect(self.push_translate)
        self.go_third.setEnabled(False)
        self.repeat.setEnabled(False)
        self.start.setEnabled(True)
        self.go_third.clicked.connect(self.third)
        self.repeat.clicked.connect(self.on_Repeat)
        self.back.clicked.connect(self.on_Back)

    def push_translate(self):
        self.thread = Get_Voice()
        self.start.setEnabled(False)
        self.go_third.setEnabled(False)
        self.repeat.setEnabled(False)
        self.thread.updateString.connect(self.update_text)
        self.thread.second_run()
        self.thread.finished.connect(self.on_Finished)

    def on_Finished(self):
        self.repeat.setEnabled(True)
        self.go_third.setEnabled(True)

    def on_Repeat(self):
        self.push_translate()

    def third(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)
        third.genderFlag = False
        third.recommend_cloth()

    def on_Back(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)

    @Slot(str)
    def update_text(self, txt):
        self.get_translate.setText(txt)


class Third_Window(QWidget, Ui_Third_Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.genderFlag = True
        self.gender = ""
        self.age = 0
        self.con = sqlite3.connect('cloth.db')
        self.cur = self.con.cursor()
        self.recommend.clicked.connect(self.recommend_cloth)
        self.cloth1_select.clicked.connect(self.select_cloth1)
        self.cloth2_select.clicked.connect(self.select_cloth2)
        self.cloth3_select.clicked.connect(self.select_cloth3)
        # self.recommend_cloth()
        self.back.clicked.connect(self.on_Back)

    def third_second(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def recommend_cloth(self):
        if self.genderFlag is True:
            print(self.gender, self.age)
            self.cur.execute(
                f'SELECT id, Image_Link FROM cloth WHERE gender="{self.gender.lower()}" AND age="{self.age // 10 * 10}" ORDER BY RANDOM() LIMIT 3;')
            self.cloth_list = self.cur.fetchall()
            cloths = [self.cloth1, self.cloth2, self.cloth3]

            for j, cloth in enumerate(cloths, start=0):
                i = self.get_normal_image(self.cloth_list[j][1])
                i = cv2.resize(i, (300, 400), interpolation=cv2.INTER_LANCZOS4)
                image = QImage(i, i.shape[1], i.shape[0],
                               i.strides[0], QImage.Format.Format_BGR888)
                # .scaled(self.width(), self.height(), aspectMode=Qt.IgnoreAspectRatio))
                cloth.setPixmap(QPixmap.fromImage(image))
        else:
            cloth_file = f"{os.path.dirname(os.path.realpath(__file__))}/Voice/clothes.txt"
            with open(cloth_file, 'r') as clothes_file:
                for line in clothes_file:
                    words = line.split()
                    print(words)
                    ctg = [word for word in words if word in [
                        '-shirt', 'long sleeve', 'man to man', 'knit']]
                    color = [word for word in words if word in [
                        'red', 'green', 'black', 'blue', 'white']]
                    if ctg == [] or color == []:
                        # 돌아가기 누르라고 해야함
                        self.set_label("돌아가기를 누르고 다시 입력해주세요")
                    ctg = ctg[-1]
                    color = color[-1]
                    if ctg == '-shirt':
                        ctg = 't-shirt'
            self.cur.execute(
                f'SELECT id, Image_Link FROM cloth WHERE category="{ctg}" AND color="{color}" ORDER BY RANDOM() LIMIT 3;')
            self.cloth_list = self.cur.fetchall()

            cloths = [self.cloth1, self.cloth2, self.cloth3]

            for j, cloth in enumerate(cloths, start=0):
                i = self.get_normal_image(self.cloth_list[j][1])
                i = cv2.resize(i, (300, 400), interpolation=cv2.INTER_LANCZOS4)
                image = QImage(i, i.shape[1], i.shape[0],
                               i.strides[0], QImage.Format.Format_BGR888)
                # .scaled(self.width(), self.height(), aspectMode=Qt.IgnoreAspectRatio))
                cloth.setPixmap(QPixmap.fromImage(image))

    def select_cloth1(self):
        forth.set_clothID(self.cloth_list[0][0])
        i = self.get_normal_image(self.cloth_list[0][1])
        cv2.imwrite('ACGPN/inputs/cloth/cloth001.png', i)
        i = cv2.resize(i, (180, 240), interpolation=cv2.INTER_LANCZOS4)
        image = QImage(i, i.shape[1], i.shape[0],
                       i.strides[0], QImage.Format.Format_BGR888)
        forth.cloth.setPixmap(QPixmap.fromImage(image))
        self.go_forth()

    def select_cloth2(self):
        forth.set_clothID(self.cloth_list[1][0])
        i = self.get_normal_image(self.cloth_list[1][1])
        cv2.imwrite('ACGPN/inputs/cloth/cloth001.png', i)
        i = cv2.resize(i, (180, 240), interpolation=cv2.INTER_LANCZOS4)
        image = QImage(i, i.shape[1], i.shape[0],
                       i.strides[0], QImage.Format.Format_BGR888)
        forth.cloth.setPixmap(QPixmap.fromImage(image))
        self.go_forth()

    def select_cloth3(self):
        forth.set_clothID(self.cloth_list[2][0])
        i = self.get_normal_image(self.cloth_list[2][1])
        cv2.imwrite('ACGPN/inputs/cloth/cloth001.png', i)
        i = cv2.resize(i, (180, 240), interpolation=cv2.INTER_LANCZOS4)
        image = QImage(i, i.shape[1], i.shape[0],
                       i.strides[0], QImage.Format.Format_BGR888)
        forth.cloth.setPixmap(QPixmap.fromImage(image))
        self.go_forth()

    def go_forth(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)
        window.thread.setting(1)

    def on_Back(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def get_normal_image(self, url):
        image_nparray = np.asarray(
            bytearray(requests.get(url).content), dtype=np.uint8)
        image = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR)
        return image

    def set_label(self, value):
        self.label_2.setText(value)


class Forth_Window(QWidget, Ui_Forth_Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.clothID = 0
        self.thread = window.thread
        self.thread.updateSignal.connect(self.update_label)
        self.retake.clicked.connect(self.retake_photo)
        self.go_next.clicked.connect(self.go_fifth)
        self.back.clicked.connect(self.on_Back)
        self.thread.updateCount.connect(self.update_count)

    def set_clothID(self, id):
        self.clothID = id
        seventh.id = id

    def go_fifth(self):
        self.thread.reset_photo()
        self.thread.setting(0)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        QTimer.singleShot(500, self.singleshot)

    def singleshot(self):
        for i in main.fifth_step():
            fifth.progressBar.setValue(i)
        fifth.run_finish()

    @Slot(QImage)
    def update_label(self, image):
        self.camera.setPixmap(QPixmap.fromImage(image))

    def retake_photo(self):
        self.thread.reset_photo()

    def on_Back(self):
        self.thread.setting(0)
        widget.setCurrentIndex(widget.currentIndex() - 1)

    @Slot(str)
    def update_count(self, value):
        self.count.setText(value)


class Fifth_Window(QWidget, Ui_Fifth_Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.done.clicked.connect(self.go_seventh)
        self.plus.clicked.connect(self.go_sixth)
        self.pushButton.clicked.connect(self.on_back)

    def run_finish(self):
        img = cv2.imread('ACGPN/results/test/try-on/img001.png')
        i = cv2.resize(img, dsize=(630, 840),
                       interpolation=cv2.INTER_LANCZOS4)
        image = QImage(i, i.shape[1], i.shape[0],
                       i.strides[0], QImage.Format.Format_BGR888)
        self.finish_photo.setPixmap(QPixmap.fromImage(image))

    def go_sixth(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def go_seventh(self):
        seventh.on_fifth_finished()
        widget.setCurrentIndex(widget.currentIndex() + 2)
        # 사진 도출

    def on_back(self):
        widget.setCurrentIndex(0)
        self.finish_photo.setText('잠시만 기다려주세요')
        seventh.photo.setText('잠시만 기다려주세요')


class Sixth_Window(QWidget, Ui_Sixth_Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.start.clicked.connect(self.push_translate)
        self.go_seventh.setEnabled(False)
        self.repeat.setEnabled(False)
        self.start.setEnabled(True)
        self.go_seventh.clicked.connect(self.seventh)
        self.repeat.clicked.connect(self.on_Repeat)
        self.back.clicked.connect(self.on_Back)

    def push_translate(self):
        self.thread = Get_Voice()
        self.start.setEnabled(False)
        self.go_seventh.setEnabled(False)
        self.repeat.setEnabled(False)
        self.thread.updateString.connect(self.update_text)
        self.thread.sixth_run()
        self.thread.finished.connect(self.on_Finished)

    def on_Finished(self):
        self.repeat.setEnabled(True)
        self.go_seventh.setEnabled(True)

    def seventh(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)
        QTimer.singleShot(500, self.singleshot)

    def singleshot(self):
        f = open('voice_image/bck_eng.txt')
        text_data = f.read()
        for i in main.seventh_step(text_data):
            seventh.on_progressbar(i)
        seventh.on_sixth_finished()

    def on_Repeat(self):
        self.push_translate()

    def on_Back(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)

    @Slot(str)
    def update_text(self, txt):
        self.get_translate.setText(txt)


class Seventh_Window(QWidget, Ui_Seventh_Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.id = 0
        self.con = sqlite3.connect('cloth.db')
        self.cur = self.con.cursor()
        self.go_first.clicked.connect(self.on_first)

    def on_fifth_finished(self):
        img = cv2.imread('ACGPN/results/test/try-on/img001.png')
        i = cv2.resize(img, dsize=(630, 840),
                       interpolation=cv2.INTER_LANCZOS4)
        self.on_start(i)
        self.progressBar.setEnabled(False)

    def on_sixth_finished(self):
        img = cv2.imread('ACGPN/results/img001.png')
        i = cv2.resize(img, dsize=(630, 840),
                       interpolation=cv2.INTER_LANCZOS4)
        self.on_start(i)

    def on_start(self, i):
        image = QImage(i, i.shape[1], i.shape[0],
                       i.strides[0], QImage.Format.Format_BGR888)
        self.photo.setPixmap(QPixmap.fromImage(image))
        self.cur.execute(f'SELECT Product_Link FROM cloth WHERE id={self.id};')
        link = self.cur.fetchone()
        myqr = qrcode.make(link[0])
        myqr.save(stream='qr_code.png')
        img = cv2.imread('qr_code.png')
        i = cv2.resize(img, dsize=(140, 140),
                       interpolation=cv2.INTER_LANCZOS4)
        image = QImage(i, i.shape[1], i.shape[0],
                       i.strides[0], QImage.Format.Format_BGR888)
        self.qrcode.setPixmap(QPixmap.fromImage(image))

    def on_progressbar(self, value):
        self.progressBar.setValue(value)

    def on_first(self):
        widget.setCurrentIndex(0)
        self.photo.setText('잠시만 기다려주세요')
        fifth.finish_photo.setText('잠시만 기다려주세요')


if __name__ == "__main__":

    app = QApplication(sys.argv)
    widget = QStackedWidget()

    window = MainWindow()
    second = Second_Window()
    third = Third_Window()
    forth = Forth_Window()
    fifth = Fifth_Window()
    sixth = Sixth_Window()
    seventh = Seventh_Window()
    widget.addWidget(window)
    widget.addWidget(second)
    widget.addWidget(third)
    # third3 들어가야함 + 할때 2
    widget.addWidget(forth)
    widget.addWidget(fifth)
    widget.addWidget(sixth)
    widget.addWidget(seventh)
    widget.setFixedHeight(1600)
    widget.setFixedWidth(900)
    widget.show()
    sys.exit(app.exec())

# basedir = os.path.dirname(__file__)

# app = QtWidgets.QApplication(sys.argv)
# ui_file = QFile('mainwindow.ui')
# loader = QUiLoader()
# window = loader.load(ui_file)
# ui_file.close()

# window.show()

# app.exec()
