# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGraphicsView,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QListView, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QTabWidget, QTextBrowser,
    QTextEdit, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1002, 582)
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(220, 0, 781, 561))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.gridLayoutWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setStyleSheet(u"\n"
"         QTabWidget#tabWidget::pane {\n"
"         background: transparent;\n"
"         border: none;\n"
"         }\n"
"\n"
"         QTabWidget#tabWidget QTabBar {\n"
"         qproperty-expanding: true;\n"
"         spacing: 6px;\n"
"         }\n"
"\n"
"         QTabWidget#tabWidget QTabBar::tab {\n"
"         height: 45px;\n"
"         background: #223a7d;\n"
"         color: #ffffff;\n"
"         font-size: 15px;\n"
"         min-width: 125px;\n"
"         qproperty-expanding: true;\n"
"         padding: 8px 16px;\n"
"         }\n"
"\n"
"        QTabWidget#tabWidget QTabBar::tab:hover {\n"
"         background: rgba(3, 9, 26, 0.25);\n"
"        }\n"
"\n"
"        QTabWidget#tabWidget QTabBar::tab:selected {\n"
"         background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #223a7d, stop:1 #223a7d);\n"
"         color: #A4B5ED;\n"
"         font-weight: 700;\n"
"         font-family: \"Microsoft YaHei\", \"PingFang SC\";\n"
"         text-decoration: underline;\n"
"        }\n"
"        ")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.gridWidget_4 = QWidget(self.tab)
        self.gridWidget_4.setObjectName(u"gridWidget_4")
        self.gridWidget_4.setGeometry(QRect(0, 0, 771, 491))
        self.gridLayout_4 = QGridLayout(self.gridWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.listView = QListView(self.gridWidget_4)
        self.listView.setObjectName(u"listView")
        self.listView.setMinimumSize(QSize(500, 0))
        self.listView.setMaximumSize(QSize(500, 16777215))
        self.listView.setStyleSheet(u"\n"
"               QListView#listView::item:selected {\n"
"                    background: #3f6e9cff;\n"
"                    color: #000000;\n"
"               }\n"
"               QListView#listView::item:selected:!active {\n"
"                    background: #3f6e9cff;\n"
"                    color: #000000;\n"
"               }\n"
"               ")

        self.gridLayout_4.addWidget(self.listView, 0, 1, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.widget = QWidget(self.gridWidget_4)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(50)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.pushButton_8 = QPushButton(self.widget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy1)
        self.pushButton_8.setMaximumSize(QSize(202, 32))
        self.pushButton_8.setStyleSheet(u"\n"
"                QPushButton#pushButton_8 {\n"
"                 min-width: 200px;\n"
"                 max-width: 200px;\n"
"                 min-height: 30px;\n"
"                 max-height: 30px;\n"
"                }\n"
"               ")

        self.verticalLayout.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.widget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy1.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy1)
        self.pushButton_9.setMaximumSize(QSize(202, 32))
        self.pushButton_9.setStyleSheet(u"\n"
"                QPushButton#pushButton_9 {\n"
"                 min-width: 200px;\n"
"                 max-width: 200px;\n"
"                 min-height: 30px;\n"
"                 max-height: 30px;\n"
"                }\n"
"               ")

        self.verticalLayout.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.widget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy1.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy1)
        self.pushButton_10.setMaximumSize(QSize(202, 32))
        self.pushButton_10.setStyleSheet(u"\n"
"                QPushButton#pushButton_10 {\n"
"                 min-width: 200px;\n"
"                 max-width: 200px;\n"
"                 min-height: 30px;\n"
"                 max-height: 30px;\n"
"                }\n"
"               ")

        self.verticalLayout.addWidget(self.pushButton_10)

        self.pushButton_22 = QPushButton(self.widget)
        self.pushButton_22.setObjectName(u"pushButton_22")
        sizePolicy1.setHeightForWidth(self.pushButton_22.sizePolicy().hasHeightForWidth())
        self.pushButton_22.setSizePolicy(sizePolicy1)
        self.pushButton_22.setMaximumSize(QSize(202, 32))
        self.pushButton_22.setStyleSheet(u"\n"
"                QPushButton#pushButton_22 {\n"
"                 min-width: 200px;\n"
"                 max-width: 200px;\n"
"                 min-height: 30px;\n"
"                 max-height: 30px;\n"
"                }\n"
"               ")

        self.verticalLayout.addWidget(self.pushButton_22)

        self.pushButton_11 = QPushButton(self.widget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy1.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy1)
        self.pushButton_11.setMaximumSize(QSize(202, 32))
        self.pushButton_11.setStyleSheet(u"\n"
"                QPushButton#pushButton_11 {\n"
"                 min-width: 200px;\n"
"                 max-width: 200px;\n"
"                 min-height: 30px;\n"
"                 max-height: 30px;\n"
"                }\n"
"               ")

        self.verticalLayout.addWidget(self.pushButton_11)

        self.pushButton_23 = QPushButton(self.widget)
        self.pushButton_23.setObjectName(u"pushButton_23")
        sizePolicy1.setHeightForWidth(self.pushButton_23.sizePolicy().hasHeightForWidth())
        self.pushButton_23.setSizePolicy(sizePolicy1)
        self.pushButton_23.setMaximumSize(QSize(202, 32))
        self.pushButton_23.setStyleSheet(u"\n"
"                QPushButton#pushButton_23 {\n"
"                 min-width: 200px;\n"
"                 max-width: 200px;\n"
"                 min-height: 30px;\n"
"                 max-height: 30px;\n"
"                }\n"
"               ")

        self.verticalLayout.addWidget(self.pushButton_23)


        self.gridLayout_4.addWidget(self.widget, 0, 2, 2, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setEnabled(True)
        self.tabWidget_2 = QTabWidget(self.tab_2)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(0, 0, 781, 521))
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridWidget_2 = QWidget(self.tab_3)
        self.gridWidget_2.setObjectName(u"gridWidget_2")
        self.gridWidget_2.setGeometry(QRect(0, 0, 771, 431))
        self.gridLayout_2 = QGridLayout(self.gridWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.gridWidget_2)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)

        self.pushButton_19 = QPushButton(self.gridWidget_2)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.gridLayout_2.addWidget(self.pushButton_19, 12, 3, 1, 1)

        self.pushButton_7 = QPushButton(self.gridWidget_2)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout_2.addWidget(self.pushButton_7, 7, 3, 1, 1)

        self.label_12 = QLabel(self.gridWidget_2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 13, 1, 1, 1)

        self.lbl_alpha = QLabel(self.gridWidget_2)
        self.lbl_alpha.setObjectName(u"lbl_alpha")

        self.gridLayout_2.addWidget(self.lbl_alpha, 15, 1, 1, 1)

        self.label_5 = QLabel(self.gridWidget_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 6, 1, 1, 1)

        self.lineEdit_5 = QLineEdit(self.gridWidget_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_2.addWidget(self.lineEdit_5, 0, 2, 1, 1)

        self.lineEdit_10 = QLineEdit(self.gridWidget_2)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.gridLayout_2.addWidget(self.lineEdit_10, 11, 2, 1, 1)

        self.pushButton_16 = QPushButton(self.gridWidget_2)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.gridLayout_2.addWidget(self.pushButton_16, 9, 3, 1, 1)

        self.lineEdit_12 = QLineEdit(self.gridWidget_2)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.gridLayout_2.addWidget(self.lineEdit_12, 13, 2, 1, 1)

        self.lineEdit_13 = QLineEdit(self.gridWidget_2)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.gridLayout_2.addWidget(self.lineEdit_13, 14, 2, 1, 1)

        self.lineEdit = QLineEdit(self.gridWidget_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit, 6, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.gridWidget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_2.addWidget(self.pushButton_4, 3, 3, 1, 1)

        self.lineEdit_11 = QLineEdit(self.gridWidget_2)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.gridLayout_2.addWidget(self.lineEdit_11, 12, 2, 1, 1)

        self.label_4 = QLabel(self.gridWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 3, 1, 1, 1)

        self.lineEdit_8 = QLineEdit(self.gridWidget_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_2.addWidget(self.lineEdit_8, 9, 2, 1, 1)

        self.pushButton_12 = QPushButton(self.gridWidget_2)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.gridLayout_2.addWidget(self.pushButton_12, 8, 3, 1, 1)

        self.label_11 = QLabel(self.gridWidget_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 8, 1, 1, 1)

        self.pushButton_17 = QPushButton(self.gridWidget_2)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.gridLayout_2.addWidget(self.pushButton_17, 10, 3, 1, 1)

        self.label_3 = QLabel(self.gridWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 2, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.gridWidget_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_2.addWidget(self.lineEdit_2, 3, 2, 1, 1)

        self.lbl_riscv32 = QLabel(self.gridWidget_2)
        self.lbl_riscv32.setObjectName(u"lbl_riscv32")

        self.gridLayout_2.addWidget(self.lbl_riscv32, 16, 1, 1, 1)

        self.label_18 = QLabel(self.gridWidget_2)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_2.addWidget(self.label_18, 11, 1, 1, 1)

        self.label_2 = QLabel(self.gridWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 1)

        self.label_19 = QLabel(self.gridWidget_2)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_2.addWidget(self.label_19, 12, 1, 1, 1)

        self.label_17 = QLabel(self.gridWidget_2)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_2.addWidget(self.label_17, 10, 1, 1, 1)

        self.btn_alpha = QPushButton(self.gridWidget_2)
        self.btn_alpha.setObjectName(u"btn_alpha")

        self.gridLayout_2.addWidget(self.btn_alpha, 15, 3, 1, 1)

        self.pushButton_2 = QPushButton(self.gridWidget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_2.addWidget(self.pushButton_2, 1, 3, 1, 1)

        self.btn_riscv32 = QPushButton(self.gridWidget_2)
        self.btn_riscv32.setObjectName(u"btn_riscv32")

        self.gridLayout_2.addWidget(self.btn_riscv32, 16, 3, 1, 1)

        self.le_riscv32 = QLineEdit(self.gridWidget_2)
        self.le_riscv32.setObjectName(u"le_riscv32")

        self.gridLayout_2.addWidget(self.le_riscv32, 16, 2, 1, 1)

        self.lineEdit_3 = QLineEdit(self.gridWidget_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_2.addWidget(self.lineEdit_3, 2, 2, 1, 1)

        self.label_13 = QLabel(self.gridWidget_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 14, 1, 1, 1)

        self.lineEdit_7 = QLineEdit(self.gridWidget_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_2.addWidget(self.lineEdit_7, 8, 2, 1, 1)

        self.pushButton_18 = QPushButton(self.gridWidget_2)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.gridLayout_2.addWidget(self.pushButton_18, 11, 3, 1, 1)

        self.pushButton_3 = QPushButton(self.gridWidget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_2.addWidget(self.pushButton_3, 2, 3, 1, 1)

        self.lineEdit_6 = QLineEdit(self.gridWidget_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_2.addWidget(self.lineEdit_6, 7, 2, 1, 1)

        self.pushButton_5 = QPushButton(self.gridWidget_2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_2.addWidget(self.pushButton_5, 6, 3, 1, 1)

        self.lineEdit_9 = QLineEdit(self.gridWidget_2)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout_2.addWidget(self.lineEdit_9, 10, 2, 1, 1)

        self.pushButton_13 = QPushButton(self.gridWidget_2)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.gridLayout_2.addWidget(self.pushButton_13, 13, 3, 1, 1)

        self.le_alpha = QLineEdit(self.gridWidget_2)
        self.le_alpha.setObjectName(u"le_alpha")

        self.gridLayout_2.addWidget(self.le_alpha, 15, 2, 1, 1)

        self.pushButton_14 = QPushButton(self.gridWidget_2)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.gridLayout_2.addWidget(self.pushButton_14, 14, 3, 1, 1)

        self.lineEdit_4 = QLineEdit(self.gridWidget_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_2.addWidget(self.lineEdit_4, 1, 2, 1, 1)

        self.label_16 = QLabel(self.gridWidget_2)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_2.addWidget(self.label_16, 9, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.gridWidget_2)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_2.addWidget(self.pushButton_6, 17, 3, 1, 1)

        self.pushButton = QPushButton(self.gridWidget_2)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 0, 3, 1, 1)

        self.label_9 = QLabel(self.gridWidget_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 7, 1, 1, 1)

        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridWidget_5 = QWidget(self.tab_5)
        self.gridWidget_5.setObjectName(u"gridWidget_5")
        self.gridWidget_5.setGeometry(QRect(0, 0, 711, 421))
        self.gridLayout_6 = QGridLayout(self.gridWidget_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.btn_riscv64 = QPushButton(self.gridWidget_5)
        self.btn_riscv64.setObjectName(u"btn_riscv64")

        self.gridLayout_6.addWidget(self.btn_riscv64, 2, 3, 1, 1)

        self.lbl_riscv64 = QLabel(self.gridWidget_5)
        self.lbl_riscv64.setObjectName(u"lbl_riscv64")

        self.gridLayout_6.addWidget(self.lbl_riscv64, 2, 1, 1, 1)

        self.btn_apply_qemu2 = QPushButton(self.gridWidget_5)
        self.btn_apply_qemu2.setObjectName(u"btn_apply_qemu2")

        self.gridLayout_6.addWidget(self.btn_apply_qemu2, 3, 3, 1, 1)

        self.le_riscv64 = QLineEdit(self.gridWidget_5)
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
        self.label_6.setTextFormat(Qt.TextFormat.PlainText)
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
        self.label_14.setTextFormat(Qt.TextFormat.AutoText)
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
        sizePolicy1.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy1)
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)
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
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignCenter)
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
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignCenter)
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
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignCenter)
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
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_23 = QLabel(self.tab_6)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(10, 270, 54, 16))
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignCenter)
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
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignCenter)
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
        self.textEdit.setGeometry(QRect(0, 50, 771, 361))
        self.textBrowser = QTextBrowser(self.tab_7)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(0, 410, 771, 81))
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.graphicsView = QGraphicsView(self.tab_8)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(150, 0, 621, 441))
        self.treeWidget = QTreeWidget(self.tab_8)
        __qtreewidgetitem = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        __qtreewidgetitem1 = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem2 = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        __qtreewidgetitem3 = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        __qtreewidgetitem4 = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem4)
        QTreeWidgetItem(__qtreewidgetitem4)
        QTreeWidgetItem(__qtreewidgetitem4)
        QTreeWidgetItem(__qtreewidgetitem4)
        QTreeWidgetItem(__qtreewidgetitem4)
        QTreeWidgetItem(__qtreewidgetitem4)
        QTreeWidgetItem(__qtreewidgetitem4)
        QTreeWidgetItem(__qtreewidgetitem4)
        QTreeWidgetItem(__qtreewidgetitem4)
        QTreeWidgetItem(__qtreewidgetitem4)
        QTreeWidgetItem(__qtreewidgetitem4)
        __qtreewidgetitem5 = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem5)
        QTreeWidgetItem(__qtreewidgetitem5)
        QTreeWidgetItem(__qtreewidgetitem5)
        QTreeWidgetItem(__qtreewidgetitem5)
        QTreeWidgetItem(__qtreewidgetitem5)
        QTreeWidgetItem(__qtreewidgetitem5)
        QTreeWidgetItem(__qtreewidgetitem5)
        QTreeWidgetItem(__qtreewidgetitem5)
        QTreeWidgetItem(__qtreewidgetitem5)
        __qtreewidgetitem6 = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem6)
        QTreeWidgetItem(__qtreewidgetitem6)
        QTreeWidgetItem(__qtreewidgetitem6)
        QTreeWidgetItem(__qtreewidgetitem6)
        __qtreewidgetitem7 = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem7)
        QTreeWidgetItem(__qtreewidgetitem7)
        QTreeWidgetItem(__qtreewidgetitem7)
        QTreeWidgetItem(__qtreewidgetitem7)
        QTreeWidgetItem(__qtreewidgetitem7)
        __qtreewidgetitem8 = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem8)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setGeometry(QRect(0, 0, 151, 501))
        self.treeWidget.setDragEnabled(True)
        self.treeWidget.setDragDropOverwriteMode(True)
        self.treeWidget.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.pushButton_66 = QPushButton(self.tab_8)
        self.pushButton_66.setObjectName(u"pushButton_66")
        self.pushButton_66.setGeometry(QRect(420, 30, 71, 61))
        self.pushButton_66.setAcceptDrops(True)
        self.label_28 = QLabel(self.tab_8)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(430, 10, 49, 16))
        self.label_28.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.line_6 = QFrame(self.tab_8)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(450, 90, 16, 341))
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_6.setLineWidth(3)
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_9 = QFrame(self.tab_8)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setGeometry(QRect(170, 120, 581, 16))
        self.line_9.setStyleSheet(u"color: rgb(184, 184, 184);")
        self.line_9.setLineWidth(3)
        self.line_9.setFrameShape(QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_10 = QFrame(self.tab_8)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setGeometry(QRect(170, 240, 581, 16))
        self.line_10.setLineWidth(3)
        self.line_10.setFrameShape(QFrame.Shape.HLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_12 = QFrame(self.tab_8)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setGeometry(QRect(170, 360, 581, 16))
        self.line_12.setLineWidth(3)
        self.line_12.setFrameShape(QFrame.Shape.HLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)
        self.horizontalWidget_1 = QWidget(self.tab_8)
        self.horizontalWidget_1.setObjectName(u"horizontalWidget_1")
        self.horizontalWidget_1.setGeometry(QRect(170, 130, 581, 71))
        self.horizontalWidget_1.setAcceptDrops(True)
        self.horizontalWidget_1.setStyleSheet(u"background-color: rgb(207, 207, 207);\n"
"color: rgb(182, 255, 169);")
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalWidget_1)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalWidget_2 = QWidget(self.tab_8)
        self.horizontalWidget_2.setObjectName(u"horizontalWidget_2")
        self.horizontalWidget_2.setGeometry(QRect(170, 250, 581, 71))
        self.horizontalWidget_2.setAcceptDrops(True)
        self.horizontalWidget_2.setStyleSheet(u"background-color: rgb(207, 207, 207);")
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalWidget_3 = QWidget(self.tab_8)
        self.horizontalWidget_3.setObjectName(u"horizontalWidget_3")
        self.horizontalWidget_3.setGeometry(QRect(170, 370, 581, 61))
        self.horizontalWidget_3.setAcceptDrops(True)
        self.horizontalWidget_3.setStyleSheet(u"background-color: rgb(207, 207, 207);")
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalWidget_3)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_72 = QPushButton(self.tab_8)
        self.pushButton_72.setObjectName(u"pushButton_72")
        self.pushButton_72.setEnabled(False)
        self.pushButton_72.setGeometry(QRect(170, 90, 61, 31))
        self.pushButton_75 = QPushButton(self.tab_8)
        self.pushButton_75.setObjectName(u"pushButton_75")
        self.pushButton_75.setEnabled(False)
        self.pushButton_75.setGeometry(QRect(170, 210, 61, 31))
        self.pushButton_92 = QPushButton(self.tab_8)
        self.pushButton_92.setObjectName(u"pushButton_92")
        self.pushButton_92.setEnabled(False)
        self.pushButton_92.setGeometry(QRect(170, 330, 61, 31))
        self.horizontalWidget_0 = QWidget(self.tab_8)
        self.horizontalWidget_0.setObjectName(u"horizontalWidget_0")
        self.horizontalWidget_0.setGeometry(QRect(190, 440, 551, 61))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalWidget_0)
        self.horizontalLayout_5.setSpacing(100)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lineEdit_14 = QLineEdit(self.horizontalWidget_0)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.horizontalLayout_5.addWidget(self.lineEdit_14)

        self.pushButton_95 = QPushButton(self.horizontalWidget_0)
        self.pushButton_95.setObjectName(u"pushButton_95")

        self.horizontalLayout_5.addWidget(self.pushButton_95)

        self.pushButton_93 = QPushButton(self.horizontalWidget_0)
        self.pushButton_93.setObjectName(u"pushButton_93")

        self.horizontalLayout_5.addWidget(self.pushButton_93)

        self.tabWidget.addTab(self.tab_8, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.verticalWidget2 = QWidget(self.centralwidget)
        self.verticalWidget2.setObjectName(u"verticalWidget2")
        self.verticalWidget2.setGeometry(QRect(0, 60, 221, 211))
        self.verticalWidget2.setStyleSheet(u"background-color: rgb(21, 56, 91);")
        self.verticalLayout_2 = QVBoxLayout(self.verticalWidget2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_68 = QPushButton(self.verticalWidget2)
        self.pushButton_68.setObjectName(u"pushButton_68")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_68.sizePolicy().hasHeightForWidth())
        self.pushButton_68.setSizePolicy(sizePolicy2)
        self.pushButton_68.setMinimumSize(QSize(0, 0))
        self.pushButton_68.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;   /* optional, removes button border */\n"
"    color: #999999;   /* set text color since background is gone */\n"
"}\n"
"QPushButton:hover {\n"
"    color: #ffffff;  /* force white text */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: #ffffff;  /* force white text */\n"
"}")

        self.verticalLayout_2.addWidget(self.pushButton_68)

        self.pushButton_71 = QPushButton(self.verticalWidget2)
        self.pushButton_71.setObjectName(u"pushButton_71")
        sizePolicy2.setHeightForWidth(self.pushButton_71.sizePolicy().hasHeightForWidth())
        self.pushButton_71.setSizePolicy(sizePolicy2)
        self.pushButton_71.setMinimumSize(QSize(0, 0))
        self.pushButton_71.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;   /* optional, removes button border */\n"
"    color: #999999;   /* set text color since background is gone */\n"
"}\n"
"QPushButton:hover {\n"
"    color: #ffffff;  /* force white text */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: #ffffff;  /* force white text */\n"
"}")

        self.verticalLayout_2.addWidget(self.pushButton_71)

        self.pushButton_69 = QPushButton(self.verticalWidget2)
        self.pushButton_69.setObjectName(u"pushButton_69")
        sizePolicy2.setHeightForWidth(self.pushButton_69.sizePolicy().hasHeightForWidth())
        self.pushButton_69.setSizePolicy(sizePolicy2)
        self.pushButton_69.setMinimumSize(QSize(0, 0))
        self.pushButton_69.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;   /* optional, removes button border */\n"
"    color: #999999;   /* set text color since background is gone */\n"
"}\n"
"QPushButton:hover {\n"
"    color: #ffffff;  /* force white text */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: #ffffff;  /* force white text */\n"
"}")

        self.verticalLayout_2.addWidget(self.pushButton_69)

        self.verticalWidget1 = QWidget(self.centralwidget)
        self.verticalWidget1.setObjectName(u"verticalWidget1")
        self.verticalWidget1.setGeometry(QRect(0, 270, 221, 291))
        sizePolicy.setHeightForWidth(self.verticalWidget1.sizePolicy().hasHeightForWidth())
        self.verticalWidget1.setSizePolicy(sizePolicy)
        self.verticalWidget1.setStyleSheet(u"background-color: rgb(21, 56, 91);")
        self.verticalLayout_5 = QVBoxLayout(self.verticalWidget1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalWidget = QWidget(self.centralwidget)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalWidget.setGeometry(QRect(0, 0, 221, 61))
        self.horizontalWidget.setStyleSheet(u"background-color: rgb(34, 58, 125);")
        self.horizontalLayout = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_27 = QLabel(self.horizontalWidget)
        self.label_27.setObjectName(u"label_27")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy3)
        self.label_27.setMaximumSize(QSize(50, 50))
        self.label_27.setStyleSheet(u"")
        self.label_27.setPixmap(QPixmap(u"logo.png"))
        self.label_27.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_27)

        self.label_15 = QLabel(self.horizontalWidget)
        self.label_15.setObjectName(u"label_15")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(8)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_15.setScaledContents(True)
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_15.setMargin(0)

        self.horizontalLayout.addWidget(self.label_15)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1002, 21))
        MainWindow.setMenuBar(self.menubar)
        QWidget.setTabOrder(self.listView, self.tabWidget_2)
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
        QWidget.setTabOrder(self.pushButton_6, self.btn_riscv64)
        QWidget.setTabOrder(self.btn_riscv64, self.btn_apply_qemu2)
        QWidget.setTabOrder(self.btn_apply_qemu2, self.le_riscv64)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(5)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"New Virtual Machine", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Start Selected Virtual Machine", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Edit Selected Virtual Machine", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"Export selected virtual machine", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Delete Selected Virtual Machine", None))
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
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"\u4eff\u771f\u8bbe\u5907", None));

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"\u5904\u7406\u5668", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"i386", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem1.child(1)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"arm", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem1.child(2)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"ppc", None));
        ___qtreewidgetitem5 = ___qtreewidgetitem1.child(3)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"mips", None));
        ___qtreewidgetitem6 = ___qtreewidgetitem1.child(4)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MainWindow", u"riscv", None));
        ___qtreewidgetitem7 = self.treeWidget.topLevelItem(1)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("MainWindow", u"\u603b\u7ebf", None));
        ___qtreewidgetitem8 = ___qtreewidgetitem7.child(0)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("MainWindow", u"pci", None));
        ___qtreewidgetitem9 = ___qtreewidgetitem7.child(1)
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("MainWindow", u"pcie", None));
        ___qtreewidgetitem10 = self.treeWidget.topLevelItem(2)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("MainWindow", u"USB", None));
        ___qtreewidgetitem11 = ___qtreewidgetitem10.child(0)
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("MainWindow", u"ich9-usb-ehci1", None));
        ___qtreewidgetitem12 = ___qtreewidgetitem10.child(1)
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("MainWindow", u"ich9-usb-ehci2", None));
        ___qtreewidgetitem13 = ___qtreewidgetitem10.child(2)
        ___qtreewidgetitem13.setText(0, QCoreApplication.translate("MainWindow", u"ich9-usb-uhci1", None));
        ___qtreewidgetitem14 = ___qtreewidgetitem10.child(3)
        ___qtreewidgetitem14.setText(0, QCoreApplication.translate("MainWindow", u"ich9-usb-uhci2", None));
        ___qtreewidgetitem15 = ___qtreewidgetitem10.child(4)
        ___qtreewidgetitem15.setText(0, QCoreApplication.translate("MainWindow", u"nec-usb-xhci", None));
        ___qtreewidgetitem16 = ___qtreewidgetitem10.child(5)
        ___qtreewidgetitem16.setText(0, QCoreApplication.translate("MainWindow", u"piix3-usb-uhci", None));
        ___qtreewidgetitem17 = ___qtreewidgetitem10.child(6)
        ___qtreewidgetitem17.setText(0, QCoreApplication.translate("MainWindow", u"piix4-usb-uhci", None));
        ___qtreewidgetitem18 = ___qtreewidgetitem10.child(7)
        ___qtreewidgetitem18.setText(0, QCoreApplication.translate("MainWindow", u"qemu-xhci", None));
        ___qtreewidgetitem19 = ___qtreewidgetitem10.child(8)
        ___qtreewidgetitem19.setText(0, QCoreApplication.translate("MainWindow", u"usb-ehci", None));
        ___qtreewidgetitem20 = self.treeWidget.topLevelItem(3)
        ___qtreewidgetitem20.setText(0, QCoreApplication.translate("MainWindow", u"\u4e32\u53e3", None));
        ___qtreewidgetitem21 = ___qtreewidgetitem20.child(0)
        ___qtreewidgetitem21.setText(0, QCoreApplication.translate("MainWindow", u"chardev", None));
        ___qtreewidgetitem22 = ___qtreewidgetitem20.child(1)
        ___qtreewidgetitem22.setText(0, QCoreApplication.translate("MainWindow", u"i8042", None));
        ___qtreewidgetitem23 = ___qtreewidgetitem20.child(2)
        ___qtreewidgetitem23.setText(0, QCoreApplication.translate("MainWindow", u"pci-serial", None));
        ___qtreewidgetitem24 = ___qtreewidgetitem20.child(3)
        ___qtreewidgetitem24.setText(0, QCoreApplication.translate("MainWindow", u"tpci200", None));
        ___qtreewidgetitem25 = ___qtreewidgetitem20.child(4)
        ___qtreewidgetitem25.setText(0, QCoreApplication.translate("MainWindow", u"usb-serial", None));
        ___qtreewidgetitem26 = ___qtreewidgetitem20.child(5)
        ___qtreewidgetitem26.setText(0, QCoreApplication.translate("MainWindow", u"virtio-serial-pci", None));
        ___qtreewidgetitem27 = self.treeWidget.topLevelItem(4)
        ___qtreewidgetitem27.setText(0, QCoreApplication.translate("MainWindow", u"\u7f51\u5361", None));
        ___qtreewidgetitem28 = ___qtreewidgetitem27.child(0)
        ___qtreewidgetitem28.setText(0, QCoreApplication.translate("MainWindow", u"netdev", None));
        ___qtreewidgetitem29 = ___qtreewidgetitem27.child(1)
        ___qtreewidgetitem29.setText(0, QCoreApplication.translate("MainWindow", u"e1000", None));
        ___qtreewidgetitem30 = ___qtreewidgetitem27.child(2)
        ___qtreewidgetitem30.setText(0, QCoreApplication.translate("MainWindow", u"e1000e", None));
        ___qtreewidgetitem31 = ___qtreewidgetitem27.child(3)
        ___qtreewidgetitem31.setText(0, QCoreApplication.translate("MainWindow", u"i82550", None));
        ___qtreewidgetitem32 = ___qtreewidgetitem27.child(4)
        ___qtreewidgetitem32.setText(0, QCoreApplication.translate("MainWindow", u"virtio-net-pci", None));
        ___qtreewidgetitem33 = ___qtreewidgetitem27.child(5)
        ___qtreewidgetitem33.setText(0, QCoreApplication.translate("MainWindow", u"i82558a", None));
        ___qtreewidgetitem34 = ___qtreewidgetitem27.child(6)
        ___qtreewidgetitem34.setText(0, QCoreApplication.translate("MainWindow", u"igb", None));
        ___qtreewidgetitem35 = ___qtreewidgetitem27.child(7)
        ___qtreewidgetitem35.setText(0, QCoreApplication.translate("MainWindow", u"ne2k_isa", None));
        ___qtreewidgetitem36 = ___qtreewidgetitem27.child(8)
        ___qtreewidgetitem36.setText(0, QCoreApplication.translate("MainWindow", u"ne2k_pci", None));
        ___qtreewidgetitem37 = ___qtreewidgetitem27.child(9)
        ___qtreewidgetitem37.setText(0, QCoreApplication.translate("MainWindow", u"rtl8139", None));
        ___qtreewidgetitem38 = ___qtreewidgetitem27.child(10)
        ___qtreewidgetitem38.setText(0, QCoreApplication.translate("MainWindow", u"usb-net", None));
        ___qtreewidgetitem39 = self.treeWidget.topLevelItem(5)
        ___qtreewidgetitem39.setText(0, QCoreApplication.translate("MainWindow", u"\u5b58\u50a8", None));
        ___qtreewidgetitem40 = ___qtreewidgetitem39.child(0)
        ___qtreewidgetitem40.setText(0, QCoreApplication.translate("MainWindow", u"drive", None));
        ___qtreewidgetitem41 = ___qtreewidgetitem39.child(1)
        ___qtreewidgetitem41.setText(0, QCoreApplication.translate("MainWindow", u"dc390", None));
        ___qtreewidgetitem42 = ___qtreewidgetitem39.child(2)
        ___qtreewidgetitem42.setText(0, QCoreApplication.translate("MainWindow", u"ide-cd", None));
        ___qtreewidgetitem43 = ___qtreewidgetitem39.child(3)
        ___qtreewidgetitem43.setText(0, QCoreApplication.translate("MainWindow", u"ide-hd", None));
        ___qtreewidgetitem44 = ___qtreewidgetitem39.child(4)
        ___qtreewidgetitem44.setText(0, QCoreApplication.translate("MainWindow", u"isa-fdc", None));
        ___qtreewidgetitem45 = ___qtreewidgetitem39.child(5)
        ___qtreewidgetitem45.setText(0, QCoreApplication.translate("MainWindow", u"isa-ide", None));
        ___qtreewidgetitem46 = ___qtreewidgetitem39.child(6)
        ___qtreewidgetitem46.setText(0, QCoreApplication.translate("MainWindow", u"sd-card", None));
        ___qtreewidgetitem47 = ___qtreewidgetitem39.child(7)
        ___qtreewidgetitem47.setText(0, QCoreApplication.translate("MainWindow", u"usb-uas", None));
        ___qtreewidgetitem48 = ___qtreewidgetitem39.child(8)
        ___qtreewidgetitem48.setText(0, QCoreApplication.translate("MainWindow", u"virtio-blk-pci", None));
        ___qtreewidgetitem49 = self.treeWidget.topLevelItem(6)
        ___qtreewidgetitem49.setText(0, QCoreApplication.translate("MainWindow", u"\u663e\u793a\u8bbe\u5907", None));
        ___qtreewidgetitem50 = ___qtreewidgetitem49.child(0)
        ___qtreewidgetitem50.setText(0, QCoreApplication.translate("MainWindow", u"ati-vga", None));
        ___qtreewidgetitem51 = ___qtreewidgetitem49.child(1)
        ___qtreewidgetitem51.setText(0, QCoreApplication.translate("MainWindow", u"cirrus-vga", None));
        ___qtreewidgetitem52 = ___qtreewidgetitem49.child(2)
        ___qtreewidgetitem52.setText(0, QCoreApplication.translate("MainWindow", u"VGA", None));
        ___qtreewidgetitem53 = ___qtreewidgetitem49.child(3)
        ___qtreewidgetitem53.setText(0, QCoreApplication.translate("MainWindow", u"virtio-gpu-pci", None));
        ___qtreewidgetitem54 = self.treeWidget.topLevelItem(7)
        ___qtreewidgetitem54.setText(0, QCoreApplication.translate("MainWindow", u"\u58f0\u5361", None));
        ___qtreewidgetitem55 = ___qtreewidgetitem54.child(0)
        ___qtreewidgetitem55.setText(0, QCoreApplication.translate("MainWindow", u"AC97", None));
        ___qtreewidgetitem56 = ___qtreewidgetitem54.child(1)
        ___qtreewidgetitem56.setText(0, QCoreApplication.translate("MainWindow", u"adlib", None));
        ___qtreewidgetitem57 = ___qtreewidgetitem54.child(2)
        ___qtreewidgetitem57.setText(0, QCoreApplication.translate("MainWindow", u"cs4231a", None));
        ___qtreewidgetitem58 = ___qtreewidgetitem54.child(3)
        ___qtreewidgetitem58.setText(0, QCoreApplication.translate("MainWindow", u"intel-hda", None));
        ___qtreewidgetitem59 = ___qtreewidgetitem54.child(4)
        ___qtreewidgetitem59.setText(0, QCoreApplication.translate("MainWindow", u"ES1370", None));
        ___qtreewidgetitem60 = self.treeWidget.topLevelItem(8)
        ___qtreewidgetitem60.setText(0, QCoreApplication.translate("MainWindow", u"\u81ea\u5b9a\u4e49", None));
        ___qtreewidgetitem61 = ___qtreewidgetitem60.child(0)
        ___qtreewidgetitem61.setText(0, QCoreApplication.translate("MainWindow", u"\u81ea\u5b9a\u4e49\u8bbe\u5907", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        self.pushButton_66.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.pushButton_72.setText("")
        self.pushButton_75.setText("")
        self.pushButton_92.setText("")
        self.pushButton_95.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.pushButton_93.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"\u4f5c\u56fe\u4eff\u771f\u5f00\u53d1", None))
        self.pushButton_68.setText(QCoreApplication.translate("MainWindow", u"QEMU\u76ee\u5f55", None))
        self.pushButton_71.setText(QCoreApplication.translate("MainWindow", u"\u8bb0\u5f55\u76ee\u5f55", None))
        self.pushButton_69.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u5fd7\u76ee\u5f55", None))
        self.label_27.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u7f51\u7edc\u5b89\u5168\u5b66\u79d1\u4e13\u4e1a\u5efa\u8bbe\n"
"\u67d0\u5b89\u5168\u6559\u5b66\u6f14\u8bad\u5206\u7cfb\u7edf", None))
    # retranslateUi

