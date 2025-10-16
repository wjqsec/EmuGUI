from translations.systemdefaultset import *

def translateMainEN(window):
    # Tab group 1
    window.tabWidget.setTabText(0, "主页") # Main
    window.tabWidget.setTabText(1, "设置") # Settings
    window.tabWidget.setTabText(3, "仿真外设信息") # Settings
    window.tabWidget.setTabText(4, "仿真API编程") # Settings
    # Main tab
    # window.pushButton_8.setText("New virtual machine") # New virtual machine
    # window.pushButton_9.setText("Start virtual machine") # Start virtual machine
    # window.pushButton_10.setText("Edit selected virtual machine") # Edit selected virtual machine
    # window.pushButton_11.setText("Delete selected virtual machine") # Delete selected virtual machine
    # window.pushButton_22.setText("Export selected virtual machine") # Export selected virtual machine
    # window.pushButton_23.setText("Import virtual machine") # Import virtual machine
    window.pushButton_8.setText("新建虚拟机") # New virtual machine
    window.pushButton_9.setText("开始虚拟机") # Start virtual machine
    window.pushButton_10.setText("编辑选中的虚拟机") # Edit selected virtual machine
    window.pushButton_11.setText("删除选中的虚拟机") # Delete selected virtual machine
    window.pushButton_22.setText("导出选中的虚拟机") # Export selected virtual machine
    window.pushButton_23.setText("导入虚拟机") # Import virtual machine

    # Settings tabs
    #window.tabWidget_2.setTabText(0, "General") # General
    #window.tabWidget_2.setTabText(3, "About EmuGUI") # About EmuGUI

    # General tab
    #window.label_15.setText("Language") # Language
    #window.pushButton_15.setText("应用") # 应用

    # Combo box for languages
    i = 0
    '''
    while i < window.comboBox_4.count():
        sysDefSet("System default", window.comboBox_4, i) # System default

        i += 1

    # Combo box for themes
    i = 0

    while i < window.comboBox_5.count():
        sysDefSet("System default", window.comboBox_5, i) # System default

        i += 1
    '''
    # QEMU tab
    window.label.setText("qemu-img 路径") # qemu-img Path
    window.label_2.setText("qemu-system-i386 路径") # qemu-system-i386 Path
    window.label_3.setText("qemu-system-x86_64 路径") # qemu-system-x86_64 Path
    window.label_4.setText("qemu-system-ppc 路径") # qemu-system-ppc Path
    window.label_5.setText("qemu-system-mips64el 路径") # qemu-system-mips64el Path
    window.label_9.setText("qemu-system-aarch64 路径") # qemu-system-aarch64 Path
    window.label_11.setText("qemu-system-arm 路径") # qemu-system-arm Path
    window.label_16.setText("qemu-system-ppc64 路径") # qemu-system-ppc64 Path
    window.label_17.setText("qemu-system-mipsel 路径") # qemu-system-mipsel Path
    window.label_18.setText("qemu-system-mips 路径") # qemu-system-mips Path
    window.label_19.setText("qemu-system-mips64 路径") # qemu-system-mips64 Path
    window.label_12.setText("qemu-system-sparc 路径") # qemu-system-sparc Path
    window.label_13.setText("qemu-system-sparc64 路径") # qemu-system-sparc64 Path
    window.lbl_alpha.setText("qemu-system-alpha 路径") # qemu-system-alpha Path
    window.lbl_riscv32.setText("qemu-system-riscv32 路径") # qemu-system-riscv32 Path
    window.lbl_riscv64.setText("qemu-system-riscv64 路径") # qemu-system-riscv64 Path

    window.pushButton.setText("浏览") # 浏览
    window.pushButton_2.setText("浏览") # 浏览
    window.pushButton_3.setText("浏览") # 浏览
    window.pushButton_4.setText("浏览") # 浏览
    window.pushButton_5.setText("浏览") # 浏览
    window.pushButton_7.setText("浏览") # 浏览
    window.pushButton_12.setText("浏览") # 浏览
    window.pushButton_16.setText("浏览") # 浏览
    window.pushButton_17.setText("浏览") # 浏览
    window.pushButton_18.setText("浏览") # 浏览
    window.pushButton_19.setText("浏览") # 浏览
    window.pushButton_13.setText("浏览") # 浏览
    window.pushButton_14.setText("浏览") # 浏览
    window.btn_alpha.setText("浏览") # 浏览
    window.btn_riscv32.setText("浏览") # 浏览
    window.btn_riscv64.setText("浏览") # 浏览
    window.pushButton_6.setText("应用") # 应用
    window.btn_apply_qemu2.setText("应用") # 应用

    # About tab
    # label_7 = Built on Python and PyQt technology, licensed under GNU General Public License 3.0
    '''
    window.label_7.setText("xiyang3 Built on Python and PyQt technology, licensed under GNU General Public License 3.0")

    window.label_10.setText(
        """
        WARNING: This program comes with ABSOLUTELY NO WARRANTY under applicable law. Please see the GNU GPL license for details.
        """
        ) # WARNING: This program comes with ABSOLUTELY NO WARRANTY under applicable law. Please see the GNU GPL license for details.

    window.label_14.setText("Banner made by Tech-FZ.") # Banner made by (insert author of current banner here).

    window.label_21.setText("EmuGUI on social media (in English)") # EmuGUI on social media (in English)
    '''
def translateNewVmEN(window):
    #window.setWindowTitle("EmuGUI - Create new VM")
    # 新建VM对话框标题
    window.setWindowTitle("EmuGUI-新建虚拟机")

    # First page
    # window.lbl_vmname.setText("Name") # Name
    # window.lbl_arch.setText("Architecture") # Architecture
    window.lbl_vmname.setText("名称")  # Name
    window.lbl_arch.setText("架构")  # Architecture
    window.cb_arch.setPlaceholderText("请选择一种架构") # Please choose an architecture

    window.btn_next1.setText("下一步 >") # Next >
    window.btn_cancel1.setText("取消") # 取消

    # Second page
    window.lbl_machine.setText("机器") # Machine
    window.lbl_cpu.setText("处理器") # CPU
    window.lbl_ram.setText("内存大小(MB)") # RAM in MB

    window.cb_machine.setPlaceholderText("请选择一种机器") # Please select a machine
    window.cb_cpu.setPlaceholderText("请选择一种处理器") # Please select a processor

    window.pb_prev2.setText("< 返回") # < Previous
    window.pb_next2.setText("下一步 >") # Next >
    window.pb_cancel2.setText("取消") # 取消

    # Combo boxes on second page
    i = 0

    while i < window.cb_machine.count():
        if window.cb_machine.itemText(i) == "QEMU适配" or window.cb_machine.itemText(i) == "QEMU überlassen":
            window.cb_machine.setItemText(i, "QEMU适配") # QEMU适配
            break

        i += 1

    i = 0

    while i < window.cb_cpu.count():
        if window.cb_cpu.itemText(i) == "QEMU适配" or window.cb_cpu.itemText(i) == "QEMU überlassen":
            window.cb_cpu.setItemText(i, "QEMU适配") # QEMU适配
            break

        i += 1

    # Third page
    window.lbl_vhdU.setText("虚拟硬盘") # VHD usage

    # Combobox for VHD usage
    i = 0

    while i < window.cb_vhdU.count():
        if window.cb_vhdU.itemText(i) == "Create a new virtual hard drive":
            window.cb_vhdU.setItemText(i, "新建虚拟硬盘") # Create a new virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdU.count():
        if window.cb_vhdU.itemText(i) == "Add an existing virtual hard drive":
            window.cb_vhdU.setItemText(i, "添加已有虚拟硬盘") # Add an existing virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdU.count():
        if window.cb_vhdU.itemText(i) == "Don't add a virtual hard drive":
            window.cb_vhdU.setItemText(i, "不使用虚拟硬盘") # Don't add a virtual hard drive
            break

        i += 1

    window.lbl_vhdP.setText("虚拟硬盘路径") # VHD path
    window.lbl_vhdF.setText("虚拟硬盘格式") # VHD file format
    window.lbl_maxsize.setText("最大空间") # Maximum size
    window.lbl_hddC.setText("硬盘控制器") # HDD controller

    i = 0

    while i < window.cb_hddC.count():
        if window.cb_hddC.itemText(i) == "QEMU适配" or window.cb_hddC.itemText(i) == "QEMU überlassen":
            window.cb_hddC.setItemText(i, "QEMU适配") # QEMU适配
            break

        i += 1

    window.cb_vhdF.setPlaceholderText("(请选择一种文件格式)") # (Please select a file format)

    window.btn_vhdP.setText("浏览") # 浏览
    window.btn_prev3.setText("< 返回") # < Previous
    window.btn_next3.setText("下一步 >") # Next >
    window.btn_cancel3.setText("取消") # 取消

    # Fourth page
    window.lbl_vga.setText("显示") # VGA
    window.lbl_net.setText("网络") # Network
    window.lbl_mouse.setText("鼠标") # Mouse
    window.label_18.setText("USB平板")
    window.checkBox_4.setText("启用")
    window.checkBox.setText("启用")

    window.cb_vga.setPlaceholderText("(选择图形适配器)") # (Please select a graphics adapter)
    window.cb_net.setPlaceholderText("(选择网卡适配器)") # (Please select a network adapter)

    window.btn_prev4.setText("< 返回") # < Previous
    window.btn_next4.setText("下一步 >") # Next >
    window.btn_cancel4.setText("取消") # 取消

    # Fifth page
    window.lbl_biosLoc.setText(
        "BIOS文件位置(留空以使用默认BIOS)"
        ) # Location of external\nBIOS file (Leave\nempty to use the\ndefault BIOS)

    window.lbl_biosF.setText("外部BIOS文件") # External BIOS file

    window.btn_biosF.setText("浏览") # 浏览
    window.btn_prev5.setText("< 返回") # < Previous
    window.btn_next5.setText("下一步 >") # Next >
    window.btn_cancel5.setText("取消") # 取消

    # Sixth page
    window.lbl_sound.setText("声卡") # Sound card
    window.lbl_cores.setText("处理器 核心	")# CPU cores
    window.lbl_kbd.setText("键盘") # Keyboard
    window.lbl_kbdlayout.setText("键盘布局") # Keyboard layout

    window.btn_prev6.setText("< 返回") # < Previous
    window.btn_next6.setText("下一步 >") # Next >
    window.btn_cancel6.setText("取消") # 取消

    # Seventh page
    window.lbl_kernel.setText("镜像文件") # Linux kernel
    window.lbl_initrd.setText("临时文件系统") # Linux initrd image
    window.lbl_cmd.setText("命令行参数") # Linux cmd args

    window.btn_kernel.setText("浏览") # 浏览
    window.btn_initrd.setText("浏览") # 浏览
    window.btn_prev7.setText("< 返回") # < Previous
    window.btn_next7.setText("下一步 >") # Next >
    window.btn_cancel7.setText("取消") # 取消

    # Eighth page
    window.lbl_accel.setText("加速器") # Acceleration
    window.lbl_cdc1.setText("光盘控制器 1") # CD controller 1
    window.lbl_cdc2.setText("光盘控制器 2") # CD controller 2

    i = 0

    while i < window.cb_cdc1.count():
        if window.cb_cdc1.itemText(i) == "QEMU适配" or window.cb_cdc1.itemText(i) == "QEMU überlassen":
            window.cb_cdc1.setItemText(i, "QEMU适配") # QEMU适配
            break

        i += 1

    i = 0

    while i < window.cb_cdc2.count():
        if window.cb_cdc2.itemText(i) == "QEMU适配" or window.cb_cdc2.itemText(i) == "QEMU überlassen":
            window.cb_cdc2.setItemText(i, "QEMU适配") # QEMU适配
            break

        i += 1

    window.btn_prev8.setText("< 返回") # < Previous
    window.btn_next8.setText("下一步 >") # Next >
    window.btn_cancel8.setText("取消") # 取消

    # Ninth page
    window.lbl_addargs.setText("额外参数(可选)") # Additional arguments (if needed)

    window.checkBox_2.setText("安装 Windows 2000") # I want to install Windows 2000\n(depreciated)
    window.chb_usb.setText("添加USB支持") # Add USB support

    window.btn_prev9.setText("< 返回") # < Previous
    window.btn_finish.setText("完成") # Finish
    window.btn_cancel9.setText("取消") # 取消

def translateStartVmEN(window, vmname):
    window.setWindowTitle(f"EmuGUI - 启动 {vmname}")
    window.label_4.setText("日期和时间") # Date & Time
    window.label_3.setText("从此启动") # Boot from
    window.label_6.setText("TPM 路径 (Linux 适用)") # TPM path (Linux only)
    window.label_7.setText("从终端创建 TPM！") # Create the TPM from the terminal!
    window.label.setText("软盘")
    window.label_2.setText("光盘 1")
    window.label_8.setText("光盘 2")
    
    window.label_5.setText("""
    注意：如果虚拟机在五分钟内没有启动，那么您应该检查虚拟机和 QEMU 设置。
    """) # Note: If the VM doesn't start within five minutes, then you should check the VM and QEMU settings.

    window.pushButton.setText("浏览") # 浏览
    window.pushButton_2.setText("浏览") # 浏览
    window.pushButton_6.setText("浏览") # 浏览
    window.pushButton_5.setText("Set to system") # Set to system
    window.pushButton_3.setText("启动虚拟机") # Start VM
    window.pushButton_4.setText("取消") # 取消
    window.checkBox.setText("使用RTC") # Use RTC option

    # Combo box for boot
    i = 0

    while i < window.comboBox.count():
        if window.comboBox.itemText(i) == "QEMU适配" or window.comboBox.itemText(i) == "QEMU überlassen":
            window.comboBox.setItemText(i, "QEMU适配") # QEMU适配
            break

        i += 1

def translateVmExistsEN(window):
    window.label.setText(
        "虚拟机名已存在。"
        ) # Sorry, but a VM with this name already exists.

    window.label_2.setText(
        "请选择删除该虚拟机或更换一个新名字。"
        ) # Please consider either deleting that VM or thinking of a new name.

    window.pushButton.setText("OK") # OK

def translateVhdExistsEN(window):
    # The dialog which used to use this translation function is no longer in use.
    window.label.setText(
        "磁盘名已存在。"
        ) # Sorry, but the disk you want to create is already existant.

    window.label_2.setText("保留或者覆盖？") # Do you want to keep or overwrite it?

    window.pushButton.setText("覆盖") # Overwrite
    window.pushButton_2.setText("保留") # Keep

def translateSettingsPendingEN(window):
    # The dialog which used to use this translation function is no longer in use.
    window.label.setText("QEMU路径未配置。")
    window.label_2.setText("请先配置QEMU路径后继续操作。")

    window.pushButton.setText("确定") # OK

def translateVmTooNewEN(window):
    window.label.setText(
        "版本不兼容。"
        ) # This VM is made with a version of EmuGUI that is too new. Please use a later version!

    window.pushButton.setText("确定") # OK

def translateQemuSysMissingEN(window, arch):
    window.label.setText(
        f"\"qemu-system-{arch}\" 未配置"
        ) # Sorry but EmuGUI is not configured for using \"qemu-system-{arch}\" yet.\nThis component however is necessary to start this virtual machine.\nPlease go to Settings/QEMU to solve this issue.

    window.pushButton.setText("确定") # OK

def translateQemuImgMissingEN(window):
    window.label.setText(
        "\"qemu-img\" 未配置"
        ) # Sorry but EmuGUI is not configured for using \"qemu-img\" yet.\nThis component however is necessary to create or edit virtual machines.\nPlease go to Settings/QEMU to solve this issue.

    window.pushButton.setText("确定") # OK

def translateEditVMEN(window, vmname):
    window.setWindowTitle(f"EmuGUI - 编辑 {vmname}")

    # Buttons on all tabs
    window.btn_cancel.setText("取消") # 取消
    window.btn_ok.setText("确定") # OK

    # Tab names
    window.tabWidget.setTabText(0, "通用") # General
    window.tabWidget.setTabText(1, "机器") # Machine
    window.tabWidget.setTabText(2, "虚拟磁盘") # Virtual hard disks
    window.tabWidget.setTabText(3, "外设") # Peripherals
    window.tabWidget.setTabText(4, "BIOS") # BIOS
    window.tabWidget.setTabText(5, "镜像") # Peripherals
    window.tabWidget.setTabText(6, "额外组件") # Additional components

    # Translations for General tab
    window.lbl_name.setText("名称") # Name
    window.lbl_arch.setText("架构") # Architecture

    # Translations for Machine tab
    window.lbl_cpu.setText("处理器") # CPU
    window.lbl_machine.setText("机器") # Machine
    window.lbl_ram.setText("内存大小(MB)") # RAM in MB

    i = 0

    while i < window.cb_cpu.count():
        if window.cb_cpu.itemText(i) == "QEMU适配" or window.cb_cpu.itemText(i) == "QEMU überlassen":
            window.cb_cpu.setItemText(i, "QEMU适配") # QEMU适配
            break

        i += 1

    i = 0

    while i < window.cb_machine.count():
        if window.cb_machine.itemText(i) == "QEMU适配" or window.cb_machine.itemText(i) == "QEMU überlassen":
            window.cb_machine.setItemText(i, "QEMU适配") # QEMU适配
            break

        i += 1

    # Translations for VHD tab
    window.lbl_vhdu.setText("虚拟硬盘路径") # VHD path
    window.lbl_vhdf.setText("虚拟硬盘格式") # VHD file format
    window.lbl_maxsize.setText("最大空间") # Maximum size
    window.btn_vhdp.setText("浏览") # 浏览
    
    # Combobox for VHD usage
    i = 0

    while i < window.cb_vhdu.count():
        if window.cb_vhdu.itemText(i) == "Create a new virtual hard drive":
            window.cb_vhdu.setItemText(i, "新建虚拟硬盘") # Create a new virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdu.count():
        if window.cb_vhdu.itemText(i) == "Add an existing virtual hard drive":
            window.cb_vhdu.setItemText(i, "添加已有虚拟硬盘") # Add an existing virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdu.count():
        if window.cb_vhdu.itemText(i) == "Don't add a virtual hard drive":
            window.cb_vhdu.setItemText(i, "不使用虚拟硬盘") # Don't add a virtual hard drive
            break

        i += 1

    window.lbl_cdc1.setText("光盘控制器 1") # CD controller 1
    window.lbl_cdc2.setText("光盘控制器 2") # CD controller 2

    i = 0

    while i < window.cb_cdc1.count():
        if window.cb_cdc1.itemText(i) == "QEMU适配" or window.cb_cdc1.itemText(i) == "QEMU überlassen":
            window.cb_cdc1.setItemText(i, "QEMU适配") # QEMU适配
            break

        i += 1

    i = 0

    while i < window.cb_cdc2.count():
        if window.cb_cdc2.itemText(i) == "QEMU适配" or window.cb_cdc2.itemText(i) == "QEMU überlassen":
            window.cb_cdc2.setItemText(i, "QEMU适配") # QEMU适配
            break

        i += 1

    window.lbl_hddc.setText("硬盘控制器") # HDD controller

    i = 0

    while i < window.cb_hddc.count():
        if window.cb_hddc.itemText(i) == "QEMU适配" or window.cb_hddc.itemText(i) == "QEMU überlassen":
            window.cb_hddc.setItemText(i, "QEMU适配") # QEMU适配
            break

        i += 1

    # Translations for Peripherals tab
    window.lbl_mouse.setText("鼠标类型") # Mouse type
    window.lbl_kbdtype.setText("键盘类型") # Keyboard type
    
    # Translations for BIOS tab
    # Location of external BIOS file (Leave empty to use the default BIOS)
    window.lbl_biosloc.setText("BIOS文件位置(留空以使用默认BIOS)")
    window.lbl_biosf.setText("外部BIOS文件") # External BIOS file
    window.btn_biosf.setText("浏览") # 浏览

    # Translations for Linux tab
    window.lbl_kernel.setText("镜像文件") # Linux kernel
    window.lbl_initrd.setText("临时文件系统") # Linux initrd image
    window.lbl_cmd.setText("命令行参数") # Linux cmd arguments
    window.btn_kernel.setText("浏览") # 浏览
    window.btn_initrd.setText("浏览") # 浏览

    # Translations for Additional components tab
    window.lbl_vga.setText("显示") # VGA
    window.lbl_net.setText("网络") # Network adapter
    window.lbl_sound.setText("声卡") # Sound card
    window.lbl_addargs.setText("额外参数(可选)") # Additional arguments (if necessary)
    window.lbl_cpuc.setText("处理器核心数") # CPU cores
    window.chb_usb.setText("添加USB支持") # Add USB support
    window.lbl_accel.setText("加速器") # Acceleration

def translateErrDialogEN(window, errcode):
    window.setWindowTitle(f"EmuGUI - 错误")
    
    if errcode.startswith("C"):
        window.label.setText("发生了一个错误，需要重启。") # EmuGUI encountered a critical error and needs to be closed.

    elif errcode.startswith("E"):
        window.label.setText("发生了一个错误。") # EmuGUI encountered an error.

    elif errcode.startswith("W"):
        window.label.setText("发生了一个警告。") # EmuGUI has to warn you.

    else:
        window.label.setText("发生了一个报告") # EmuGUI has something to say.

    window.label_2.setText("错误码: " + errcode) # Error Code:

    window.label_3.setText(
        "如果此错误多次出现，请联系您的管理员。"
        ) # If this error occurs multiple times, contact your administrator and/or ask for help on the EmuGUI Discord Server or on its GitHub repository.
    
    window.pushButton.setText("确定") # OK
