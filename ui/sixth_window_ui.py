# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sixth_window.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Sixth_Window(object):
    def setupUi(self, Sixth_Window):
        if not Sixth_Window.objectName():
            Sixth_Window.setObjectName(u"Sixth_Window")
        Sixth_Window.resize(900, 1600)
        Sixth_Window.setMinimumSize(QSize(900, 1600))
        Sixth_Window.setMaximumSize(QSize(900, 1600))
        self.verticalLayout_2 = QVBoxLayout(Sixth_Window)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(Sixth_Window)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(0, 70))
        self.label_3.setMaximumSize(QSize(16777215, 70))
        self.label_3.setPixmap(QPixmap(u"backup/temp2/\ubc30\uacbd\uc774\ubbf8\uc9c0.png"))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(Sixth_Window)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(30)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_4)

        self.start = QPushButton(Sixth_Window)
        self.start.setObjectName(u"start")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.start.sizePolicy().hasHeightForWidth())
        self.start.setSizePolicy(sizePolicy1)
        self.start.setMaximumSize(QSize(16777215, 150))

        self.verticalLayout.addWidget(self.start)

        self.get_translate = QLabel(Sixth_Window)
        self.get_translate.setObjectName(u"get_translate")
        self.get_translate.setFont(font)
        self.get_translate.setAlignment(Qt.AlignCenter)
        self.get_translate.setWordWrap(True)

        self.verticalLayout.addWidget(self.get_translate)

        self.label_2 = QLabel(Sixth_Window)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 70))
        self.label_2.setMaximumSize(QSize(16777215, 70))
        self.label_2.setPixmap(QPixmap(u"backup/temp2/\ubc30\uacbd\uc774\ubbf8\uc9c0.png"))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.label_5 = QLabel(Sixth_Window)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_5)

        self.go_seventh = QPushButton(Sixth_Window)
        self.go_seventh.setObjectName(u"go_seventh")
        sizePolicy1.setHeightForWidth(self.go_seventh.sizePolicy().hasHeightForWidth())
        self.go_seventh.setSizePolicy(sizePolicy1)
        self.go_seventh.setMaximumSize(QSize(16777215, 150))
        self.go_seventh.setIconSize(QSize(16, 16))

        self.verticalLayout.addWidget(self.go_seventh)

        self.repeat = QPushButton(Sixth_Window)
        self.repeat.setObjectName(u"repeat")
        sizePolicy1.setHeightForWidth(self.repeat.sizePolicy().hasHeightForWidth())
        self.repeat.setSizePolicy(sizePolicy1)
        self.repeat.setMaximumSize(QSize(16777215, 150))

        self.verticalLayout.addWidget(self.repeat)

        self.back = QPushButton(Sixth_Window)
        self.back.setObjectName(u"back")
        sizePolicy1.setHeightForWidth(self.back.sizePolicy().hasHeightForWidth())
        self.back.setSizePolicy(sizePolicy1)
        self.back.setMaximumSize(QSize(16777215, 150))

        self.verticalLayout.addWidget(self.back)

        self.label = QLabel(Sixth_Window)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setMinimumSize(QSize(0, 70))
        self.label.setMaximumSize(QSize(16777215, 70))
        self.label.setPixmap(QPixmap(u"backup/temp2/\ubc30\uacbd\uc774\ubbf8\uc9c0.png"))
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 1)
        self.verticalLayout.setStretch(7, 1)
        self.verticalLayout.setStretch(8, 1)
        self.verticalLayout.setStretch(9, 1)

        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Sixth_Window)

        QMetaObject.connectSlotsByName(Sixth_Window)
    # setupUi

    def retranslateUi(self, Sixth_Window):
        Sixth_Window.setWindowTitle(QCoreApplication.translate("Sixth_Window", u"Form", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("Sixth_Window", u"START\ub97c \ub204\ub978 \ud6c4 \uc74c\uc131\uc744 \uc785\ub825\ud558\uc138\uc694.", None))
        self.start.setText(QCoreApplication.translate("Sixth_Window", u"START", None))
        self.get_translate.setText(QCoreApplication.translate("Sixth_Window", u"\uc0c1\ud0dc \ucc3d ex) \uc785\ub825\uc774 \uc798\ubabb\ub418\uc5c8\uc2b5\ub2c8\ub2e4 \ub2e4\uc2dc\ud574\uc8fc\uc138\uc694 \ub610\ub294 \uc81c\ub300\ub85c \uc785\ub825 \ub418\uc5c8\uc73c\uba74 \ubb38\uc790\ucd9c\ub825", None))
        self.label_2.setText("")
        self.label_5.setText(QCoreApplication.translate("Sixth_Window", u"\uc704\uc758 \ud14d\uc2a4\ud2b8\uac00 \ub9de\ub2e4\uba74 accept\uc744 \ub20c\ub7ec\uc8fc\uc138\uc694                           \ub2e4\uc2dc \uc785\ub825\ud558\ub824\uba74 repeat", None))
        self.go_seventh.setText(QCoreApplication.translate("Sixth_Window", u"ACCEPT", None))
        self.repeat.setText(QCoreApplication.translate("Sixth_Window", u"REPEAT", None))
        self.back.setText(QCoreApplication.translate("Sixth_Window", u"\ub3cc\uc544\uac00\uae30", None))
        self.label.setText("")
    # retranslateUi

