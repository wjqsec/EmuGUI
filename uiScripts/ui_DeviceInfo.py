# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DeviceInfo.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(650, 710)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 631, 691))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.textBrowser = QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout.addWidget(self.textBrowser)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.textBrowser_2 = QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser_2.setObjectName(u"textBrowser_2")

        self.verticalLayout.addWidget(self.textBrowser_2)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout.addWidget(self.label_3)

        self.textBrowser_3 = QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser_3.setObjectName(u"textBrowser_3")

        self.verticalLayout.addWidget(self.textBrowser_3)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout.addWidget(self.label_4)

        self.textBrowser_4 = QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser_4.setObjectName(u"textBrowser_4")

        self.verticalLayout.addWidget(self.textBrowser_4)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout.addWidget(self.label_5)

        self.textBrowser_5 = QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser_5.setObjectName(u"textBrowser_5")

        self.verticalLayout.addWidget(self.textBrowser_5)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u4eff\u771f\u7c7b\u578b\u4fe1\u606f", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u4eff\u771f\u73af\u5883\u4fe1\u606f", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u4eff\u771f\u6846\u67b6\u4fe1\u606f", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u4eff\u771f\u6a21\u677f\u7c7b\u578b\u4fe1\u606f", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u5916\u8bbe\u7ec4\u4ef6\u4fe1\u606f", None))
    # retranslateUi

