#include "qemu/osdep.h"
#include "qemu/units.h"
#include "hw/acpi/acpi.h"
#include "hw/char/parallel-isa.h"
#include "hw/loader.h"
#include "hw/i2c/smbus_eeprom.h"
#include "hw/rtc/mc146818rtc.h"
#include "system/tcg.h"
#include "system/kvm.h"
#include "hw/i386/kvm/clock.h"
#include "hw/pci-host/q35.h"
#include "hw/pci/pcie_port.h"
#include "hw/qdev-properties.h"
#include "hw/i386/x86.h"
#include "hw/i386/pc.h"
#include "hw/i386/amd_iommu.h"
#include "hw/i386/intel_iommu.h"
#include "hw/vfio/types.h"
#include "hw/virtio/virtio-iommu.h"
#include "hw/display/ramfb.h"
#include "hw/ide/pci.h"
#include "hw/ide/ahci-pci.h"
#include "hw/intc/ioapic.h"
#include "hw/southbridge/ich9.h"
#include "hw/usb.h"
#include "hw/usb/hcd-uhci.h"
#include "qapi/error.h"
#include "qemu/error-report.h"
#include "system/numa.h"
#include "hw/hyperv/vmbus-bridge.h"
#include "hw/mem/nvdimm.h"
#include "hw/uefi/var-service-api.h"
#include "hw/i386/acpi-build.h"
#include "target/i386/cpu.h"

#include "qemu/osdep.h"
#include CONFIG_DEVICES

#include "qemu/units.h"
#include "hw/char/parallel-isa.h"
#include "hw/dma/i8257.h"
#include "hw/loader.h"
#include "hw/i386/x86.h"
#include "hw/i386/pc.h"
#include "hw/i386/apic.h"
#include "hw/pci-host/i440fx.h"
#include "hw/rtc/mc146818rtc.h"
#include "hw/southbridge/piix.h"
#include "hw/display/ramfb.h"
#include "hw/pci/pci.h"
#include "hw/pci/pci_ids.h"
#include "hw/usb.h"
#include "net/net.h"
#include "hw/ide/isa.h"
#include "hw/ide/pci.h"
#include "hw/irq.h"
#include "system/kvm.h"
#include "hw/i386/kvm/clock.h"
#include "hw/sysbus.h"
#include "hw/i2c/smbus_eeprom.h"
#include "system/memory.h"
#include "hw/acpi/acpi.h"
#include "hw/vfio/types.h"
#include "qapi/error.h"
#include "qemu/error-report.h"
#include "system/xen.h"
#ifdef CONFIG_XEN
#include <xen/hvm/hvm_info_table.h>
#include "hw/xen/xen_pt.h"
#include "hw/xen/xen_igd.h"
#endif
#include "hw/xen/xen-x86.h"
#include "hw/xen/xen.h"
#include "migration/global_state.h"
#include "migration/misc.h"
#include "system/runstate.h"
#include "system/numa.h"
#include "hw/hyperv/vmbus-bridge.h"
#include "hw/mem/nvdimm.h"
#include "hw/uefi/var-service-api.h"
#include "hw/i386/acpi-build.h"
#include "target/i386/cpu.h"
#include "qemu/option.h"

typedef struct XXMachineClass
{
    /*< private >*/
    PCMachineClass parent_class;
} XXMachineClass;
typedef struct XXMachineState
{
    /*< private >*/
    PCMachineState parent_obj;
} XXMachineState;
extern QemuOptsList qemu_netdev_opts;
extern QemuOptsList qemu_chardev_opts;

#define TYPE_XX_MACHINE MACHINE_TYPE_NAME("xx")
DECLARE_OBJ_CHECKERS(XXMachineState, XXMachineClass,
                     XX_MACHINE, TYPE_XX_MACHINE)
void pc_i440fx_init(MachineState *machine);
BusState *qbus_find_recursive(BusState *bus, const char *name,
                                     const char *bus_typename);
bool qbus_is_full(BusState *bus);
static void xx_machine_initfn(Object *obj)
{
    XXMachineState *pcms = XX_MACHINE(obj);
    XXMachineClass *pcmc = XX_MACHINE_GET_CLASS(pcms);
    MachineClass *mc = MACHINE_CLASS(pcmc);
}
static void xx_board_init(MachineState *machine)
{
    X86MachineState *x86ms = X86_MACHINE(machine);
    PCMachineState *pcms = PC_MACHINE(machine);
    pc_i440fx_init(machine);
    DeviceState *dev;
    QemuOpts *opts;
    DriveInfo *pnor;
    BlockBackend *blkbackend;
    char *arg;
    BusState *pcibus = qbus_find_recursive(sysbus_get_default(), NULL, TYPE_PCI_BUS);
    BusState *i2cbus = qbus_find_recursive(sysbus_get_default(), NULL, TYPE_I2C_BUS);
    BusState *ssibus = qbus_find_recursive(sysbus_get_default(), NULL, "SSI");
    BusState *idebus =  qbus_find_recursive(sysbus_get_default(), NULL, TYPE_IDE_BUS);
    BusState *isabus = qbus_find_recursive(sysbus_get_default(), NULL, TYPE_ISA_BUS);
    BusState *usbbus = qbus_find_recursive(sysbus_get_default(), NULL, TYPE_USB_BUS);
    BusState *scsibus = qbus_find_recursive(sysbus_get_default(), NULL, "SCSI");
    BusState *virtiobus = qbus_find_recursive(sysbus_get_default(), NULL, "virtio-bus");
    
    printf("%p %p %p %p %p %p %p %p\n", pcibus, i2cbus, ssibus, idebus, isabus, usbbus, scsibus, virtiobus);















    // DeviceState *dev = qdev_new("AC97");
    // qdev_realize_and_unref(dev, pcms->pcibus, &error_fatal);
    // DeviceState *dev2 = qdev_new("hpet");
    // qdev_prop_set_uint32(dev2, "hpet-intcap", 2);
    // sysbus_realize_and_unref(dev2, &error_fatal);
    // sysbus_mmio_map(SYS_BUS_DEVICE(dev2), 0, 0xfed00000);
    // sysbus_connect_irq(SYS_BUS_DEVICE(dev2), 0, x86ms->gsi);
}
static void xx_machine_class_init(ObjectClass *oc, const void *data)
{
    XXMachineClass *kmc = XX_MACHINE_CLASS(oc);
    PCMachineClass *x86mc = X86_MACHINE_CLASS(oc);
    MachineClass *mc = MACHINE_CLASS(oc);
    pc_i440fx_machine_10_0_options(mc);
    mc->init = xx_board_init;
}
static const TypeInfo xx_machine_info = {
    .name = TYPE_XX_MACHINE,
    .parent = TYPE_PC_MACHINE,
    .instance_size = sizeof(XXMachineState),
    .instance_init = xx_machine_initfn,
    .class_size = sizeof(XXMachineClass),
    .class_init = xx_machine_class_init,
};

static void xx_machine_register_types(void)
{
    type_register_static(&xx_machine_info);
}

type_init(xx_machine_register_types)