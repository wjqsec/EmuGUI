def generate_dev_config(dev_name):
    if dev_name == "ich9-usb-ehci1" or dev_name == "ich9-usb-ehci2" or dev_name == "ich9-usb-uhci1" or dev_name == "ich9-usb-uhci2" or dev_name == "piix3-usb-uhci" or dev_name == "piix4-usb-uhci" or dev_name == "usb-ehci":
        return [
            ["acpi 索引","acpi-index",0],
            ["最大帧数","maxframes",128],
            ["多功能控制","multifunction",False],
            ["最大跳数缓存大小","x-max-bounce-buffer-size",4096],
            ["开户下一功能","x-pcie-ari-nextfn-1",False],
            ["开启错误掩码","x-pcie-err-unc-mask",True],
            ["开启拓展标签","x-pcie-ext-tag",True],
            ["开启拓展功能初始化","x-pcie-extcap-init",True],
            ["开启连接dllla","x-pcie-lnksta-dllla",True]
        ]
    elif dev_name == "nec-usb-xhci":
        return [
            ["acpi 索引","acpi-index",0],
            ["开启指令映射","conditional-intr-mapping",False],
            ["指令数","intrs",16],
            ["多功能控制","multifunction",False],
            ["p2","p2",4],
            ["p3","p3",4],
            ["最大跳数缓存大小","x-max-bounce-buffer-size",4096],
            ["开户下一功能","x-pcie-ari-nextfn-1",False],
            ["开启错误掩码","x-pcie-err-unc-mask",True],
            ["开启拓展标签","x-pcie-ext-tag",True],
            ["开启拓展功能初始化","x-pcie-extcap-init",True],
            ["开启连接dllla","x-pcie-lnksta-dllla",True]
        ]
    elif dev_name == "qemu-xhci":
        return [
            ["acpi 索引","acpi-index",0],
            ["开启指令映射","conditional-intr-mapping",False],
            ["MSI","msi", ["auto","on","off"]],
            ["MSIX","msix",["auto","on","off"]],
            ["多功能控制","multifunction",False],
            ["p2","p2",4],
            ["p3","p3",4],
            ["最大跳数缓存大小","x-max-bounce-buffer-size",4096],
            ["开户下一功能","x-pcie-ari-nextfn-1",False],
            ["开启错误掩码","x-pcie-err-unc-mask",True],
            ["开启拓展标签","x-pcie-ext-tag",True],
            ["开启拓展功能初始化","x-pcie-extcap-init",True],
            ["开启连接dllla","x-pcie-lnksta-dllla",True]
        ]
    elif dev_name == "ati-vga":
        return [
            ["vga内存 (MB)","vgamem_mb",16],
            ["pixman","x-pixman",[3,1,2]],
            ["硬件光标","guest_hwcursor",False],
            ["模型","model",""],
            ["acpi 索引","acpi-index",0],
            ["多功能控制","multifunction",False],
            ["最大跳数缓存大小","x-max-bounce-buffer-size",4096],
            ["开户下一功能","x-pcie-ari-nextfn-1",False],
            ["开启错误掩码","x-pcie-err-unc-mask",True],
            ["开启拓展标签","x-pcie-ext-tag",True],
            ["开启拓展功能初始化","x-pcie-extcap-init",True],
            ["开启连接dllla","x-pcie-lnksta-dllla",True]
        ]
    elif dev_name == "cirrus-vga":
        return [
            ["vga内存 (MB)","vgamem_mb",16],
            ["acpi 索引","acpi-index",0],
            ["多功能控制","multifunction",False],
            ["最大跳数缓存大小","x-max-bounce-buffer-size",4096],
            ["开户下一功能","x-pcie-ari-nextfn-1",False],
            ["开启错误掩码","x-pcie-err-unc-mask",True],
            ["开启拓展标签","x-pcie-ext-tag",True],
            ["开启拓展功能初始化","x-pcie-extcap-init",True],
            ["开启连接dllla","x-pcie-lnksta-dllla",True]
        ]
    elif dev_name == "VGA":
        return [
            ["开启大端帧缓存","big-endian-framebuffer",False],
            ["开启ed编号","edid",True],
            ["开启mmio","mmio",True],
            ["开启qemu拓展寄存器","qemu-extended-regs",True],
            ["刷新率","refresh_rate",0],
            ["vga内存 (MB)","vgamem_mb",16],
            ["acpi 索引","acpi-index",0],
            ["多功能控制","multifunction",False],
            ["最大跳数缓存大小","x-max-bounce-buffer-size",4096],
            ["开户下一功能","x-pcie-ari-nextfn-1",False],
            ["开启错误掩码","x-pcie-err-unc-mask",True],
            ["开启拓展标签","x-pcie-ext-tag",True],
            ["开启拓展功能初始化","x-pcie-extcap-init",True],
            ["开启连接dllla","x-pcie-lnksta-dllla",True],
            ["最大x","xmax",0],
            ["x分辨","xres",0],
            ["最大y","ymax",0],
            ["y分辨","yres",0]
        ]
    elif dev_name == "virtio-gpu-pci":
        return [
            ["启用AER", "aer", False],
            ["启用ATS", "ats", False],
            ["启用EDID", "edid", True],
            ["最大输出数", "max_outputs", 1],
            ["最大主机内存", "max_hostmem", 268435456],
            ["启用IOMMU平台", "iommu_platform", False],
            ["启用压缩","packed",False],
            ["队列重启","queue_reset",True],
            ["X分辨率", "xres", 1280],
            ["Y分辨率", "yres", 800],
            ["最大Bounce缓冲区大小", "x-max-bounce-buffer-size", 4096],
            ["开启通知","notify_on_empty",True]
        ]
    elif dev_name == "AC97":
        return [
            ["音频后端ID", "audiodev", ""],
            ["ACPI索引", "acpi-index", 0],
            ["多功能设备", "multifunction", False],
            ["最大Bounce缓冲区大小", "x-max-bounce-buffer-size", 4096],
            ["PCIe ARI下一个函数", "x-pcie-ari-nextfn-1", False],
            ["PCIe不可恢复错误掩码", "x-pcie-err-unc-mask", True],
            ["PCIe扩展标签", "x-pcie-ext-tag", True],
            ["PCIe扩展能力初始化", "x-pcie-extcap-init", True],
            ["PCIe链路状态DLLLA", "x-pcie-lnksta-dllla", True],
        ]
    elif dev_name == "adlib":  #BUS ISA
        return [
            ["音频后端ID", "audiodev", ""],
            ["采样频率", "freq", 44100],
            ["I/O基址", "iobase", 544],
        ]
    elif dev_name == "cs4231a": #BUS ISA
        return [
            ["音频后端ID", "audiodev", ""],
            ["DMA通道", "dma", 3],
            ["I/O基址", "iobase", 1332],
            ["中断号", "irq", 9],
        ]
    elif dev_name == "ES1370":
        return [
            ["音频后端ID", "audiodev", ""],
            ["ACPI索引", "acpi-index", 0],
            ["多功能设备", "multifunction", False],
            ["最大Bounce缓冲区大小", "x-max-bounce-buffer-size", 4096],
            ["PCIe ARI下一个函数", "x-pcie-ari-nextfn-1", False],
            ["PCIe不可恢复错误掩码", "x-pcie-err-unc-mask", True],
            ["PCIe扩展标签", "x-pcie-ext-tag", True],
            ["PCIe扩展能力初始化", "x-pcie-extcap-init", True],
            ["PCIe链路状态DLLLA", "x-pcie-lnksta-dllla", True],
        ]
    elif dev_name == "intel-hda":
        return [
            ["ACPI索引", "acpi-index", 0],
            ["调试","debug",0],
            ["MSI","msi",["auto","on","off"]],
            ["多功能设备", "multifunction", False],
            ["最大Bounce缓冲区大小", "x-max-bounce-buffer-size", 4096],
            ["PCIe ARI下一个函数", "x-pcie-ari-nextfn-1", False],
            ["PCIe不可恢复错误掩码", "x-pcie-err-unc-mask", True],
            ["PCIe扩展标签", "x-pcie-ext-tag", True],
            ["PCIe扩展能力初始化", "x-pcie-extcap-init", True],
            ["PCIe链路状态DLLLA", "x-pcie-lnksta-dllla", True],
        ]
    elif dev_name == "drive":
        return [
            ["标识符","id",""],
            ["文件路径","file",""],
            ["格式","format",["raw","qcow2","qed","luks","vdi"]],
            ["只读","readonly",["on","off"]],
        ]
    elif dev_name == "dc390":
        return [
            ["acpi 索引","acpi-index",0],
            ["多功能控制","multifunction",False],
            ["最大跳数缓存大小","x-max-bounce-buffer-size",4096],
            ["开户下一功能","x-pcie-ari-nextfn-1",False],
            ["开启错误掩码","x-pcie-err-unc-mask",True],
            ["开启拓展标签","x-pcie-ext-tag",True],
            ["开启拓展功能初始化","x-pcie-extcap-init",True],
            ["开启连接dllla","x-pcie-lnksta-dllla",True]
        ]
    # elif dev_name == "floppy":  #floppy-bus
    #     return [
    #         ["账号失败","account-failed",["auto","on","off"]],
    #         ["账号失效","account-invalid",["auto","on","off"]],
    #         ["默认后端","backend_defaults",["auto","on","off"]],
    #         ["丢弃粒度","discard_granularity",4294967295],
    #         ["硬盘类型","drive-type",["auto", "144","288," "120", "none"]],
    #         ["对应硬盘ID","drive",""],
    #         ["逻辑块大小","logical_block_size",0],
    #         ["最小io大小","min_io_size",0],
    #         ["最佳io大小","opt_io_size",0],
    #         ["物理块大小","physical_block_size",0],
    #         ["读写共享","share-rw",False],
    #         ["缓存写","write-cache",["auto","on","off"]]
    #     ]
    elif dev_name == "ide-cd" or dev_name == "ide-hd": #bus ide
        return [
            ["账号失败","account-failed",["auto","on","off"]],
            ["账号失效","account-invalid",["auto","on","off"]],
            ["默认后端","backend_defaults",["auto","on","off"]],
            ["丢弃粒度","discard_granularity",4294967295],
            ["对应硬盘ID","drive",""],
            ["逻辑块大小","logical_block_size",0],
            ["最小io大小","min_io_size",0],
            ["最佳io大小","opt_io_size",0],
            ["物理块大小","physical_block_size",0],
            ["读写共享","share-rw",False],
            ["缓存写","write-cache",["auto","on","off"]]
        ]
    elif dev_name == "isa-fdc": #bus-isa
        return [
            ["启动索引A","bootindexA",0],
            ["启动索引B","bootindexB",0],
            ["DMA","dma",2],
            ["IO基地址","iobase",1008],
            ["中断","irq",6],
        ]
    elif dev_name == "isa-ide": #bus-isa
        return [
            ["IO基地址2","iobase2",1014],
            ["IO基地址","iobase",496],
            ["中断","irq",14]
        ]
    elif dev_name == "sd-card": #bus sd-bus
        return [
            ["硬盘路径","drive",""],
            ["版本信息","spec_version",3]
        ]
    elif dev_name == "usb-uas": #bus usb-bus
        return [
            ["连接","attached",False],
            ["scsi序号","log-scsi-req",0],
            ["开启msos描述","msos-desc",True],
            ["pcap","pcap",""],
            ["端口","port",""],
            ["串口","serial",""]
        ]
    elif dev_name == "virtio-blk-pci":
        return [
            ["账号失败","account-failed",["auto","on","off"]],
            ["账号失效","account-invalid",["auto","on","off"]],
            ["默认后端","backend_defaults",["auto","on","off"]],
            ["丢弃粒度","discard_granularity",4294967295],
            ["对应硬盘ID","drive",""],
            ["逻辑块大小","logical_block_size",0],
            ["最小io大小","min_io_size",0],
            ["最佳io大小","opt_io_size",0],
            ["物理块大小","physical_block_size",0],
            ["读写共享","share-rw",False],
            ["缓存写","write-cache",["auto","on","off"]]
        ]
    elif dev_name == "netdev":
        return [
            ["类型","type",["tap"]],
            ["标识符","id",""],
            ["Host网卡","ifname",""]
        ]
    elif dev_name == "e1000":
        return [
            ["ACPI索引", "acpi-index", 0],
            ["初始化VET标志", "init-vet", True],
            ["MAC地址", "mac", "52:54:00:12:34:56"],
            ["迁移TSO属性", "migrate_tso_props", True],
            ["多功能设备", "multifunction", False],
            ["网络后端ID", "netdev", ""],
            ["最大Bounce缓冲区大小", "x-max-bounce-buffer-size", 4096],
            ["PCIe ARI下一个函数", "x-pcie-ari-nextfn-1", False],
            ["PCIe不可恢复错误掩码", "x-pcie-err-unc-mask", True],
            ["PCIe扩展标签", "x-pcie-ext-tag", True],
            ["PCIe扩展能力初始化", "x-pcie-extcap-init", True],
            ["PCIe链路状态DLLLA", "x-pcie-lnksta-dllla", True],
        ]
    elif dev_name == "e1000e":
        return [
            ["ACPI索引", "acpi-index", 0],
            ["初始化VET标志", "init-vet", True],
            ["MAC地址", "mac", "52:54:00:12:34:56"],
            ["迁移TIMADJ属性", "migrate-timadj", True],
            ["多功能设备", "multifunction", False],
            ["网络后端ID", "netdev", ""],
            ["最大Bounce缓冲区大小", "x-max-bounce-buffer-size", 4096],
            ["PCIe ARI下一个函数", "x-pcie-ari-nextfn-1", False],
            ["PCIe不可恢复错误掩码", "x-pcie-err-unc-mask", True],
            ["PCIe扩展标签", "x-pcie-ext-tag", True],
            ["PCIe扩展能力初始化", "x-pcie-extcap-init", True],
            ["PCIe链路状态DLLLA", "x-pcie-lnksta-dllla", True],
        ]
    elif dev_name == "i82550" or dev_name == "i82558a" or dev_name == "igb" or dev_name == "ne2k_pci" or dev_name == "rtl8139":
        return [
            ["ACPI索引", "acpi-index", 0],
            ["MAC地址", "mac", "52:54:00:12:34:56"],
            ["多功能设备", "multifunction", False],
            ["网络后端ID", "netdev", ""],
            ["最大Bounce缓冲区大小", "x-max-bounce-buffer-size", 4096],
            ["PCIe ARI下一个函数", "x-pcie-ari-nextfn-1", False],
            ["PCIe不可恢复错误掩码", "x-pcie-err-unc-mask", True],
            ["PCIe扩展标签", "x-pcie-ext-tag", True],
            ["PCIe扩展能力初始化", "x-pcie-extcap-init", True],
            ["PCIe链路状态DLLLA", "x-pcie-lnksta-dllla", True],
        ]
    elif dev_name == "virtio-net-pci":
        return [
            ["ACPI索引", "acpi-index", 0],
            ["MAC地址", "mac", "52:54:00:12:34:56"],
            ["Hash IPV4","hash-ipv4",["auto","on","off"]],
            ["Hash IPV6","hash-ipv6",["auto","on","off"]],
            ["Hash TCP4","hash-tcp4",["auto","on","off"]],
            ["Hash TCP6","hash-tcp6",["auto","on","off"]],
            ["主机MTU大小","host_mtu",0],
            ["多功能设备", "multifunction", False],
            ["网络后端ID", "netdev", ""],
            ["最大Bounce缓冲区大小", "x-max-bounce-buffer-size", 4096],
            ["PCIe ARI下一个函数", "x-pcie-ari-nextfn-1", False],
            ["PCIe不可恢复错误掩码", "x-pcie-err-unc-mask", True],
            ["PCIe扩展标签", "x-pcie-ext-tag", True],
            ["PCIe扩展能力初始化", "x-pcie-extcap-init", True],
            ["PCIe链路状态DLLLA", "x-pcie-lnksta-dllla", True],
        ]
    elif dev_name == "ne2k_isa":  # bus isa
        return [
            ["IO基地址", "iobase", 768],
            ["中断", "irq", 9],
            ["MAC地址","mac","52:54:00:12:34:56"],
            ["网络后端ID","netdev",""],
        ]
    elif dev_name == "usb-net": # bus usb-bus
        return [
            ["MAC地址","mac","52:54:00:12:34:56"],
            ["网络后端ID","netdev",""],
            ["开启msos描述","msos-desc",True],
            ["pcap","pcap",""],
            ["端口","port",""],
            ["串口","serial",""]
        ]
    elif dev_name == "chardev":
        return [
            ["类型","type",["stdio","file","pty"]],
            ["标识符","id",""],
            ["文件路径","path",""]
        ]
    elif dev_name == "i8042":
        return [
            ["键盘IRQ号", "kbd-irq", 1],
            ["鼠标IRQ号", "mouse-irq", 12],
        ]
    elif dev_name == "pci-serial":
        return [
            ["acpi 索引","acpi-index",0],
            ["后端字符设备","chardev",""],
            ["波特率","baudbase",115200],
            ["多功能控制","multifunction",False],
            ["最大跳数缓存大小","x-max-bounce-buffer-size",4096],
            ["开户下一功能","x-pcie-ari-nextfn-1",False],
            ["开启错误掩码","x-pcie-err-unc-mask",True],
            ["开启拓展标签","x-pcie-ext-tag",True],
            ["开启拓展功能初始化","x-pcie-extcap-init",True],
            ["开启连接dllla","x-pcie-lnksta-dllla",True]
        ]
    elif dev_name == "tpci200":
        return [
            ["acpi 索引","acpi-index",0],
            ["多功能控制","multifunction",False],
            ["最大跳数缓存大小","x-max-bounce-buffer-size",4096],
            ["开户下一功能","x-pcie-ari-nextfn-1",False],
            ["开启错误掩码","x-pcie-err-unc-mask",True],
            ["开启拓展标签","x-pcie-ext-tag",True],
            ["开启拓展功能初始化","x-pcie-extcap-init",True],
            ["开启连接dllla","x-pcie-lnksta-dllla",True]
        ]
    elif dev_name == "usb-serial": #bus usb-bus
        return [
            ["后端字符设备","chardev",""],
            ["开启msos描述","msos-desc",True],
            ["pcap","pcap",""],
            ["端口","port",""],
            ["串口","serial",""]
        ]
    elif dev_name == "virtio-serial-pci":
        return [
            ["ACPI索引", "acpi-index", 0],
            ["启用AER", "aer", False],
            ["任意布局", "any_layout", True],
            ["启用ATS", "ats", False],
            ["类代码", "class", 0],
            ["启动标志支持", "use-started", True],
            ["中断向量数", "vectors", 2],
            ["最大Bounce缓冲区大小", "x-max-bounce-buffer-size", 4096],
            ["PCIe ARI下一个函数", "x-pcie-ari-nextfn-1", False],
            ["PCIe设备错误初始化", "x-pcie-deverr-init", True],
            ["PCIe不可恢复错误掩码", "x-pcie-err-unc-mask", True],
            ["PCIe扩展标签", "x-pcie-ext-tag", True],
            ["PCIe扩展能力初始化", "x-pcie-extcap-init", True],
            ["PCIe功能级复位", "x-pcie-flr-init", True],
            ["PCIe链路控制初始化", "x-pcie-lnkctl-init", True],
            ["PCIe链路状态DLLLA", "x-pcie-lnksta-dllla", True],
            ["PCIe电源管理初始化", "x-pcie-pm-init", True],
        ]
    
def generate_dev_header(dev_name):
    if dev_name == "drive":
        return ""
    if dev_name == "netdev":
        return ""
    if dev_name == "chardev":
        return ""
    return f'''
    dev = qdev_new("{dev_name}");
    '''

def generate_dev_body(dev_name, dev_config):
    source_add = ""
    if dev_name == "drive":
        source_add += f'''
    opts = drive_add(IF_NONE, -1, "{dev_config[1][2]}", "format={dev_config[2][2][0]},readonly={dev_config[3][2][0]},id={dev_config[0][2]}");
    pnor = drive_new(opts, IF_NONE, &error_fatal);
    blkbackend = blk_by_legacy_dinfo(pnor);
    '''
        return source_add
    if dev_name == "netdev":
        source_add += f'''
    arg = "{dev_config[0][2][0]},id={dev_config[1][2]},ifname={dev_config[2][2]},script=no,downscript=no";
    opts = qemu_opts_parse(&qemu_netdev_opts, arg, 1, &error_fatal);
    netdev_add(opts, &error_fatal);
    '''
        return source_add
    if dev_name == "chardev":
        source_add += f'''
    arg = "{dev_config[0][2][0]},id={dev_config[1][2]},path={dev_config[2][2]}";
    opts = qemu_opts_parse(&qemu_chardev_opts, arg, 1, &error_fatal);
    qemu_chr_new_from_opts(opts, NULL, &error_fatal);
    '''
        return source_add
    for config in dev_config:
        if type(config[2]) is int:
            source_add += f"qdev_prop_set_uint64(dev, \"{config[1]}\", {config[2]});\n"
        elif type(config[2]) is bool:
            source_add += f"qdev_prop_set_bit(dev, \"{config[1]}\", {str(config[2]).lower()});\n"
        elif type(config[2]) is str:
            source_add += f"qdev_prop_set_string(dev, \"{config[1]}\", \"{config[2]}\");\n"
        elif type(config[2]) is list:
            if type(config[2][0]) is int:
                source_add += f"qdev_prop_set_uint64(dev, \"{config[1]}\", {config[2][0]});\n"
            elif type(config[2][0]) is str:
                source_add += f"qdev_prop_set_string(dev, \"{config[1]}\", \"{config[2][0]}\");\n"  
    return source_add

def generate_dev_tail(dev_name):
    if dev_name == "drive":
        return ""
    if dev_name == "netdev":
        return ""
    if dev_name == "chardev":
        return ""
    if get_dev_bus_type(dev_name) == "isa":
        return '''
    qdev_realize_and_unref(dev, isabus, &error_fatal);
    '''
    if get_dev_bus_type(dev_name) == "ide":
        return '''
    qdev_realize_and_unref(dev, idebus, &error_fatal);
    '''
    if get_dev_bus_type(dev_name) == "pci":
        return '''
    qdev_realize_and_unref(dev, pcibus, &error_fatal);
    '''


def get_dev_bus_type(dev_name):
    if dev_name == "ne2k_isa" or dev_name == "isa-ide" or dev_name == "isa-fdc" or dev_name == "cs4231a" or dev_name == "adlib":
        return "isa"
    if dev_name == "ide-cd" or dev_name == "ide-hd":
        return "ide"
    return "pci"

def get_devices_info():
    return {
        "i386" : {
            "USB" : [
                ["ich9-usb-ehci1", "pci"],
                ["ich9-usb-ehci2", "pci"],
                ["ich9-usb-uhci1", "pci"],
                ["ich9-usb-uhci2", "pci"],
                ["piix3-usb-uhci", "pci"],
                ["piix4-usb-uhci", "pci"],
                ["usb-ehci", "pci"],
                ["nec-usb-xhci", "pci"],
                ["qemu-xhci", "pci"],
            ],
            "串口" : [
                ["chardev", "pci"],
                ["i8042", "pci"],
                ["pci-serial", "pci"],
                ["tpci200", "pci"],
                ["usb-serial", "usb"],
                ["virtio-serial-pci", "pci"],
            ],
            "网卡" : [
                ["netdev", "pci"],
                ["e1000", "pci"],
                ["e1000e", "pci"],
                ["i82550", "pci"],
                ["i82558a", "pci"],
                ["igb", "pci"],
                ["ne2k_pci", "pci"],
                ["rtl8139", "pci"],
                ["virtio-net-pci", "pci"],
                ["ne2k_isa", "isa"],
                ["usb-net", "usb"],
            ],
            "存储" : [
                ["drive", "pci"],
                ["dc390", "pci"],
                ["ide-cd", "ide"],
                ["ide-hd", "ide"],
                ["isa-fdc", "isa"],
                ["isa-ide", "isa"],
                # ["sd-card", "sd"],
                ["usb-uas", "usb"],
                ["virtio-blk-pci", "pci"],
            ],
            "显示设备" : [
                ["ati-vga", "pci"],
                ["cirrus-vga", "pci"],
                ["VGA", "pci"],
                ["virtio-gpu-pci", "pci"],
            ],
            "声卡" : [
                ["adlib", "isa"],
                ["cs4231a", "isa"],
                ["ES1370", "pci"],
                ["intel-hda", "pci"],
            ],
            "自定义" : [
                ["自定义", "pci"],
            ]
        },
        "arm" : {
            "USB" : [

            ],
            "串口" : [

            ],
            "网卡" : [

            ],
            "存储" : [

            ],
            "显示设备" : [

            ],
            "声卡" : [

            ],
            "自定义" : [

            ]
        },
        "ppc" : {
            "USB" : [
                
            ],
            "串口" : [

            ],
            "网卡" : [

            ],
            "存储" : [

            ],
            "显示设备" : [

            ],
            "声卡" : [

            ],
            "自定义" : [

            ]
        },
        "mips" : {
            "USB" : [
                
            ],
            "串口" : [

            ],
            "网卡" : [

            ],
            "存储" : [

            ],
            "显示设备" : [

            ],
            "声卡" : [

            ],
            "自定义" : [

            ]
        },
        "riscv" : {
            "USB" : [

            ],
            "串口" : [

            ],
            "网卡" : [

            ],
            "存储" : [

            ],
            "显示设备" : [

            ],
            "声卡" : [

            ],
            "自定义" : [

            ]
        }
    }

def get_devs_by_arch(arch):
    info = get_devices_info()
    return info[arch]

def get_bus_by_arch_dev(arch, dev_name):
    info = get_devices_info()
    dev_types = info[arch]
    for dev_type, devs in dev_types.items():
        for dev in devs:
            if dev[0] == dev_name:
                return dev[1]
    return None

def get_init_buses_by_arch(arch):
    init_buses = {
        "i386" : 
            ["sysbus", "pci", "isa", "ide"]
        ,
        "arm" : [

        ],
        "ppc" : [

        ],
        "mips" : [

        ],
        "riscv" : [

        ],
    }
    return init_buses[arch]

def validate_bus_type(arch, dev_name, assgined_bus):
    valid_bus = get_bus_by_arch_dev(arch, dev_name)
    if valid_bus == assgined_bus:
        return True
    return False
    