pci_configs = [
    ["acpi 索引","acpi-index",0],
    ["多功能控制","multifunction",False],
    ["最大跳数缓存大小","x-max-bounce-buffer-size",4096],
    ["开户下一功能","x-pcie-ari-nextfn-1",False],
    ["开启错误掩码","x-pcie-err-unc-mask",True],
    ["开启拓展标签","x-pcie-ext-tag",True],
    ["开启连接dllla","x-pcie-lnksta-dllla",True]
]
def get_devices_info(dev_name):
    if dev_name == "ich9-usb-ehci1" or dev_name == "ich9-usb-ehci2" or dev_name == "ich9-usb-uhci1" or dev_name == "ich9-usb-uhci2" or dev_name == "piix3-usb-uhci" or dev_name == "piix4-usb-uhci" or dev_name == "usb-ehci":
        return "pci", "usb", [
            ["最大帧数","maxframes",128],
        ] + pci_configs
    elif dev_name == "nec-usb-xhci":
        return "pci", "usb", [
            ["开启指令映射","conditional-intr-mapping",False],
            ["指令数","intrs",16],
            ["卡槽数","slots",64],
        ] + pci_configs
    elif dev_name == "qemu-xhci":
        return "pci", "usb", [
            ["开启指令映射","conditional-intr-mapping",False],
            ["MSI","msi", ["auto","on","off"]],
            ["MSIX","msix",["auto","on","off"]],
        ] + pci_configs
    elif dev_name == "ati-vga":
        return "pci", None, [
            ["vga内存 (MB)","vgamem_mb",16],
            ["pixman","x-pixman",[3,1,2]],
            ["硬件光标","guest_hwcursor",False],
            ["模型","model",""],
        ] + pci_configs
    elif dev_name == "cirrus-vga":
        return "pci", None, [
            ["vga内存 (MB)","vgamem_mb",16],
        ] + pci_configs
    elif dev_name == "VGA":
        return "pci", None, [
            ["开启大端帧缓存","big-endian-framebuffer",False],
            ["开启ed编号","edid",True],
            ["开启mmio","mmio",True],
            ["开启qemu拓展寄存器","qemu-extended-regs",True],
            ["刷新率","refresh_rate",0],
            ["vga内存 (MB)","vgamem_mb",16],
            ["最大x","xmax",0],
            ["x分辨","xres",0],
            ["最大y","ymax",0],
            ["y分辨","yres",0]
        ]
    elif dev_name == "virtio-gpu-pci":
        return "pci", "virtiop-gpu",[
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
            ["开启通知","notify_on_empty",True]
        ] + pci_configs
    elif dev_name == "virtio-gpu-device":
        return "virtiop-gpu", None,[
            ["启用任意布局", "any_layout", True],
            ["启用blob", " blob", False],
            ["启用edid", "edid", True],
            ["启用事件索引", "event_idx", True],
            ["X分辨率", "xres", 1289],
            ["Y分辨率", "yres", 800],
            ["启用压缩", "packed", False],
            ["启用间接描述", "indirect_desc", True],
        ]
    elif dev_name == "AC97":
        return "pci", None, [
            ["音频后端ID", "audiodev", ""],
        ] + pci_configs
    elif dev_name == "adlib":  #BUS ISA
        return "isa", None, [
            ["音频后端ID", "audiodev", ""],
            ["采样频率", "freq", 44100],
            ["I/O基址", "iobase", 544],
        ]
    elif dev_name == "cs4231a": #BUS ISA
        return "isa", None, [
            ["音频后端ID", "audiodev", ""],
            ["DMA通道", "dma", 3],
            ["I/O基址", "iobase", 1332],
            ["中断号", "irq", 9],
        ]
    elif dev_name == "ES1370":
        return "pci", None, [
            ["音频后端ID", "audiodev", ""],
        ] + pci_configs
    elif dev_name == "intel-hda":
        return "pci", None, [
            ["调试","debug",0],
            ["MSI","msi",["auto","on","off"]],
        ] + pci_configs
    elif dev_name == "drive":
        return "backend", None, [
            ["标识符","id",""],
            ["文件路径","file",""],
            ["格式","format",["raw","qcow2","qed","luks","vdi"]],
            ["只读","readonly",["on","off"]],
        ]
    elif dev_name == "dc390":
        return "pci", None, [
        ] + pci_configs
    elif dev_name == "ide-cd" or dev_name == "ide-hd": #bus ide
        return "ide", None, [
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
        return "isa", None, [
            ["启动索引A","bootindexA",0],
            ["启动索引B","bootindexB",0],
            ["DMA","dma",2],
            ["IO基地址","iobase",1008],
            ["中断","irq",6],
        ]
    elif dev_name == "isa-ide": #bus-isa
        return "ide", None, [
            ["IO基地址2","iobase2",1014],
            ["IO基地址","iobase",496],
            ["中断","irq",14]
        ]
    elif dev_name == "sd-card": #bus sd-bus
        return "sd", None, [
            ["硬盘路径","drive",""],
            ["版本信息","spec_version",3]
        ]
    elif dev_name == "usb-uas": #bus usb-bus
        return "usb", None, [
            ["连接","attached",False],
            ["scsi序号","log-scsi-req",0],
            ["开启msos描述","msos-desc",True],
            ["pcap","pcap",""],
            ["端口","port",""],
            ["串口","serial",""]
        ]
    elif dev_name == "virtio-blk-pci":
        return "pci", "virtio-blk",[
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
    elif dev_name == "virtio-blk-device":
        return "virtio-blk", None, [
            ["硬盘路径","drive",""],
            ["启用任意布局", "any_layout", True],
            ["配置WCE","config-wce", True],
            ["逻辑块大小","logical_block_size",0],
            ["最大清零扇区大小","max-write-zeroes-sectors",4194303],
            ["队列大小","queue-size", 256],
            ["读写共享","share-rw",False],
        ]
    elif dev_name == "netdev":
        return "backend", None, [
            ["类型","type",["tap"]],
            ["标识符","id",""],
            ["Host网卡","ifname",""]
        ]
    elif dev_name == "e1000":
        return "pci", None, [
            ["初始化VET标志", "init-vet", True],
            ["MAC地址", "mac", "52:54:00:12:34:56"],
            ["迁移TSO属性", "migrate_tso_props", True],
            ["网络后端ID", "netdev", ""],
        ] + pci_configs
    elif dev_name == "e1000e":
        return "pci", None, [
            ["初始化VET标志", "init-vet", True],
            ["MAC地址", "mac", "52:54:00:12:34:56"],
            ["迁移TIMADJ属性", "migrate-timadj", True],
            ["网络后端ID", "netdev", ""],
        ] + pci_configs
    elif dev_name == "i82550" or dev_name == "i82558a" or dev_name == "igb" or dev_name == "ne2k_pci" or dev_name == "rtl8139":
        return "pci", None, [
            ["MAC地址", "mac", "52:54:00:12:34:56"],
            ["网络后端ID", "netdev", ""],
        ] + pci_configs
    elif dev_name == "virtio-net-pci":
        return "pci", "virtio-net", [
            ["MAC地址", "mac", "52:54:00:12:34:56"],
            ["Hash IPV4","hash-ipv4",["auto","on","off"]],
            ["Hash IPV6","hash-ipv6",["auto","on","off"]],
            ["Hash TCP4","hash-tcp4",["auto","on","off"]],
            ["Hash TCP6","hash-tcp6",["auto","on","off"]],
            ["主机MTU大小","host_mtu",0],
            ["网络后端ID", "netdev", ""],
        ] + pci_configs
    elif dev_name == "virtio-net-device":
        return "virtio-net", None, [
            ["启用任意布局", "any_layout", True],
            ["MAC地址", "mac", "52:54:00:12:34:56"],
            ["Hash IPV4","hash-ipv4",["auto","on","off"]],
            ["Hash IPV6","hash-ipv6",["auto","on","off"]],
            ["Hash TCP4","hash-tcp4",["auto","on","off"]],
            ["Hash TCP6","hash-tcp6",["auto","on","off"]],
            ["主机MTU大小","host_mtu",0],
            ["发送队列大小","tx_queue_size", 256],
        ]
    elif dev_name == "ne2k_isa":  # bus isa
        return "isa", None,[
            ["IO基地址", "iobase", 768],
            ["中断", "irq", 9],
            ["MAC地址","mac","52:54:00:12:34:56"],
            ["网络后端ID","netdev",""],
        ]
    elif dev_name == "usb-net": # bus usb-bus
        return "usb", None, [
            ["MAC地址","mac","52:54:00:12:34:56"],
            ["网络后端ID","netdev",""],
            ["开启msos描述","msos-desc",True],
            ["pcap","pcap",""],
            ["端口","port",""],
            ["串口","serial",""]
        ]
    elif dev_name == "chardev":
        return "backend", None,[
            ["类型","type",["stdio","file","pty"]],
            ["标识符","id",""],
            ["文件路径","path",""]
        ]
    elif dev_name == "i8042":
        return "isa", None,[
            ["键盘IRQ号", "kbd-irq", 1],
            ["鼠标IRQ号", "mouse-irq", 12],
        ]
    elif dev_name == "pci-serial":
        return "pci", None, [
            ["后端字符设备","chardev",""],
            ["波特率","baudbase",115200],
        ] + pci_configs
    elif dev_name == "tpci200":
        return "pci", None,[
        ] + pci_configs
    elif dev_name == "usb-serial": #bus usb-bus
        return "usb", None, [
            ["后端字符设备","chardev",""],
            ["开启msos描述","msos-desc",True],
            ["pcap","pcap",""],
            ["端口","port",""],
            ["串口","serial",""]
        ]
    elif dev_name == "virtio-serial-pci":
        return "pci", "virtio-serial", [
            ["启用AER", "aer", False],
            ["任意布局", "any_layout", True],
            ["启用ATS", "ats", False],
            ["类代码", "class", 0],
            ["启动标志支持", "use-started", True],
            ["中断向量数", "vectors", 2],
        ] + pci_configs
    elif dev_name == "virtio-serial-device":
        return "virtio-serial", None, [
            ["启用任意布局", "any_layout", True],
            ["紧急写", "emergency-write", True],

        ] 
    
def generate_dev_header(dev_name):
    if get_dev_bus_type(dev_name) == "backend":
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
    if get_dev_bus_type(dev_name) == "backend":
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



def get_devices_list():
    return {
        "i386" : {
            "USB" : 
                [
                    "ich9-usb-ehci1", 
                    "ich9-usb-ehci2", 
                    "ich9-usb-uhci1", 
                    "ich9-usb-uhci2", 
                    "piix3-usb-uhci", 
                    "piix4-usb-uhci", 
                    "usb-ehci", 
                    "nec-usb-xhci", 
                    "qemu-xhci", 
                ],
            "串口" :
                [
                    "i8042", 
                    "pci-serial", 
                    "tpci200", 
                    "usb-serial", 
                    "virtio-serial-pci"
                ],
            "网卡" : 
                [
                    "e1000", 
                    "e1000e", 
                    "i82550", 
                    "i82558a", 
                    "igb", 
                    "ne2k_pci", 
                    "rtl8139", 
                    "virtio-net-pci", 
                    "ne2k_isa", 
                    "usb-net"
                ],
            "存储" : 
                [
                    "dc390", 
                    "ide-cd", 
                    "ide-hd", 
                    "isa-fdc", 
                    "isa-ide", 
                    "usb-uas", 
                    "virtio-blk-pci"
                ],
            "显示设备" : 
                [
                    "ati-vga", 
                    "cirrus-vga", 
                    "VGA", 
                    "virtio-gpu-pci"
                ],
            "声卡" :
                [
                    "adlib", 
                    "cs4231a", 
                    "ES1370", 
                    "intel-hda"
                ],
            "后端设备" :
                [
                    "drive",
                    "chardev",
                    "netdev",
                ],
            "自定义" :
                [
                    "自定义"
                ],
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
def get_init_buses_by_arch(arch):
    init_buses = {
        "i386" : 
            ["sysbus", "pci", "isa", "ide", "i2c", "backend"]
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

def get_devices_list_by_arch(arch):
    lists = get_devices_list()
    return lists[arch]
def get_dev_bus_type(dev_name):
    bus, generate_bus, config = get_devices_info(dev_name)
    return bus
def get_dev_generate_bus_type(dev_name):
    bus, generate_bus, config = get_devices_info(dev_name)
    return generate_bus
def get_dev_config(dev_name):
    bus, generate_bus, config = get_devices_info(dev_name)
    return config
def validate_bus_type(dev_name, assgined_bus):
    if "." in assgined_bus:
        assgined_bus = assgined_bus.split(".")[0]
    valid_bus = get_dev_bus_type(dev_name)
    if valid_bus == assgined_bus:
        return True
    return False
    