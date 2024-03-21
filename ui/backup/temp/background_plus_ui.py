# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'background_plus.ui'
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
        self.gridLayout_3 = QGridLayout(Form)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 2)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 450))

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_4, 1, 0, 1, 2)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_7.addWidget(self.label_4, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_7, 2, 0, 1, 2)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 100))

        self.gridLayout_5.addWidget(self.pushButton, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_5, 3, 0, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 100))

        self.gridLayout_6.addWidget(self.pushButton_2, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_6, 3, 1, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 4, 0, 1, 2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\ubc30\uacbd", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\ucc29\uc7a5\uc0ac\uc9c4 png", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\ubc30\uacbd\uc744 \ucd94\uac00\ud558\uace0 \uc2f6\uc73c\uc2dc\ub2e4\uba74 PLUS \uc544\ub2c8\uba74 DONE \ubc84\ud2bc \ub204\ub974\uc2dc\uc624 txt", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"DONE", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"PLUS", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\ubc30\uacbd", None))
    # retranslateUi

