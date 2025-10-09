from uiScripts.ui_DeviceInfo import Ui_Dialog
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


class DeviceInfoDialog(QDialog, Ui_Dialog):
    def __init__(self,parent = None,info_path = ""):
        try:
            super().__init__(parent)

        except:
            super().__init__()

        self.setupUi(self)
        self.exec_folder = pf.retrieveExecFolder()
        self.setWindowTitle("")
        currentWidget = None
        with open(info_path,"r") as f:
            for line in f.readlines():
                if "仿真类型信息" in line:
                    currentWidget = self.textBrowser
                    continue
                elif "仿真环境信息" in line:
                    currentWidget = self.textBrowser_2
                    continue
                elif "仿真框架信息" in line:
                    currentWidget = self.textBrowser_3
                    continue
                elif "仿真模板类型信息" in line:
                    currentWidget = self.textBrowser_4
                    continue
                elif "外设组件信息" in line:
                    currentWidget = self.textBrowser_5
                    continue
                if currentWidget != None:
                    currentWidget.append(line.strip())
