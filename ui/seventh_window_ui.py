# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'seventh_window.ui'
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
    QProgressBar, QPushButton, QSizePolicy, QWidget)

class Ui_Seventh_Window(object):
    def setupUi(self, Seventh_Window):
        if not Seventh_Window.objectName():
            Seventh_Window.setObjectName(u"Seventh_Window")
        Seventh_Window.resize(900, 1600)
        Seventh_Window.setMinimumSize(QSize(900, 1600))
        Seventh_Window.setMaximumSize(QSize(900, 1600))
        self.gridLayout_7 = QGridLayout(Seventh_Window)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.progressBar = QProgressBar(Seventh_Window)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(True)
        self.progressBar.setValue(0)

        self.gridLayout_7.addWidget(self.progressBar, 2, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(Seventh_Window)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 70))
        self.label_3.setMaximumSize(QSize(16777215, 70))
        self.label_3.setPixmap(QPixmap(u"../../Downloads/\ubc30\uacbd\uc774\ubbf8\uc9c0.png"))

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_3, 5, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Seventh_Window)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 70))
        self.label.setMaximumSize(QSize(16777215, 70))
        self.label.setPixmap(QPixmap(u"../../Downloads/\ubc30\uacbd\uc774\ubbf8\uc9c0.png"))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(Seventh_Window)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setFamilies([u"aakar"])
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_4)

        self.qrcode = QLabel(Seventh_Window)
        self.qrcode.setObjectName(u"qrcode")
        self.qrcode.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.qrcode)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)

        self.gridLayout_5.addLayout(self.horizontalLayout, 1, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_5, 3, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.photo = QLabel(Seventh_Window)
        self.photo.setObjectName(u"photo")
        self.photo.setMinimumSize(QSize(720, 960))
        self.photo.setMaximumSize(QSize(720, 960))
        font1 = QFont()
        font1.setPointSize(50)
        self.photo.setFont(font1)
        self.photo.setAlignment(Qt.AlignCenter)
        self.photo.setWordWrap(True)

        self.gridLayout_2.addWidget(self.photo, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.go_first = QPushButton(Seventh_Window)
        self.go_first.setObjectName(u"go_first")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.go_first.sizePolicy().hasHeightForWidth())
        self.go_first.setSizePolicy(sizePolicy)
        self.go_first.setMinimumSize(QSize(0, 100))
        self.go_first.setMaximumSize(QSize(16777215, 100))

        self.gridLayout_4.addWidget(self.go_first, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_4, 4, 0, 1, 1)


        self.retranslateUi(Seventh_Window)

        QMetaObject.connectSlotsByName(Seventh_Window)
    # setupUi

    def retranslateUi(self, Seventh_Window):
        Seventh_Window.setWindowTitle(QCoreApplication.translate("Seventh_Window", u"Form", None))
        self.label_3.setText("")
        self.label.setText("")
        self.label_4.setText(QCoreApplication.translate("Seventh_Window", u"\uad6c\ub9e4 \ub9c1\ud06c", None))
        self.qrcode.setText(QCoreApplication.translate("Seventh_Window", u"TextLabel", None))
        self.photo.setText(QCoreApplication.translate("Seventh_Window", u"\uc7a0\uc2dc\ub9cc \uae30\ub2e4\ub824\uc8fc\uc138\uc694", None))
        self.go_first.setText(QCoreApplication.translate("Seventh_Window", u"\ub2e4\uc2dc \ud558\uae30", None))
    # retranslateUi

