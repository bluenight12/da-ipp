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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_Second_Window(object):
    def setupUi(self, Second_Window):
        if not Second_Window.objectName():
            Second_Window.setObjectName(u"Second_Window")
        Second_Window.resize(540, 960)
        self.gridLayout = QGridLayout(Second_Window)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.go_third_first = QPushButton(Second_Window)
        self.go_third_first.setObjectName(u"go_third_first")
        self.go_third_first.setMaximumSize(QSize(300, 300))

        self.horizontalLayout.addWidget(self.go_third_first)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.go_third_second = QPushButton(Second_Window)
        self.go_third_second.setObjectName(u"go_third_second")
        self.go_third_second.setMaximumSize(QSize(300, 300))

        self.horizontalLayout.addWidget(self.go_third_second)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.scrollArea = QScrollArea(Second_Window)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 520, 466))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_4 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(200, 0))
        self.label.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_4.addWidget(self.label)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.retranslateUi(Second_Window)

        QMetaObject.connectSlotsByName(Second_Window)
    # setupUi

    def retranslateUi(self, Second_Window):
        Second_Window.setWindowTitle(QCoreApplication.translate("Second_Window", u"Form", None))
        self.go_third_first.setText(QCoreApplication.translate("Second_Window", u"PushButton", None))
        self.go_third_second.setText(QCoreApplication.translate("Second_Window", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("Second_Window", u"TextLabel", None))
    # retranslateUi

