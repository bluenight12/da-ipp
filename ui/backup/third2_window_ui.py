# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'third2_window.ui'
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
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Third2_Window(object):
    def setupUi(self, Third2_Window):
        if not Third2_Window.objectName():
            Third2_Window.setObjectName(u"Third2_Window")
        Third2_Window.resize(540, 960)
        self.gridLayout_2 = QGridLayout(Third2_Window)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.description = QLabel(Third2_Window)
        self.description.setObjectName(u"description")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.description.sizePolicy().hasHeightForWidth())
        self.description.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(30)
        font.setBold(False)
        font.setStrikeOut(False)
        self.description.setFont(font)
        self.description.setTextFormat(Qt.AutoText)
        self.description.setScaledContents(False)
        self.description.setAlignment(Qt.AlignCenter)
        self.description.setWordWrap(True)

        self.verticalLayout.addWidget(self.description)

        self.get_translate = QLabel(Third2_Window)
        self.get_translate.setObjectName(u"get_translate")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(3)
        sizePolicy1.setHeightForWidth(self.get_translate.sizePolicy().hasHeightForWidth())
        self.get_translate.setSizePolicy(sizePolicy1)
        self.get_translate.setMaximumSize(QSize(600, 600))
        self.get_translate.setScaledContents(False)

        self.verticalLayout.addWidget(self.get_translate)

        self.pushbutton = QPushButton(Third2_Window)
        self.pushbutton.setObjectName(u"pushbutton")

        self.verticalLayout.addWidget(self.pushbutton)

        self.go_forth = QPushButton(Third2_Window)
        self.go_forth.setObjectName(u"go_forth")

        self.verticalLayout.addWidget(self.go_forth)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Third2_Window)

        QMetaObject.connectSlotsByName(Third2_Window)
    # setupUi

    def retranslateUi(self, Third2_Window):
        Third2_Window.setWindowTitle(QCoreApplication.translate("Third2_Window", u"Form", None))
        self.description.setText(QCoreApplication.translate("Third2_Window", u"\uc544\ub798 \ubc84\ud2bc\uc744 \ub204\ub974\uace0 \uc6d0\ud558\ub294 \uc637\uc5d0 \ub300\ud574 \ub9d0\uc500\ud574\uc8fc\uc138\uc694", None))
        self.get_translate.setText("")
        self.pushbutton.setText(QCoreApplication.translate("Third2_Window", u"\ub9d0\ud558\uae30", None))
        self.go_forth.setText(QCoreApplication.translate("Third2_Window", u"\ub118\uc5b4\uac00\uae30", None))
    # retranslateUi

