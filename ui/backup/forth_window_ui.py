# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'forth_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Forth_Window(object):
    def setupUi(self, Forth_Window):
        if not Forth_Window.objectName():
            Forth_Window.setObjectName(u"Forth_Window")
        Forth_Window.resize(540, 976)
        Forth_Window.setMinimumSize(QSize(540, 960))
        Forth_Window.setMaximumSize(QSize(5000, 16777215))
        self.gridLayout_8 = QGridLayout(Forth_Window)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.deco_2 = QLabel(Forth_Window)
        self.deco_2.setObjectName(u"deco_2")
        self.deco_2.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_6.addWidget(self.deco_2, 0, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_6, 0, 0, 1, 2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.photo = QLabel(Forth_Window)
        self.photo.setObjectName(u"photo")
        self.photo.setMinimumSize(QSize(300, 400))
        self.photo.setScaledContents(True)

        self.gridLayout.addWidget(self.photo, 0, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout, 1, 0, 4, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.txt = QLabel(Forth_Window)
        self.txt.setObjectName(u"txt")
        self.txt.setMinimumSize(QSize(0, 100))
        self.txt.setMaximumSize(QSize(200, 100))

        self.gridLayout_2.addWidget(self.txt, 1, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_2, 1, 1, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pose = QLabel(Forth_Window)
        self.pose.setObjectName(u"pose")
        self.pose.setMinimumSize(QSize(0, 400))
        self.pose.setMaximumSize(QSize(200, 64440))

        self.gridLayout_5.addWidget(self.pose, 0, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_5, 2, 1, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pushButton = QPushButton(Forth_Window)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 50))
        self.pushButton.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_4.addWidget(self.pushButton, 0, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_4, 3, 1, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.retake = QPushButton(Forth_Window)
        self.retake.setObjectName(u"retake")
        self.retake.setMinimumSize(QSize(0, 50))
        self.retake.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_7.addWidget(self.retake, 0, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_7, 4, 1, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.deco = QLabel(Forth_Window)
        self.deco.setObjectName(u"deco")
        self.deco.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_3.addWidget(self.deco, 0, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_3, 5, 0, 1, 2)


        self.retranslateUi(Forth_Window)

        QMetaObject.connectSlotsByName(Forth_Window)
    # setupUi

    def retranslateUi(self, Forth_Window):
        Forth_Window.setWindowTitle(QCoreApplication.translate("Forth_Window", u"Form", None))
        self.deco_2.setText(QCoreApplication.translate("Forth_Window", u"\uafb8\ubbf8\uae30 \ubc30\uacbd", None))
        self.photo.setText(QCoreApplication.translate("Forth_Window", u"camera", None))
        self.txt.setText(QCoreApplication.translate("Forth_Window", u"\uc120\ud0dd\ud55c \uc637\uc774 \ub9de\ub2e4\uba74 START\ub97c \ub204\ub974\uace0 \uc544\ub798\uc758 \ud3ec\uc988\ub97c  \ucde8\ud558\uc2dc\uc624 ", None))
        self.pose.setText(QCoreApplication.translate("Forth_Window", u"\uc608\uc81c\ud3ec\uc988", None))
        self.pushButton.setText(QCoreApplication.translate("Forth_Window", u"START", None))
        self.retake.setText(QCoreApplication.translate("Forth_Window", u"\ub2e4\uc2dc\uc120\ud0dd", None))
        self.deco.setText(QCoreApplication.translate("Forth_Window", u"\uafb8\ubbf8\uae30 \ubc30\uacbd", None))
    # retranslateUi

