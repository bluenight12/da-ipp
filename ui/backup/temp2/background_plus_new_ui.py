# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'background_plus_new.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QProgressBar, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Fifth_Window(object):
    def setupUi(self, Fifth_Window):
        if not Fifth_Window.objectName():
            Fifth_Window.setObjectName(u"Fifth_Window")
        Fifth_Window.resize(900, 1600)
        Fifth_Window.setMinimumSize(QSize(900, 1600))
        Fifth_Window.setMaximumSize(QSize(900, 1600))
        self.verticalLayout_2 = QVBoxLayout(Fifth_Window)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(Fifth_Window)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 70))
        self.label_2.setMaximumSize(QSize(16777215, 70))
        self.label_2.setPixmap(QPixmap(u"\ubc30\uacbd\uc774\ubbf8\uc9c0.png"))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.photo = QLabel(Fifth_Window)
        self.photo.setObjectName(u"photo")
        self.photo.setMaximumSize(QSize(16777215, 1000))
        self.photo.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.photo)

        self.label_3 = QLabel(Fifth_Window)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 200))
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_3)

        self.progressBar = QProgressBar(Fifth_Window)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout.addWidget(self.progressBar)

        self.done = QPushButton(Fifth_Window)
        self.done.setObjectName(u"done")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.done.sizePolicy().hasHeightForWidth())
        self.done.setSizePolicy(sizePolicy)
        self.done.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout.addWidget(self.done)

        self.plus = QPushButton(Fifth_Window)
        self.plus.setObjectName(u"plus")
        sizePolicy.setHeightForWidth(self.plus.sizePolicy().hasHeightForWidth())
        self.plus.setSizePolicy(sizePolicy)
        self.plus.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout.addWidget(self.plus)

        self.go_first = QPushButton(Fifth_Window)
        self.go_first.setObjectName(u"go_first")
        sizePolicy.setHeightForWidth(self.go_first.sizePolicy().hasHeightForWidth())
        self.go_first.setSizePolicy(sizePolicy)
        self.go_first.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout.addWidget(self.go_first)

        self.label = QLabel(Fifth_Window)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 70))
        self.label.setMaximumSize(QSize(16777215, 70))
        self.label.setPixmap(QPixmap(u"\ubc30\uacbd\uc774\ubbf8\uc9c0.png"))
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 4)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 1)
        self.verticalLayout.setStretch(7, 1)

        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Fifth_Window)

        QMetaObject.connectSlotsByName(Fifth_Window)
    # setupUi

    def retranslateUi(self, Fifth_Window):
        Fifth_Window.setWindowTitle(QCoreApplication.translate("Fifth_Window", u"Form", None))
        self.label_2.setText("")
        self.photo.setText(QCoreApplication.translate("Fifth_Window", u"\ucc29\uc7a5\uc0ac\uc9c4 png", None))
        self.label_3.setText(QCoreApplication.translate("Fifth_Window", u"\ubc30\uacbd\uc744 \ucd94\uac00\ud558\uace0 \uc2f6\uc73c\uc2dc\ub2e4\uba74 PLUS \uc544\ub2c8\uba74 DONE \ubc84\ud2bc \ub204\ub974\uc2dc\uc624 txt", None))
        self.done.setText(QCoreApplication.translate("Fifth_Window", u"DONE", None))
        self.plus.setText(QCoreApplication.translate("Fifth_Window", u"PLUS", None))
        self.go_first.setText(QCoreApplication.translate("Fifth_Window", u"\uc81c\uc77c \ucc98\uc74c\uc73c\ub85c \ub3cc\uc544\uac00\uae30", None))
        self.label.setText("")
    # retranslateUi

