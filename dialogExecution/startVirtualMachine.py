# Importing required modules (PySide 6, platform, sqlite3, subprocess, internal program files)
from PySide6.QtWidgets import *
from PySide6 import QtGui
from uiScripts.ui_StartVM import Ui_Dialog
import platform

if platform.system() == "Windows":
    import platformSpecific.windowsSpecific

else:
    import platformSpecific.unixSpecific
    import shlex
    
import sqlite3
import subprocess
from PySide6.QtCore import QDateTime
from random import randint
import magic

import translations.en

import locale
import errors.errCodes
from dialogExecution.errDialog import ErrDialog
import services.pathfinder as pf

class StartVirtualMachineDialog(QDialog, Ui_Dialog):
    # Initializing VM starting
    def __init__(self, parent=None):
        try:
            super().__init__(parent)

        except:
            super().__init__()
            
        self.setupUi(self)
        self.exec_folder = pf.retrieveExecFolder()
        self.connectSignalsSlots()
        
        self.architectures = [
            "i386", "x86_64", "ppc", "ppc64", "mips64", "mips64el",
            "mipsel", "mips", "aarch64", "arm", "sparc", "sparc64",
            "alpha", "riscv32", "riscv64"
        ]

        try:
            self.vmSpecs = self.readTempVmFile()

        except:
            if platform.system() == "Windows":
                errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
            else:
                errorFile = platformSpecific.unixSpecific.unixErrorFile()

            with open(errorFile, "w+") as errCodeFile:
                errCodeFile.write(errors.errCodes.errCodes[13])

            dialog = ErrDialog(self)
            dialog.exec()

        print(self.vmSpecs)
        self.setWindowTitle(f"EmuGUI - Start {self.vmSpecs[0]}")
        self.langDetect()
        self.timeUsageTrigger()
        
        try:
            self.setWindowIcon(QtGui.QIcon(f"{self.exec_folder}EmuGUI.png"))

        except:
            pass

        if platform.system() == "Windows":
            self.connection = platformSpecific.windowsSpecific.setupWindowsBackend()
        
        else:
            self.connection = platformSpecific.unixSpecific.setupUnixBackend()

    def connectSignalsSlots(self):
        # This code connects the buttons to their functions
        self.pushButton.clicked.connect(self.set_fda_path)
        self.pushButton_2.clicked.connect(self.set_cdrom_path)
        self.pushButton_6.clicked.connect(self.set_cdrom2_path)
        self.pushButton_3.clicked.connect(self.start_virtual_machine)
        self.pushButton_4.clicked.connect(self.close)
        self.pushButton_5.clicked.connect(self.set_date_to_system)
        self.checkBox.clicked.connect(self.timeUsageTrigger)

    def timeUsageTrigger(self):
        if self.checkBox.isChecked():
            self.dateTimeEdit.setEnabled(True)
            self.pushButton_5.setEnabled(True)

        else:
            self.dateTimeEdit.setEnabled(False)
            self.pushButton_5.setEnabled(False)

    def langDetect(self):
        select_language = """
        SELECT name, value FROM settings
        WHERE name = "lang";
        """

        if platform.system() == "Windows":
            connection = platformSpecific.windowsSpecific.setupWindowsBackend()
        
        else:
            connection = platformSpecific.unixSpecific.setupUnixBackend()

        cursor = connection.cursor()

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

                if result[0][1] == "en":
                    langmode = "en"

                elif result[0][1] == "de":
                    langmode = "de"

                elif result[0][1] == "uk":
                    langmode = "uk"

                elif result[0][1] == "fr":
                    langmode = "fr"

                elif result[0][1] == "es":
                    langmode = "es"

                elif result[0][1] == "ro":
                    langmode = "ro"

                elif result[0][1] == "ru":
                    langmode = "ru"

                elif result[0][1] == "be":
                    langmode = "be"

                elif result[0][1] == "cz":
                    langmode = "cz"

                elif result[0][1] == "pt":
                    langmode = "pt"

                elif result[0][1] == "pl":
                    langmode = "pl"

                elif result[0][1] == "it":
                    langmode = "it"

                elif result[0][1] == "system":
                    langmode = "system"

                self.setLanguage(langmode)
                print("The query was executed successfully. The language slot already is in the database.")

            except:
                langmode = "system"
                self.setLanguage(langmode)
                print("The query was executed successfully. The language slot has been created.")
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

    def setLanguage(self, langmode):
        if langmode == "system" or langmode == None:
            languageToUse = locale.getlocale()[0]

        else:
            languageToUse = langmode

        if languageToUse != None:
            translations.en.translateStartVmEN(self, self.vmSpecs[0])
        
        else:
            if platform.system() == "Windows":
                langfile = platformSpecific.windowsSpecific.windowsLanguageFile()
            
            else:
                langfile = platformSpecific.unixSpecific.unixLanguageFile()
            
            try:
                with open(langfile, "r+") as language:
                    languageContent = language.readlines()
                    languageToUse = languageContent[0].replace("\n", "")
                
                if languageToUse != None:
                    translations.en.translateStartVmEN(self, self.vmSpecs[0])
            
            except:
                print("Translation can't be figured out. Using English language.")

                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[11])

                dialog = ErrDialog(self)
                dialog.exec()

                translations.en.translateStartVmEN(self, self.vmSpecs[0])
                

    def readTempVmFile(self):
        # Searching temporary files
        if platform.system() == "Windows":
            tempVmDef = platformSpecific.windowsSpecific.windowsTempVmStarterFile()
        
        else:
            tempVmDef = platformSpecific.unixSpecific.unixTempVmStarterFile()

        vmSpecs = []

        with open(tempVmDef, "r+") as tempVmDefFile:
            vmSpecsRaw = tempVmDefFile.readlines()

        for vmSpec in vmSpecsRaw:
            vmSpecNew = vmSpec.replace("\n", "")
            vmSpecs.append(vmSpecNew)

        return vmSpecs

    # These are asked every time you want to run the VMs.

    def set_fda_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select floppy disk', dir='.', filter='Floppy image (*.img);;Floppy file (*.flp);;Floppy image (*.ima);;All files (*.*)')

        if filename:
            self.lineEdit.setText(filename)

    def set_cdrom_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select first cdrom file', dir='.', filter='ISO image (*.iso);;All files (*.*)')

        if filename:
            self.lineEdit_2.setText(filename)

    def set_cdrom2_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select second cdrom file', dir='.', filter='ISO image (*.iso);;All files (*.*)')

        if filename:
            self.lineEdit_4.setText(filename)

    def set_date_to_system(self):
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())

    # Here, it chooses the architecture for your VM and starts the right thing.

    def start_virtual_machine(self):
        connection = self.connection
        cursor = connection.cursor()

        fda_file = self.lineEdit.text()
        cdrom_file = self.lineEdit_2.text()
        cdrom_file2 = self.lineEdit_4.text()
        bootfrom = self.comboBox.currentText()
        dateTimeForVM = self.dateTimeEdit.text()

        print(fda_file)
        print(cdrom_file)
        print(bootfrom)
        print(dateTimeForVM)

        qemu_cmd = ""

        try:
            for architecture in self.architectures:
                if self.vmSpecs[1] == architecture:
                    sel_query = f"""
                    SELECT value FROM settings
                    WHERE name = 'qemu-system-{architecture}';
                    """

                    cursor.execute(sel_query)
                    connection.commit()
                    result = cursor.fetchall()
                    print(result)
                    break
            mode = result[0][26]
            qemu_to_execute = result[0][0]

            qemu_cmd = f"\"{qemu_to_execute}\" -m {self.vmSpecs[4]} -smp {self.vmSpecs[17]} -k {self.vmSpecs[22]}"
            qemu_cmd_list = [qemu_to_execute, f"-m", self.vmSpecs[4], f"-smp", self.vmSpecs[17], f"-k", self.vmSpecs[22]]

            if self.checkBox.isChecked():
                qemu_cmd = qemu_cmd + f" -rtc base=\"{dateTimeForVM}\",clock=vm"
                qemu_cmd_list.append(f"-rtc")
                qemu_cmd_list.append(f"base=\"{dateTimeForVM}\",clock=vm")

            if self.vmSpecs[5] != "NULL":
                if magic.from_file(self.vmSpecs[5]) == "block special":
                    qemu_cmd = qemu_cmd + f" -drive format=raw,file=\"{self.vmSpecs[5]}\""
                    qemu_cmd_list.append(f"-drive")
                    qemu_cmd_list.append(f"format=raw,file=\"{self.vmSpecs[5]}\"")

                else:
                    if self.vmSpecs[26] == "Let QEMU decide":
                        qemu_cmd = qemu_cmd + f" -hda \"{self.vmSpecs[5]}\""
                        qemu_cmd_list.append(f"-hda")
                        qemu_cmd_list.append(f"{self.vmSpecs[5]}")

                    else:
                        qemu_cmd = qemu_cmd + " -drive"
                        qemu_cmd_list.append(f"-drive")

                        if self.vmSpecs[26] == "IDE":
                            qemu_cmd = qemu_cmd + f" file=\"{self.vmSpecs[5]}\",if=ide,media=disk"
                            qemu_cmd_list.append(f"file=\"{self.vmSpecs[5]}\",if=ide,media=disk")

                        elif self.vmSpecs[26] == "VirtIO SCSI":
                            qemu_cmd = qemu_cmd + f" file=\"{self.vmSpecs[5]}\",if=none,discard=unmap,aio=native,cache=none,id=hd1 -device scsi-hd,drive=hd1,bus=scsi0.0"
                            qemu_cmd_list.append(f"file=\"{self.vmSpecs[5]}\",if=none,discard=unmap,aio=native,cache=none,id=hd1")
                            qemu_cmd_list.append(f"-device")
                            qemu_cmd_list.append(f"scsi-hd,drive=hd1,bus=scsi0.0")

                        elif self.vmSpecs[26] == "AHCI":
                            qemu_cmd = qemu_cmd + f" file=\"{self.vmSpecs[5]}\",if=none -device ahci,id=ahci -device ide-hd,drive=disk,bus=ahci.0"
                            qemu_cmd_list.append(f"file=\"{self.vmSpecs[5]}\",if=none")
                            qemu_cmd_list.append(f"-device")
                            qemu_cmd_list.append(f"ahci,id=ahci")
                            qemu_cmd_list.append(f"-device")
                            qemu_cmd_list.append(f"ide-hd,drive=disk,bus=ahci.0")

            if self.vmSpecs[2] != "Let QEMU decide":
                qemu_cmd = qemu_cmd + f" -M {self.vmSpecs[2]}"
                qemu_cmd_list.append(f"-M")
                qemu_cmd_list.append(f"self.vmSpecs[2]")
            '''    
            elif self.vmSpecs[1] == "aarch64" or self.vmSpecs[1] == "arm":
                qemu_cmd = qemu_cmd + " -M virt"
                qemu_cmd_list.append(f"-M")
                qemu_cmd_list.append(f"virt")
            '''
            
            if self.vmSpecs[3] != "Let QEMU decide":
                qemu_cmd = qemu_cmd + f" -cpu {self.vmSpecs[3]}"
                qemu_cmd_list.append(f"-cpu")
                qemu_cmd_list.append(f"self.vmSpecs[3]")

            if self.vmSpecs[6] != "Let QEMU decide":
                if self.vmSpecs[6] == "std" or self.vmSpecs[6] == "qxl" or self.vmSpecs[6] == "cirrus" or self.vmSpecs[6] == "cg3" or self.vmSpecs[6] == "tcx":
                    qemu_cmd = qemu_cmd + f" -vga {self.vmSpecs[6]}"
                    qemu_cmd_list.append(f"-vga")
                    qemu_cmd_list.append(f"self.vmSpecs[6]")

                else:
                    qemu_cmd = qemu_cmd + f" -device {self.vmSpecs[6]}"
                    qemu_cmd_list.append(f"-device")
                    qemu_cmd_list.append(f"self.vmSpecs[6]")

            if self.vmSpecs[7] != "none":
                if self.vmSpecs[1] == "i386" or self.vmSpecs[1] == "x86_64" or self.vmSpecs[1] == "ppc" or self.vmSpecs[1] == "ppc64" or self.vmSpecs[1] == "sparc" or self.vmSpecs[1] == "sparc64":
                    qemu_cmd = qemu_cmd + f" -net nic,model={self.vmSpecs[7]} -net user"
                    qemu_cmd_list.append(f"-net")
                    qemu_cmd_list.append(f"nic,model={self.vmSpecs[7]}")
                    qemu_cmd_list.append(f"-net")
                    qemu_cmd_list.append(f"user")

                if self.vmSpecs[1] == "riscv32" or self.vmSpecs[1] == "riscv64" or self.vmSpecs[1] == "alpha":
                    qemu_cmd = qemu_cmd + f" -net nic,model={self.vmSpecs[7]} -net user"
                    qemu_cmd_list.append(f"-net")
                    qemu_cmd_list.append(f"nic,model={self.vmSpecs[7]}")
                    qemu_cmd_list.append(f"-net")
                    qemu_cmd_list.append(f"user")

                elif self.vmSpecs[1] == "mips64el" or self.vmSpecs[1] == "mipsel":
                    qemu_cmd = qemu_cmd + f" -nic user,model={self.vmSpecs[7]}"
                    qemu_cmd_list.append(f"-net")
                    qemu_cmd_list.append(f"user,model={self.vmSpecs[7]}")

                elif self.vmSpecs[1] == "aarch64" or self.vmSpecs[1] == "arm":
                    # Due to the circumstances here, for the VM, a random MAC address is
                    # generated at runtime. Due to that, the MAC changes every time you
                    # start your virtual machine.

                    mac_possible_chars = "0123456789abcdef"

                    mac_gen = []
                    i = 0

                    while i < 6:
                        firstLetter = mac_possible_chars[randint(0, 15)]
                        secondLetter = mac_possible_chars[randint(0, 15)]
                        mac_part = firstLetter + secondLetter
                        mac_gen.append(mac_part)
                        i += 1

                    mac_to_use = f"{mac_gen[0]}:{mac_gen[1]}:{mac_gen[2]}:{mac_gen[3]}:{mac_gen[4]}:{mac_gen[5]}"
                    qemu_cmd = qemu_cmd + f" -device {self.vmSpecs[7]},netdev=hostnet0,mac={mac_to_use} -netdev user,id=hostnet0"
                    qemu_cmd_list.append(f"-device")
                    qemu_cmd_list.append(f"{self.vmSpecs[7]},netdev=hostnet0,mac={mac_to_use}")
                    qemu_cmd_list.append(f"-netdev")
                    qemu_cmd_list.append(f"user,id=hostnet0")

            if self.vmSpecs[20] == "1":
                if self.vmSpecs[21] == "Host":
                    import usb.core
                    import usb.util
                    devices = usb.core.find(find_all=True)
                    for dev in devices:
                        bus = dev.bus
                        addr = dev.address
                        qemu_cmd = qemu_cmd + f" -device usb-host,hostbus={bus},hostaddr={addr}"
                        qemu_cmd_list.append(f"-device")
                        qemu_cmd_list.append(f"usb-host,hostbus={bus},hostaddr={addr}")
                else:
                    qemu_cmd = qemu_cmd + f" -usb -device {self.vmSpecs[21]}"
                    qemu_cmd_list.append(f"-usb")
                    qemu_cmd_list.append(f"-device")
                    qemu_cmd_list.append(f"{self.vmSpecs[21]}")
            
            if self.vmSpecs[8] == "1":
                print("WARNING: Using the checkbox for the USB tablet is depreciated.")
                print("This feature is going to be removed in a future update.")
                print("Please use the combo box for this task instead.")
                qemu_cmd = qemu_cmd + " -usbdevice tablet"
                qemu_cmd_list.append(f"-usbdevice")
                qemu_cmd_list.append(f"tablet")

            if self.vmSpecs[8] == "1" and self.vmSpecs[0] == "i386":
                qemu_cmd = qemu_cmd + " -win2k-hack"
                qemu_cmd_list.append(f"-win2k-hack")

            if fda_file != "":
                qemu_cmd = qemu_cmd + f" -drive format=raw,file=\"{fda_file}\",index=0,if=floppy"
                qemu_cmd_list.append(f"-drive")
                qemu_cmd_list.append(f"format=raw,file=\"{fda_file}\",index=0,if=floppy")

            if cdrom_file != "":
                if self.vmSpecs[24] == "Let QEMU decide":
                    qemu_cmd = qemu_cmd + f" -cdrom \"{cdrom_file}\""
                    qemu_cmd_list.append(f"-cdrom")
                    qemu_cmd_list.append(f"\"{cdrom_file}\"")

                else:
                    if self.vmSpecs[24] == "IDE":
                        qemu_cmd = qemu_cmd + f" -drive file=\"{cdrom_file}\",if=ide,media=cdrom"
                        qemu_cmd_list.append(f"-drive")
                        qemu_cmd_list.append(f"file=\"{cdrom_file}\",if=ide,media=cdrom")

                    elif self.vmSpecs[24] == "SCSI":
                        qemu_cmd = qemu_cmd + f" -drive file=\"{cdrom_file}\",if=scsi,media=cdrom"
                        qemu_cmd_list.append(f"-drive")
                        qemu_cmd_list.append(f"file=\"{cdrom_file}\",if=scsi,media=cdrom")

                    elif self.vmSpecs[24] == "Virtio":
                        qemu_cmd = qemu_cmd + f" -drive file=\"{cdrom_file}\",if=virtio,media=cdrom"
                        qemu_cmd_list.append(f"-drive")
                        qemu_cmd_list.append(f"file=\"{cdrom_file}\",if=virtio,media=cdrom")

            if cdrom_file2 != "":
                if self.vmSpecs[25] == "Let QEMU decide":
                    qemu_cmd = qemu_cmd + f" -cdrom \"{cdrom_file2}\""
                    qemu_cmd_list.append(f"-cdrom")
                    qemu_cmd_list.append(f"\"{cdrom_file2}\"")

                else:
                    if self.vmSpecs[25] == "IDE":
                        qemu_cmd = qemu_cmd + f" -drive file={cdrom_file2},if=ide,media=cdrom"
                        qemu_cmd_list.append(f"-drive")
                        qemu_cmd_list.append(f"file=\"{cdrom_file2}\",if=ide,media=cdrom")

                    elif self.vmSpecs[25] == "SCSI":
                        qemu_cmd = qemu_cmd + f" -drive file={cdrom_file2},if=scsi,media=cdrom"
                        qemu_cmd_list.append(f"-drive")
                        qemu_cmd_list.append(f"file=\"{cdrom_file2}\",if=scsi,media=cdrom")

                    elif self.vmSpecs[25] == "Virtio":
                        qemu_cmd = qemu_cmd + f" -drive file={cdrom_file2},if=virtio,media=cdrom"
                        qemu_cmd_list.append(f"-drive")
                        qemu_cmd_list.append(f"file=\"{cdrom_file2}\",if=virtio,media=cdrom")

            if bootfrom == "c" or bootfrom == "a" and fda_file == "" or bootfrom == "d" and cdrom_file == "":
                qemu_cmd = qemu_cmd + " -boot c"
                qemu_cmd_list.append(f"-boot")
                qemu_cmd_list.append(f"c")

            elif bootfrom == "a" and fda_file != "":
                qemu_cmd = qemu_cmd + " -boot a"
                qemu_cmd_list.append(f"-boot")
                qemu_cmd_list.append(f"a")
            
            elif bootfrom == "d" and cdrom_file != "":
                qemu_cmd = qemu_cmd + " -boot d"
                qemu_cmd_list.append(f"-boot")
                qemu_cmd_list.append(f"d")

            if self.vmSpecs[10] != "":
                qemu_cmd = qemu_cmd + f" -L {self.vmSpecs[10]}"
                qemu_cmd_list.append(f"-L")
                qemu_cmd_list.append(f"{self.vmSpecs[10]}")

            if self.vmSpecs[12] != "none":
                qemu_cmd = qemu_cmd + f" -device {self.vmSpecs[12]}"
                qemu_cmd_list.append(f"-device")
                qemu_cmd_list.append(f"{self.vmSpecs[12]}")

                if self.vmSpecs[12] == "intel-hda":
                    qemu_cmd = qemu_cmd + " -device hda-duplex"
                    qemu_cmd_list.append(f"-device")
                    qemu_cmd_list.append(f"hda-duplex")

            if self.vmSpecs[13] != "":
                qemu_cmd = qemu_cmd + f" -kernel \"{self.vmSpecs[13]}\""
                qemu_cmd_list.append(f"-kernel")
                qemu_cmd_list.append(f"\"{self.vmSpecs[13]}\"")

            if self.vmSpecs[14] != "":
                qemu_cmd = qemu_cmd + f" -initrd \"{self.vmSpecs[14]}\""
                qemu_cmd_list.append(f"-initrd")
                qemu_cmd_list.append(f"\"{self.vmSpecs[14]}\"")

            if self.vmSpecs[15] != "":
                qemu_cmd = qemu_cmd + f" -append \"{self.vmSpecs[15]}\""
                qemu_cmd_list.append(f"-append")
                qemu_cmd_list.append(f"\"{self.vmSpecs[15]}\"")

            if self.vmSpecs[16] == "USB Mouse" and self.vmSpecs[7] == "0":
                if self.vmSpecs[1] == "aarch64" or self.vmSpecs[1] == "arm":
                    qemu_cmd = qemu_cmd + " -device usb-mouse"
                    qemu_cmd_list.append(f"-device")
                    qemu_cmd_list.append(f"usb-mouse")

                else:
                    qemu_cmd = qemu_cmd + " -usbdevice mouse"
                    qemu_cmd_list.append(f"-usbdevice")
                    qemu_cmd_list.append(f"mouse")

            if self.vmSpecs[16] == "USB Tablet Device" and self.vmSpecs[7] == "0":
                if self.vmSpecs[1] == "aarch64" or self.vmSpecs[1] == "arm":
                    qemu_cmd = qemu_cmd + " -device usb-tablet"
                    qemu_cmd_list.append(f"-device")
                    qemu_cmd_list.append(f"usb-tablet")

                else:
                    qemu_cmd = qemu_cmd + " -usbdevice tablet"
                    qemu_cmd_list.append(f"-usbdevice")
                    qemu_cmd_list.append(f"tablet")

            if self.vmSpecs[18] != "" and self.vmSpecs[18] != None and self.vmSpecs[18] != "None":
                qemu_cmd = qemu_cmd + f" -bios \"{self.vmSpecs[18]}\""
                qemu_cmd_list.append(f"-bios")
                qemu_cmd_list.append(f"\"{self.vmSpecs[18]}\"")

            if self.vmSpecs[19] == "USB Keyboard":
                qemu_cmd = qemu_cmd + " -device usb-kbd"
                qemu_cmd_list.append(f"-device")
                qemu_cmd_list.append(f"usb-kbd")

            if self.vmSpecs[11] != "":
                qemu_cmd = qemu_cmd + f" {self.vmSpecs[11]}"
                qemu_cmd_list.append(self.vmSpecs[11])

            if self.vmSpecs[23] == "TCG":
                qemu_cmd = qemu_cmd + " -accel tcg"
                qemu_cmd_list.append(f"-accel")
                qemu_cmd_list.append(f"tcg")

            elif self.vmSpecs[23] == "HAXM":
                qemu_cmd = qemu_cmd + " -accel hax"
                qemu_cmd_list.append(f"-accel")
                qemu_cmd_list.append(f"hax")

            elif self.vmSpecs[23] == "WHPX":
                qemu_cmd = qemu_cmd + " -accel whpx"
                qemu_cmd_list.append("-accel")
                qemu_cmd_list.append("whpx")

            elif self.vmSpecs[23] == "WHPX (kernel-irqchip off)":
                qemu_cmd = qemu_cmd + " -accel whpx,kernel-irqchip=off"
                qemu_cmd_list.append(f"-accel")
                qemu_cmd_list.append(f"whpx,kernel-irqchip=off")

            elif self.vmSpecs[23] == "KVM":
                qemu_cmd = qemu_cmd + " -enable-kvm"
                qemu_cmd_list.append(f"-enable-kvm")

            if self.lineEdit_3.text() != "":
                if self.vmSpecs[1] == "x86_64":
                    qemu_cmd = qemu_cmd + f" -chardev socket,id=chrtpm,path={self.lineEdit_3.text()}/swtpm-sock -tpmdev emulator,id=tpm0,chardev=chrtpm -device tpm-tis,tpmdev=tpm0"
                    qemu_cmd_list.append(f"-chardev")
                    qemu_cmd_list.append(f"socket,id=chrtpm,path={self.lineEdit_3.text()}/swtpm-sock")
                    qemu_cmd_list.append(f"-tpmdev")
                    qemu_cmd_list.append(f"emulator,id=tpm0,chardev=chrtpm")
                    qemu_cmd_list.append(f"-device")
                    qemu_cmd_list.append(f"tpm-tis,tpmdev=tpm0")

                elif self.vmSpecs[1] == "aarch64":
                    qemu_cmd = qemu_cmd + f" -chardev socket,id=chrtpm,path={self.lineEdit_3.text()}/swtpm-sock -tpmdev emulator,id=tpm0,chardev=chrtpm -device tpm-tis-device,tpmdev=tpm0"
                    qemu_cmd_list.append(f"-chardev")
                    qemu_cmd_list.append(f"socket,id=chrtpm,path={self.lineEdit_3.text()}/swtpm-sock")
                    qemu_cmd_list.append(f"-tpmdev")
                    qemu_cmd_list.append(f"emulator,id=tpm0,chardev=chrtpm")
                    qemu_cmd_list.append(f"-device")
                    qemu_cmd_list.append(f"tpm-tis-device,tpmdev=tpm0")

                elif self.vmSpecs[1] == "ppc64":
                    qemu_cmd = qemu_cmd + f" -chardev socket,id=chrtpm,path={self.lineEdit_3.text()}/swtpm-sock -tpmdev emulator,id=tpm0,chardev=chrtpm -device tpm-spapr,tpmdev=tpm0"
                    qemu_cmd_list.append(f"-chardev")
                    qemu_cmd_list.append(f"socket,id=chrtpm,path={self.lineEdit_3.text()}/swtpm-sock")
                    qemu_cmd_list.append(f"-tpmdev")
                    qemu_cmd_list.append(f"emulator,id=tpm0,chardev=chrtpm")
                    qemu_cmd_list.append(f"-device")
                    qemu_cmd_list.append(f"tpm-spapr,tpmdev=tpm0")
            if mode == "固件托管仿真":
                qemu_to_execute = qemu_to_execute.replace("-system", "")
                
                qemu_cmd = f"\"{qemu_to_execute}\""
                qemu_cmd_list = [qemu_to_execute]
                
                qemu_cmd = qemu_cmd + f" -kernel \"{self.vmSpecs[13]}\""
                qemu_cmd_list.append(f"-kernel \"{self.vmSpecs[13]}\"")
                
                qemu_cmd = qemu_cmd + f" -append \"{self.vmSpecs[15]}\""
                qemu_cmd_list.append(f"-append \"{self.vmSpecs[15]}\"")

            if self.checkBox_debug.isChecked():
                qemu_cmd = qemu_cmd + f" -s -S"
                qemu_cmd_list.append(f"-s -S")
            if self.checkBox_debug_2.isChecked():
                qemu_cmd = qemu_cmd + " -nographic"
                qemu_cmd_list.append("-nographic")
            qemu_cmd_list = ["gnome-terminal", "--", "bash", "-c"] + [qemu_cmd + "; exec bash"]
            print(qemu_cmd_list)
            subprocess.Popen(qemu_cmd_list)

        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")
        
        except:
            pass
            '''
            print("Qemu couldn't be executed. Trying subprocess.run")

            try:
                subprocess.run(shlex.split(qemu_cmd))
            
            except:
                print("Qemu couldn't be executed. Trying subprocess.call.")

                try:
                    if platform.system() == "Windows":
                        subprocess.call(qemu_cmd)

                    else:
                        subprocess.call(shlex.split(qemu_cmd))

                except:
                    print("Qemu couldn't be executed. Please check if the settings of your VM and/or the QEMU paths are correct.")
            '''
        self.close()
