from uiScripts.ui_DevConfig import Ui_Dialog
from PySide6.QtWidgets import *
from PySide6 import QtGui
import platform
from time import sleep
from PySide6.QtCore import QThread, Signal, QTimer
if platform.system() == "Windows":
    import platformSpecific.windowsSpecific

else:
    import platformSpecific.unixSpecific

import translations.en
import locale
import sqlite3
import services.pathfinder as pf
import subprocess

from PySide6.QtWidgets import *
from PySide6 import QtGui
from PySide6.QtCore import *


class DevConfigDialog(QDialog, Ui_Dialog):
    def __init__(self,config_data,parent = None):
        try:
            super().__init__(parent)

        except:
            super().__init__()
        self.config = config_data
        self.setupUi(self)
        for i in config_data:
            key = i[1]
            item_key = QLabel(key)
            item_key.setFixedHeight(30)
            item_key.setAlignment(Qt.AlignCenter)
            self.verticalWidget_2.layout().addWidget(item_key)


            if type(i[2]) is int or type(i[2]) is str:
                item_value = QLineEdit()
            elif type(i[2]) is bool:
                item_value = QCheckBox()
            elif type(i[2]) is list:
                item_value = QComboBox()
                item_value.addItems(i[2])
            item_value.setFixedHeight(30)
            self.verticalWidget_3.layout().addWidget(item_value)
        self.pushButton.clicked.connect(self.accept)
    def accept(self) -> None:
        for i in range(len(self.config)):
            widget = self.verticalWidget_3.layout().itemAt(i).widget()
            if type(self.config[i][2]) is int:
                self.config[i][2] = int(widget.text())
            elif type(self.config[i][2]) is str:
                self.config[i][2] = widget.text()
            elif type(self.config[i][2]) is bool:
                self.config[i][2] = widget.isChecked()
            elif type(self.config[i][2]) is list:
                self.config[i][2] = widget.currentText()
        self.close()
