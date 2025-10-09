 # Importing required modules
import os

try:
    import platform

    if platform.system() == "Windows":
        import platformSpecific.windowsSpecific

    else:
        import platformSpecific.unixSpecific

        try:
            import qdarktheme

        except:
            print("EmuGUI has to warn you.")
            print("Error code: W-11-CLZLM")
            print("If this error occurs multiple times, contact your administrator and/or ask for help on the EmuGUI Discord Server or on its GitHub repository.")

except:
    print("EmuGUI encountered a critical error and needs to be closed.")
    print("Error code: C-07-39KHE")
    print("If this error occurs multiple times, contact your administrator and/or ask for help on the EmuGUI Discord Server or on its GitHub repository.")
    input("Press any key to exit.")
    exit()

try:
    import sys

except:
    print("EmuGUI encountered a critical error and needs to be closed.")
    print("Error code: C-06-2FZIM")
    print("If this error occurs multiple times, contact your administrator and/or ask for help on the EmuGUI Discord Server or on its GitHub repository.")
    input("Press any key to exit.")
    exit()
    
try:
    from PySide6.QtWidgets import *
    from PySide6 import QtGui
    from PySide6.QtCore import *
    from uiScripts.ui_Main import Ui_MainWindow

except:
    print("EmuGUI encountered a critical error and needs to be closed.")
    print("Error code: C-00-LOVJL")
    print("If this error occurs multiple times, contact your administrator and/or ask for help on the EmuGUI Discord Server or on its GitHub repository.")
    input("Press any key to exit.")
    exit()

import errors.errCodes

# NewVirtualMachineDialog 对话框
from dialogExecution.newVirtualMachine import NewVirtualMachineDialog
from dialogExecution.startVirtualMachine import StartVirtualMachineDialog
from dialogExecution.editVMNew import EditVMNewDialog
from dialogExecution.win81NearEOS import Win812012R2NearEOS
from dialogExecution.errDialog import ErrDialog
from dialogExecution.CompileQemuDialog import CompileQemuDialog
from dialogExecution.ShowCode import ShowCodeDialog
from dialogExecution.EditCode import EditCodeDialog
from dialogExecution.DeviceInfo import DeviceInfoDialog
from dialogExecution.settingsRequireRestart import *

try:
    import translations.en
    import locale

except:
    print("EmuGUI encountered an error.")
    print("Error code: E-08-LXG6H")
    print("If this error occurs multiple times, contact your administrator and/or ask for help on the EmuGUI Discord Server or on its GitHub repository.")

try:
    import sqlite3

except:
    print("EmuGUI encountered a critical error and needs to be closed.")
    print("Error code: C-03-DR8ZW")
    print("If this error occurs multiple times, contact your administrator and/or ask for help on the EmuGUI Discord Server or on its GitHub repository.")
    input("Press any key to exit.")
    exit()

import glob
import webbrowser
import datetime
import dateutil.easter
import zipfile
import errors.logman
import errors.logID

try:
    import psutil

except:
    print("EmuGUI has to warn you.")
    print("Error code: W-06-NPGOP")
    print("If this error occurs multiple times, contact your administrator and/or ask for help on the EmuGUI Discord Server or on its GitHub repository.")

try:
    import services.pathfinder as pf

except:
    print("EmuGUI has to warn you.")
    print("Error code: W-12-JBJM9")
    print("If this error occurs multiple times, contact your administrator and/or ask for help on the EmuGUI Discord Server or on its GitHub repository.")

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        # This function initializes and runs EmuGUI
        try:
            super().__init__(parent)

        except:
            super().__init__()
        
        self.setupUi(self)
        # 隐藏 tab_6 general
        if hasattr(self, "tab_6"):
            self.tabWidget_2.removeTab(self.tabWidget_2.indexOf(self.tab_6))
        # 隐藏 tab_4 about EmuGUI
        if hasattr(self, "tab_4"):
            self.tabWidget_2.removeTab(self.tabWidget_2.indexOf(self.tab_4))
        self.exec_folder = pf.retrieveExecFolder()
        print(self.exec_folder)
        self.connectSignalsSlots()
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateVmList)
        logman = errors.logman.LogMan()
        logman.generateLogID()
        logman.logFile = logman.setLogFile()
        self.version = ""
        translations.en.translateMainEN(self)
        self.architectures = [
            ["i386", self.lineEdit_4],
            ["x86_64", self.lineEdit_3],
            ["ppc", self.lineEdit_2],
            ["ppc64", self.lineEdit_8],
            ["mips64el", self.lineEdit],
            ["mips64", self.lineEdit_11],
            ["mipsel", self.lineEdit_9],
            ["mips", self.lineEdit_10],
            ["aarch64", self.lineEdit_6],
            ["arm", self.lineEdit_7],
            ["sparc", self.lineEdit_12],
            ["sparc64", self.lineEdit_13],
            ["alpha", self.le_alpha],
            ["riscv32", self.le_riscv32],
            ["riscv64", self.le_riscv64]
        ]

        print(f"EmuGUI {self.version}")

        print(f"Current date: {datetime.date.today()}")

        if platform.system() == "Windows" and sys.getwindowsversion().build >= 21296:
            print(f"OS: Windows 11 or later, Version {platform.uname().version}")

        else:
            print(f"OS: {platform.uname().system} {platform.uname().release}, Version {platform.uname().version}")

        try:
            print(f"CPU: {str(os.cpu_count())}x {platform.uname().processor} @{round((psutil.cpu_freq().max / 1024), 2)} GHz ({platform.machine()})")
            print(f"RAM: {psutil.virtual_memory().total} bytes ({round((psutil.virtual_memory().total / 1024 / 1024 / 1024), 2)} GB)")
        
        except:
            print(f"CPU: {str(os.cpu_count())}x {platform.uname().processor} ({platform.machine()})")

        print(f"Python: {platform.python_version()} {platform.python_branch()}, compiled with {platform.python_compiler()}")

        logman.writeToLogFile(f"{errors.errCodes.errCodes[38]}: Running EmuGUI {self.version}")

        if self.version.__contains__("_dev") or self.version.__contains__("_rc") or self.version.__contains__("_b"):
            logman.writeToLogFile(f"{errors.errCodes.errCodes[39]}: This version is a pre-release. Don't use it for production")

        if platform.system() == "Windows" and sys.getwindowsversion().build >= 21296:
            logman.writeToLogFile(
                f"{errors.errCodes.errCodes[40]}: Device powered by Windows 11 or later, Version {platform.uname().version}"
                )
            
        else:
            logman.writeToLogFile(
                f"{errors.errCodes.errCodes[40]}: Device powered by {platform.uname().system} {platform.uname().release}, Version {platform.uname().version}"
                )
        
        logman.writeToLogFile(
            f"{errors.errCodes.errCodes[41]}: EmuGUI powered by Python {platform.python_version()} {platform.python_branch()}, compiled with {platform.python_compiler()}"
            )
        
        # logman.writeToLogFile(
        #     f"{errors.errCodes.errCodes[42]}: CPU is {str(os.cpu_count())}x {platform.uname().processor} @{round((psutil.cpu_freq().max / 1024), 2)} GHz ({platform.machine()})"
        #     )
        
        if os.cpu_count() == 1:
            logman.writeToLogFile(
                f"{errors.errCodes.errCodes[43]}: Single-core CPU detected! Proceed at your own risk. Support requests won't be prioritised."
                )
            
        logman.writeToLogFile(
            f"{errors.errCodes.errCodes[44]}: Device contains {psutil.virtual_memory().total} bytes of RAM"
            )
        
        if round(psutil.virtual_memory().total / (1024 * 3), 2) < 3.84: # Ik, should be 4, but I defined 3.84 GB bc of most PC's habits of taking some RAM away
            logman.writeToLogFile(
                f"{errors.errCodes.errCodes[45]}: Less than 4 GB of RAM detected! Proceed at your own risk. Support requests won't be prioritised."
                )
            
        if platform.system() == "Windows":
            winvers = sys.getwindowsversion()
            if winvers.build >= 21296 and round(psutil.virtual_memory().total / (1024 * 3), 2) < 5.84:
                logman.writeToLogFile(
                    f"{errors.errCodes.errCodes[46]}: Less than 6 GB of RAM detected! As you're using Windows 11, proceed at your own risk. Support requests won't be prioritised."
                    )

        #self.label_8.setText(f"EmuGUI {self.version}\nCodename 'Ioana Rosa'")
        #self.setWindowTitle(f"EmuGUI {self.version}")

        if datetime.date.today().day == 1 and datetime.date.today().month == 4:
            wintitle = self.windowTitle()
            self.setWindowTitle("".join(reversed(wintitle)))

        self.languageInUse = "system"

        try:
            self.setWindowIcon(QtGui.QIcon(f"{self.exec_folder}EmuGUI.png"))

        except:
            pass

        self.versionCode = 5620

        if platform.system() == "Windows":
            self.connection = platformSpecific.windowsSpecific.setupWindowsBackend()
        
        else:
            self.connection = platformSpecific.unixSpecific.setupUnixBackend()

        self.defaultTheme = self.style().objectName()
        self.osThemes = QStyleFactory.keys()
        print(self.osThemes)

        for osTheme in self.osThemes:
            #self.comboBox_5.addItem(osTheme)
            print(osTheme)

        self.userThemeFileList = glob.glob(f"{self.exec_folder}themes/*.qss")
        self.userThemeList = []
        
        for userThemeFile in self.userThemeFileList:
            userTheme = userThemeFile.replace(".qss", "")
            
            if platform.system() == "Windows":
                userTheme = userTheme.replace(f"{self.exec_folder}themes\\", "")
            
            else:
                userTheme = userTheme.replace(f"{self.exec_folder}themes/", "")
            
            #self.comboBox_5.addItem(userTheme)
            #self.userThemeList.append(userTheme)
        
        self.prepareDatabase(self.connection)
        self.updateVmList()

        if platform.system() == "Windows":
            winvers = sys.getwindowsversion()
            if winvers.major <= 6 and winvers.minor <= 3:
                dialog = Win812012R2NearEOS(self)
                dialog.exec()
                
                self.label_8.setText(
                    f"EmuGUI {self.version}\nCodename 'Ioana Rosa'\nYour OS is no longer supported by EmuGUI. You should upgrade at least to Windows 10. You're currently running Windows {platform.release()}")
    
    def resizeEvent(self, event: QtGui.QResizeEvent):
        super().resizeEvent(event)

        #self.gridLayoutWidget.resize(event.size())
        #self.tabWidget_2.resize(event.size())
        #self.gridLayoutWidget_4.resize(QSize(event.size().width() - 9, event.size().height() - 66))
        #self.tabWidget_2.resize(QSize(event.size().width() - 9, event.size().height() - 56))
        #self.gridLayoutWidget_2.resize(QSize(event.size().width() - 19, event.size().height() - 86))
        #self.gridLayoutWidget_3.resize(QSize(event.size().width() - 19, event.size().height() - 86))
        #self.gridLayoutWidget_6.resize(QSize(event.size().width() - 19, event.size().height() - 86))
        
        #self.centralwidget.resize(event.size())
    

    def connectSignalsSlots(self):
        # These buttons are connected to their incorporate functions
        self.pushButton_8.clicked.connect(self.createNewVM)
        self.pushButton.clicked.connect(self.set_qemu_img_path)
        self.pushButton_2.clicked.connect(self.set_qemu_i386_path)
        self.pushButton_3.clicked.connect(self.set_qemu_x86_64_path)
        self.pushButton_4.clicked.connect(self.set_qemu_ppc_path)
        self.pushButton_5.clicked.connect(self.set_qemu_mips64el_path)
        self.pushButton_17.clicked.connect(self.set_qemu_mipsel_path)
        self.pushButton_19.clicked.connect(self.set_qemu_mips64_path)
        self.pushButton_18.clicked.connect(self.set_qemu_mips_path)
        self.pushButton_16.clicked.connect(self.set_qemu_ppc64_path)
        self.btn_alpha.clicked.connect(self.set_qemu_alpha_path)
        self.btn_riscv32.clicked.connect(self.set_qemu_riscv32_path)
        self.btn_riscv64.clicked.connect(self.set_qemu_riscv64_path)
        self.pushButton_6.clicked.connect(self.applyChangesQemu)
        self.btn_apply_qemu2.clicked.connect(self.applyChangesQemu)
        self.pushButton_9.clicked.connect(self.startVM)
        self.pushButton_11.clicked.connect(self.deleteVM)
        self.pushButton_10.clicked.connect(self.editVM)
        self.pushButton_22.clicked.connect(self.exportVM)
        self.pushButton_23.clicked.connect(self.importVM)
        self.pushButton_7.clicked.connect(self.set_qemu_aarch64_path)
        self.pushButton_12.clicked.connect(self.set_qemu_arm_path)
        #self.pushButton_15.clicked.connect(self.applyGeneric)
        self.pushButton_13.clicked.connect(self.set_qemu_sparc_path)
        self.pushButton_14.clicked.connect(self.set_qemu_sparc64_path)
        #self.pushButton_20.clicked.connect(self.toGithub)
        #self.pushButton_21.clicked.connect(self.toDiscord)
        #self.pushButton_24.clicked.connect(self.toYouTube)
        #self.pushButton_25.clicked.connect(self.toOdysee)
        #self.btn_guilded.clicked.connect(self.toGuilded)
        self.pushButton_32.clicked.connect(self.runPythonScript)
        
        self.pushButton_25.clicked.connect(self.compileQemu)
        self.pushButton_26.clicked.connect(self.compileQemu)
        self.pushButton_27.clicked.connect(self.compileQemu)
        self.pushButton_28.clicked.connect(self.compileQemu)
        
        self.pushButton_30.clicked.connect(self.showAPIExample1)
        self.pushButton_31.clicked.connect(self.showAPIExample2)
        self.pushButton_29.clicked.connect(self.showAPI)
        
        self.pushButton_21.clicked.connect(self.editInsCode)
        
        self.pushButton_33.clicked.connect(self.showDeviceInfo)
        easter_this_year = dateutil.easter.easter(datetime.date.today().year)
        good_friday_delta = datetime.timedelta(days=-2)
        good_saturday_delta = datetime.timedelta(days=-1)
        easter_monday_delta = datetime.timedelta(days=1)

        print(easter_this_year)

        if datetime.date.today() == easter_this_year or datetime.date.today() == easter_this_year + good_friday_delta:
            self.label_6.setPixmap(QtGui.QPixmap(f"{self.exec_folder}banners/RobertRabbit.png"))

        elif datetime.date.today() == easter_this_year + easter_monday_delta or datetime.date.today() == easter_this_year + good_saturday_delta:
            self.label_6.setPixmap(QtGui.QPixmap(f"{self.exec_folder}banners/RobertRabbit.png"))

        else:
            pass
            #self.label_6.setPixmap(QtGui.QPixmap(f"{self.exec_folder}banners/IoanaRosa.png"))

        if datetime.date.today().day == 1 and datetime.date.today().month == 4:
            pixmap = self.label_6.pixmap()
            self.rotation = 180

            transform = QtGui.QTransform().rotate(self.rotation)
            pixmap = pixmap.transformed(transform, Qt.FastTransformation)
            self.label_6.setPixmap(pixmap)

    def setLanguage(self, langmode):
        self.languageInUse = "en"

    def prepareDatabase(self, connection):
        # Some SQL statements to initialize EmuGUI
        create_settings_table = """
        CREATE TABLE IF NOT EXISTS settings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            value TEXT
        );
        """

        create_vm_table = """
        CREATE TABLE IF NOT EXISTS virtualmachines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            mode TEXT NOT NULL,
            architecture TEXT NOT NULL,
            machine TEXT NOT NULL,
            cpu TEXT NOT NULL,
            ram INTEGER NOT NULL,
            hda TEXT,
            vga TEXT NOT NULL,
            net TEXT,
            usbtablet INTEGER NOT NULL,
            win2k INTEGER NOT NULL,
            dirbios TEXT,
            additionalargs TEXT,
            sound TEXT NOT NULL,
            linuxkernel TEXT NOT NULL,
            linuxinitrid TEXT NOT NULL,
            linuxcmd TEXT NOT NULL,
            mousetype TEXT NOT NULL,
            cores INT DEFAULT 1 NOT NULL,
            filebios TEXT DEFAULT "" NOT NULL,
            keyboardtype TEXT NOT NULL,
            usbsupport INT DEFAULT 0 NOT NULL,
            usbcontroller TEXT DEFAULT "pci-ohci" NOT NULL,
            kbdtype TEXT DEFAULT "en-us" NOT NULL,
            acceltype TEXT DEFAULT "None" NOT NULL,
            storagecontrollercd1 TEXT DEFAULT "Let QEMU decide" NOT NULL,
            storagecontrollercd2 TEXT DEFAULT "Let QEMU decide" NOT NULL,
            hdacontrol TEXT DEFAULT "Let QEMU decide" NOT NULL
        );
        """

        create_update_table = """
        CREATE TABLE IF NOT EXISTS updater (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            value TEXT NOT NULL
        );
        """

        # The v0.2 feature set
        select02ColumnsVM = """
        SELECT sound, linuxkernel, linuxinitrid, linuxcmd FROM virtualmachines;
        """

        # The v0.3 feature set
        select03ColumnsVM = """
        SELECT mousetype FROM virtualmachines;
        """

        select03ColumnsVM2 = """
        SELECT cores, filebios FROM virtualmachines;
        """

        # The v0.4 feature set
        select04ColumnsVM = """
        SELECT keyboardtype, usbsupport FROM virtualmachines;
        """

        # The v0.5 feature set
        select05ColumnsVM = """
        SELECT usbcontroller FROM virtualmachines;
        """

        # The v0.9 feature set
        select09ColumnsVM = """
        SELECT kbdtype FROM virtualmachines;
        """

        # The v1.1 feature set
        select11ColumnsVM = """
        SELECT acceltype FROM virtualmachines;
        """

        # The v1.2 feature set
        select12ColumnsVM = """
        SELECT storagecontrollercd1, storagecontrollercd2 FROM virtualmachines;
        """

        select12ColumnsVM2 = """
        SELECT hdacontrol FROM virtualmachines;
        """

        insertSoundColVM = """
        ALTER TABLE virtualmachines
        ADD COLUMN sound TEXT DEFAULT "none" NOT NULL;
        """

        insertLinuxKernelColVM = """
        ALTER TABLE virtualmachines
        ADD COLUMN linuxkernel TEXT DEFAULT "" NOT NULL;
        """

        insertLinuxInitridColVM = """
        ALTER TABLE virtualmachines
        ADD COLUMN linuxinitrid TEXT DEFAULT "" NOT NULL;
        """

        insertLinuxCmdColVM = """
        ALTER TABLE virtualmachines
        ADD COLUMN linuxcmd TEXT DEFAULT "" NOT NULL;
        """

        insertMouseTypeVM = """
        ALTER TABLE virtualmachines
        ADD COLUMN mousetype TEXT DEFAULT "PS/2 Mouse" NOT NULL;
        """

        insertCpuCoresVM = """
        ALTER TABLE virtualmachines
        ADD COLUMN cores TEXT DEFAULT 1 NOT NULL;
        """

        insertBiosFileVM = """
        ALTER TABLE virtualmachines
        ADD COLUMN filebios TEXT DEFAULT "" NOT NULL;
        """

        insertKeyboardTypeVM = """
        ALTER TABLE virtualmachines
        ADD COLUMN keyboardtype TEXT DEFAULT "PS/2 Keyboard" NOT NULL;
        """

        insertUsbSupportVM = """
        ALTER TABLE virtualmachines
        ADD COLUMN usbsupport INT DEFAULT 0 NOT NULL;
        """

        insertUsbControllerVM = """
        ALTER TABLE virtualmachines
        ADD COLUMN usbcontroller TEXT DEFAULT "pci-ohci" NOT NULL;
        """

        insertKbdLayoutVM = """
        ALTER TABLE virtualmachines
        ADD COLUMN kbdtype TEXT DEFAULT "en-us" NOT NULL;
        """

        insertAccelTypeVM = """
        ALTER TABLE virtualmachines
        ADD COLUMN acceltype TEXT DEFAULT "None" NOT NULL;
        """

        insertStorageControllerCD1VM = """
        ALTER TABLE virtualmachines
        ADD COLUMN storagecontrollercd1 TEXT DEFAULT "Let QEMU decide" NOT NULL;
        """

        insertStorageControllerCD2VM = """
        ALTER TABLE virtualmachines
        ADD COLUMN storagecontrollercd2 TEXT DEFAULT "Let QEMU decide" NOT NULL;
        """

        inserthdaControlVM = """
        ALTER TABLE virtualmachines
        ADD COLUMN hdacontrol TEXT DEFAULT "Let QEMU decide" NOT NULL;
        """

        insert_qemu_img = """
        INSERT INTO settings (
            name
        ) VALUES (
            "qemu-img"
        );
        """

        # Language codes:
        # default: same language as system (English if not present)
        # en: English
        # de: German
        # uk: Ukranian
        # fr: French
        # es: Spanish
        # ro: Romanian
        # be: Belarusian
        # cz: Czech
        # ru: Russian
        # pt: Portuguese
        # it: Italian
        # pl: Polish
        insert_language = """
        INSERT INTO settings (
            name, value
        ) VALUES (
            "lang", "default"
        );
        """

        # Theme support
        insert_theme = """
        INSERT INTO settings (
            name, value
        ) VALUES (
            "theme", "default"
        );
        """

        debug_db_settings = """
        SELECT name, value FROM settings;
        """

        select_qemu_img = """
        SELECT name, value FROM settings
        WHERE name = "qemu-img";
        """

        select_language = """
        SELECT name, value FROM settings
        WHERE name = "lang";
        """

        select_theme = """
        SELECT name, value FROM settings
        WHERE name = "theme";
        """

        cursor = connection.cursor()
        logman = errors.logman.LogMan()
        logman.logFile = logman.setLogFile()

        # If they don't exist yet, the settings and VM tables are created.

        try:
            cursor.execute(create_settings_table)
            connection.commit()
            print("The settings table was created successfully.")
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

            if platform.system() == "Windows":
                errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
            else:
                errorFile = platformSpecific.unixSpecific.unixErrorFile()

            with open(errorFile, "w+") as errCodeFile:
                errCodeFile.write(errors.errCodes.errCodes[2])

            logman.writeToLogFile(
                f"{errors.errCodes.errCodes[2]}: Could not connect to the database to create the settings table."
                )

            dialog = ErrDialog(self)
            dialog.exec()

        try:
            cursor.execute(create_vm_table)
            connection.commit()
            print("The VM table was created successfully.")
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

            if platform.system() == "Windows":
                errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
            else:
                errorFile = platformSpecific.unixSpecific.unixErrorFile()

            with open(errorFile, "w+") as errCodeFile:
                errCodeFile.write(errors.errCodes.errCodes[2])

            logman.writeToLogFile(
                f"{errors.errCodes.errCodes[2]}: Could not connect to the database to create the VM table."
                )

            dialog = ErrDialog(self)
            dialog.exec()

        try:
            cursor.execute(create_update_table)
            connection.commit()
            print("The update table was created successfully.")
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        # Then, the tables will be checked for completeness.

        try:
            cursor.execute(select_qemu_img)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                self.lineEdit_5.setText(result[0][1])
                print("The query was executed successfully. The qemu-img slot already is in the database.")

            except:
                cursor.execute(insert_qemu_img)
                connection.commit()
                print("The query was executed successfully. The qemu-img slot has been created.")
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

            if platform.system() == "Windows":
                errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
            else:
                errorFile = platformSpecific.unixSpecific.unixErrorFile()

            with open(errorFile, "w+") as errCodeFile:
                errCodeFile.write(errors.errCodes.errCodes[2])

            logman.writeToLogFile(
                f"{errors.errCodes.errCodes[2]}: Could not connect to the database to update the qemu-img slot."
                )

            dialog = ErrDialog(self)
            dialog.exec()

        for architecture in self.architectures:
            sel_query = f"""
            SELECT name, value FROM settings
            WHERE name = "qemu-system-{architecture[0]}";
            """

            ins_query = f"""
            INSERT INTO settings (name)
            VALUES ("qemu-system-{architecture[0]}");
            """

            try:
                cursor.execute(sel_query)
                connection.commit()
                result = cursor.fetchall()

                try:
                    qemu_img_slot = str(result[0])
                    architecture[1].setText(result[0][1])
                    print(f"The query was executed successfully. The qemu-system-{architecture[0]} slot already is in the database.")

                except:
                    cursor.execute(ins_query)
                    connection.commit()
                    print(f"The query was executed successfully. The qemu-system-{architecture[0]} slot has been created.")
        
            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[2])

                logman.writeToLogFile(
                    f"{errors.errCodes.errCodes[2]}: Could not connect to the database to update the qemu-system-{architecture[0]} slot."
                    )

                dialog = ErrDialog(self)
                dialog.exec()

        try:
            cursor.execute(select_language)
            connection.commit()
            result = cursor.fetchall()

            # Language modes
            # system: language of OS
            # en: English
            # de: German
            langmode = "system"

            try:
                qemu_img_slot = str(result[0])

                i = 0
                
                if result[0][1] == "en":
                    while i < self.comboBox_4.count():
                        if self.comboBox_4.itemText(i) == "English":
                            self.comboBox_4.setCurrentIndex(i)
                            break

                        i += 1

                    langmode = "en"


                if platform.system() == "Windows":
                    langfile = platformSpecific.windowsSpecific.windowsLanguageFile()
                
                else:
                    langfile = platformSpecific.unixSpecific.unixLanguageFile()

                if langmode == "system":
                    languageToUseLater = locale.getlocale()[0]
                    languageToUseEvenLater = languageToUseLater.split("_")
                    languageToUseHere = languageToUseEvenLater[0]

                else:
                    languageToUseHere = langmode
                
                try:
                    with open(langfile, "w+") as language:
                        language.write(languageToUseHere)

                except:
                    print("EmuGUI failed to create a language file. Expect some issues.")

                    if platform.system() == "Windows":
                        errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                    else:
                        errorFile = platformSpecific.unixSpecific.unixErrorFile()

                    with open(errorFile, "w+") as errCodeFile:
                        errCodeFile.write(errors.errCodes.errCodes[54])

                    logman.writeToLogFile(
                        f"{errors.errCodes.errCodes[54]}: Could not create the language file. Expect issues."
                    )

                    dialog = ErrDialog(self)
                    dialog.exec()

                self.setLanguage(langmode)

                print("The query was executed successfully. The language slot already is in the database.")

            except:
                try:
                    cursor.execute(insert_language)
                    connection.commit()
                    langmode = "system"

                    if platform.system() == "Windows":
                        langfile = platformSpecific.windowsSpecific.windowsLanguageFile()
                
                    else:
                        langfile = platformSpecific.unixSpecific.unixLanguageFile()

                    if langmode == "system":
                        languageToUseLater = locale.getlocale()[0]
                        languageToUseEvenLater = languageToUseLater.split("_")
                        languageToUseHere = languageToUseEvenLater[0]

                    else:
                        languageToUseHere = langmode
                
                    try:
                        with open(langfile, "w+") as language:
                            language.write(languageToUseHere)

                    except:
                        print("EmuGUI failed to create a language file. Expect some issues.")

                        if platform.system() == "Windows":
                            errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                        else:
                            errorFile = platformSpecific.unixSpecific.unixErrorFile()

                        with open(errorFile, "w+") as errCodeFile:
                            errCodeFile.write(errors.errCodes.errCodes[54])

                        logman.writeToLogFile(
                            f"{errors.errCodes.errCodes[54]}: Could not create the language file. Expect issues."
                        )

                        dialog = ErrDialog(self)
                        dialog.exec()
                    
                    self.setLanguage(langmode)
                    print("The query was executed successfully. The language slot has been created.")

                except:
                    if platform.system() == "Windows":
                        errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                    else:
                        errorFile = platformSpecific.unixSpecific.unixErrorFile()

                    with open(errorFile, "w+") as errCodeFile:
                        errCodeFile.write(errors.errCodes.errCodes[54])

                    logman.writeToLogFile(
                        f"{errors.errCodes.errCodes[54]}: Could not create the language file. Expect issues."
                    )

                    dialog = ErrDialog(self)
                    dialog.exec()

                self.setLanguage(langmode)
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

            if platform.system() == "Windows":
                errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
            else:
                errorFile = platformSpecific.unixSpecific.unixErrorFile()

            with open(errorFile, "w+") as errCodeFile:
                errCodeFile.write(errors.errCodes.errCodes[2])

            logman.writeToLogFile(
                f"{errors.errCodes.errCodes[2]}: Could not connect to the database to update the language settings."
                )

            dialog = ErrDialog(self)
            dialog.exec()

        try:
            cursor.execute(select_theme)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                print("The query was executed successfully. The theme slot already is in the database.")
                print(result[0][1])

                if result[0][1] != "default":
                    for osTheme in self.osThemes:
                        if result[0][1].__contains__(osTheme):
                            try:
                                print(osTheme)
                                app.setStyle(osTheme)

                                i = 0
                                while i < self.comboBox_5.count():
                                    if self.comboBox_5.itemText(i) == osTheme:
                                        self.comboBox_5.setCurrentIndex(i)
                                        break

                                    i += 1
                            except:
                                print("Style couldn't be applied.")

                                if platform.system() == "Windows":
                                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
    
                                else:
                                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                                with open(errorFile, "w+") as errCodeFile:
                                    errCodeFile.write(errors.errCodes.errCodes[55])

                                logman.writeToLogFile(
                                    f"{errors.errCodes.errCodes[55]}: Could not apply the theme."
                                    )

                                dialog = ErrDialog(self)
                                dialog.exec()
                    
                    for userTheme in self.userThemeList:
                        if result[0][1].__contains__(userTheme):
                            try:
                                print(userTheme)
                                userThemeFile = f"{self.exec_folder}themes/" + userTheme + ".qss"

                                with open(userThemeFile, "r") as themeFile:
                                    style = themeFile.read()
                                    app.setStyleSheet(style)

                                i = 0
                                while i < self.comboBox_5.count():
                                    if self.comboBox_5.itemText(i) == userTheme:
                                        self.comboBox_5.setCurrentIndex(i)
                                        break

                                    i += 1
                            except:
                                print("Style couldn't be applied.")

                                if platform.system() == "Windows":
                                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
    
                                else:
                                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                                with open(errorFile, "w+") as errCodeFile:
                                    errCodeFile.write(errors.errCodes.errCodes[55])

                                logman.writeToLogFile(
                                    f"{errors.errCodes.errCodes[55]}: Could not apply the theme."
                                    )

                                dialog = ErrDialog(self)
                                dialog.exec()
                
                else:
                    with open(f"{self.exec_folder}translations/systemdefault.txt", "r+") as sysDefFile:
                        sysDefContent = sysDefFile.read()

                    i = 0
                    while i < self.comboBox_5.count():
                        if sysDefContent.__contains__(self.comboBox_5.itemText(i)):
                            self.comboBox_5.setCurrentIndex(i)
                            break

                        i += 1

            except:
                cursor.execute(insert_theme)
                connection.commit()
                print("The query was executed successfully. The theme slot has been created.")
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

            if platform.system() == "Windows":
                errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
            else:
                errorFile = platformSpecific.unixSpecific.unixErrorFile()

            with open(errorFile, "w+") as errCodeFile:
                errCodeFile.write(errors.errCodes.errCodes[12])

            logman.writeToLogFile(
                f"{errors.errCodes.errCodes[12]}: Could not connect to the database to access the theme settings."
                )

            dialog = ErrDialog(self)
            dialog.exec()

        try:
            cursor.execute(select02ColumnsVM)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                print("The query was executed successfully. The v0.2 feature columns already are in the VM table.")

            except:
                pass
        
        except sqlite3.Error as e:
            try:
                cursor.execute(insertSoundColVM)
                connection.commit()

                cursor.execute(insertLinuxKernelColVM)
                connection.commit()

                cursor.execute(insertLinuxInitridColVM)
                connection.commit()

                cursor.execute(insertLinuxCmdColVM)
                connection.commit()
                print("The queries were executed successfully. The missing features have been added to the database.")
            
            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[2])

                logman.writeToLogFile(
                    f"{errors.errCodes.errCodes[2]}: Could not connect to the database to update the VM list."
                    )

                dialog = ErrDialog(self)
                dialog.exec()

        try:
            cursor.execute(select03ColumnsVM)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                print("The query was executed successfully. The first v0.3 feature columns already are in the VM table.")

            except:
                pass
        
        except sqlite3.Error as e:
            try:
                cursor.execute(insertMouseTypeVM)
                connection.commit()
                print("The queries were executed successfully. The missing features have been added to the database.")
            
            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[2])

                logman.writeToLogFile(
                    f"{errors.errCodes.errCodes[2]}: Could not connect to the database to update the VM list."
                    )

                dialog = ErrDialog(self)
                dialog.exec()

        try:
            cursor.execute(select03ColumnsVM2)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                print("The query was executed successfully. The second v0.3 feature columns already are in the VM table.")

            except:
                pass
        
        except sqlite3.Error as e:
            try:
                cursor.execute(insertCpuCoresVM)
                connection.commit()

                cursor.execute(insertBiosFileVM)
                connection.commit()
                print("The queries were executed successfully. The missing features have been added to the database.")
            
            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[2])

                logman.writeToLogFile(
                    f"{errors.errCodes.errCodes[2]}: Could not connect to the database to update the VM list."
                    )

                dialog = ErrDialog(self)
                dialog.exec()

        try:
            cursor.execute(select04ColumnsVM)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                print("The query was executed successfully. The v0.4 feature columns already are in the VM table.")

            except:
                pass
        
        except sqlite3.Error as e:
            try:
                cursor.execute(insertKeyboardTypeVM)
                connection.commit()

                cursor.execute(insertUsbSupportVM)
                connection.commit()
                print("The queries were executed successfully. The missing features have been added to the database.")
            
            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[2])

                logman.writeToLogFile(
                    f"{errors.errCodes.errCodes[2]}: Could not connect to the database to update the VM list."
                    )

                dialog = ErrDialog(self)
                dialog.exec()

        try:
            cursor.execute(select05ColumnsVM)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                print("The query was executed successfully. The v0.5 feature columns already are in the VM table.")

            except:
                pass
        
        except sqlite3.Error as e:
            try:
                cursor.execute(insertUsbControllerVM)
                connection.commit()
                print("The queries were executed successfully. The missing features have been added to the database.")
            
            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[2])

                logman.writeToLogFile(
                    f"{errors.errCodes.errCodes[2]}: Could not connect to the database to update the VM list."
                    )

                dialog = ErrDialog(self)
                dialog.exec()

        try:
            cursor.execute(select09ColumnsVM)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                print("The query was executed successfully. The v1.0 feature columns already are in the VM table.")

            except:
                pass
        
        except sqlite3.Error as e:
            try:
                cursor.execute(insertKbdLayoutVM)
                connection.commit()
                print("The queries were executed successfully. The missing features have been added to the database.")
            
            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[2])

                logman.writeToLogFile(
                    f"{errors.errCodes.errCodes[2]}: Could not connect to the database to update the VM list."
                    )

                dialog = ErrDialog(self)
                dialog.exec()

        try:
            cursor.execute(select11ColumnsVM)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                print("The query was executed successfully. The v1.1 feature columns already are in the VM table.")

            except:
                pass
        
        except sqlite3.Error as e:
            try:
                cursor.execute(insertAccelTypeVM)
                connection.commit()

                print("The queries were executed successfully. The missing features have been added to the database.")
            
            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[2])

                logman.writeToLogFile(
                    f"{errors.errCodes.errCodes[2]}: Could not connect to the database to update the VM list."
                    )

                dialog = ErrDialog(self)
                dialog.exec()

        try:
            cursor.execute(select12ColumnsVM)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                print("The query was executed successfully. The first v1.2 feature columns already are in the VM table.")

            except:
                pass
        
        except sqlite3.Error as e:
            try:
                cursor.execute(insertStorageControllerCD1VM)
                connection.commit()

                cursor.execute(insertStorageControllerCD2VM)
                connection.commit()
                print("The queries were executed successfully. The missing features have been added to the database.")
            
            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[2])

                logman.writeToLogFile(
                    f"{errors.errCodes.errCodes[2]}: Could not connect to the database to update the VM list."
                    )

                dialog = ErrDialog(self)
                dialog.exec()

        try:
            cursor.execute(select12ColumnsVM2)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                print("The query was executed successfully. The second v1.2 feature columns already are in the VM table.")

            except:
                pass
        
        except sqlite3.Error as e:
            try:
                cursor.execute(inserthdaControlVM)
                connection.commit()
                print("The queries were executed successfully. The missing features have been added to the database.")
            
            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[2])

                logman.writeToLogFile(
                    f"{errors.errCodes.errCodes[2]}: Could not connect to the database to update the VM list."
                    )

                dialog = ErrDialog(self)
                dialog.exec()

        try:
            cursor.execute(debug_db_settings)
            connection.commit()
            print(cursor.fetchall())
            print("The query was executed successfully.")
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

    def createNewVM(self):
        logman = errors.logman.LogMan()
        logman.logFile = logman.setLogFile()

        # This is the code that launches the dialog for creating a VM.
        debug_db_settings = """
        SELECT name, value FROM settings;
        """

        connection = self.connection
        cursor = connection.cursor()

        try:
            cursor.execute(debug_db_settings)
            connection.commit()
            result = cursor.fetchall()
            print(result)

            i = 0

            while i < len(result):
                if result[i][0] == "qemu-img":
                    if result[i][1] == "":
                        if platform.system() == "Windows":
                            errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                        else:
                            errorFile = platformSpecific.unixSpecific.unixErrorFile()

                        with open(errorFile, "w+") as errCodeFile:
                            errCodeFile.write(errors.errCodes.errCodes[18])

                        logman.writeToLogFile(
                            f"{errors.errCodes.errCodes[18]}: qemu-img is not registered in settings."
                        )

                        dialog = ErrDialog(self,msg="qemu-img没有设置")
                        dialog.exec()

                    else:
                        dialog = NewVirtualMachineDialog(self)
                        dialog.exec()
                
                    break

                i += 1
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

            if platform.system() == "Windows":
                errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
            else:
                errorFile = platformSpecific.unixSpecific.unixErrorFile()

            with open(errorFile, "w+") as errCodeFile:
                errCodeFile.write(errors.errCodes.errCodes[12])

            logman.writeToLogFile(
                f"{errors.errCodes.errCodes[12]}: Could not connect to the database to check if qemu-img is there."
                )

            dialog = ErrDialog(self)
            dialog.exec()

    def startVM(self):
        # This is the code that lets you power your virtual machines in the first place.

        debug_db_settings = """
        SELECT name, value FROM settings;
        """

        connection = self.connection
        cursor = connection.cursor()
        logman = errors.logman.LogMan()
        logman.logFile = logman.setLogFile()

        try:
            cursor.execute(debug_db_settings)
            connection.commit()
            result_settings = cursor.fetchall()



            selectedVM = self.listView.currentIndex().data()


            get_vm_to_start = f"""
            SELECT architecture, machine, cpu, ram, hda, vga, net, usbtablet, win2k, dirbios, additionalargs, sound, linuxkernel,
            linuxinitrid, linuxcmd, mousetype, cores, filebios, keyboardtype, usbsupport, usbcontroller, kbdtype, acceltype,
            storagecontrollercd1, storagecontrollercd2, hdacontrol, mode
            FROM virtualmachines WHERE name = '{selectedVM}'
            """

            try:
                cursor.execute(get_vm_to_start)
                connection.commit()
                result = cursor.fetchall()
                


                architecture_of_vm = result[0][0]
                machine_of_vm = result[0][1]
                cpu_of_vm = result[0][2]
                ram_of_vm = result[0][3]
                hda_of_vm = result[0][4]
                vga_of_vm = result[0][5]
                net_of_vm = result[0][6]
                usbtablet_wanted = result[0][7]
                os_is_win2k = result[0][8]
                dir_bios = result[0][9]
                additional_arguments = result[0][10]
                sound_card = result[0][11]
                linux_kernel = result[0][12]
                linux_initrid = result[0][13]
                linux_cmd = result[0][14]
                mouse_type = result[0][15]
                cpu_cores = result[0][16]
                file_bios = result[0][17]
                kbd_type = result[0][18]
                usb_support = result[0][19]
                usb_controller = result[0][20]
                kbd_layout = result[0][21]
                accel_type = result[0][22]
                cd_control1 = result[0][23]
                cd_control2 = result[0][24]
                hda_control = result[0][25]
                mode = result[0][26]

            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[12])

                logman.writeToLogFile(
                    f"{errors.errCodes.errCodes[12]}: Could not connect to the database to check the VM data."
                    )

                dialog = ErrDialog(self)
                dialog.exec()

            if platform.system() == "Windows":
                tempVmDef = platformSpecific.windowsSpecific.windowsTempVmStarterFile()
        
            else:
                tempVmDef = platformSpecific.unixSpecific.unixTempVmStarterFile()
                
            try:
                with open(tempVmDef, "w+") as tempVmDefFile:
                    tempVmDefFile.write(selectedVM + "\n")
                    tempVmDefFile.write(architecture_of_vm + "\n")
                    tempVmDefFile.write(machine_of_vm + "\n")
                    tempVmDefFile.write(cpu_of_vm + "\n")
                    tempVmDefFile.write(str(ram_of_vm) + "\n")
                    tempVmDefFile.write(hda_of_vm + "\n")
                    tempVmDefFile.write(vga_of_vm + "\n")
                    tempVmDefFile.write(net_of_vm + "\n")
                    tempVmDefFile.write(str(usbtablet_wanted) + "\n")
                    tempVmDefFile.write(str(os_is_win2k) + "\n")
                    tempVmDefFile.write(dir_bios + "\n")
                    tempVmDefFile.write(additional_arguments + "\n")
                    tempVmDefFile.write(sound_card + "\n")
                    tempVmDefFile.write(linux_kernel + "\n")
                    tempVmDefFile.write(linux_initrid + "\n")
                    tempVmDefFile.write(linux_cmd + "\n")
                    tempVmDefFile.write(mouse_type + "\n")
                    tempVmDefFile.write(str(cpu_cores) + "\n")
                    tempVmDefFile.write(str(file_bios) + "\n")
                    tempVmDefFile.write(kbd_type + "\n")
                    tempVmDefFile.write(str(usb_support) + "\n")
                    tempVmDefFile.write(usb_controller + "\n")
                    tempVmDefFile.write(kbd_layout + "\n")
                    tempVmDefFile.write(accel_type + "\n")
                    tempVmDefFile.write(cd_control1 + "\n")
                    tempVmDefFile.write(cd_control2 + "\n")
                    tempVmDefFile.write(hda_control + "\n")
                    tempVmDefFile.write(mode + "\n")

            except:
                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[36])

                logman.writeToLogFile(
                    f"{errors.errCodes.errCodes[36]}: Could not write VM data onto temporary definition file."
                    )

                dialog = ErrDialog(self)
                dialog.exec()

            if usbtablet_wanted == 1:
                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
    
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[30])

                logman.writeToLogFile(f"{errors.errCodes.errCodes[30]}: Depreciated feature: USB Tablet Checkbox (replaced by a combobox)")
                dialog = ErrDialog(self)
                dialog.exec()

            if os_is_win2k == 1:
                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
    
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[30])

                logman.writeToLogFile(f"{errors.errCodes.errCodes[30]}: Depreciated feature: Windows 2000 Hack (became obsolete)")
                dialog = ErrDialog(self)
                dialog.exec()

            if cpu_of_vm == "Icelake-Client":
                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
    
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[30])

                logman.writeToLogFile(f"{errors.errCodes.errCodes[30]}: Depreciated feature: Icelake-Client CPU (absent since QEMU 7.1)")
                dialog = ErrDialog(self)
                dialog.exec()

            if accel_type == "HAXM":
                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
    
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[30])

                logman.writeToLogFile(f"{errors.errCodes.errCodes[30]}: Depreciated feature: HAXM accelerator (absent since QEMU 8.2)")
                dialog = ErrDialog(self)
                dialog.exec()

            arch_supported = False

            for architecture in self.architectures:
                if architecture[0] == architecture_of_vm:
                    for res in result_settings:
                        if res[0] == f"qemu-system-{architecture_of_vm}":
                            if res[1] != "":
                                dialog = StartVirtualMachineDialog(self)
                                dialog.exec()
                                arch_supported = True
                                break

                            else:
                                if platform.system() == "Windows":
                                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                                else:
                                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                                with open(errorFile, "w+") as errCodeFile:
                                    errCodeFile.write(errors.errCodes.errCodes[17])

                                logman.writeToLogFile(f"{errors.errCodes.errCodes[17]}: The QEMU emulator for {architecture_of_vm} could not be found.")

                                dialog = ErrDialog(self,"对应qemu路径未配置")
                                dialog.exec()
                                arch_supported = True
                                break

                    break
                    
            if arch_supported == False:
                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[32])

                logman.writeToLogFile(
                    f"{errors.errCodes.errCodes[32]}: This VM is not supported by this version of EmuGUI. Please upgrade to a later version."
                    )

                dialog = ErrDialog(self)
                dialog.exec()
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

            if platform.system() == "Windows":
                errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
            else:
                errorFile = platformSpecific.unixSpecific.unixErrorFile()

            with open(errorFile, "w+") as errCodeFile:
                errCodeFile.write(errors.errCodes.errCodes[12])

            logman.writeToLogFile(
                        f"{errors.errCodes.errCodes[12]}: The database could not be accessed. SQLite describes the error as follows: \"{e}\""
                        )

            dialog = ErrDialog(self)
            dialog.exec()

    def exportVM(self):
        debug_db_settings = """
        SELECT name, value FROM settings;
        """

        connection = self.connection
        cursor = connection.cursor()
        logman = errors.logman.LogMan()
        logman.logFile = logman.setLogFile()

        try:
            cursor.execute(debug_db_settings)
            connection.commit()
            result_settings = cursor.fetchall()

            print(result_settings)

            selectedVM = self.listView.currentIndex().data()
            print(selectedVM)

            get_vm_to_start = f"""
            SELECT architecture, machine, cpu, ram, hda, vga, net, usbtablet, win2k, dirbios, additionalargs, sound, linuxkernel,
            linuxinitrid, linuxcmd, mousetype, cores, filebios, keyboardtype, usbsupport, usbcontroller, kbdtype, acceltype,
            storagecontrollercd1, storagecontrollercd2, hdacontrol, mode
            FROM virtualmachines WHERE name = '{selectedVM}'
            """

            try:
                cursor.execute(get_vm_to_start)
                connection.commit()
                result = cursor.fetchall()

                print(result)

                architecture_of_vm = result[0][0]
                machine_of_vm = result[0][1]
                cpu_of_vm = result[0][2]
                ram_of_vm = result[0][3]
                hda_of_vm = result[0][4]
                vga_of_vm = result[0][5]
                net_of_vm = result[0][6]
                dir_bios = result[0][9]
                additional_arguments = result[0][10]
                sound_card = result[0][11]
                linux_kernel = result[0][12]
                linux_initrid = result[0][13]
                linux_cmd = result[0][14]
                mouse_type = result[0][15]
                cpu_cores = result[0][16]
                file_bios = result[0][17]
                kbd_type = result[0][18]
                usb_support = result[0][19]
                usb_controller = result[0][20]
                kbd_layout = result[0][21]
                accel_type = result[0][22]
                cd_control1 = result[0][23]
                cd_control2 = result[0][24]
                hda_control = result[0][25]
                mode = result[0][26]

            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[12])

                logman.writeToLogFile(
                    f"{errors.errCodes.errCodes[12]}: Could not connect to the database to check the VM data."
                    )

                dialog = ErrDialog(self)
                dialog.exec()

            if platform.system() == "Windows":
                tempVmDef = platformSpecific.windowsSpecific.windowsExportFile()
        
            else:
                tempVmDef = platformSpecific.unixSpecific.unixExportFile()

            try:
                with open(tempVmDef, "w+") as vmDefFile:
                    vmDefFile.write("name = " + selectedVM + "\n")
                    vmDefFile.write("arch = " + architecture_of_vm + "\n")
                    vmDefFile.write("machine = " + machine_of_vm + "\n")
                    vmDefFile.write("cpu = " + cpu_of_vm + "\n")
                    vmDefFile.write("ram = " + str(ram_of_vm) + "\n")
                    vmDefFile.write("vga = " + vga_of_vm + "\n")
                    vmDefFile.write("network = " + net_of_vm + "\n")
                    vmDefFile.write("biosdir = " + dir_bios + "\n")
                    vmDefFile.write("additionalargs = " + additional_arguments + "\n")
                    vmDefFile.write("soundcard = " + sound_card + "\n")
                    vmDefFile.write("linuxkernel = " + linux_kernel + "\n")
                    vmDefFile.write("linuxinitrd = " + linux_initrid + "\n")
                    vmDefFile.write("linuxcmd = " + linux_cmd + "\n")
                    vmDefFile.write("mouse = " + mouse_type + "\n")
                    vmDefFile.write("cpucores = " + str(cpu_cores) + "\n")
                    vmDefFile.write("biosfile = " + str(file_bios) + "\n")
                    vmDefFile.write("kbdtype = " + kbd_type + "\n")
                    vmDefFile.write("usbsupport = " + str(usb_support) + "\n")
                    vmDefFile.write("usbcontroller = " + usb_controller + "\n")
                    vmDefFile.write("kbdlayout = " + kbd_layout + "\n")
                    vmDefFile.write("hwaccel = " + accel_type + "\n")
                    vmDefFile.write("cdcontrol1 = " + cd_control1 + "\n")
                    vmDefFile.write("cdcontrol2 = " + cd_control2 + "\n")
                    vmDefFile.write("hdacontrol = " + hda_control + "\n")
                    vmDefFile.write("mode = " + mode + "\n")

            except:
                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                logman.writeToLogFile(
                    f"{errors.errCodes.errCodes[36]}: Could not write VM data onto temporary definition file."
                    )

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[36])

                dialog = ErrDialog(self)
                dialog.exec()

            filename, filter = QFileDialog.getSaveFileName(parent=self, caption='Export VM file', dir='.', filter='ZIP file (*.zip);;All files (*.*)')

            if filename:
                with zipfile.ZipFile(filename, "w") as vmFile:
                    vmFile.write(tempVmDef, os.path.basename(tempVmDef))

                    if hda_of_vm != "NULL":
                        vmFile.write(hda_of_vm, os.path.basename(hda_of_vm))

                if os.path.exists(filename):
                    print("Export successful!")

                else:
                    print("Export failed!")

                    if platform.system() == "Windows":
                        errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                    else:
                        errorFile = platformSpecific.unixSpecific.unixErrorFile()

                    with open(errorFile, "w+") as errCodeFile:
                        errCodeFile.write(errors.errCodes.errCodes[33])

                    logman.writeToLogFile(
                        f"{errors.errCodes.errCodes[33]}: This VM could not be exported. Please check its settings."
                        )

                    dialog = ErrDialog(self)
                    dialog.exec()

        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

    def importVM(self):
        logman = errors.logman.LogMan()
        logman.logFile = logman.setLogFile()

        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Import VM file', dir='.', filter='ZIP file (*.zip);;All files (*.*)')

        if filename:
            zip_vm_file = zipfile.ZipFile(filename)
            vm_file_names = []

            vhd_file_types = [
                ".img", ".IMG", ".vhdx", ".VHDX", ".vmdk", ".VMDK", ".qcow", ".QCOW", ".qcow2", ".QCOW2", ".vdi", ".VDI", ".vpc", ".VPC",
                ".parallels", ".PARALLELS"
                ]
            
            vhd_path = ""
            
            for content_name in zip_vm_file.namelist():
                vm_file_names.append(content_name)

            for content_name in vm_file_names:
                for filetype in vhd_file_types:
                    if str(content_name).endswith(filetype):
                        vhd_filename, filter = QFileDialog.getSaveFileName(parent=self, caption='Save VHD file', dir='.', filter='Hard disk file (*.img);;VirtualBox disk image (*.vdi);;VMware disk file (*.vmdk);;Virtual hard disk file with extra features (*.vhdx);;All files (*.*)')

                        if vhd_filename:
                            zip_vm_file.extract(content_name, vhd_filename)
                            vhd_path = vhd_filename + "/" + content_name

                        break

            for content_name in vm_file_names:
                if content_name.endswith(".txt"):
                    if platform.system() == "Windows":
                        tempVmDef = platformSpecific.windowsSpecific.windowsExportFile()
        
                    else:
                        tempVmDef = platformSpecific.unixSpecific.unixExportFile()

                    vm_data = []
                    try:
                        zip_vm_file.extract(content_name, os.path.dirname(tempVmDef))
                        

                    except Exception as e:
                        if platform.system() == "Windows":
                            errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                        else:
                            errorFile = platformSpecific.unixSpecific.unixErrorFile()

                        with open(errorFile, "w+") as errCodeFile:
                            errCodeFile.write(errors.errCodes.errCodes[34])
                        print(e)
                        dialog = ErrDialog(self)
                        dialog.exec()

                    with open(tempVmDef, "r+") as vmDefFile:
                        vmDefContent = vmDefFile.readlines()

                        for vmDefLine in vmDefContent:
                            vmDefLineClean = vmDefLine.replace("\n", "")

                            if vmDefLineClean.startswith("name = "):
                                vm_data.append(vmDefLineClean.replace("name = ", ""))

                            elif vmDefLineClean.startswith("arch = "):
                                vm_data.append(vmDefLineClean.replace("arch = ", ""))

                            elif vmDefLineClean.startswith("machine = "):
                                vm_data.append(vmDefLineClean.replace("machine = ", ""))

                            elif vmDefLineClean.startswith("cpu = "):
                                vm_data.append(vmDefLineClean.replace("cpu = ", ""))

                            elif vmDefLineClean.startswith("ram = "):
                                vm_data.append(vmDefLineClean.replace("ram = ", ""))

                            elif vmDefLineClean.startswith("vga = "):
                                vm_data.append(vmDefLineClean.replace("vga = ", ""))

                            elif vmDefLineClean.startswith("network = "):
                                vm_data.append(vmDefLineClean.replace("network = ", ""))

                            elif vmDefLineClean.startswith("biosdir = "):
                                vm_data.append(vmDefLineClean.replace("biosdir = ", ""))

                            elif vmDefLineClean.startswith("additionalargs = "):
                                vm_data.append(vmDefLineClean.replace("additionalargs = ", ""))

                            elif vmDefLineClean.startswith("soundcard = "):
                                vm_data.append(vmDefLineClean.replace("soundcard = ", ""))

                            elif vmDefLineClean.startswith("linuxkernel = "):
                                vm_data.append(vmDefLineClean.replace("linuxkernel = ", ""))

                            elif vmDefLineClean.startswith("linuxinitrd = "):
                                vm_data.append(vmDefLineClean.replace("linuxinitrd = ", ""))

                            elif vmDefLineClean.startswith("linuxcmd = "):
                                vm_data.append(vmDefLineClean.replace("linuxcmd = ", ""))

                            elif vmDefLineClean.startswith("mouse = "):
                                vm_data.append(vmDefLineClean.replace("mouse = ", ""))

                            elif vmDefLineClean.startswith("cpucores = "):
                                vm_data.append(vmDefLineClean.replace("cpucores = ", ""))

                            elif vmDefLineClean.startswith("biosfile = "):
                                vm_data.append(vmDefLineClean.replace("biosfile = ", ""))

                            elif vmDefLineClean.startswith("kbdtype = "):
                                vm_data.append(vmDefLineClean.replace("kbdtype = ", ""))

                            elif vmDefLineClean.startswith("usbsupport = "):
                                vm_data.append(vmDefLineClean.replace("usbsupport = ", ""))

                            elif vmDefLineClean.startswith("usbcontroller = "):
                                vm_data.append(vmDefLineClean.replace("usbcontroller = ", ""))

                            elif vmDefLineClean.startswith("kbdlayout = "):
                                vm_data.append(vmDefLineClean.replace("kbdlayout = ", ""))

                            elif vmDefLineClean.startswith("hwaccel = "):
                                vm_data.append(vmDefLineClean.replace("hwaccel = ", ""))

                            elif vmDefLineClean.startswith("cdcontrol1 = "):
                                vm_data.append(vmDefLineClean.replace("cdcontrol1 = ", ""))

                            elif vmDefLineClean.startswith("cdcontrol2 = "):
                                vm_data.append(vmDefLineClean.replace("cdcontrol2 = ", ""))

                            elif vmDefLineClean.startswith("hdacontrol = "):
                                vm_data.append(vmDefLineClean.replace("hdacontrol = ", ""))
                            
                            elif vmDefLineClean.startswith("mode = "):
                                vm_data.append(vmDefLineClean.replace("hdacontrol = ", ""))

                    insert_into_vm_database = f"""
                    INSERT INTO virtualmachines (
                        name,
                        architecture,
                        machine,
                        cpu,
                        ram,
                        hda,
                        vga,
                        net,
                        usbtablet,
                        win2k,
                        dirbios,
                        additionalargs,
                        sound,
                        linuxkernel,
                        linuxinitrid,
                        linuxcmd,
                        mousetype,
                        cores,
                        filebios,
                        keyboardtype,
                        usbsupport,
                        usbcontroller,
                        kbdtype,
                        acceltype,
                        storagecontrollercd1,
                        storagecontrollercd2,
                        hdacontrol,
                        mode
                    ) VALUES (
                        "{vm_data[0]}",
                        "{vm_data[1]}",
                        "{vm_data[2]}",
                        "{vm_data[3]}",
                        {int(vm_data[4])},
                        "{vhd_path}",
                        "{vm_data[5]}",
                        "{vm_data[6]}",
                        0,
                        0,
                        "{vm_data[7]}",
                        "{vm_data[8]}",
                        "{vm_data[9]}",
                        "{vm_data[10]}",
                        "{vm_data[11]}",
                        "{vm_data[12]}",
                        "{vm_data[13]}",
                        {int(vm_data[14])},
                        "{vm_data[15]}",
                        "{vm_data[16]}",
                        {int(vm_data[17])},
                        "{vm_data[18]}",
                        "{vm_data[19]}",
                        "{vm_data[20]}",
                        "{vm_data[21]}",
                        "{vm_data[22]}",
                        "{vm_data[23]}",
                        "{vm_data[24]}"
        );
        """
                    
        if platform.system() == "Windows":
            connection = platformSpecific.windowsSpecific.setupWindowsBackend()
        
        else:
            connection = platformSpecific.unixSpecific.setupUnixBackend()
                    
        cursor = connection.cursor()

        try:
            cursor.execute(insert_into_vm_database)
            connection.commit()
            print("The query was executed successfully.")
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

            if platform.system() == "Windows":
                errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
            else:
                errorFile = platformSpecific.unixSpecific.unixErrorFile()

            with open(errorFile, "w+") as errCodeFile:
                errCodeFile.write(errors.errCodes.errCodes[35])

            logman.writeToLogFile(
                        f"{errors.errCodes.errCodes[35]}: The database could not be accessed, meaning the export failed. SQLite describes the error as follows: \"{e}\""
                        )

            dialog = ErrDialog(self)
            dialog.exec()

    def editVM(self):
        # Of course, this code prepares the dialog for editing VMs.
        logman = errors.logman.LogMan()
        logman.logFile = logman.setLogFile()

        debug_db_settings = """
        SELECT name, value FROM settings;
        """

        connection = self.connection
        cursor = connection.cursor()

        try:
            cursor.execute(debug_db_settings)
            connection.commit()
            result_settings = cursor.fetchall()

            print(result_settings)

            selectedVM = self.listView.currentIndex().data()
            print(selectedVM)

            get_vm_to_start = f"""
            SELECT architecture, machine, cpu, ram, hda, vga, net, usbtablet, win2k, dirbios, additionalargs, sound, linuxkernel,
            linuxinitrid, linuxcmd, mousetype, cores, filebios, keyboardtype, usbsupport, usbcontroller, kbdtype, acceltype,
            storagecontrollercd1, storagecontrollercd2, hdacontrol, mode
            FROM virtualmachines WHERE name = '{selectedVM}'
            """

            try:
                cursor.execute(get_vm_to_start)
                connection.commit()
                result = cursor.fetchall()

                print(result)

                architecture_of_vm = result[0][0]
                machine_of_vm = result[0][1]
                cpu_of_vm = result[0][2]
                ram_of_vm = result[0][3]
                hda_of_vm = result[0][4]
                vga_of_vm = result[0][5]
                net_of_vm = result[0][6]
                usbtablet_wanted = result[0][7]
                os_is_win2k = result[0][8]
                dir_bios = result[0][9]
                additional_arguments = result[0][10]
                sound_card = result[0][11]
                linux_kernel = result[0][12]
                linux_initrid = result[0][13]
                linux_cmd = result[0][14]
                mouse_type = result[0][15]
                cpu_cores = result[0][16]
                file_bios = result[0][17]
                kbd_type = result[0][18]
                usb_support = result[0][19]
                usb_controller = result[0][20]
                kbd_layout = result[0][21]
                accel_type = result[0][22]
                cd_control1 = result[0][23]
                cd_control2 = result[0][24]
                hda_control = result[0][25]
                mode = result[0][26]

            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[12])

                logman.writeToLogFile(
                        f"{errors.errCodes.errCodes[12]}: The database could not be accessed. SQLite describes the error as follows: \"{e}\""
                        )

                dialog = ErrDialog(self)
                dialog.exec()

            if platform.system() == "Windows":
                tempVmDef = platformSpecific.windowsSpecific.windowsTempVmStarterFile()
        
            else:
                tempVmDef = platformSpecific.unixSpecific.unixTempVmStarterFile()
                
            try:
                with open(tempVmDef, "w+") as tempVmDefFile:
                    tempVmDefFile.write(selectedVM + "\n")
                    tempVmDefFile.write(architecture_of_vm + "\n") #1
                    tempVmDefFile.write(machine_of_vm + "\n") #2
                    tempVmDefFile.write(cpu_of_vm + "\n") #3
                    tempVmDefFile.write(str(ram_of_vm) + "\n") #4
                    tempVmDefFile.write(hda_of_vm + "\n") #5
                    tempVmDefFile.write(vga_of_vm + "\n") #6
                    tempVmDefFile.write(net_of_vm + "\n") #7
                    tempVmDefFile.write(str(usbtablet_wanted) + "\n") #8
                    tempVmDefFile.write(str(os_is_win2k) + "\n") #9
                    tempVmDefFile.write(dir_bios + "\n") #10
                    tempVmDefFile.write(additional_arguments + "\n") #11
                    tempVmDefFile.write(sound_card + "\n") #12
                    tempVmDefFile.write(linux_kernel + "\n") #13
                    tempVmDefFile.write(linux_initrid + "\n") #14
                    tempVmDefFile.write(linux_cmd + "\n") #15
                    tempVmDefFile.write(mouse_type + "\n") #16
                    tempVmDefFile.write(str(cpu_cores) + "\n") #17
                    tempVmDefFile.write(str(file_bios) + "\n") #18
                    tempVmDefFile.write(kbd_type + "\n") #19
                    tempVmDefFile.write(str(usb_support) + "\n") #20
                    tempVmDefFile.write(usb_controller + "\n") #21
                    tempVmDefFile.write(kbd_layout + "\n") #22
                    tempVmDefFile.write(accel_type + "\n") #23
                    tempVmDefFile.write(cd_control1 + "\n") #24
                    tempVmDefFile.write(cd_control2 + "\n") # 25
                    tempVmDefFile.write(hda_control + "\n") # 26
                    tempVmDefFile.write(mode + "\n") # 27

            except:
                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[36])

                logman.writeToLogFile(
                        f"{errors.errCodes.errCodes[36]}: The temporary VM definition file couldn't be written. Please check the permissions."
                        )

                dialog = ErrDialog(self)
                dialog.exec()

            i = 0

            while i < len(result_settings):
                if result_settings[i][0] == "qemu-img":
                    if result_settings[i][1] == "":
                        if platform.system() == "Windows":
                            errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                        else:
                            errorFile = platformSpecific.unixSpecific.unixErrorFile()

                        with open(errorFile, "w+") as errCodeFile:
                            errCodeFile.write(errors.errCodes.errCodes[18])

                        dialog = ErrDialog(self)
                        dialog.exec()

                    else:
                        dialog = EditVMNewDialog(self)
                        dialog.exec()
                
                    break

                i += 1
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

    # These functions are for setting the QEMU paths.

    def set_qemu_img_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select qemu-img executable', dir='.', filter='Windows executables (*.exe);;All files (*.*)')

        if filename:
            self.lineEdit_5.setText(filename)

    def set_qemu_i386_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select qemu-system-i386 executable', dir='.', filter='Windows executables (*.exe);;All files (*.*)')

        if filename:
            self.lineEdit_4.setText(filename)

    def set_qemu_x86_64_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select qemu-system-x86_64 executable', dir='.', filter='Windows executables (*.exe);;All files (*.*)')

        if filename:
            self.lineEdit_3.setText(filename)

    def set_qemu_ppc_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select qemu-system-ppc executable', dir='.', filter='Windows executables (*.exe);;All files (*.*)')

        if filename:
            self.lineEdit_2.setText(filename)

    def set_qemu_ppc64_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select qemu-system-ppc64 executable', dir='.', filter='Windows executables (*.exe);;All files (*.*)')

        if filename:
            self.lineEdit_8.setText(filename)

    def set_qemu_alpha_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select qemu-system-alpha executable', dir='.', filter='Windows executables (*.exe);;All files (*.*)')

        if filename:
            self.le_alpha.setText(filename)

    def set_qemu_riscv32_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select qemu-system-riscv32 executable', dir='.', filter='Windows executables (*.exe);;All files (*.*)')

        if filename:
            self.le_riscv32.setText(filename)

    def set_qemu_riscv64_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select qemu-system-riscv64 executable', dir='.', filter='Windows executables (*.exe);;All files (*.*)')

        if filename:
            self.le_riscv64.setText(filename)

    def set_qemu_mips64el_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select qemu-system-mips64el executable', dir='.', filter='Windows executables (*.exe);;All files (*.*)')

        if filename:
            self.lineEdit.setText(filename)

    def set_qemu_mipsel_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select qemu-system-mipsel executable', dir='.', filter='Windows executables (*.exe);;All files (*.*)')

        if filename:
            self.lineEdit_9.setText(filename)

    def set_qemu_mips64_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select qemu-system-mips64 executable', dir='.', filter='Windows executables (*.exe);;All files (*.*)')

        if filename:
            self.lineEdit_11.setText(filename)

    def set_qemu_mips_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select qemu-system-mips executable', dir='.', filter='Windows executables (*.exe);;All files (*.*)')

        if filename:
            self.lineEdit_10.setText(filename)

    def set_qemu_aarch64_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select qemu-system-aarch64 executable', dir='.', filter='Windows executables (*.exe);;All files (*.*)')

        if filename:
            self.lineEdit_6.setText(filename)

    def set_qemu_arm_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select qemu-system-arm executable', dir='.', filter='Windows executables (*.exe);;All files (*.*)')

        if filename:
            self.lineEdit_7.setText(filename)

    def set_qemu_sparc_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select qemu-system-sparc executable', dir='.', filter='Windows executables (*.exe);;All files (*.*)')

        if filename:
            self.lineEdit_12.setText(filename)

    def set_qemu_sparc64_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select qemu-system-sparc64 executable', dir='.', filter='Windows executables (*.exe);;All files (*.*)')

        if filename:
            self.lineEdit_13.setText(filename)

    def applyChangesQemu(self):
        logman = errors.logman.LogMan()
        logman.logFile = logman.setLogFile()
        pathQemuImg = self.lineEdit_5.text()

        qemu_img_update = f"""
        UPDATE settings
        SET value = '{pathQemuImg}'
        WHERE name = 'qemu-img';
        """

        connection = self.connection
        cursor = connection.cursor()

        try:
            cursor.execute(qemu_img_update)
            connection.commit()
            print("The qemu-img slot was updated successfully.")

        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

            if platform.system() == "Windows":
                errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
            else:
                errorFile = platformSpecific.unixSpecific.unixErrorFile()

            with open(errorFile, "w+") as errCodeFile:
                errCodeFile.write(errors.errCodes.errCodes[12])

            logman.writeToLogFile(
                f"{errors.errCodes.errCodes[12]}: The database could not be accessed and the settings are therefore not applied. SQLite describes the error as follows: \"{e}\""
                )

            dialog = ErrDialog(self)
            dialog.exec()

        for architecture in self.architectures:
            upd_query = f"""
            UPDATE settings
            SET value = '{architecture[1].text()}'
            WHERE name = 'qemu-system-{architecture[0]}';
            """

            try:
                cursor.execute(upd_query)
                connection.commit()
                print(f"The qemu-system-{architecture[0]} slot has been updated.")

            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[12])

                logman.writeToLogFile(
                    f"{errors.errCodes.errCodes[12]}: The database could not be accessed and the settings are therefore not applied. SQLite describes the error as follows: \"{e}\""
                    )

                dialog = ErrDialog(self)
                dialog.exec()

    def applyGeneric(self):
        logman = errors.logman.LogMan()
        logman.logFile = logman.setLogFile()

        with open("translations/systemdefault.txt", "r+", encoding="utf8") as sysDefFile:
            sysDefContent = sysDefFile.read()

        language_system = f"""
        UPDATE settings
        SET value = 'default'
        WHERE name = 'lang';
        """

        language_en = f"""
        UPDATE settings
        SET value = 'en'
        WHERE name = 'lang';
        """

        language_de = f"""
        UPDATE settings
        SET value = 'de'
        WHERE name = 'lang';
        """

        language_uk = f"""
        UPDATE settings
        SET value = 'uk'
        WHERE name = 'lang';
        """

        language_fr = f"""
        UPDATE settings
        SET value = 'fr'
        WHERE name = 'lang';
        """

        language_es = f"""
        UPDATE settings
        SET value = 'es'
        WHERE name = 'lang';
        """

        language_ro = f"""
        UPDATE settings
        SET value = 'ro'
        WHERE name = 'lang';
        """

        language_ru = f"""
        UPDATE settings
        SET value = 'ru'
        WHERE name = 'lang';
        """

        language_be = f"""
        UPDATE settings
        SET value = 'be'
        WHERE name = 'lang';
        """

        language_cz = f"""
        UPDATE settings
        SET value = 'cz'
        WHERE name = 'lang';
        """

        language_pt = f"""
        UPDATE settings
        SET value = 'pt'
        WHERE name = 'lang';
        """

        language_pl = f"""
        UPDATE settings
        SET value = 'pl'
        WHERE name = 'lang';
        """

        language_it = f"""
        UPDATE settings
        SET value = 'it'
        WHERE name = 'lang';
        """

        theme_default = f"""
        UPDATE settings
        SET value = 'default'
        WHERE name = 'theme';
        """

        theme_custom = f"""
        UPDATE settings
        SET value = '{self.comboBox_5.currentText()}'
        WHERE name = 'theme';
        """

        connection = self.connection
        cursor = connection.cursor()

        if sysDefContent.__contains__(self.comboBox_4.currentText()): #self.comboBox_4.currentText() == "System default" or self.comboBox_4.currentText() == "Systemstandard":
            langmode = "system"

            try:
                cursor.execute(language_system)
                connection.commit()
                

                if platform.system() == "Windows":
                    langfile = platformSpecific.windowsSpecific.windowsLanguageFile()
                
                else:
                    langfile = platformSpecific.unixSpecific.unixLanguageFile()

                if langmode == "system":
                    languageToUseLater = locale.getlocale()[0]
                    languageToUseEvenLater = languageToUseLater.split("_")
                    languageToUseHere = languageToUseEvenLater[0]

                else:
                    languageToUseHere = langmode
                
                try:
                    with open(langfile, "w+") as language:
                        language.write(languageToUseHere)

                except:
                    print("EmuGUI failed to create a language file. Expect some issues.")

                    if platform.system() == "Windows":
                        errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                    else:
                        errorFile = platformSpecific.unixSpecific.unixErrorFile()

                    with open(errorFile, "w+") as errCodeFile:
                        errCodeFile.write(errors.errCodes.errCodes[54])

                    logman.writeToLogFile(
                        f"{errors.errCodes.errCodes[54]}: Could not create the language file. Expect issues."
                    )

                    dialog = ErrDialog(self)
                    dialog.exec()

                self.setLanguage(langmode)
                print("The query was executed successfully.")

            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[12])

                logman.writeToLogFile(
                    f"{errors.errCodes.errCodes[12]}: The database could not be accessed and the settings are therefore not applied. SQLite describes the error as follows: \"{e}\""
                    )

                dialog = ErrDialog(self)
                dialog.exec()

            except:
                dialog = SettingsRequireEmuGUIReboot(self)
                dialog.exec()

        elif self.comboBox_4.currentText() == "English":
            langmode = "en"

            try:
                cursor.execute(language_en)
                connection.commit()

                if platform.system() == "Windows":
                    langfile = platformSpecific.windowsSpecific.windowsLanguageFile()
                
                else:
                    langfile = platformSpecific.unixSpecific.unixLanguageFile()

                if langmode == "system":
                    languageToUseLater = locale.getlocale()[0]
                    languageToUseEvenLater = languageToUseLater.split("_")
                    languageToUseHere = languageToUseEvenLater[0]

                else:
                    languageToUseHere = langmode
                
                try:
                    with open(langfile, "w+") as language:
                        language.write(languageToUseHere)

                except:
                    print("EmuGUI failed to create a language file. Expect some issues.")

                    if platform.system() == "Windows":
                        errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                    else:
                        errorFile = platformSpecific.unixSpecific.unixErrorFile()

                    with open(errorFile, "w+") as errCodeFile:
                        errCodeFile.write(errors.errCodes.errCodes[54])

                    logman.writeToLogFile(
                        f"{errors.errCodes.errCodes[54]}: Could not create the language file. Expect issues."
                    )

                    dialog = ErrDialog(self)
                    dialog.exec()

                self.setLanguage(langmode)
                print("The query was executed successfully.")

            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[12])

                logman.writeToLogFile(
                    f"{errors.errCodes.errCodes[12]}: The database could not be accessed and the settings are therefore not applied. SQLite describes the error as follows: \"{e}\""
                    )

                dialog = ErrDialog(self)
                dialog.exec()

            except:
                dialog = SettingsRequireEmuGUIReboot(self)
                dialog.exec()

        elif self.comboBox_4.currentText() == "Deutsch":
            langmode = "de"

            try:
                cursor.execute(language_de)
                connection.commit()

                if platform.system() == "Windows":
                    langfile = platformSpecific.windowsSpecific.windowsLanguageFile()
                
                else:
                    langfile = platformSpecific.unixSpecific.unixLanguageFile()

                if langmode == "system":
                    languageToUseLater = locale.getlocale()[0]
                    languageToUseEvenLater = languageToUseLater.split("_")
                    languageToUseHere = languageToUseEvenLater[0]

                else:
                    languageToUseHere = langmode
                
                try:
                    with open(langfile, "w+") as language:
                        language.write(languageToUseHere)

                except:
                    print("EmuGUI failed to create a language file. Expect some issues.")

                    if platform.system() == "Windows":
                        errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                    else:
                        errorFile = platformSpecific.unixSpecific.unixErrorFile()

                    with open(errorFile, "w+") as errCodeFile:
                        errCodeFile.write(errors.errCodes.errCodes[54])

                    logman.writeToLogFile(
                        f"{errors.errCodes.errCodes[54]}: Could not create the language file. Expect issues."
                    )

                    dialog = ErrDialog(self)
                    dialog.exec()

                self.setLanguage(langmode)
                print("The query was executed successfully.")

            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[12])

                logman.writeToLogFile(
                    f"{errors.errCodes.errCodes[12]}: The database could not be accessed and the settings are therefore not applied. SQLite describes the error as follows: \"{e}\""
                    )

                dialog = ErrDialog(self)
                dialog.exec()

            except:
                dialog = SettingsRequireEmuGUIReboot(self)
                dialog.exec()

        elif self.comboBox_4.currentText() == "Français":
            langmode = "fr"

            try:
                cursor.execute(language_fr)
                connection.commit()

                if platform.system() == "Windows":
                    langfile = platformSpecific.windowsSpecific.windowsLanguageFile()
                
                else:
                    langfile = platformSpecific.unixSpecific.unixLanguageFile()

                if langmode == "system":
                    languageToUseLater = locale.getlocale()[0]
                    languageToUseEvenLater = languageToUseLater.split("_")
                    languageToUseHere = languageToUseEvenLater[0]

                else:
                    languageToUseHere = langmode
                
                try:
                    with open(langfile, "w+") as language:
                        language.write(languageToUseHere)

                except:
                    print("EmuGUI failed to create a language file. Expect some issues.")

                    if platform.system() == "Windows":
                        errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                    else:
                        errorFile = platformSpecific.unixSpecific.unixErrorFile()

                    with open(errorFile, "w+") as errCodeFile:
                        errCodeFile.write(errors.errCodes.errCodes[54])

                    logman.writeToLogFile(
                        f"{errors.errCodes.errCodes[54]}: Could not create the language file. Expect issues."
                    )

                    dialog = ErrDialog(self)
                    dialog.exec()

                self.setLanguage(langmode)
                print("The query was executed successfully.")

            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[12])

                logman.writeToLogFile(
                    f"{errors.errCodes.errCodes[12]}: The database could not be accessed and the settings are therefore not applied. SQLite describes the error as follows: \"{e}\""
                    )

                dialog = ErrDialog(self)
                dialog.exec()

            except:
                dialog = SettingsRequireEmuGUIReboot(self)
                dialog.exec()

        elif self.comboBox_4.currentText() == "Español":
            langmode = "es"

            try:
                cursor.execute(language_es)
                connection.commit()

                if platform.system() == "Windows":
                    langfile = platformSpecific.windowsSpecific.windowsLanguageFile()
                
                else:
                    langfile = platformSpecific.unixSpecific.unixLanguageFile()

                if langmode == "system":
                    languageToUseLater = locale.getlocale()[0]
                    languageToUseEvenLater = languageToUseLater.split("_")
                    languageToUseHere = languageToUseEvenLater[0]

                else:
                    languageToUseHere = langmode
                
                try:
                    with open(langfile, "w+") as language:
                        language.write(languageToUseHere)

                except:
                    print("EmuGUI failed to create a language file. Expect some issues.")

                    if platform.system() == "Windows":
                        errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                    else:
                        errorFile = platformSpecific.unixSpecific.unixErrorFile()

                    with open(errorFile, "w+") as errCodeFile:
                        errCodeFile.write(errors.errCodes.errCodes[54])

                    logman.writeToLogFile(
                        f"{errors.errCodes.errCodes[54]}: Could not create the language file. Expect issues."
                    )

                    dialog = ErrDialog(self)
                    dialog.exec()

                self.setLanguage(langmode)
                print("The query was executed successfully.")

            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[12])

                logman.writeToLogFile(
                    f"{errors.errCodes.errCodes[12]}: The database could not be accessed and the settings are therefore not applied. SQLite describes the error as follows: \"{e}\""
                    )

                dialog = ErrDialog(self)
                dialog.exec()

            except:
                dialog = SettingsRequireEmuGUIReboot(self)
                dialog.exec()

        elif self.comboBox_4.currentText() == "Português":
            langmode = "pt"

            try:
                cursor.execute(language_pt)
                connection.commit()

                if platform.system() == "Windows":
                    langfile = platformSpecific.windowsSpecific.windowsLanguageFile()
                
                else:
                    langfile = platformSpecific.unixSpecific.unixLanguageFile()

                if langmode == "system":
                    languageToUseLater = locale.getlocale()[0]
                    languageToUseEvenLater = languageToUseLater.split("_")
                    languageToUseHere = languageToUseEvenLater[0]

                else:
                    languageToUseHere = langmode
                
                try:
                    with open(langfile, "w+") as language:
                        language.write(languageToUseHere)

                except:
                    print("EmuGUI failed to create a language file. Expect some issues.")

                    if platform.system() == "Windows":
                        errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                    else:
                        errorFile = platformSpecific.unixSpecific.unixErrorFile()

                    with open(errorFile, "w+") as errCodeFile:
                        errCodeFile.write(errors.errCodes.errCodes[54])

                    logman.writeToLogFile(
                        f"{errors.errCodes.errCodes[54]}: Could not create the language file. Expect issues."
                    )

                    dialog = ErrDialog(self)
                    dialog.exec()

                self.setLanguage(langmode)
                print("The query was executed successfully.")

            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[12])

                logman.writeToLogFile(
                    f"{errors.errCodes.errCodes[12]}: The database could not be accessed and the settings are therefore not applied. SQLite describes the error as follows: \"{e}\""
                    )

                dialog = ErrDialog(self)
                dialog.exec()

            except:
                dialog = SettingsRequireEmuGUIReboot(self)
                dialog.exec()

        elif self.comboBox_4.currentText() == "Polski":
            langmode = "pl"

            try:
                cursor.execute(language_pl)
                connection.commit()

                if platform.system() == "Windows":
                    langfile = platformSpecific.windowsSpecific.windowsLanguageFile()
                
                else:
                    langfile = platformSpecific.unixSpecific.unixLanguageFile()

                if langmode == "system":
                    languageToUseLater = locale.getlocale()[0]
                    languageToUseEvenLater = languageToUseLater.split("_")
                    languageToUseHere = languageToUseEvenLater[0]

                else:
                    languageToUseHere = langmode
                
                try:
                    with open(langfile, "w+") as language:
                        language.write(languageToUseHere)

                except:
                    print("EmuGUI failed to create a language file. Expect some issues.")

                    if platform.system() == "Windows":
                        errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                    else:
                        errorFile = platformSpecific.unixSpecific.unixErrorFile()

                    with open(errorFile, "w+") as errCodeFile:
                        errCodeFile.write(errors.errCodes.errCodes[54])

                    logman.writeToLogFile(
                        f"{errors.errCodes.errCodes[54]}: Could not create the language file. Expect issues."
                    )

                    dialog = ErrDialog(self)
                    dialog.exec()

                self.setLanguage(langmode)
                print("The query was executed successfully.")

            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[12])

                logman.writeToLogFile(
                    f"{errors.errCodes.errCodes[12]}: The database could not be accessed and the settings are therefore not applied. SQLite describes the error as follows: \"{e}\""
                    )

                dialog = ErrDialog(self)
                dialog.exec()

            except:
                dialog = SettingsRequireEmuGUIReboot(self)
                dialog.exec()

        elif self.comboBox_4.currentText() == "Italiano":
            langmode = "it"

            try:
                cursor.execute(language_it)
                connection.commit()

                if platform.system() == "Windows":
                    langfile = platformSpecific.windowsSpecific.windowsLanguageFile()
                
                else:
                    langfile = platformSpecific.unixSpecific.unixLanguageFile()

                if langmode == "system":
                    languageToUseLater = locale.getlocale()[0]
                    languageToUseEvenLater = languageToUseLater.split("_")
                    languageToUseHere = languageToUseEvenLater[0]

                else:
                    languageToUseHere = langmode
                
                try:
                    with open(langfile, "w+") as language:
                        language.write(languageToUseHere)

                except:
                    print("EmuGUI failed to create a language file. Expect some issues.")

                    if platform.system() == "Windows":
                        errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                    else:
                        errorFile = platformSpecific.unixSpecific.unixErrorFile()

                    with open(errorFile, "w+") as errCodeFile:
                        errCodeFile.write(errors.errCodes.errCodes[54])

                    logman.writeToLogFile(
                        f"{errors.errCodes.errCodes[54]}: Could not create the language file. Expect issues."
                    )

                    dialog = ErrDialog(self)
                    dialog.exec()

                self.setLanguage(langmode)
                print("The query was executed successfully.")

            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[12])

                logman.writeToLogFile(
                    f"{errors.errCodes.errCodes[12]}: The database could not be accessed and the settings are therefore not applied. SQLite describes the error as follows: \"{e}\""
                    )

                dialog = ErrDialog(self)
                dialog.exec()

            except:
                dialog = SettingsRequireEmuGUIReboot(self)
                dialog.exec()

        elif self.comboBox_4.currentText() == "Românã":
            langmode = "ro"

            try:
                cursor.execute(language_ro)
                connection.commit()

                if platform.system() == "Windows":
                    langfile = platformSpecific.windowsSpecific.windowsLanguageFile()
                
                else:
                    langfile = platformSpecific.unixSpecific.unixLanguageFile()

                if langmode == "system":
                    languageToUseLater = locale.getlocale()[0]
                    languageToUseEvenLater = languageToUseLater.split("_")
                    languageToUseHere = languageToUseEvenLater[0]

                else:
                    languageToUseHere = langmode
                
                try:
                    with open(langfile, "w+") as language:
                        language.write(languageToUseHere)

                except:
                    print("EmuGUI failed to create a language file. Expect some issues.")

                    if platform.system() == "Windows":
                        errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                    else:
                        errorFile = platformSpecific.unixSpecific.unixErrorFile()

                    with open(errorFile, "w+") as errCodeFile:
                        errCodeFile.write(errors.errCodes.errCodes[54])

                    logman.writeToLogFile(
                        f"{errors.errCodes.errCodes[54]}: Could not create the language file. Expect issues."
                    )

                    dialog = ErrDialog(self)
                    dialog.exec()

                self.setLanguage(langmode)
                print("The query was executed successfully.")

            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[12])

                logman.writeToLogFile(
                    f"{errors.errCodes.errCodes[12]}: The database could not be accessed and the settings are therefore not applied. SQLite describes the error as follows: \"{e}\""
                    )

                dialog = ErrDialog(self)
                dialog.exec()

            except:
                dialog = SettingsRequireEmuGUIReboot(self)
                dialog.exec()

        elif self.comboBox_4.currentText() == "Беларуская":
            langmode = "be"

            try:
                cursor.execute(language_be)
                connection.commit()

                if platform.system() == "Windows":
                    langfile = platformSpecific.windowsSpecific.windowsLanguageFile()
                
                else:
                    langfile = platformSpecific.unixSpecific.unixLanguageFile()

                if langmode == "system":
                    languageToUseLater = locale.getlocale()[0]
                    languageToUseEvenLater = languageToUseLater.split("_")
                    languageToUseHere = languageToUseEvenLater[0]

                else:
                    languageToUseHere = langmode
                
                try:
                    with open(langfile, "w+") as language:
                        language.write(languageToUseHere)

                except:
                    print("EmuGUI failed to create a language file. Expect some issues.")

                    if platform.system() == "Windows":
                        errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                    else:
                        errorFile = platformSpecific.unixSpecific.unixErrorFile()

                    with open(errorFile, "w+") as errCodeFile:
                        errCodeFile.write(errors.errCodes.errCodes[54])

                    logman.writeToLogFile(
                        f"{errors.errCodes.errCodes[54]}: Could not create the language file. Expect issues."
                    )

                    dialog = ErrDialog(self)
                    dialog.exec()

                self.setLanguage(langmode)
                print("The query was executed successfully.")

            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[12])

                logman.writeToLogFile(
                    f"{errors.errCodes.errCodes[12]}: The database could not be accessed and the settings are therefore not applied. SQLite describes the error as follows: \"{e}\""
                    )

                dialog = ErrDialog(self)
                dialog.exec()

            except:
                dialog = SettingsRequireEmuGUIReboot(self)
                dialog.exec()

        elif self.comboBox_4.currentText() == "Русский":
            langmode = "ru"

            try:
                cursor.execute(language_ru)
                connection.commit()

                if platform.system() == "Windows":
                    langfile = platformSpecific.windowsSpecific.windowsLanguageFile()
                
                else:
                    langfile = platformSpecific.unixSpecific.unixLanguageFile()

                if langmode == "system":
                    languageToUseLater = locale.getlocale()[0]
                    languageToUseEvenLater = languageToUseLater.split("_")
                    languageToUseHere = languageToUseEvenLater[0]

                else:
                    languageToUseHere = langmode
                
                try:
                    with open(langfile, "w+") as language:
                        language.write(languageToUseHere)

                except:
                    print("EmuGUI failed to create a language file. Expect some issues.")

                    if platform.system() == "Windows":
                        errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                    else:
                        errorFile = platformSpecific.unixSpecific.unixErrorFile()

                    with open(errorFile, "w+") as errCodeFile:
                        errCodeFile.write(errors.errCodes.errCodes[54])

                    logman.writeToLogFile(
                        f"{errors.errCodes.errCodes[54]}: Could not create the language file. Expect issues."
                    )

                    dialog = ErrDialog(self)
                    dialog.exec()

                self.setLanguage(langmode)
                print("The query was executed successfully.")

            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[12])

                logman.writeToLogFile(
                    f"{errors.errCodes.errCodes[12]}: The database could not be accessed and the settings are therefore not applied. SQLite describes the error as follows: \"{e}\""
                    )

                dialog = ErrDialog(self)
                dialog.exec()

            except:
                dialog = SettingsRequireEmuGUIReboot(self)
                dialog.exec()

        elif self.comboBox_4.currentText() == "Čeština":
            langmode = "cz"

            try:
                cursor.execute(language_cz)
                connection.commit()

                if platform.system() == "Windows":
                    langfile = platformSpecific.windowsSpecific.windowsLanguageFile()
                
                else:
                    langfile = platformSpecific.unixSpecific.unixLanguageFile()

                if langmode == "system":
                    languageToUseLater = locale.getlocale()[0]
                    languageToUseEvenLater = languageToUseLater.split("_")
                    languageToUseHere = languageToUseEvenLater[0]

                else:
                    languageToUseHere = langmode
                
                try:
                    with open(langfile, "w+") as language:
                        language.write(languageToUseHere)

                except:
                    print("EmuGUI failed to create a language file. Expect some issues.")

                    if platform.system() == "Windows":
                        errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                    else:
                        errorFile = platformSpecific.unixSpecific.unixErrorFile()

                    with open(errorFile, "w+") as errCodeFile:
                        errCodeFile.write(errors.errCodes.errCodes[54])

                    logman.writeToLogFile(
                        f"{errors.errCodes.errCodes[54]}: Could not create the language file. Expect issues."
                    )

                    dialog = ErrDialog(self)
                    dialog.exec()

                self.setLanguage(langmode)
                print("The query was executed successfully.")

            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[12])

                logman.writeToLogFile(
                    f"{errors.errCodes.errCodes[12]}: The database could not be accessed and the settings are therefore not applied. SQLite describes the error as follows: \"{e}\""
                    )

                dialog = ErrDialog(self)
                dialog.exec()

            except:
                dialog = SettingsRequireEmuGUIReboot(self)
                dialog.exec()

        elif self.comboBox_4.currentText() == "Українська":
            langmode = "uk"

            try:
                cursor.execute(language_uk)
                connection.commit()

                if platform.system() == "Windows":
                    langfile = platformSpecific.windowsSpecific.windowsLanguageFile()
                
                else:
                    langfile = platformSpecific.unixSpecific.unixLanguageFile()

                if langmode == "system":
                    languageToUseLater = locale.getlocale()[0]
                    languageToUseEvenLater = languageToUseLater.split("_")
                    languageToUseHere = languageToUseEvenLater[0]

                else:
                    languageToUseHere = langmode
                
                try:
                    with open(langfile, "w+") as language:
                        language.write(languageToUseHere)

                except:
                    print("EmuGUI failed to create a language file. Expect some issues.")

                    if platform.system() == "Windows":
                        errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                    else:
                        errorFile = platformSpecific.unixSpecific.unixErrorFile()

                    with open(errorFile, "w+") as errCodeFile:
                        errCodeFile.write(errors.errCodes.errCodes[54])

                    logman.writeToLogFile(
                        f"{errors.errCodes.errCodes[54]}: Could not create the language file. Expect issues."
                    )

                    dialog = ErrDialog(self)
                    dialog.exec()

                self.setLanguage(langmode)
                print("The query was executed successfully.")

            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[12])

                logman.writeToLogFile(
                    f"{errors.errCodes.errCodes[12]}: The database could not be accessed and the settings are therefore not applied. SQLite describes the error as follows: \"{e}\""
                    )

                dialog = ErrDialog(self)
                dialog.exec()

            except:
                dialog = SettingsRequireEmuGUIReboot(self)
                dialog.exec()

        if sysDefContent.__contains__(self.comboBox_5.currentText()): #self.comboBox_5.currentText() == "System default" or self.comboBox_5.currentText() == "Systemstandard":
            try:
                cursor.execute(theme_default)
                connection.commit()
                
                app.setStyle(self.defaultTheme)

                print("The query was executed successfully.")

                dialog = SettingsRequireEmuGUIReboot(self)
                dialog.exec()

            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[12])

                logman.writeToLogFile(
                    f"{errors.errCodes.errCodes[12]}: The database could not be accessed and the settings are therefore not applied. SQLite describes the error as follows: \"{e}\""
                    )

                dialog = ErrDialog(self)
                dialog.exec()

            except:
                dialog = SettingsRequireEmuGUIReboot(self)
                dialog.exec()
        
        else:
            try:
                cursor.execute(theme_custom)
                connection.commit()
                
                for osTheme in self.osThemes:
                    if self.comboBox_5.currentText() == osTheme:
                        app.setStyle(self.comboBox_5.currentText())

                        dialog = SettingsRequireEmuGUIReboot(self)
                        dialog.exec()

                for userTheme in self.userThemeList:
                    if self.comboBox_5.currentText() == userTheme:
                        print(userTheme)
                        userThemeFile = "themes/" + userTheme + ".qss"

                        with open(userThemeFile, "r") as themeFile:
                            style = themeFile.read()
                            app.setStyleSheet(style)

                print("The query was executed successfully.")

            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[12])

                logman.writeToLogFile(
                    f"{errors.errCodes.errCodes[12]}: The database could not be accessed and the settings are therefore not applied. SQLite describes the error as follows: \"{e}\""
                    )

                dialog = ErrDialog(self)
                dialog.exec()

            except:
                dialog = SettingsRequireEmuGUIReboot(self)
                dialog.exec()

    # Your VM list will be updated every 10 seconds.

    def updateVmList(self):
        try:
            self.timer.stop()

        except:
            pass

        connection = self.connection
        cursor = connection.cursor()

        sel_vm_names = """
        SELECT name FROM virtualmachines;
        """

        try:
            cursor.execute(sel_vm_names)
            connection.commit()
            result = cursor.fetchall()
            i = 0
            entries = []
            model = QtGui.QStandardItemModel()
            self.listView.setModel(model)

            while i < len(result):
                try:
                    entries.append(str(result[i][0]))
                    print("The VM list was updated successfully.")

                except:
                    pass

                i += 1

            for entry in entries:
                item = QtGui.QStandardItem(entry)
                model.appendRow(item)
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        self.timer.start(10000)

    def deleteVM(self):
        # This code wipes your obsolete VM from the list.

        connection = self.connection
        cursor = connection.cursor()
        selectedVM = self.listView.currentIndex().data()
        print(selectedVM)

        get_vm_to_start = f"""
        DELETE FROM virtualmachines
        WHERE name = '{selectedVM}'
        """

        try:
            cursor.execute(get_vm_to_start)
            connection.commit()
            print("The VM was deleted successfully.")
            self.updateVmList()

        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

    def toGithub(self):
        webbrowser.open_new_tab("https://www.github.com/Tech-FZ/EmuGUI")
    
    def toDiscord(self):
        webbrowser.open_new_tab("https://discord.gg/rTGpYCwF89")

    def toYouTube(self):
        webbrowser.open_new_tab("https://www.youtube.com/@EmuGUI-vr2xd")

    def toOdysee(self):
        webbrowser.open_new_tab("https://odysee.com/@EmuGUI:0")
    
    def toGuilded(self):
        webbrowser.open_new_tab("https://www.guilded.gg/i/pBAY6BAk")
    def compileQemu(self):
        dialog = CompileQemuDialog(self,qemu_dir="/home/w/Desktop/EmuGUI/qemu/qemu-10.1.0")
        dialog.exec()
    def runPythonScript(self):
        import subprocess
        import sys
        def run_python_script(script_text: str, timeout: float = None):
            try:
                proc = subprocess.run(
                    [sys.executable, "-c", script_text],  # -c executes the string as code
                    capture_output=True,                  # capture stdout and stderr
                    text=True,                            # return strings instead of bytes
                    timeout=timeout
                )
                return proc.stdout, proc.stderr, proc.returncode
            except subprocess.TimeoutExpired as e:
                return "", f"TimeoutExpired: {e}", -1
        text = self.textEdit.toPlainText().replace("\x00","")
        out_smg,err_smg,err_code = run_python_script(text)
        self.textBrowser.append (out_smg)
        self.textBrowser.append (err_smg)
    def showAPIExample1(self):
        dialog = ShowCodeDialog(self,code='''
from unicorn import *
from unicorn.x86_const import *

# code to be emulated
X86_CODE32 = b"\\x41\\x4a" # INC ecx; DEC edx

# memory address where emulation starts
ADDRESS = 0x1000000

print("Emulate i386 code")
try:
    # Initialize emulator in X86-32bit mode
    mu = Uc(UC_ARCH_X86, UC_MODE_32)

    # map 2MB memory for this emulation
    mu.mem_map(ADDRESS, 2 * 1024 * 1024)

    # write machine code to be emulated to memory
    mu.mem_write(ADDRESS, X86_CODE32)

    # initialize machine registers
    mu.reg_write(UC_X86_REG_ECX, 0x1234)
    mu.reg_write(UC_X86_REG_EDX, 0x7890)

    # emulate code in infinite time & unlimited instructions
    mu.emu_start(ADDRESS, ADDRESS + len(X86_CODE32))

    # now print out some registers
    print("Emulation done. Below is the CPU context")

    r_ecx = mu.reg_read(UC_X86_REG_ECX)
    r_edx = mu.reg_read(UC_X86_REG_EDX)
    print(">>> ECX = 0x%x" %r_ecx)
    print(">>> EDX = 0x%x" %r_edx)

except UcError as e:
    print("ERROR: %s" % e)
        ''')
        dialog.exec()
    def showAPIExample2(self):
        dialog = ShowCodeDialog(self,code='''
#!/usr/bin/env python
# Sample code for ARM64 of Unicorn. Nguyen Anh Quynh <aquynh@gmail.com>
# Python sample ported by Loi Anh Tuan <loianhtuan@gmail.com>

from unicorn import *
from unicorn.arm64_const import *

# code to be emulated
ARM64_CODE = b"\\xab\\x05\\x00\\xb8\\xaf\\x05\\x40\\x38"  # str x11, [x13]; ldrb x15, [x13]

# MSR code
ARM64_MRS_CODE = b"\\x62\\xd0\\x3b\\xd5"  # mrs        x2, tpidrro_el0

# memory address where emulation starts
ADDRESS = 0x10000


# callback for tracing basic blocks
def hook_block(uc, address, size, user_data):
    print(">>> Tracing basic block at 0x%x, block size = 0x%x" % (address, size))


# callback for tracing instructions
def hook_code(uc, address, size, user_data):
    print(">>> Tracing instruction at 0x%x, instruction size = 0x%x" % (address, size))


# Test ARM64
def test_arm64():
    print("Emulate ARM64 code")
    try:
        # Initialize emulator in ARM mode
        mu = Uc(UC_ARCH_ARM64, UC_MODE_ARM)

        # map 2MB memory for this emulation
        mu.mem_map(ADDRESS, 2 * 1024 * 1024)

        # write machine code to be emulated to memory
        mu.mem_write(ADDRESS, ARM64_CODE)

        # initialize machine registers
        mu.reg_write(UC_ARM64_REG_X11, 0x12345678)
        mu.reg_write(UC_ARM64_REG_X13, 0x10008)
        mu.reg_write(UC_ARM64_REG_X15, 0x33)

        # tracing all basic blocks with customized callback
        mu.hook_add(UC_HOOK_BLOCK, hook_block)

        # tracing one instruction with customized callback
        mu.hook_add(UC_HOOK_CODE, hook_code, begin=ADDRESS, end=ADDRESS)

        # emulate machine code in infinite time
        mu.emu_start(ADDRESS, ADDRESS + len(ARM64_CODE))

        # now print out some registers
        print(">>> Emulation done. Below is the CPU context")
        print(">>> As little endian, X15 should be 0x78:")

        x11 = mu.reg_read(UC_ARM64_REG_X11)
        x13 = mu.reg_read(UC_ARM64_REG_X13)
        x15 = mu.reg_read(UC_ARM64_REG_X15)
        print(">>> X15 = 0x%x" % x15)

    except UcError as e:
        print("ERROR: %s" % e)


def test_arm64_read_sctlr():
    print("Read SCTLR_EL1")
    try:
        # Initialize emulator in ARM mode
        mu = Uc(UC_ARCH_ARM64, UC_MODE_ARM)

        # Read SCTLR_EL1
        # crn = 1;
        # crm = 0;
        # op0 = 3;
        # op1 = 0;
        # op2 = 0;
        val = mu.reg_read(UC_ARM64_REG_CP_REG, (1, 0, 3, 0, 0))
        print(">>> SCTLR_EL1 = 0x%x" % val)

    except UcError as e:
        print("ERROR: %s" % e)


def test_arm64_hook_mrs():
    def _hook_mrs(uc, reg, cp_reg, _):
        print(">>> Hook MRS instruction: reg = {reg:#x}(UC_ARM64_REG_X2) cp_reg = {cp_reg}".format(reg=reg,
                                                                                                   cp_reg=cp_reg))
        uc.reg_write(reg, 0x114514)
        print(">>> Write 0x114514 to X")

        # Skip MRS instruction
        return True

    print("Test hook MRS instruction")
    try:
        # Initialize emulator in ARM mode
        mu = Uc(UC_ARCH_ARM64, UC_MODE_ARM)

        # Map an area for code
        mu.mem_map(0x1000, 0x1000)

        # Write code
        mu.mem_write(0x1000, ARM64_MRS_CODE)

        # Hook MRS instruction
        mu.hook_add(UC_HOOK_INSN, _hook_mrs, None, 1, 0, UC_ARM64_INS_MRS)

        # Start emulation
        mu.emu_start(0x1000, 0x1000 + len(ARM64_MRS_CODE))

        print(">>> X2 = {reg:#x}".format(reg=mu.reg_read(UC_ARM64_REG_X2)))

    except UcError as e:
        print("ERROR: %s" % e)


if __name__ == '__main__':
    test_arm64()
    print("=" * 26)
    test_arm64_read_sctlr()
    print("=" * 26)
    test_arm64_hook_mrs()
        ''')
        dialog.exec()
        
    def showAPI(self):
        dialog = ShowCodeDialog(self,code='''
// =========================
// 初始化与关闭
// =========================

uc_err uc_open(uc_arch arch, uc_mode mode, uc_engine **uc);
// 创建并初始化仿真上下文，指定架构和模式。

uc_err uc_close(uc_engine *uc);
// 关闭仿真上下文，释放资源。

// =========================
// 内存管理
// =========================

uc_err uc_mem_map(uc_engine *uc, uint64_t address, size_t size, uint32_t perms);
// 映射一段仿真内存，设置地址、大小和权限（读/写/执行）。

uc_err uc_mem_unmap(uc_engine *uc, uint64_t address, size_t size);
// 解除映射指定范围的仿真内存。

uc_err uc_mem_protect(uc_engine *uc, uint64_t address, size_t size, uint32_t perms);
// 修改已映射内存区域的访问权限。

uc_err uc_mem_read(uc_engine *uc, uint64_t address, void *bytes, size_t size);
// 从仿真内存读取数据到缓冲区。

uc_err uc_mem_write(uc_engine *uc, uint64_t address, const void *bytes, size_t size);
// 将数据写入仿真内存。

// =========================
// 寄存器访问
// =========================

uc_err uc_reg_read(uc_engine *uc, int regid, void *value);
// 读取指定寄存器的值。

uc_err uc_reg_write(uc_engine *uc, int regid, const void *value);
// 写入指定寄存器的值。

uc_err uc_reg_read_batch(uc_engine *uc, int *regs, void **vals, int count);
// 批量读取多个寄存器。

uc_err uc_reg_write_batch(uc_engine *uc, int *regs, void **vals, int count);
// 批量写入多个寄存器。

// =========================
// 仿真执行
// =========================

uc_err uc_emu_start(uc_engine *uc, uint64_t begin, uint64_t until, uint64_t timeout, size_t count);
// 启动仿真，从指定地址开始执行，直到指定结束条件。

uc_err uc_emu_stop(uc_engine *uc);
// 手动停止仿真执行。

// =========================
// 钩子与回调
// =========================

uc_err uc_hook_add(uc_engine *uc, uc_hook *hh, int type, void *callback, void *user_data,
                   uint64_t begin, uint64_t end, ...);
// 添加钩子函数，用于拦截代码执行、内存访问或中断等事件。

uc_err uc_hook_del(uc_engine *uc, uc_hook hh);
// 删除指定钩子。

// 常见回调函数原型
void code_hook(uc_engine *uc, uint64_t address, uint32_t size, void *user_data);
// 在指令执行时被调用。

bool mem_read_hook(uc_engine *uc, uc_mem_type type, uint64_t address, int size, int64_t value, void *user_data);
// 在内存读取时被调用。

bool mem_write_hook(uc_engine *uc, uc_mem_type type, uint64_t address, int size, int64_t value, void *user_data);
// 在内存写入时被调用。

bool intr_hook(uc_engine *uc, uint32_t intno, void *user_data);
// 在中断发生时被调用。

// =========================
// 架构与模式常量
// =========================

typedef enum uc_arch {
    UC_ARCH_ARM,
    UC_ARCH_ARM64,
    UC_ARCH_MIPS,
    UC_ARCH_X86,
    UC_ARCH_PPC,
    UC_ARCH_SPARC,
    UC_ARCH_RISCV,
} uc_arch;
// 支持的处理器架构类型。

typedef enum uc_mode {
    UC_MODE_LITTLE_ENDIAN = 0,
    UC_MODE_BIG_ENDIAN = 1 << 30,
    UC_MODE_16 = 1 << 1,
    UC_MODE_32 = 1 << 2,
    UC_MODE_64 = 1 << 3,
    UC_MODE_THUMB = 1 << 4,
    UC_MODE_MCLASS = 1 << 5,
    UC_MODE_V8 = 1 << 6,
} uc_mode;
// 仿真模式，如 16/32/64 位、Thumb、M-Class、V8 等。

// =========================
// 内存权限常量
// =========================

#define UC_PROT_NONE  0
#define UC_PROT_READ  (1 << 0)
#define UC_PROT_WRITE (1 << 1)
#define UC_PROT_EXEC  (1 << 2)
// 内存页权限位，用于映射或保护。

// =========================
// 钩子类型常量
// =========================

#define UC_HOOK_INTR              1 << 0
#define UC_HOOK_INSN              1 << 1
#define UC_HOOK_CODE              1 << 2
#define UC_HOOK_BLOCK             1 << 3
#define UC_HOOK_MEM_READ_UNMAPPED 1 << 4
#define UC_HOOK_MEM_WRITE_UNMAPPED 1 << 5
#define UC_HOOK_MEM_FETCH_UNMAPPED 1 << 6
#define UC_HOOK_MEM_READ_PROT     1 << 7
#define UC_HOOK_MEM_WRITE_PROT    1 << 8
#define UC_HOOK_MEM_FETCH_PROT    1 << 9
#define UC_HOOK_MEM_READ          1 << 10
#define UC_HOOK_MEM_WRITE         1 << 11
#define UC_HOOK_MEM_FETCH         1 << 12
// 不同事件类型的钩子，用于注册不同类别的回调。

// =========================
// 错误码
// =========================

typedef enum uc_err {
    UC_ERR_OK = 0,           // 无错误
    UC_ERR_NOMEM,            // 内存不足
    UC_ERR_ARCH,             // 不支持的架构
    UC_ERR_HANDLE,           // 无效的句柄
    UC_ERR_MODE,             // 模式错误
    UC_ERR_VERSION,          // 版本不匹配
    UC_ERR_READ_UNMAPPED,    // 读取未映射内存
    UC_ERR_WRITE_UNMAPPED,   // 写入未映射内存
    UC_ERR_FETCH_UNMAPPED,   // 取指未映射内存
    UC_ERR_HOOK,             // 钩子错误
    UC_ERR_INSN_INVALID,     // 无效指令
    UC_ERR_MAP,              // 内存映射失败
    UC_ERR_WRITE_PROT,       // 写保护错误
    UC_ERR_READ_PROT,        // 读保护错误
    UC_ERR_FETCH_PROT,       // 执行保护错误
    UC_ERR_ARG,              // 参数错误
    UC_ERR_READ_UNALIGNED,   // 非对齐读取
    UC_ERR_WRITE_UNALIGNED,  // 非对齐写入
    UC_ERR_FETCH_UNALIGNED,  // 非对齐执行
    UC_ERR_RESOURCE,         // 资源不足
    UC_ERR_EXCEPTION,        // 异常发生
} uc_err;
// 所有可能的错误返回码。

// =========================
// 辅助函数
// =========================

const char *uc_strerror(uc_err code);
// 将错误码转换为字符串描述。

uc_err uc_query(uc_engine *uc, uc_query_type type, size_t *result);
// 查询仿真状态或特定属性。

        ''')
        dialog.exec()
    def editInsCode(self):
        dialog = EditCodeDialog(title = "aaaa",path = "/home/w/Downloads/test.c")
        dialog.exec()
    def showDeviceInfo(self):
        dialog = DeviceInfoDialog(info_path = "/home/w/Downloads/info.txt")
        dialog.exec()
    def addQemuItems():
        std_item = QtGui.QStandardItem ("Dinner")
        child_std_item = QtGui.QStandardItem ("Drinks")
        std_item.appendRow (child_std_item)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)

    try:
        if platform.system() == "Linux":
            app.setPalette(qdarktheme.load_palette(theme="auto"))
            app.setStyleSheet(qdarktheme.load_stylesheet(theme="auto"))

    except:
        print("EmuGUI has something to say.")
        print("Error code: N-11-6RRJN")
        print("If this error occurs multiple times, contact your administrator and/or ask for help on the EmuGUI Discord Server or on its GitHub repository.")

    win = Window()
    win.show()
    sys.exit(app.exec())
