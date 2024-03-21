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
        MainWindow.resize(900, 1600)
        MainWindow.setMinimumSize(QSize(900, 1600))
        MainWindow.setMaximumSize(QSize(900, 1600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.go_third = QPushButton(self.centralwidget)
        self.go_third.setObjectName(u"go_third")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.go_third.sizePolicy().hasHeightForWidth())
        self.go_third.setSizePolicy(sizePolicy)
        self.go_third.setMinimumSize(QSize(420, 250))
        self.go_third.setMaximumSize(QSize(420, 250))

        self.gridLayout.addWidget(self.go_third, 3, 1, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.camera = QLabel(self.centralwidget)
        self.camera.setObjectName(u"camera")
        self.camera.setMinimumSize(QSize(720, 960))
        self.camera.setMaximumSize(QSize(720, 960))
        self.camera.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.camera, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_5, 2, 0, 1, 2)

        self.go_second = QPushButton(self.centralwidget)
        self.go_second.setObjectName(u"go_second")
        sizePolicy.setHeightForWidth(self.go_second.sizePolicy().hasHeightForWidth())
        self.go_second.setSizePolicy(sizePolicy)
        self.go_second.setMinimumSize(QSize(440, 250))
        self.go_second.setMaximumSize(QSize(440, 250))

        self.gridLayout.addWidget(self.go_second, 3, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetNoConstraint)
        self.teamname_2 = QLabel(self.centralwidget)
        self.teamname_2.setObjectName(u"teamname_2")
        self.teamname_2.setMinimumSize(QSize(0, 70))
        self.teamname_2.setMaximumSize(QSize(16777215, 70))
        self.teamname_2.setPixmap(QPixmap(u"temp2/\ubc30\uacbd\uc774\ubbf8\uc9c0.png"))

        self.verticalLayout_3.addWidget(self.teamname_2)


        self.gridLayout.addLayout(self.verticalLayout_3, 4, 0, 1, 2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.teamname = QLabel(self.centralwidget)
        self.teamname.setObjectName(u"teamname")
        self.teamname.setMinimumSize(QSize(0, 70))
        self.teamname.setMaximumSize(QSize(16777215, 70))
        self.teamname.setPixmap(QPixmap(u"temp2/\ubc30\uacbd\uc774\ubbf8\uc9c0.png"))

        self.verticalLayout.addWidget(self.teamname)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 2)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Z003 [UKWN]"])
        font.setPointSize(50)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_4, 1, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.go_third.setText(QCoreApplication.translate("MainWindow", u"\uae30\uc874 \ucd94\ucc9c \ubc1b\uae30", None))
        self.camera.setText(QCoreApplication.translate("MainWindow", u"CAMERA", None))
        self.go_second.setText(QCoreApplication.translate("MainWindow", u"\uc74c\uc131\uc73c\ub85c \ucd94\ucc9c \ubc1b\uae30", None))
        self.teamname_2.setText("")
        self.teamname.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"DA - IPP", None))
    # retranslateUi

