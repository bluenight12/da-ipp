# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'final_page.ui'
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
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(540, 960)
        Form.setMinimumSize(QSize(540, 960))
        self.gridLayout_10 = QGridLayout(Form)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.clothes_info = QLabel(Form)
        self.clothes_info.setObjectName(u"clothes_info")
        self.clothes_info.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.clothes_info, 0, 0, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_2, 2, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.link = QLabel(Form)
        self.link.setObjectName(u"link")
        self.link.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.link, 1, 0, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_4, 3, 0, 1, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.background = QLabel(Form)
        self.background.setObjectName(u"background")
        self.background.setMinimumSize(QSize(0, 30))

        self.gridLayout_9.addWidget(self.background, 0, 0, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_9, 4, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.backgorund = QLabel(Form)
        self.backgorund.setObjectName(u"backgorund")
        self.backgorund.setMinimumSize(QSize(0, 30))

        self.gridLayout.addWidget(self.backgorund, 0, 0, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.final_image = QLabel(Form)
        self.final_image.setObjectName(u"final_image")
        self.final_image.setMinimumSize(QSize(0, 500))

        self.gridLayout_5.addWidget(self.final_image, 0, 0, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_5, 1, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.clothes_info.setText(QCoreApplication.translate("Form", u"\uc637 \uc815\ubcf4", None))
        self.link.setText(QCoreApplication.translate("Form", u"\ub9c1\ud06c\uc8fc\uc18c", None))
        self.background.setText(QCoreApplication.translate("Form", u"\ubc30\uacbd", None))
        self.backgorund.setText(QCoreApplication.translate("Form", u"\ubc30\uacbd", None))
        self.final_image.setText(QCoreApplication.translate("Form", u"\ucd5c\uc885 \uc774\ubbf8\uc9c0", None))
    # retranslateUi

