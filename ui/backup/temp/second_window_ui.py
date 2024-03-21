# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'second_window.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(540, 960)
        Form.setMinimumSize(QSize(540, 960))
        self.gridLayout_21 = QGridLayout(Form)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.background_2 = QLabel(Form)
        self.background_2.setObjectName(u"background_2")
        self.background_2.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.background_2, 0, 0, 1, 1)


        self.gridLayout_21.addLayout(self.gridLayout_4, 0, 0, 1, 2)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.select_2 = QPushButton(Form)
        self.select_2.setObjectName(u"select_2")
        self.select_2.setMinimumSize(QSize(0, 45))

        self.gridLayout_9.addWidget(self.select_2, 0, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_9, 1, 0, 1, 1)

        self.text_2 = QLabel(Form)
        self.text_2.setObjectName(u"text_2")
        self.text_2.setMinimumSize(QSize(100, 100))

        self.gridLayout_8.addWidget(self.text_2, 0, 0, 1, 1, Qt.AlignHCenter)


        self.gridLayout_7.addLayout(self.gridLayout_8, 1, 0, 1, 1)

        self.clothes_2 = QLabel(Form)
        self.clothes_2.setObjectName(u"clothes_2")
        self.clothes_2.setMinimumSize(QSize(100, 360))
        self.clothes_2.setMaximumSize(QSize(16777215, 360))

        self.gridLayout_7.addWidget(self.clothes_2, 0, 0, 1, 1)


        self.gridLayout_21.addLayout(self.gridLayout_7, 2, 0, 1, 1)

        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.text_4 = QLabel(Form)
        self.text_4.setObjectName(u"text_4")
        self.text_4.setMinimumSize(QSize(100, 100))

        self.gridLayout_17.addWidget(self.text_4, 0, 0, 1, 1, Qt.AlignHCenter)

        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.select_4 = QPushButton(Form)
        self.select_4.setObjectName(u"select_4")
        self.select_4.setMinimumSize(QSize(0, 45))

        self.gridLayout_18.addWidget(self.select_4, 0, 0, 1, 1)


        self.gridLayout_17.addLayout(self.gridLayout_18, 1, 0, 1, 1)


        self.gridLayout_16.addLayout(self.gridLayout_17, 1, 0, 1, 1)

        self.clothes_4 = QLabel(Form)
        self.clothes_4.setObjectName(u"clothes_4")
        self.clothes_4.setMinimumSize(QSize(100, 360))
        self.clothes_4.setMaximumSize(QSize(16777215, 360))

        self.gridLayout_16.addWidget(self.clothes_4, 0, 0, 1, 1)


        self.gridLayout_21.addLayout(self.gridLayout_16, 2, 1, 1, 1)

        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 50))
        self.pushButton_4.setMaximumSize(QSize(16777215, 60))

        self.gridLayout_19.addWidget(self.pushButton_4, 0, 0, 1, 1)


        self.gridLayout_21.addLayout(self.gridLayout_19, 3, 0, 1, 2)

        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 50))
        self.pushButton_3.setMaximumSize(QSize(16777215, 60))

        self.gridLayout_15.addWidget(self.pushButton_3, 0, 0, 1, 1)


        self.gridLayout_21.addLayout(self.gridLayout_15, 4, 0, 1, 2)

        self.gridLayout_20 = QGridLayout()
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.txt_2 = QLabel(Form)
        self.txt_2.setObjectName(u"txt_2")
        self.txt_2.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_20.addWidget(self.txt_2, 0, 0, 1, 1)


        self.gridLayout_21.addLayout(self.gridLayout_20, 1, 0, 1, 2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.background_2.setText(QCoreApplication.translate("Form", u"\ubc30\uacbd", None))
        self.select_2.setText(QCoreApplication.translate("Form", u"\uc120\ud0dd\ud558\uae30(\uc637\uc785\ud788\uae30)", None))
        self.text_2.setText(QCoreApplication.translate("Form", u"         \ucd94\ucc9c 1", None))
        self.clothes_2.setText(QCoreApplication.translate("Form", u"\uc0ac\uc9c4", None))
        self.text_4.setText(QCoreApplication.translate("Form", u"         \ucd94\ucc9c 2", None))
        self.select_4.setText(QCoreApplication.translate("Form", u"\uc120\ud0dd\ud558\uae30(\uc637\uc785\ud788\uae30)", None))
        self.clothes_4.setText(QCoreApplication.translate("Form", u"\uc0ac\uc9c4", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\ub2e4\uc2dc \ucd94\ucc9c \ubc1b\uae30", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\ub0b4\uac00 \uc6d0\ud558\ub294 \uc637 \ucd94\ucc9c\ubc1b\uae30 (\uc74c\uc131\ucd94\ucc9c)", None))
        self.txt_2.setText(QCoreApplication.translate("Form", u"\ub2f9\uc2e0\uc5d0\uac8c \uc5b4\uc6b8\ub9ac\ub294 \uc637 \ucd94\ucc9c", None))
    # retranslateUi

