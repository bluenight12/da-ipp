# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'third_window_new.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(900, 1600)
        Form.setMinimumSize(QSize(900, 1600))
        Form.setMaximumSize(QSize(900, 1600))
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 70))
        self.label.setMaximumSize(QSize(16777215, 70))
        self.label.setPixmap(QPixmap(u"\ubc30\uacbd\uc774\ubbf8\uc9c0.png"))
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 200))
        font = QFont()
        font.setPointSize(25)
        self.label_2.setFont(font)
        self.label_2.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setFrameShape(QFrame.NoFrame)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.label_2)


        self.verticalLayout_3.addLayout(self.verticalLayout_8)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.cloth1 = QLabel(Form)
        self.cloth1.setObjectName(u"cloth1")
        self.cloth1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.cloth1)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_9)

        self.cloth1_select = QPushButton(Form)
        self.cloth1_select.setObjectName(u"cloth1_select")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cloth1_select.sizePolicy().hasHeightForWidth())
        self.cloth1_select.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(20)
        self.cloth1_select.setFont(font1)

        self.verticalLayout_17.addWidget(self.cloth1_select)

        self.verticalLayout_17.setStretch(0, 4)
        self.verticalLayout_17.setStretch(1, 1)
        self.verticalLayout_17.setStretch(2, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_17)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.cloth2 = QLabel(Form)
        self.cloth2.setObjectName(u"cloth2")
        self.cloth2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.cloth2)

        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_11)

        self.cloth2_select = QPushButton(Form)
        self.cloth2_select.setObjectName(u"cloth2_select")
        sizePolicy.setHeightForWidth(self.cloth2_select.sizePolicy().hasHeightForWidth())
        self.cloth2_select.setSizePolicy(sizePolicy)
        self.cloth2_select.setFont(font1)

        self.verticalLayout_16.addWidget(self.cloth2_select)

        self.verticalLayout_16.setStretch(0, 4)
        self.verticalLayout_16.setStretch(1, 1)
        self.verticalLayout_16.setStretch(2, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_16)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.cloth3 = QLabel(Form)
        self.cloth3.setObjectName(u"cloth3")
        self.cloth3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.cloth3)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_7)

        self.cloth3_select = QPushButton(Form)
        self.cloth3_select.setObjectName(u"cloth3_select")
        sizePolicy.setHeightForWidth(self.cloth3_select.sizePolicy().hasHeightForWidth())
        self.cloth3_select.setSizePolicy(sizePolicy)
        self.cloth3_select.setFont(font1)

        self.verticalLayout_15.addWidget(self.cloth3_select)

        self.verticalLayout_15.setStretch(0, 4)
        self.verticalLayout_15.setStretch(1, 1)
        self.verticalLayout_15.setStretch(2, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_15)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.recommend = QPushButton(Form)
        self.recommend.setObjectName(u"recommend")
        sizePolicy.setHeightForWidth(self.recommend.sizePolicy().hasHeightForWidth())
        self.recommend.setSizePolicy(sizePolicy)
        self.recommend.setMinimumSize(QSize(0, 100))
        self.recommend.setMaximumSize(QSize(16777215, 80))

        self.verticalLayout_10.addWidget(self.recommend)

        self.back = QPushButton(Form)
        self.back.setObjectName(u"back")
        sizePolicy.setHeightForWidth(self.back.sizePolicy().hasHeightForWidth())
        self.back.setSizePolicy(sizePolicy)
        self.back.setMinimumSize(QSize(0, 100))
        self.back.setMaximumSize(QSize(16777215, 80))

        self.verticalLayout_10.addWidget(self.back)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 70))
        self.label_3.setMaximumSize(QSize(16777215, 70))
        self.label_3.setPixmap(QPixmap(u"\ubc30\uacbd\uc774\ubbf8\uc9c0.png"))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_3)


        self.verticalLayout_3.addLayout(self.verticalLayout_10)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 4)
        self.verticalLayout_3.setStretch(2, 2)

        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"\ub2f9\uc2e0\uc5d0\uac8c \uc5b4\uc6b8\ub9ac\ub294 \uc637 \ucd94\ucc9c", None))
        self.cloth1.setText(QCoreApplication.translate("Form", u"\uc637 \uc0ac\uc9c4 1", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\ucd94\ucc9c 1 ", None))
        self.cloth1_select.setText(QCoreApplication.translate("Form", u"\uc120\ud0dd\ud558\uae30", None))
        self.cloth2.setText(QCoreApplication.translate("Form", u"\uc637 \uc0ac\uc9c4 2", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\ucd94\ucc9c 2", None))
        self.cloth2_select.setText(QCoreApplication.translate("Form", u"\uc120\ud0dd\ud558\uae30", None))
        self.cloth3.setText(QCoreApplication.translate("Form", u"\uc637 \uc0ac\uc9c4 3", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\ucd94\ucc9c 3", None))
        self.cloth3_select.setText(QCoreApplication.translate("Form", u"\uc120\ud0dd\ud558\uae30", None))
        self.recommend.setText(QCoreApplication.translate("Form", u"\ub2e4\uc2dc \ucd94\ucc9c \ubc1b\uae30", None))
        self.back.setText(QCoreApplication.translate("Form", u"\ub3cc\uc544\uac00\uae30", None))
        self.label_3.setText("")
    # retranslateUi

