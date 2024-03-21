# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fifth_window.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QProgressBar,
    QPushButton, QSizePolicy, QWidget)

class Ui_Fifth_Window(object):
    def setupUi(self, Fifth_Window):
        if not Fifth_Window.objectName():
            Fifth_Window.setObjectName(u"Fifth_Window")
        Fifth_Window.resize(540, 960)
        Fifth_Window.setMinimumSize(QSize(540, 960))
        self.gridLayout_3 = QGridLayout(Fifth_Window)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Fifth_Window)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 2)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.finish_photo = QLabel(Fifth_Window)
        self.finish_photo.setObjectName(u"finish_photo")
        self.finish_photo.setMinimumSize(QSize(0, 450))
        self.finish_photo.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.finish_photo, 0, 0, 1, 1)

        self.progressBar = QProgressBar(Fifth_Window)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.gridLayout_4.addWidget(self.progressBar, 1, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_4, 1, 0, 1, 2)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_4 = QLabel(Fifth_Window)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_7.addWidget(self.label_4, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_7, 2, 0, 1, 2)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.done = QPushButton(Fifth_Window)
        self.done.setObjectName(u"done")
        self.done.setMinimumSize(QSize(0, 100))

        self.gridLayout_5.addWidget(self.done, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_5, 3, 0, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.sixth = QPushButton(Fifth_Window)
        self.sixth.setObjectName(u"sixth")
        self.sixth.setMinimumSize(QSize(0, 100))

        self.gridLayout_6.addWidget(self.sixth, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_6, 3, 1, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(Fifth_Window)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 4, 0, 1, 2)


        self.retranslateUi(Fifth_Window)

        QMetaObject.connectSlotsByName(Fifth_Window)
    # setupUi

    def retranslateUi(self, Fifth_Window):
        Fifth_Window.setWindowTitle(QCoreApplication.translate("Fifth_Window", u"Form", None))
        self.label.setText(QCoreApplication.translate("Fifth_Window", u"\ubc30\uacbd", None))
        self.finish_photo.setText(QCoreApplication.translate("Fifth_Window", u"\ucc29\uc7a5\uc0ac\uc9c4 png", None))
        self.label_4.setText(QCoreApplication.translate("Fifth_Window", u"\ubc30\uacbd\uc744 \ucd94\uac00\ud558\uace0 \uc2f6\uc73c\uc2dc\ub2e4\uba74 PLUS \uc544\ub2c8\uba74 DONE \ubc84\ud2bc \ub204\ub974\uc2dc\uc624 txt", None))
        self.done.setText(QCoreApplication.translate("Fifth_Window", u"DONE", None))
        self.sixth.setText(QCoreApplication.translate("Fifth_Window", u"PLUS", None))
        self.label_2.setText(QCoreApplication.translate("Fifth_Window", u"\ubc30\uacbd", None))
    # retranslateUi

