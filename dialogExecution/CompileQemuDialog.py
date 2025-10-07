from uiScripts.ui_CompileQemuDialog import Ui_Dialog
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


class CompileQemuDialog(QDialog, Ui_Dialog):
    def __init__(self,parent = None,qemu_dir = ""):
        try:
            super().__init__(parent)

        except:
            super().__init__()

        self.setupUi(self)
        self.exec_folder = pf.retrieveExecFolder()
        self.setWindowTitle("")
        self.connectSignalsSlots()
        self.qemu_dir = qemu_dir
        

    def compile(self):
        self.pushButton_2.setParent(None)
        self.pushButton_2.deleteLater()
        process = subprocess.Popen(
            "make",
            cwd=self.qemu_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,       # Decode bytes to str automatically
            bufsize=1        # Line-buffered output
        )
        for line in process.stdout:
            self.add_text(line)
        process.wait()
        self.enable_cancel()
        
        
    def add_text(self,txt):
        self.textBrowser.append(txt)
    def enable_cancel(self):
        self.pushButton.setEnabled(True)
    def connectSignalsSlots(self):
        self.pushButton.clicked.connect(self.pushBtnClicked)
        self.pushButton_2.clicked.connect(self.compile)
    def pushBtnClicked(self):
        self.close()
