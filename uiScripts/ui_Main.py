# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QListView, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QTextBrowser, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(798, 598)
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 801, 551))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.gridLayoutWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabWidget#tabWidget::pane {\n"
"         background: transparent;\n"
"         border: none;\n"
"        }\n"
"\n"
"        QTabWidget#tabWidget QTabBar {\n"
"         qproperty-expanding: false;\n"
"         margin-left: auto;\n"
"         margin-right: auto;\n"
"         spacing: 6px;\n"
"        }\n"
"\n"
"        QTabWidget#tabWidget QTabBar::tab {\n"
"         background: transparent;\n"
"         color: #2b2b2b;\n"
"         padding: 8px 16px;\n"
"         border-radius: 6px;\n"
"         font-size: 13px;\n"
"         min-width: 72px;\n"
"        }\n"
"\n"
"        QTabWidget#tabWidget QTabBar::tab:hover {\n"
"         background: rgba(0,0,0,0.04);\n"
"        }\n"
"\n"
"        QTabWidget#tabWidget QTabBar::tab:selected {\n"
"         background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ffffff, stop:1 #f5f7fa);\n"
"         color: #111111;\n"
"         font-weight: 600;\n"
"         border: 1px solid rgba(0,0,0,0.08);\n"
"        }")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.gridLayoutWidget_4 = QWidget(self.tab)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(0, 0, 791, 511))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_8 = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.verticalLayout.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.verticalLayout.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.verticalLayout.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.verticalLayout.addWidget(self.pushButton_11)

        self.pushButton_22 = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_22.setObjectName(u"pushButton_22")

        self.verticalLayout.addWidget(self.pushButton_22)

        self.pushButton_23 = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_23.setObjectName(u"pushButton_23")

        self.verticalLayout.addWidget(self.pushButton_23)


        self.gridLayout_4.addLayout(self.verticalLayout, 1, 2, 2, 1)

        self.listView = QListView(self.gridLayoutWidget_4)
        self.listView.setObjectName(u"listView")

        self.gridLayout_4.addWidget(self.listView, 1, 1, 1, 1, Qt.AlignRight)

        self.listView_2 = QListView(self.gridLayoutWidget_4)
        self.listView_2.setObjectName(u"listView_2")
        self.listView_2.setMinimumSize(QSize(128, 128))
        self.listView_2.setMaximumSize(QSize(128, 16777215))

        self.gridLayout_4.addWidget(self.listView_2, 1, 0, 1, 1, Qt.AlignLeft)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setEnabled(True)
        self.tabWidget_2 = QTabWidget(self.tab_2)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(0, 0, 791, 521))
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayoutWidget_2 = QWidget(self.tab_3)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 0, 781, 557))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)

        self.pushButton_19 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.gridLayout_2.addWidget(self.pushButton_19, 12, 3, 1, 1)

        self.pushButton_7 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout_2.addWidget(self.pushButton_7, 7, 3, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget_2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 13, 1, 1, 1)

        self.lbl_alpha = QLabel(self.gridLayoutWidget_2)
        self.lbl_alpha.setObjectName(u"lbl_alpha")

        self.gridLayout_2.addWidget(self.lbl_alpha, 15, 1, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 6, 1, 1, 1)

        self.lineEdit_5 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_2.addWidget(self.lineEdit_5, 0, 2, 1, 1)

        self.lineEdit_10 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.gridLayout_2.addWidget(self.lineEdit_10, 11, 2, 1, 1)

        self.pushButton_16 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.gridLayout_2.addWidget(self.pushButton_16, 9, 3, 1, 1)

        self.lineEdit_12 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.gridLayout_2.addWidget(self.lineEdit_12, 13, 2, 1, 1)

        self.lineEdit_13 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.gridLayout_2.addWidget(self.lineEdit_13, 14, 2, 1, 1)

        self.lineEdit = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit, 6, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_2.addWidget(self.pushButton_4, 3, 3, 1, 1)

        self.lineEdit_11 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.gridLayout_2.addWidget(self.lineEdit_11, 12, 2, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 3, 1, 1, 1)

        self.lineEdit_8 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_2.addWidget(self.lineEdit_8, 9, 2, 1, 1)

        self.pushButton_12 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.gridLayout_2.addWidget(self.pushButton_12, 8, 3, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 8, 1, 1, 1)

        self.pushButton_17 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.gridLayout_2.addWidget(self.pushButton_17, 10, 3, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 2, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_2.addWidget(self.lineEdit_2, 3, 2, 1, 1)

        self.lbl_riscv32 = QLabel(self.gridLayoutWidget_2)
        self.lbl_riscv32.setObjectName(u"lbl_riscv32")

        self.gridLayout_2.addWidget(self.lbl_riscv32, 16, 1, 1, 1)

        self.label_18 = QLabel(self.gridLayoutWidget_2)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_2.addWidget(self.label_18, 11, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 1)

        self.label_19 = QLabel(self.gridLayoutWidget_2)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_2.addWidget(self.label_19, 12, 1, 1, 1)

        self.label_17 = QLabel(self.gridLayoutWidget_2)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_2.addWidget(self.label_17, 10, 1, 1, 1)

        self.btn_alpha = QPushButton(self.gridLayoutWidget_2)
        self.btn_alpha.setObjectName(u"btn_alpha")

        self.gridLayout_2.addWidget(self.btn_alpha, 15, 3, 1, 1)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_2.addWidget(self.pushButton_2, 1, 3, 1, 1)

        self.btn_riscv32 = QPushButton(self.gridLayoutWidget_2)
        self.btn_riscv32.setObjectName(u"btn_riscv32")

        self.gridLayout_2.addWidget(self.btn_riscv32, 16, 3, 1, 1)

        self.le_riscv32 = QLineEdit(self.gridLayoutWidget_2)
        self.le_riscv32.setObjectName(u"le_riscv32")

        self.gridLayout_2.addWidget(self.le_riscv32, 16, 2, 1, 1)

        self.lineEdit_3 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_2.addWidget(self.lineEdit_3, 2, 2, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 14, 1, 1, 1)

        self.lineEdit_7 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_2.addWidget(self.lineEdit_7, 8, 2, 1, 1)

        self.pushButton_18 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.gridLayout_2.addWidget(self.pushButton_18, 11, 3, 1, 1)

        self.pushButton_3 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_2.addWidget(self.pushButton_3, 2, 3, 1, 1)

        self.lineEdit_6 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_2.addWidget(self.lineEdit_6, 7, 2, 1, 1)

        self.pushButton_5 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_2.addWidget(self.pushButton_5, 6, 3, 1, 1)

        self.lineEdit_9 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout_2.addWidget(self.lineEdit_9, 10, 2, 1, 1)

        self.pushButton_13 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.gridLayout_2.addWidget(self.pushButton_13, 13, 3, 1, 1)

        self.le_alpha = QLineEdit(self.gridLayoutWidget_2)
        self.le_alpha.setObjectName(u"le_alpha")

        self.gridLayout_2.addWidget(self.le_alpha, 15, 2, 1, 1)

        self.pushButton_14 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.gridLayout_2.addWidget(self.pushButton_14, 14, 3, 1, 1)

        self.lineEdit_4 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_2.addWidget(self.lineEdit_4, 1, 2, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget_2)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_2.addWidget(self.label_16, 9, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_2.addWidget(self.pushButton_6, 17, 3, 1, 1)

        self.pushButton = QPushButton(self.gridLayoutWidget_2)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 0, 3, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 7, 1, 1, 1)

        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayoutWidget_5 = QWidget(self.tab_5)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(0, 0, 781, 498))
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_riscv64 = QPushButton(self.gridLayoutWidget_5)
        self.btn_riscv64.setObjectName(u"btn_riscv64")

        self.gridLayout_6.addWidget(self.btn_riscv64, 2, 3, 1, 1)

        self.lbl_riscv64 = QLabel(self.gridLayoutWidget_5)
        self.lbl_riscv64.setObjectName(u"lbl_riscv64")

        self.gridLayout_6.addWidget(self.lbl_riscv64, 2, 1, 1, 1)

        self.btn_apply_qemu2 = QPushButton(self.gridLayoutWidget_5)
        self.btn_apply_qemu2.setObjectName(u"btn_apply_qemu2")

        self.gridLayout_6.addWidget(self.btn_apply_qemu2, 3, 3, 1, 1)

        self.le_riscv64 = QLineEdit(self.gridLayoutWidget_5)
        self.le_riscv64.setObjectName(u"le_riscv64")

        self.gridLayout_6.addWidget(self.le_riscv64, 2, 2, 1, 1)

        self.tabWidget_2.addTab(self.tab_5, "")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayoutWidget_2 = QWidget(self.tab_4)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(350, 80, 121, 371))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_21 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_21.setObjectName(u"pushButton_21")

        self.verticalLayout_3.addWidget(self.pushButton_21)

        self.pushButton_20 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_20.setObjectName(u"pushButton_20")

        self.verticalLayout_3.addWidget(self.pushButton_20)

        self.pushButton_15 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.verticalLayout_3.addWidget(self.pushButton_15)

        self.pushButton_24 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_24.setObjectName(u"pushButton_24")

        self.verticalLayout_3.addWidget(self.pushButton_24)

        self.verticalLayoutWidget_3 = QWidget(self.tab_4)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(500, 80, 121, 371))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_25 = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_25.setObjectName(u"pushButton_25")

        self.verticalLayout_4.addWidget(self.pushButton_25)

        self.pushButton_26 = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_26.setObjectName(u"pushButton_26")

        self.verticalLayout_4.addWidget(self.pushButton_26)

        self.pushButton_27 = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_27.setObjectName(u"pushButton_27")

        self.verticalLayout_4.addWidget(self.pushButton_27)

        self.pushButton_28 = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_28.setObjectName(u"pushButton_28")

        self.verticalLayout_4.addWidget(self.pushButton_28)

        self.label_6 = QLabel(self.tab_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(150, 130, 121, 31))
        self.label_6.setTextFormat(Qt.PlainText)
        self.label_7 = QLabel(self.tab_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(150, 210, 121, 31))
        self.label_8 = QLabel(self.tab_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(150, 290, 121, 31))
        self.label_10 = QLabel(self.tab_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(150, 370, 121, 31))
        self.label_14 = QLabel(self.tab_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(50, 20, 661, 41))
        self.label_14.setTextFormat(Qt.AutoText)
        self.label_14.setScaledContents(False)
        self.line = QFrame(self.tab_4)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(-10, 170, 811, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_2 = QFrame(self.tab_4)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 250, 811, 20))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_3 = QFrame(self.tab_4)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(-10, 330, 811, 20))
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_4 = QFrame(self.tab_4)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(-10, 410, 811, 20))
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_5 = QFrame(self.tab_4)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(0, 100, 811, 20))
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.pushButton_64 = QPushButton(self.tab_6)
        self.pushButton_64.setObjectName(u"pushButton_64")
        self.pushButton_64.setGeometry(QRect(510, 290, 121, 23))
        self.pushButton_45 = QPushButton(self.tab_6)
        self.pushButton_45.setObjectName(u"pushButton_45")
        self.pushButton_45.setGeometry(QRect(510, 100, 121, 23))
        self.pushButton_84 = QPushButton(self.tab_6)
        self.pushButton_84.setObjectName(u"pushButton_84")
        self.pushButton_84.setGeometry(QRect(510, 420, 121, 23))
        self.pushButton_55 = QPushButton(self.tab_6)
        self.pushButton_55.setObjectName(u"pushButton_55")
        self.pushButton_55.setGeometry(QRect(510, 210, 121, 23))
        self.pushButton_86 = QPushButton(self.tab_6)
        self.pushButton_86.setObjectName(u"pushButton_86")
        self.pushButton_86.setGeometry(QRect(230, 390, 121, 23))
        self.pushButton_67 = QPushButton(self.tab_6)
        self.pushButton_67.setObjectName(u"pushButton_67")
        self.pushButton_67.setGeometry(QRect(510, 340, 121, 23))
        self.pushButton_33 = QPushButton(self.tab_6)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setGeometry(QRect(80, 20, 121, 23))
        self.pushButton_74 = QPushButton(self.tab_6)
        self.pushButton_74.setObjectName(u"pushButton_74")
        self.pushButton_74.setGeometry(QRect(370, 340, 121, 23))
        self.pushButton_52 = QPushButton(self.tab_6)
        self.pushButton_52.setObjectName(u"pushButton_52")
        self.pushButton_52.setGeometry(QRect(370, 180, 121, 23))
        self.pushButton_43 = QPushButton(self.tab_6)
        self.pushButton_43.setObjectName(u"pushButton_43")
        self.pushButton_43.setGeometry(QRect(80, 100, 121, 23))
        self.pushButton_79 = QPushButton(self.tab_6)
        self.pushButton_79.setObjectName(u"pushButton_79")
        self.pushButton_79.setGeometry(QRect(80, 390, 121, 23))
        self.pushButton_78 = QPushButton(self.tab_6)
        self.pushButton_78.setObjectName(u"pushButton_78")
        self.pushButton_78.setGeometry(QRect(650, 390, 111, 23))
        self.label_20 = QLabel(self.tab_6)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 40, 54, 16))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setAlignment(Qt.AlignCenter)
        self.line_16 = QFrame(self.tab_6)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setGeometry(QRect(80, 160, 721, 20))
        self.line_16.setFrameShape(QFrame.Shape.HLine)
        self.line_16.setFrameShadow(QFrame.Shadow.Sunken)
        self.pushButton_35 = QPushButton(self.tab_6)
        self.pushButton_35.setObjectName(u"pushButton_35")
        self.pushButton_35.setGeometry(QRect(370, 20, 121, 23))
        self.pushButton_51 = QPushButton(self.tab_6)
        self.pushButton_51.setObjectName(u"pushButton_51")
        self.pushButton_51.setGeometry(QRect(230, 180, 121, 23))
        self.label_25 = QLabel(self.tab_6)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(10, 400, 54, 31))
        self.label_25.setAlignment(Qt.AlignCenter)
        self.pushButton_48 = QPushButton(self.tab_6)
        self.pushButton_48.setObjectName(u"pushButton_48")
        self.pushButton_48.setGeometry(QRect(230, 210, 121, 23))
        self.pushButton_56 = QPushButton(self.tab_6)
        self.pushButton_56.setObjectName(u"pushButton_56")
        self.pushButton_56.setGeometry(QRect(650, 210, 111, 23))
        self.pushButton_36 = QPushButton(self.tab_6)
        self.pushButton_36.setObjectName(u"pushButton_36")
        self.pushButton_36.setGeometry(QRect(510, 20, 121, 23))
        self.pushButton_42 = QPushButton(self.tab_6)
        self.pushButton_42.setObjectName(u"pushButton_42")
        self.pushButton_42.setGeometry(QRect(230, 100, 121, 23))
        self.pushButton_77 = QPushButton(self.tab_6)
        self.pushButton_77.setObjectName(u"pushButton_77")
        self.pushButton_77.setGeometry(QRect(650, 420, 111, 23))
        self.pushButton_83 = QPushButton(self.tab_6)
        self.pushButton_83.setObjectName(u"pushButton_83")
        self.pushButton_83.setGeometry(QRect(230, 420, 121, 23))
        self.pushButton_46 = QPushButton(self.tab_6)
        self.pushButton_46.setObjectName(u"pushButton_46")
        self.pushButton_46.setGeometry(QRect(230, 130, 121, 23))
        self.pushButton_82 = QPushButton(self.tab_6)
        self.pushButton_82.setObjectName(u"pushButton_82")
        self.pushButton_82.setGeometry(QRect(370, 420, 121, 23))
        self.pushButton_44 = QPushButton(self.tab_6)
        self.pushButton_44.setObjectName(u"pushButton_44")
        self.pushButton_44.setGeometry(QRect(650, 100, 111, 23))
        self.line_33 = QFrame(self.tab_6)
        self.line_33.setObjectName(u"line_33")
        self.line_33.setGeometry(QRect(80, 370, 721, 20))
        self.line_33.setFrameShape(QFrame.Shape.HLine)
        self.line_33.setFrameShadow(QFrame.Shadow.Sunken)
        self.pushButton_37 = QPushButton(self.tab_6)
        self.pushButton_37.setObjectName(u"pushButton_37")
        self.pushButton_37.setGeometry(QRect(650, 20, 111, 23))
        self.pushButton_41 = QPushButton(self.tab_6)
        self.pushButton_41.setObjectName(u"pushButton_41")
        self.pushButton_41.setGeometry(QRect(80, 130, 121, 23))
        self.line_23 = QFrame(self.tab_6)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setGeometry(QRect(60, 240, 731, 20))
        self.line_23.setFrameShape(QFrame.Shape.HLine)
        self.line_23.setFrameShadow(QFrame.Shadow.Sunken)
        self.pushButton_57 = QPushButton(self.tab_6)
        self.pushButton_57.setObjectName(u"pushButton_57")
        self.pushButton_57.setGeometry(QRect(230, 260, 121, 23))
        self.pushButton_85 = QPushButton(self.tab_6)
        self.pushButton_85.setObjectName(u"pushButton_85")
        self.pushButton_85.setGeometry(QRect(80, 420, 121, 23))
        self.pushButton_60 = QPushButton(self.tab_6)
        self.pushButton_60.setObjectName(u"pushButton_60")
        self.pushButton_60.setGeometry(QRect(370, 260, 121, 23))
        self.pushButton_76 = QPushButton(self.tab_6)
        self.pushButton_76.setObjectName(u"pushButton_76")
        self.pushButton_76.setGeometry(QRect(650, 340, 111, 23))
        self.label_21 = QLabel(self.tab_6)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(10, 110, 54, 21))
        self.label_21.setAlignment(Qt.AlignCenter)
        self.pushButton_38 = QPushButton(self.tab_6)
        self.pushButton_38.setObjectName(u"pushButton_38")
        self.pushButton_38.setGeometry(QRect(80, 50, 121, 23))
        self.line_28 = QFrame(self.tab_6)
        self.line_28.setObjectName(u"line_28")
        self.line_28.setGeometry(QRect(80, 320, 721, 20))
        self.line_28.setFrameShape(QFrame.Shape.HLine)
        self.line_28.setFrameShadow(QFrame.Shadow.Sunken)
        self.pushButton_73 = QPushButton(self.tab_6)
        self.pushButton_73.setObjectName(u"pushButton_73")
        self.pushButton_73.setGeometry(QRect(230, 340, 121, 23))
        self.label_24 = QLabel(self.tab_6)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(3, 340, 71, 21))
        self.label_24.setAlignment(Qt.AlignCenter)
        self.pushButton_34 = QPushButton(self.tab_6)
        self.pushButton_34.setObjectName(u"pushButton_34")
        self.pushButton_34.setGeometry(QRect(230, 20, 121, 23))
        self.pushButton_54 = QPushButton(self.tab_6)
        self.pushButton_54.setObjectName(u"pushButton_54")
        self.pushButton_54.setGeometry(QRect(370, 210, 121, 23))
        self.line_11 = QFrame(self.tab_6)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setGeometry(QRect(80, 80, 721, 20))
        self.line_11.setFrameShape(QFrame.Shape.HLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)
        self.pushButton_47 = QPushButton(self.tab_6)
        self.pushButton_47.setObjectName(u"pushButton_47")
        self.pushButton_47.setGeometry(QRect(650, 180, 111, 23))
        self.pushButton_70 = QPushButton(self.tab_6)
        self.pushButton_70.setObjectName(u"pushButton_70")
        self.pushButton_70.setGeometry(QRect(80, 340, 121, 23))
        self.pushButton_63 = QPushButton(self.tab_6)
        self.pushButton_63.setObjectName(u"pushButton_63")
        self.pushButton_63.setGeometry(QRect(230, 290, 121, 23))
        self.pushButton_61 = QPushButton(self.tab_6)
        self.pushButton_61.setObjectName(u"pushButton_61")
        self.pushButton_61.setGeometry(QRect(370, 290, 121, 23))
        self.pushButton_53 = QPushButton(self.tab_6)
        self.pushButton_53.setObjectName(u"pushButton_53")
        self.pushButton_53.setGeometry(QRect(80, 180, 121, 23))
        self.pushButton_49 = QPushButton(self.tab_6)
        self.pushButton_49.setObjectName(u"pushButton_49")
        self.pushButton_49.setGeometry(QRect(80, 210, 121, 23))
        self.pushButton_58 = QPushButton(self.tab_6)
        self.pushButton_58.setObjectName(u"pushButton_58")
        self.pushButton_58.setGeometry(QRect(650, 260, 111, 23))
        self.pushButton_39 = QPushButton(self.tab_6)
        self.pushButton_39.setObjectName(u"pushButton_39")
        self.pushButton_39.setGeometry(QRect(230, 50, 121, 23))
        self.label_22 = QLabel(self.tab_6)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(10, 190, 54, 16))
        self.label_22.setAlignment(Qt.AlignCenter)
        self.label_23 = QLabel(self.tab_6)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(10, 270, 54, 16))
        self.label_23.setAlignment(Qt.AlignCenter)
        self.pushButton_65 = QPushButton(self.tab_6)
        self.pushButton_65.setObjectName(u"pushButton_65")
        self.pushButton_65.setGeometry(QRect(80, 290, 121, 23))
        self.pushButton_62 = QPushButton(self.tab_6)
        self.pushButton_62.setObjectName(u"pushButton_62")
        self.pushButton_62.setGeometry(QRect(80, 260, 121, 23))
        self.pushButton_59 = QPushButton(self.tab_6)
        self.pushButton_59.setObjectName(u"pushButton_59")
        self.pushButton_59.setGeometry(QRect(510, 260, 121, 23))
        self.pushButton_50 = QPushButton(self.tab_6)
        self.pushButton_50.setObjectName(u"pushButton_50")
        self.pushButton_50.setGeometry(QRect(510, 180, 121, 23))
        self.pushButton_40 = QPushButton(self.tab_6)
        self.pushButton_40.setObjectName(u"pushButton_40")
        self.pushButton_40.setGeometry(QRect(370, 100, 121, 23))
        self.pushButton_81 = QPushButton(self.tab_6)
        self.pushButton_81.setObjectName(u"pushButton_81")
        self.pushButton_81.setGeometry(QRect(510, 390, 121, 23))
        self.pushButton_80 = QPushButton(self.tab_6)
        self.pushButton_80.setObjectName(u"pushButton_80")
        self.pushButton_80.setGeometry(QRect(370, 390, 121, 23))
        self.line_34 = QFrame(self.tab_6)
        self.line_34.setObjectName(u"line_34")
        self.line_34.setGeometry(QRect(80, 450, 721, 20))
        self.line_34.setFrameShape(QFrame.Shape.HLine)
        self.line_34.setFrameShadow(QFrame.Shadow.Sunken)
        self.pushButton_87 = QPushButton(self.tab_6)
        self.pushButton_87.setObjectName(u"pushButton_87")
        self.pushButton_87.setGeometry(QRect(650, 470, 111, 23))
        self.pushButton_88 = QPushButton(self.tab_6)
        self.pushButton_88.setObjectName(u"pushButton_88")
        self.pushButton_88.setGeometry(QRect(230, 470, 121, 23))
        self.pushButton_89 = QPushButton(self.tab_6)
        self.pushButton_89.setObjectName(u"pushButton_89")
        self.pushButton_89.setGeometry(QRect(80, 470, 121, 23))
        self.pushButton_90 = QPushButton(self.tab_6)
        self.pushButton_90.setObjectName(u"pushButton_90")
        self.pushButton_90.setGeometry(QRect(370, 470, 121, 23))
        self.pushButton_91 = QPushButton(self.tab_6)
        self.pushButton_91.setObjectName(u"pushButton_91")
        self.pushButton_91.setGeometry(QRect(510, 470, 121, 23))
        self.label_26 = QLabel(self.tab_6)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(10, 460, 54, 31))
        self.label_26.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.pushButton_29 = QPushButton(self.tab_7)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setGeometry(QRect(40, 10, 121, 31))
        self.pushButton_30 = QPushButton(self.tab_7)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setGeometry(QRect(250, 10, 101, 31))
        self.pushButton_31 = QPushButton(self.tab_7)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setGeometry(QRect(440, 10, 101, 31))
        self.pushButton_32 = QPushButton(self.tab_7)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setGeometry(QRect(620, 10, 101, 31))
        self.textEdit = QTextEdit(self.tab_7)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(0, 50, 791, 361))
        self.textBrowser = QTextBrowser(self.tab_7)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(0, 410, 791, 111))
        self.tabWidget.addTab(self.tab_7, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 798, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.listView, self.pushButton_8)
        QWidget.setTabOrder(self.pushButton_8, self.pushButton_9)
        QWidget.setTabOrder(self.pushButton_9, self.pushButton_10)
        QWidget.setTabOrder(self.pushButton_10, self.pushButton_11)
        QWidget.setTabOrder(self.pushButton_11, self.tabWidget_2)
        QWidget.setTabOrder(self.tabWidget_2, self.lineEdit_5)
        QWidget.setTabOrder(self.lineEdit_5, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.lineEdit_4)
        QWidget.setTabOrder(self.lineEdit_4, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.lineEdit_3)
        QWidget.setTabOrder(self.lineEdit_3, self.pushButton_3)
        QWidget.setTabOrder(self.pushButton_3, self.lineEdit_2)
        QWidget.setTabOrder(self.lineEdit_2, self.pushButton_4)
        QWidget.setTabOrder(self.pushButton_4, self.lineEdit)
        QWidget.setTabOrder(self.lineEdit, self.pushButton_5)
        QWidget.setTabOrder(self.pushButton_5, self.lineEdit_6)
        QWidget.setTabOrder(self.lineEdit_6, self.pushButton_7)
        QWidget.setTabOrder(self.pushButton_7, self.lineEdit_7)
        QWidget.setTabOrder(self.lineEdit_7, self.pushButton_12)
        QWidget.setTabOrder(self.pushButton_12, self.lineEdit_8)
        QWidget.setTabOrder(self.lineEdit_8, self.pushButton_16)
        QWidget.setTabOrder(self.pushButton_16, self.lineEdit_9)
        QWidget.setTabOrder(self.lineEdit_9, self.pushButton_17)
        QWidget.setTabOrder(self.pushButton_17, self.lineEdit_10)
        QWidget.setTabOrder(self.lineEdit_10, self.pushButton_18)
        QWidget.setTabOrder(self.pushButton_18, self.lineEdit_11)
        QWidget.setTabOrder(self.lineEdit_11, self.pushButton_19)
        QWidget.setTabOrder(self.pushButton_19, self.lineEdit_12)
        QWidget.setTabOrder(self.lineEdit_12, self.pushButton_13)
        QWidget.setTabOrder(self.pushButton_13, self.lineEdit_13)
        QWidget.setTabOrder(self.lineEdit_13, self.pushButton_14)
        QWidget.setTabOrder(self.pushButton_14, self.le_alpha)
        QWidget.setTabOrder(self.le_alpha, self.btn_alpha)
        QWidget.setTabOrder(self.btn_alpha, self.le_riscv32)
        QWidget.setTabOrder(self.le_riscv32, self.btn_riscv32)
        QWidget.setTabOrder(self.btn_riscv32, self.pushButton_6)
        QWidget.setTabOrder(self.pushButton_6, self.pushButton_22)
        QWidget.setTabOrder(self.pushButton_22, self.pushButton_23)
        QWidget.setTabOrder(self.pushButton_23, self.btn_riscv64)
        QWidget.setTabOrder(self.btn_riscv64, self.btn_apply_qemu2)
        QWidget.setTabOrder(self.btn_apply_qemu2, self.le_riscv64)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"New Virtual Machine", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Start Selected Virtual Machine", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Edit Selected Virtual Machine", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Delete Selected Virtual Machine", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"Export selected virtual machine", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"Import virtual machine", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Main", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"qemu-img Path", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"qemu-system-sparc path", None))
        self.lbl_alpha.setText(QCoreApplication.translate("MainWindow", u"qemu-system-alpha path", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"qemu-system-mips64el path", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"qemu-system-ppc path", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"qemu-system-arm path", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"qemu-system-x86_64 path", None))
        self.lbl_riscv32.setText(QCoreApplication.translate("MainWindow", u"qemu-system-riscv32 path", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"qemu-system-mips path", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"qemu-system-i386 path", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"qemu-system-mips64 path", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"qemu-system-mipsel path", None))
        self.btn_alpha.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.btn_riscv32.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"qemu-system-sparc64 path", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"qemu-system-ppc64 path", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"qemu-system-aarch64 path", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"QEMU (1)", None))
        self.btn_riscv64.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.lbl_riscv64.setText(QCoreApplication.translate("MainWindow", u"qemu-system-riscv64 path", None))
        self.btn_apply_qemu2.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"QEMU (2)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91\u6e90\u4ee3\u7801", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91\u6e90\u4ee3\u7801", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91\u6e90\u4ee3\u7801", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91\u6e90\u4ee3\u7801", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"\u5e94\u7528", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"\u5e94\u7528", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"\u5e94\u7528", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"\u5e94\u7528", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u6307\u4ee4\u7ea7", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u672c\u5757\u7ea7", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u51fd\u6570\u7ea7", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u5757\u7ea7", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u4e3b\u63d2\u6869\u5b9a\u5236\uff0c\u9700\u8981\u9009\u4fee\u6539\u5bf9\u6e90\u4ee3\u7801\uff0c\u7136\u540e\u5e94\u7528\u5230\u8be5\u6846\u67b6\u4e0a\uff0c\u4e0b\u6b21\u6a21\u62df\u56fa\u4ef6\u5373\u53ef\u4f7f\u7528", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Hook", None))
        self.pushButton_64.setText(QCoreApplication.translate("MainWindow", u"digic-timer", None))
        self.pushButton_45.setText(QCoreApplication.translate("MainWindow", u"virtio-blk", None))
        self.pushButton_84.setText(QCoreApplication.translate("MainWindow", u"xilinx-axidma", None))
        self.pushButton_55.setText(QCoreApplication.translate("MainWindow", u"sungem", None))
        self.pushButton_86.setText(QCoreApplication.translate("MainWindow", u"i82500", None))
        self.pushButton_67.setText(QCoreApplication.translate("MainWindow", u"stm32f2xx-adc", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"ich9-usb-echi1", None))
        self.pushButton_74.setText(QCoreApplication.translate("MainWindow", u"npcm7xx-adc", None))
        self.pushButton_52.setText(QCoreApplication.translate("MainWindow", u"ne2k", None))
        self.pushButton_43.setText(QCoreApplication.translate("MainWindow", u"cd", None))
        self.pushButton_79.setText(QCoreApplication.translate("MainWindow", u"bcm2835-dma", None))
        self.pushButton_78.setText(QCoreApplication.translate("MainWindow", u"pl080", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"USB", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"pci-ohci", None))
        self.pushButton_51.setText(QCoreApplication.translate("MainWindow", u"i82500", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"DMA", None))
        self.pushButton_48.setText(QCoreApplication.translate("MainWindow", u"virtio-net", None))
        self.pushButton_56.setText(QCoreApplication.translate("MainWindow", u"sunhme", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"piix3-usb-uhci", None))
        self.pushButton_42.setText(QCoreApplication.translate("MainWindow", u"fdc", None))
        self.pushButton_77.setText(QCoreApplication.translate("MainWindow", u"sparc32-dma", None))
        self.pushButton_83.setText(QCoreApplication.translate("MainWindow", u"rc4030", None))
        self.pushButton_46.setText(QCoreApplication.translate("MainWindow", u"scsi", None))
        self.pushButton_82.setText(QCoreApplication.translate("MainWindow", u"sifive-pdma", None))
        self.pushButton_44.setText(QCoreApplication.translate("MainWindow", u"ide", None))
        self.pushButton_37.setText(QCoreApplication.translate("MainWindow", u"qemu-xhci", None))
        self.pushButton_41.setText(QCoreApplication.translate("MainWindow", u"sata", None))
        self.pushButton_57.setText(QCoreApplication.translate("MainWindow", u"allwinner-a10", None))
        self.pushButton_85.setText(QCoreApplication.translate("MainWindow", u"pxa2xx-dma", None))
        self.pushButton_60.setText(QCoreApplication.translate("MainWindow", u"ne2k", None))
        self.pushButton_76.setText(QCoreApplication.translate("MainWindow", u"zynq-xadc", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u5b58\u50a8", None))
        self.pushButton_38.setText(QCoreApplication.translate("MainWindow", u"usb-ehci", None))
        self.pushButton_73.setText(QCoreApplication.translate("MainWindow", u"max111x", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u6570\u6a21\u8f6c\u6362", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"nec-usb-xhci", None))
        self.pushButton_54.setText(QCoreApplication.translate("MainWindow", u"tulip", None))
        self.pushButton_47.setText(QCoreApplication.translate("MainWindow", u"igb", None))
        self.pushButton_70.setText(QCoreApplication.translate("MainWindow", u"aspeed-adc", None))
        self.pushButton_63.setText(QCoreApplication.translate("MainWindow", u"aspeed-timer", None))
        self.pushButton_61.setText(QCoreApplication.translate("MainWindow", u"bcm2835-syst", None))
        self.pushButton_53.setText(QCoreApplication.translate("MainWindow", u"e1000", None))
        self.pushButton_49.setText(QCoreApplication.translate("MainWindow", u"pcnet", None))
        self.pushButton_58.setText(QCoreApplication.translate("MainWindow", u"nrf51-timer", None))
        self.pushButton_39.setText(QCoreApplication.translate("MainWindow", u"nec-usb-ehci", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u7f51\u5361", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u5b9a\u65f6\u5668", None))
        self.pushButton_65.setText(QCoreApplication.translate("MainWindow", u"arm-timer", None))
        self.pushButton_62.setText(QCoreApplication.translate("MainWindow", u"a9gtimer", None))
        self.pushButton_59.setText(QCoreApplication.translate("MainWindow", u"i8254", None))
        self.pushButton_50.setText(QCoreApplication.translate("MainWindow", u"virtio-blk", None))
        self.pushButton_40.setText(QCoreApplication.translate("MainWindow", u"pflash", None))
        self.pushButton_81.setText(QCoreApplication.translate("MainWindow", u"i8257", None))
        self.pushButton_80.setText(QCoreApplication.translate("MainWindow", u"etraxfs-dma", None))
        self.pushButton_87.setText(QCoreApplication.translate("MainWindow", u"virtio-console", None))
        self.pushButton_88.setText(QCoreApplication.translate("MainWindow", u"imx-serial", None))
        self.pushButton_89.setText(QCoreApplication.translate("MainWindow", u"bcm2835-aux", None))
        self.pushButton_90.setText(QCoreApplication.translate("MainWindow", u"omap-uart", None))
        self.pushButton_91.setText(QCoreApplication.translate("MainWindow", u"sifive-uart", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u4e32\u53e3", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Peripheral Info", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"API \u624b\u518c", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"\u793a\u4f8b\u4ee3\u78011", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"\u793a\u4f8b\u4ee3\u78012", None))
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Programming", None))
    # retranslateUi

