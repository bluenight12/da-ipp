# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLayout,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(540, 960)
        MainWindow.setMinimumSize(QSize(540, 960))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetNoConstraint)
        self.background = QLabel(self.centralwidget)
        self.background.setObjectName(u"background")
        self.background.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_3.addWidget(self.background)


        self.gridLayout.addLayout(self.verticalLayout_3, 2, 0, 1, 2)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.camera = QLabel(self.centralwidget)
        self.camera.setObjectName(u"camera")
        self.camera.setMinimumSize(QSize(320, 600))

        self.gridLayout_5.addWidget(self.camera, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_5, 1, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.txt = QLabel(self.centralwidget)
        self.txt.setObjectName(u"txt")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.txt.sizePolicy().hasHeightForWidth())
        self.txt.setSizePolicy(sizePolicy)
        self.txt.setMaximumSize(QSize(300, 100))

        self.verticalLayout_2.addWidget(self.txt)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.data = QLabel(self.centralwidget)
        self.data.setObjectName(u"data")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(10)
        sizePolicy1.setVerticalStretch(10)
        sizePolicy1.setHeightForWidth(self.data.sizePolicy().hasHeightForWidth())
        self.data.setSizePolicy(sizePolicy1)
        self.data.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_2.addWidget(self.data, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.Start = QPushButton(self.centralwidget)
        self.Start.setObjectName(u"Start")
        self.Start.setMinimumSize(QSize(0, 200))

        self.gridLayout_3.addWidget(self.Start, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_3)


        self.gridLayout.addLayout(self.verticalLayout_2, 1, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.teamname = QLabel(self.centralwidget)
        self.teamname.setObjectName(u"teamname")
        self.teamname.setMinimumSize(QSize(0, 100))
        self.teamname.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout.addWidget(self.teamname)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.background.setText(QCoreApplication.translate("MainWindow", u"\ubc30\uacbd \uc0ac\uc9c4", None))
        self.camera.setText(QCoreApplication.translate("MainWindow", u"CAMERA", None))
        self.txt.setText(QCoreApplication.translate("MainWindow", u"txt . \ub2f9\uc2e0\uc758 \uce21\uc815 \ub370\uc774\ud130", None))
        self.data.setText(QCoreApplication.translate("MainWindow", u"\uce21\uc815\ub41c \ub370\uc774\ud130", None))
        self.Start.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.teamname.setText(QCoreApplication.translate("MainWindow", u"\ud300 \uc774\ub984 \ubc0f \uc0ac\uc9c4", None))
    # retranslateUi

