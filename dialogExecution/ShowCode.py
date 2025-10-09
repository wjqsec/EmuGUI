from uiScripts.ui_ShowCode import Ui_Dialog
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


class ShowCodeDialog(QDialog, Ui_Dialog):
    def __init__(self,parent = None,code = ""):
        try:
            super().__init__(parent)

        except:
            super().__init__()

        self.setupUi(self)
        self.exec_folder = pf.retrieveExecFolder()
        self.setWindowTitle("")
        self.textBrowser.setText(code)
