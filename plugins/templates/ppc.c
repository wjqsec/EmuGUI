#include "qemu/osdep.h"
#include "qemu/datadir.h"
#include "qemu/memalign.h"
#include "qemu/guest-random.h"
#include "qapi/error.h"
#include "qapi/qapi-events-machine.h"
#include "qapi/qapi-events-qdev.h"
#include "qapi/visitor.h"
#include "system/system.h"
#include "system/hostmem.h"
#include "system/numa.h"
#include "system/tcg.h"
#include "system/qtest.h"
#include "system/reset.h"
#include "system/runstate.h"
#include "qemu/log.h"
#include "hw/fw-path-provider.h"
#include "elf.h"
#include "net/net.h"
#include "system/device_tree.h"
#include "system/cpus.h"
#include "system/hw_accel.h"
#include "kvm_ppc.h"
#include "migration/misc.h"
#include "migration/qemu-file-types.h"
#include "migration/global_state.h"
#include "migration/register.h"
#include "migration/blocker.h"
#include "mmu-hash64.h"
#include "mmu-book3s-v3.h"
#include "cpu-models.h"
#include "hw/core/cpu.h"

#include "hw/ppc/ppc.h"
#include "hw/loader.h"

#include "hw/ppc/fdt.h"
#include "hw/ppc/spapr.h"
#include "hw/ppc/spapr_nested.h"
#include "hw/ppc/spapr_vio.h"
#include "hw/ppc/vof.h"
#include "hw/qdev-properties.h"
#include "hw/pci-host/spapr.h"
#include "hw/pci/msi.h"

#include "hw/pci/pci.h"
#include "hw/scsi/scsi.h"
#include "hw/virtio/virtio-scsi.h"
#include "hw/virtio/vhost-scsi-common.h"

#include "system/ram_addr.h"
#include "system/confidential-guest-support.h"
#include "hw/usb.h"
#include "qemu/config-file.h"
#include "qemu/error-report.h"
#include "trace.h"
#include "hw/nmi.h"
#include "hw/intc/intc.h"

#include "hw/ppc/spapr_cpu_core.h"
#include "hw/mem/memory-device.h"
#include "hw/ppc/spapr_tpm_proxy.h"
#include "hw/ppc/spapr_nvdimm.h"
#include "hw/ppc/spapr_numa.h"
#include "hw/pci/pci.h"
#include "hw/i2c/i2c.h"
#include "hw/ide/ide-bus.h"
#include "hw/usb.h"
#include <libfdt.h>
#include "qemu/osdep.h"
#include "qemu/units.h"
#include "qemu/datadir.h"
#include "qemu/log.h"
#include "qemu/error-report.h"
#include "qapi/error.h"
#include "hw/ppc/ppc.h"
#include "hw/boards.h"
#include "hw/loader.h"
#include "hw/pci-host/articia.h"
#include "hw/isa/vt82c686.h"
#include "hw/ide/pci.h"
#include "hw/i2c/smbus_eeprom.h"
#include "hw/ppc/ppc.h"
#include "system/block-backend.h"
#include "system/qtest.h"
#include "system/reset.h"
#include "kvm_ppc.h"
#include "elf.h"

#include <zlib.h> /* for crc32 */
typedef struct XXMachineClass
{
    /*< private >*/
    MachineClass parent_class;
} XXMachineClass;
typedef struct XXMachineState
{
    /*< private >*/
    MachineState parent_obj;
} XXMachineState;
extern QemuOptsList qemu_netdev_opts;
extern QemuOptsList qemu_chardev_opts;
#define TYPE_XX_MACHINE MACHINE_TYPE_NAME("xx")
DECLARE_OBJ_CHECKERS(XXMachineState, XXMachineClass,
                     XX_MACHINE, TYPE_XX_MACHINE)
BusState *qbus_find_recursive(BusState *bus, const char *name,
                                     const char *bus_typename);
bool qbus_is_full(BusState *bus);
void amigaone_init(MachineState *machine);
static void xx_machine_initfn(Object *obj)
{
    XXMachineState *pcms = XX_MACHINE(obj);
    XXMachineClass *pcmc = XX_MACHINE_GET_CLASS(pcms);
    MachineClass *mc = MACHINE_CLASS(pcmc);
}
static void xx_board_init(MachineState *machine)
{
    amigaone_init(machine);
    XXMachineState *pcms = XX_MACHINE(machine);
    XXMachineClass *pcmc = XX_MACHINE_GET_CLASS(pcms);
    MachineClass *mc = MACHINE_CLASS(pcmc);
    MemoryRegion *system_memory = get_system_memory();
    BusState *pcibus = qbus_find_recursive(sysbus_get_default(), NULL, TYPE_PCI_BUS);
    BusState *i2cbus = qbus_find_recursive(sysbus_get_default(), NULL, TYPE_I2C_BUS);
    BusState *ssibus = qbus_find_recursive(sysbus_get_default(), NULL, "SSI");
    BusState *idebus =  qbus_find_recursive(sysbus_get_default(), NULL, TYPE_IDE_BUS);
    BusState *isabus = qbus_find_recursive(sysbus_get_default(), NULL, TYPE_ISA_BUS);
    BusState *usbbus = qbus_find_recursive(sysbus_get_default(), NULL, TYPE_USB_BUS);
    BusState *scsibus = qbus_find_recursive(sysbus_get_default(), NULL, TYPE_ISA_BUS);
    BusState *virtiobus = qbus_find_recursive(sysbus_get_default(), NULL, TYPE_USB_BUS);
    printf("pci:%p i2c:%p ssi:%p ide:%p isa:%p usb:%p scsi:%p virt:%p\n", pcibus, i2cbus, ssibus, idebus, isabus, usbbus, scsibus, virtiobus);
}
static void xx_machine_class_init(ObjectClass *oc, const void *data)
{
    XXMachineClass *kmc = XX_MACHINE_CLASS(oc);
    MachineClass *mc = MACHINE_CLASS(oc);
    mc->init = xx_board_init;
    mc->block_default_type = IF_IDE;
    mc->default_cpu_type = POWERPC_CPU_TYPE_NAME("7457_v1.2");
    mc->default_display = "std";
    mc->default_ram_id = "ram";
    mc->default_ram_size = 512 * MiB;
}

static const TypeInfo xx_machine_info = {
    .name = TYPE_XX_MACHINE,
    .parent = TYPE_MACHINE,
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