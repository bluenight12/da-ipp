# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'final_result_new.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Second_Window(object):
    def setupUi(self, Second_Window):
        if not Second_Window.objectName():
            Second_Window.setObjectName(u"Second_Window")
        Second_Window.resize(920, 1644)
        self.gridLayout = QGridLayout(Second_Window)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.back1 = QLabel(Second_Window)
        self.back1.setObjectName(u"back1")
        self.back1.setMinimumSize(QSize(900, 70))
        self.back1.setMaximumSize(QSize(900, 70))
        font = QFont()
        font.setPointSize(15)
        self.back1.setFont(font)
        self.back1.setPixmap(QPixmap(u"../../Pictures/Screenshots/\ubc30\uacbd\uc774\ubbf8\uc9c0.png"))
        self.back1.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.back1)

        self.final_result = QLabel(Second_Window)
        self.final_result.setObjectName(u"final_result")
        self.final_result.setMinimumSize(QSize(720, 1280))
        self.final_result.setMaximumSize(QSize(720, 1280))
        self.final_result.setFont(font)
        self.final_result.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.final_result)

        self.clothes_info = QLabel(Second_Window)
        self.clothes_info.setObjectName(u"clothes_info")
        self.clothes_info.setMinimumSize(QSize(900, 90))
        self.clothes_info.setMaximumSize(QSize(900, 90))
        self.clothes_info.setFont(font)
        self.clothes_info.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.clothes_info)

        self.label_4 = QLabel(Second_Window)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(900, 90))
        self.label_4.setMaximumSize(QSize(900, 90))
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.back2 = QLabel(Second_Window)
        self.back2.setObjectName(u"back2")
        self.back2.setMinimumSize(QSize(900, 70))
        self.back2.setMaximumSize(QSize(900, 70))
        self.back2.setFont(font)
        self.back2.setPixmap(QPixmap(u"../../Pictures/Screenshots/\ubc30\uacbd\uc774\ubbf8\uc9c0.png"))
        self.back2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.back2)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 1)

        self.retranslateUi(Second_Window)

        QMetaObject.connectSlotsByName(Second_Window)
    # setupUi

    def retranslateUi(self, Second_Window):
        Second_Window.setWindowTitle(QCoreApplication.translate("Second_Window", u"Form", None))
        self.back1.setText("")
        self.final_result.setText(QCoreApplication.translate("Second_Window", u"\uc0ac\uc9c4", None))
        self.clothes_info.setText(QCoreApplication.translate("Second_Window", u"\uc637\uc815\ubcf4", None))
        self.label_4.setText(QCoreApplication.translate("Second_Window", u"\ub9c1\ud06c", None))
        self.back2.setText("")
    # retranslateUi

