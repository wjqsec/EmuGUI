# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EditVM.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpinBox, QStackedWidget, QTabWidget,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(813, 474)
        Dialog.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 811, 421))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayoutWidget = QWidget(self.tab)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 791, 371))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.comboBox = QComboBox(self.gridLayoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.stackedWidget = QStackedWidget(self.tab_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 801, 391))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayoutWidget_7 = QWidget(self.page)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(10, 10, 781, 371))
        self.gridLayout_7 = QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.gridLayoutWidget_7)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_7.addWidget(self.label_17, 0, 0, 1, 1)

        self.label_19 = QLabel(self.gridLayoutWidget_7)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_7.addWidget(self.label_19, 1, 0, 1, 1)

        self.label_18 = QLabel(self.gridLayoutWidget_7)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_7.addWidget(self.label_18, 2, 0, 1, 1)

        self.comboBox_11 = QComboBox(self.gridLayoutWidget_7)
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.setObjectName(u"comboBox_11")

        self.gridLayout_7.addWidget(self.comboBox_11, 0, 1, 1, 1)

        self.spinBox_2 = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMaximum(32768)

        self.gridLayout_7.addWidget(self.spinBox_2, 1, 1, 1, 1)

        self.comboBox_12 = QComboBox(self.gridLayoutWidget_7)
        self.comboBox_12.setObjectName(u"comboBox_12")

        self.gridLayout_7.addWidget(self.comboBox_12, 2, 1, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayoutWidget_2 = QWidget(self.tab_3)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 10, 781, 371))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_2.addWidget(self.pushButton_3, 1, 2, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)

        self.spinBox = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(214748368)

        self.gridLayout_2.addWidget(self.spinBox, 3, 1, 1, 1)

        self.comboBox_4 = QComboBox(self.gridLayoutWidget_2)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.gridLayout_2.addWidget(self.comboBox_4, 3, 2, 1, 1)

        self.comboBox_2 = QComboBox(self.gridLayoutWidget_2)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_2.addWidget(self.comboBox_2, 0, 1, 1, 2)

        self.comboBox_3 = QComboBox(self.gridLayoutWidget_2)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout_2.addWidget(self.comboBox_3, 2, 1, 1, 2)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayoutWidget_3 = QWidget(self.tab_5)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 10, 781, 371))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.gridLayoutWidget_3)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)

        self.comboBox_5 = QComboBox(self.gridLayoutWidget_3)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.gridLayout_3.addWidget(self.comboBox_5, 0, 1, 1, 1)

        self.comboBox_6 = QComboBox(self.gridLayoutWidget_3)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.gridLayout_3.addWidget(self.comboBox_6, 1, 1, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget_3)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 1, 0, 1, 1)

        self.checkBox_2 = QCheckBox(self.gridLayoutWidget_3)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout_3.addWidget(self.checkBox_2, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayoutWidget_5 = QWidget(self.tab_6)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(10, 10, 781, 371))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_4 = QLineEdit(self.gridLayoutWidget_5)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_5.addWidget(self.lineEdit_4, 1, 1, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setWordWrap(True)

        self.gridLayout_5.addWidget(self.label_11, 0, 0, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setWordWrap(True)

        self.gridLayout_5.addWidget(self.label_12, 1, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.gridLayoutWidget_5)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_5.addWidget(self.pushButton_4, 1, 2, 1, 1)

        self.lineEdit_3 = QLineEdit(self.gridLayoutWidget_5)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_5.addWidget(self.lineEdit_3, 0, 1, 1, 2)

        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.gridLayoutWidget_6 = QWidget(self.tab_7)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(10, 10, 781, 371))
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_6 = QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_6.addWidget(self.lineEdit_6, 1, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.gridLayoutWidget_6)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_6.addWidget(self.pushButton_5, 0, 2, 1, 1)

        self.lineEdit_5 = QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_6.addWidget(self.lineEdit_5, 0, 1, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget_6)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_6.addWidget(self.label_14, 1, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.gridLayoutWidget_6)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_6.addWidget(self.pushButton_6, 1, 2, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget_6)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_6.addWidget(self.label_13, 0, 0, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget_6)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_6.addWidget(self.label_15, 2, 0, 1, 1)

        self.lineEdit_7 = QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_6.addWidget(self.lineEdit_7, 2, 1, 1, 2)

        self.tabWidget.addTab(self.tab_7, "")
        self.tab_4 = QWidget()
        self.tab_4.hide()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayoutWidget_4 = QWidget(self.tab_4)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(10, 10, 781, 371))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.gridLayoutWidget_4)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_4.addWidget(self.label_10, 1, 0, 1, 1)

        self.comboBox_10 = QComboBox(self.gridLayoutWidget_4)
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.setObjectName(u"comboBox_10")

        self.gridLayout_4.addWidget(self.comboBox_10, 2, 1, 1, 1)

        self.checkBox = QCheckBox(self.gridLayoutWidget_4)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_4.addWidget(self.checkBox, 3, 0, 1, 1)

        self.comboBox_9 = QComboBox(self.gridLayoutWidget_4)
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.setObjectName(u"comboBox_9")

        self.gridLayout_4.addWidget(self.comboBox_9, 3, 1, 1, 1)

        self.comboBox_8 = QComboBox(self.gridLayoutWidget_4)
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.setObjectName(u"comboBox_8")

        self.gridLayout_4.addWidget(self.comboBox_8, 1, 1, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget_4)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_4.addWidget(self.label_16, 2, 0, 1, 1)

        self.comboBox_7 = QComboBox(self.gridLayoutWidget_4)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")

        self.gridLayout_4.addWidget(self.comboBox_7, 0, 1, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget_4)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 1)

        self.checkBox_3 = QCheckBox(self.gridLayoutWidget_4)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout_4.addWidget(self.checkBox_3, 4, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(720, 430, 75, 24))
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(630, 430, 75, 24))

        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"EmuGUI - Edit VM", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Architecture", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"i386", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"amd64", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"mips", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"mips64", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Dialog", u"mipsel", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Dialog", u"mips64el", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("Dialog", u"ppc", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("Dialog", u"ppc64", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("Dialog", u"arm", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("Dialog", u"aarch64", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog", u"General", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"CPU", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"RAM in MB", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"Machine", None))
        self.comboBox_11.setItemText(0, QCoreApplication.translate("Dialog", u"Let QEMU decide", None))
        self.comboBox_11.setItemText(1, QCoreApplication.translate("Dialog", u"486", None))
        self.comboBox_11.setItemText(2, QCoreApplication.translate("Dialog", u"Broadwell", None))
        self.comboBox_11.setItemText(3, QCoreApplication.translate("Dialog", u"Cascadelake-Server", None))
        self.comboBox_11.setItemText(4, QCoreApplication.translate("Dialog", u"Conroe", None))
        self.comboBox_11.setItemText(5, QCoreApplication.translate("Dialog", u"Cooperlake", None))
        self.comboBox_11.setItemText(6, QCoreApplication.translate("Dialog", u"Denverton", None))
        self.comboBox_11.setItemText(7, QCoreApplication.translate("Dialog", u"Dhyana", None))
        self.comboBox_11.setItemText(8, QCoreApplication.translate("Dialog", u"EPYC", None))
        self.comboBox_11.setItemText(9, QCoreApplication.translate("Dialog", u"EPYC-Milan", None))
        self.comboBox_11.setItemText(10, QCoreApplication.translate("Dialog", u"EPYC-Rome", None))
        self.comboBox_11.setItemText(11, QCoreApplication.translate("Dialog", u"Haswell", None))
        self.comboBox_11.setItemText(12, QCoreApplication.translate("Dialog", u"Icelake-Client", None))
        self.comboBox_11.setItemText(13, QCoreApplication.translate("Dialog", u"Icelake-Server", None))
        self.comboBox_11.setItemText(14, QCoreApplication.translate("Dialog", u"IvyBridge", None))
        self.comboBox_11.setItemText(15, QCoreApplication.translate("Dialog", u"KnightsMill", None))
        self.comboBox_11.setItemText(16, QCoreApplication.translate("Dialog", u"Nehalem", None))
        self.comboBox_11.setItemText(17, QCoreApplication.translate("Dialog", u"Opteron_G1", None))
        self.comboBox_11.setItemText(18, QCoreApplication.translate("Dialog", u"Opteron_G2", None))
        self.comboBox_11.setItemText(19, QCoreApplication.translate("Dialog", u"Opteron_G3", None))
        self.comboBox_11.setItemText(20, QCoreApplication.translate("Dialog", u"Opteron_G4", None))
        self.comboBox_11.setItemText(21, QCoreApplication.translate("Dialog", u"Opteron_G5", None))
        self.comboBox_11.setItemText(22, QCoreApplication.translate("Dialog", u"Penryn", None))
        self.comboBox_11.setItemText(23, QCoreApplication.translate("Dialog", u"SandyBridge", None))
        self.comboBox_11.setItemText(24, QCoreApplication.translate("Dialog", u"Skylake-Client", None))
        self.comboBox_11.setItemText(25, QCoreApplication.translate("Dialog", u"Skylake-Server", None))
        self.comboBox_11.setItemText(26, QCoreApplication.translate("Dialog", u"Snowridge", None))
        self.comboBox_11.setItemText(27, QCoreApplication.translate("Dialog", u"Westmere", None))
        self.comboBox_11.setItemText(28, QCoreApplication.translate("Dialog", u"athlon", None))
        self.comboBox_11.setItemText(29, QCoreApplication.translate("Dialog", u"core2duo", None))
        self.comboBox_11.setItemText(30, QCoreApplication.translate("Dialog", u"coreduo", None))
        self.comboBox_11.setItemText(31, QCoreApplication.translate("Dialog", u"kvm32", None))
        self.comboBox_11.setItemText(32, QCoreApplication.translate("Dialog", u"kvm64", None))
        self.comboBox_11.setItemText(33, QCoreApplication.translate("Dialog", u"n270", None))
        self.comboBox_11.setItemText(34, QCoreApplication.translate("Dialog", u"pentium", None))
        self.comboBox_11.setItemText(35, QCoreApplication.translate("Dialog", u"pentium2", None))
        self.comboBox_11.setItemText(36, QCoreApplication.translate("Dialog", u"pentium3", None))
        self.comboBox_11.setItemText(37, QCoreApplication.translate("Dialog", u"phenom", None))
        self.comboBox_11.setItemText(38, QCoreApplication.translate("Dialog", u"qemu32", None))
        self.comboBox_11.setItemText(39, QCoreApplication.translate("Dialog", u"qemu64", None))
        self.comboBox_11.setItemText(40, QCoreApplication.translate("Dialog", u"base", None))
        self.comboBox_11.setItemText(41, QCoreApplication.translate("Dialog", u"max", None))
        self.comboBox_11.setItemText(42, QCoreApplication.translate("Dialog", u"host", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"Machine", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"VHD path", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"VHD usage", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Browse", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"VHD file format", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Maximum size", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("Dialog", u"KB", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("Dialog", u"MB", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("Dialog", u"GB", None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate("Dialog", u"Add an existing virtual hard disk", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Dialog", u"Create a new virtual hard disk", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("Dialog", u"Don't add a virtual hard disk", None))

        self.comboBox_3.setItemText(0, QCoreApplication.translate("Dialog", u"qcow2", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("Dialog", u"qcow", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("Dialog", u"vdi", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("Dialog", u"raw", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("Dialog", u"vhdx", None))
        self.comboBox_3.setItemText(5, QCoreApplication.translate("Dialog", u"vpc", None))
        self.comboBox_3.setItemText(6, QCoreApplication.translate("Dialog", u"vmdk", None))
        self.comboBox_3.setItemText(7, QCoreApplication.translate("Dialog", u"parallels", None))
        self.comboBox_3.setItemText(8, QCoreApplication.translate("Dialog", u"file", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Dialog", u"Virtual hard disks", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Mouse type", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("Dialog", u"PS/2 Mouse", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("Dialog", u"USB Mouse", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("Dialog", u"USB Tablet Device", None))

        self.comboBox_6.setItemText(0, QCoreApplication.translate("Dialog", u"PS/2 Keyboard", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("Dialog", u"USB Keyboard", None))

        self.label_8.setText(QCoreApplication.translate("Dialog", u"Keyboard type", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"USB Tablet Device (depreciated)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("Dialog", u"Peripherals", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Location of external BIOS file (Leave empty to use the default BIOS)", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"External BIOS file", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"Browse", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("Dialog", u"BIOS", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"Browse", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"Linux initrd image", None))
        self.pushButton_6.setText(QCoreApplication.translate("Dialog", u"Browse", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"Linux kernel", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"Linux cmd arguments", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("Dialog", u"Linux", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Network adapter", None))
        self.comboBox_10.setItemText(0, QCoreApplication.translate("Dialog", u"none", None))
        self.comboBox_10.setItemText(1, QCoreApplication.translate("Dialog", u"sb16", None))
        self.comboBox_10.setItemText(2, QCoreApplication.translate("Dialog", u"pcspk", None))
        self.comboBox_10.setItemText(3, QCoreApplication.translate("Dialog", u"intel-hda", None))
        self.comboBox_10.setItemText(4, QCoreApplication.translate("Dialog", u"gus", None))
        self.comboBox_10.setItemText(5, QCoreApplication.translate("Dialog", u"ES1370", None))
        self.comboBox_10.setItemText(6, QCoreApplication.translate("Dialog", u"cs4231a", None))
        self.comboBox_10.setItemText(7, QCoreApplication.translate("Dialog", u"adlib", None))
        self.comboBox_10.setItemText(8, QCoreApplication.translate("Dialog", u"AC97", None))

        self.checkBox.setText(QCoreApplication.translate("Dialog", u"Add USB support", None))
        self.comboBox_9.setItemText(0, QCoreApplication.translate("Dialog", u"pci-ohci", None))
        self.comboBox_9.setItemText(1, QCoreApplication.translate("Dialog", u"piix3-usb-uhci", None))
        self.comboBox_9.setItemText(2, QCoreApplication.translate("Dialog", u"qemu-xhci", None))
        self.comboBox_9.setItemText(3, QCoreApplication.translate("Dialog", u"usb-ehci", None))

        self.comboBox_8.setItemText(0, QCoreApplication.translate("Dialog", u"e1000", None))
        self.comboBox_8.setItemText(1, QCoreApplication.translate("Dialog", u"e1000-82545em", None))
        self.comboBox_8.setItemText(2, QCoreApplication.translate("Dialog", u"e1000e", None))
        self.comboBox_8.setItemText(3, QCoreApplication.translate("Dialog", u"i82550", None))
        self.comboBox_8.setItemText(4, QCoreApplication.translate("Dialog", u"i82551", None))
        self.comboBox_8.setItemText(5, QCoreApplication.translate("Dialog", u"i82557a", None))
        self.comboBox_8.setItemText(6, QCoreApplication.translate("Dialog", u"i82557b", None))
        self.comboBox_8.setItemText(7, QCoreApplication.translate("Dialog", u"i82557c", None))
        self.comboBox_8.setItemText(8, QCoreApplication.translate("Dialog", u"i82558a", None))
        self.comboBox_8.setItemText(9, QCoreApplication.translate("Dialog", u"i82558b", None))
        self.comboBox_8.setItemText(10, QCoreApplication.translate("Dialog", u"i82559a", None))
        self.comboBox_8.setItemText(11, QCoreApplication.translate("Dialog", u"i82559b", None))
        self.comboBox_8.setItemText(12, QCoreApplication.translate("Dialog", u"i82559c", None))
        self.comboBox_8.setItemText(13, QCoreApplication.translate("Dialog", u"i82559er", None))
        self.comboBox_8.setItemText(14, QCoreApplication.translate("Dialog", u"i82562", None))
        self.comboBox_8.setItemText(15, QCoreApplication.translate("Dialog", u"i82801", None))
        self.comboBox_8.setItemText(16, QCoreApplication.translate("Dialog", u"ne2k_pci", None))
        self.comboBox_8.setItemText(17, QCoreApplication.translate("Dialog", u"pcnet", None))
        self.comboBox_8.setItemText(18, QCoreApplication.translate("Dialog", u"rtl8139", None))
        self.comboBox_8.setItemText(19, QCoreApplication.translate("Dialog", u"tulip", None))
        self.comboBox_8.setItemText(20, QCoreApplication.translate("Dialog", u"virtio-net", None))
        self.comboBox_8.setItemText(21, QCoreApplication.translate("Dialog", u"virtio-net-device", None))
        self.comboBox_8.setItemText(22, QCoreApplication.translate("Dialog", u"virtio-net-pci", None))
        self.comboBox_8.setItemText(23, QCoreApplication.translate("Dialog", u"virtio-net-pci-non-transitional", None))
        self.comboBox_8.setItemText(24, QCoreApplication.translate("Dialog", u"virtio-net-pci-transitional", None))
        self.comboBox_8.setItemText(25, QCoreApplication.translate("Dialog", u"vmxnet3", None))
        self.comboBox_8.setItemText(26, QCoreApplication.translate("Dialog", u"dp83932", None))
        self.comboBox_8.setItemText(27, QCoreApplication.translate("Dialog", u"none", None))

        self.label_16.setText(QCoreApplication.translate("Dialog", u"Sound card", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("Dialog", u"none", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("Dialog", u"std", None))
        self.comboBox_7.setItemText(2, QCoreApplication.translate("Dialog", u"virtio", None))
        self.comboBox_7.setItemText(3, QCoreApplication.translate("Dialog", u"virtio-gpu-pci", None))
        self.comboBox_7.setItemText(4, QCoreApplication.translate("Dialog", u"vmware", None))
        self.comboBox_7.setItemText(5, QCoreApplication.translate("Dialog", u"xenfb", None))
        self.comboBox_7.setItemText(6, QCoreApplication.translate("Dialog", u"qxl", None))
        self.comboBox_7.setItemText(7, QCoreApplication.translate("Dialog", u"cirrus", None))

        self.label_9.setText(QCoreApplication.translate("Dialog", u"VGA", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"I want to install Windows 2000 (depreciated)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Dialog", u"Additional components", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"OK", None))
    # retranslateUi

