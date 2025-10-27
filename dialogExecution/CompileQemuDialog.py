from uiScripts.ui_CompileQemuDialog import Ui_Dialog
from PySide6.QtWidgets import *
from PySide6 import QtGui
import platform
from time import sleep
from PySide6.QtCore import QThread, Signal, QTimer, Signal
if platform.system() == "Windows":
    import platformSpecific.windowsSpecific

else:
    import platformSpecific.unixSpecific

import translations.en
import locale
import sqlite3
import services.pathfinder as pf
import subprocess


class CompileQemuWorker(QThread):
    output = Signal(str)
    finished = Signal(int)
    def __init__(self, qemu_path):
        super().__init__()
        self.qemu_path = qemu_path
    def run(self):
        process = subprocess.Popen(
            "make",
            cwd=self.qemu_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,       # Decode bytes to str automatically
            bufsize=1        # Line-buffered output
        )
        for line in process.stdout:
            self.output.emit(line.strip())
        process.wait()
        self.finished.emit(process.returncode)

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
        
    def append_output(self, text):
        self.textBrowser.append(text)
    def task_done(self, code):
        msgBox = QMessageBox()
        msgBox.setStandardButtons(QMessageBox.Ok)
        if code == 0:
            msgBox.setText(f"应用成功")
        else:
            msgBox.setText(f"应用失败，请检查修改的源代码！")
        msgBox.exec()
        self.enable_cancel()
    def compile(self):
        self.pushButton_2.setParent(None)
        self.pushButton_2.deleteLater()
        self.worker = CompileQemuWorker(self.qemu_dir)
        self.worker.output.connect(self.append_output)
        self.worker.finished.connect(self.task_done)
        self.worker.start()
        
        
        

    def enable_cancel(self):
        self.pushButton.setEnabled(True)
    def connectSignalsSlots(self):
        self.pushButton.clicked.connect(self.pushBtnClicked)
        self.pushButton_2.clicked.connect(self.compile)
    def pushBtnClicked(self):
        self.close()
