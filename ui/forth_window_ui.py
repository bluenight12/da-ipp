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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Forth_Window(object):
    def setupUi(self, Forth_Window):
        if not Forth_Window.objectName():
            Forth_Window.setObjectName(u"Forth_Window")
        Forth_Window.resize(900, 1600)
        Forth_Window.setMinimumSize(QSize(900, 1600))
        Forth_Window.setMaximumSize(QSize(900, 1600))
        self.gridLayout_7 = QGridLayout(Forth_Window)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.count = QLabel(Forth_Window)
        self.count.setObjectName(u"count")
        self.count.setMinimumSize(QSize(0, 70))
        self.count.setMaximumSize(QSize(16777215, 70))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        self.count.setFont(font)
        self.count.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.count, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout, 0, 0, 1, 3)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.camera = QLabel(Forth_Window)
        self.camera.setObjectName(u"camera")
        self.camera.setMinimumSize(QSize(720, 960))
        self.camera.setMaximumSize(QSize(720, 960))
        self.camera.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.camera, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_3, 1, 0, 1, 3)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_3 = QLabel(Forth_Window)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(280, 350))
        self.label_3.setMaximumSize(QSize(280, 350))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_4, 2, 0, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_4 = QLabel(Forth_Window)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(280, 100))
        self.label_4.setMaximumSize(QSize(280, 100))
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setWordWrap(True)

        self.gridLayout_5.addWidget(self.label_4, 0, 0, 1, 1)

        self.cloth = QLabel(Forth_Window)
        self.cloth.setObjectName(u"cloth")
        self.cloth.setMinimumSize(QSize(280, 245))
        self.cloth.setMaximumSize(QSize(280, 245))
        self.cloth.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.cloth, 1, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_5, 2, 1, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.back = QPushButton(Forth_Window)
        self.back.setObjectName(u"back")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back.sizePolicy().hasHeightForWidth())
        self.back.setSizePolicy(sizePolicy)

        self.gridLayout_6.addWidget(self.back, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.retake = QPushButton(Forth_Window)
        self.retake.setObjectName(u"retake")
        sizePolicy.setHeightForWidth(self.retake.sizePolicy().hasHeightForWidth())
        self.retake.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.retake)

        self.go_next = QPushButton(Forth_Window)
        self.go_next.setObjectName(u"go_next")
        sizePolicy.setHeightForWidth(self.go_next.sizePolicy().hasHeightForWidth())
        self.go_next.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.go_next)


        self.gridLayout_6.addLayout(self.horizontalLayout, 1, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_6, 2, 2, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(Forth_Window)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 70))
        self.label_2.setMaximumSize(QSize(16777215, 70))
        self.label_2.setPixmap(QPixmap(u"../../Downloads/\ubc30\uacbd\uc774\ubbf8\uc9c0.png"))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_2, 3, 0, 1, 3)


        self.retranslateUi(Forth_Window)

        QMetaObject.connectSlotsByName(Forth_Window)
    # setupUi

    def retranslateUi(self, Forth_Window):
        Forth_Window.setWindowTitle(QCoreApplication.translate("Forth_Window", u"Form", None))
        self.count.setText("")
        self.camera.setText(QCoreApplication.translate("Forth_Window", u"camera", None))
        self.label_3.setText(QCoreApplication.translate("Forth_Window", u"\uc608\uc81c \ud3ec\uc988", None))
        self.label_4.setText(QCoreApplication.translate("Forth_Window", u"\uc120\ud0dd\ud55c \uc758\uc0c1\uc774 \ub9de\ub2e4\uba74 Take\ub97c \ub20c\ub7ec\uc8fc\uc138\uc694", None))
        self.cloth.setText(QCoreApplication.translate("Forth_Window", u"\uc758\ub958 \uc0ac\uc9c4 .png", None))
        self.back.setText(QCoreApplication.translate("Forth_Window", u"\ub3cc\uc544\uac00\uae30", None))
        self.retake.setText(QCoreApplication.translate("Forth_Window", u"ReTake", None))
        self.go_next.setText(QCoreApplication.translate("Forth_Window", u"Next", None))
        self.label_2.setText("")
    # retranslateUi

