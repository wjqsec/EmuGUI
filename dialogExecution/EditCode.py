from uiScripts.ui_EditCode import Ui_Dialog
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


class EditCodeDialog(QDialog, Ui_Dialog):
    def __init__(self,parent = None,title = "",path = "",start_line = 0):
        try:
            super().__init__(parent)

        except:
            super().__init__()

        self.setupUi(self)
        self.exec_folder = pf.retrieveExecFolder()
        self.setWindowTitle("")
        self.label.setText(title)
        self.path = path
        if path != "":
            f = open(path,"r")
            self.textEdit.setPlainText(f.read())
        self.pushButton.clicked.connect(self.close_all)
    def close_all(self):
        if self.path != "":
            f = open(self.path,"w")
            f.write(self.textEdit.toPlainText())
        self.close()
