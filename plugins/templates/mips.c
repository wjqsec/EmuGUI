#include "qemu/osdep.h"
#include "qemu/datadir.h"
#include "hw/clock.h"
#include "hw/mips/mips.h"
#include "hw/intc/i8259.h"
#include "hw/dma/i8257.h"
#include "hw/char/serial-mm.h"
#include "hw/char/parallel.h"
#include "hw/isa/isa.h"
#include "hw/block/fdc.h"
#include "system/system.h"
#include "hw/boards.h"
#include "net/net.h"
#include "hw/scsi/esp.h"
#include "hw/loader.h"
#include "hw/rtc/mc146818rtc.h"
#include "hw/timer/i8254.h"
#include "hw/display/vga.h"
#include "hw/display/bochs-vbe.h"
#include "hw/audio/pcspk.h"
#include "hw/input/i8042.h"
#include "hw/sysbus.h"
#include "system/qtest.h"
#include "system/reset.h"
#include "qapi/error.h"
#include "qemu/error-report.h"
#include "qemu/help_option.h"
#ifdef CONFIG_TCG
#include "accel/tcg/cpu-ops.h"
#endif /* CONFIG_TCG */
#include "cpu.h"
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
static void xx_machine_initfn(Object *obj)
{
    XXMachineState *pcms = XX_MACHINE(obj);
    XXMachineClass *pcmc = XX_MACHINE_GET_CLASS(pcms);
    MachineClass *mc = MACHINE_CLASS(pcmc);
}
static void xx_board_init(MachineState *machine)
{
    XXMachineState *pcms = XX_MACHINE(machine);
    XXMachineClass *pcmc = XX_MACHINE_GET_CLASS(pcms);
    MachineClass *mc = MACHINE_CLASS(pcmc);
    MemoryRegion *system_memory = get_system_memory();
    BusState *pcibus = qbus_find_recursive(sysbus_get_default(), NULL, TYPE_PCI_BUS);
    BusState *i2cbus = qbus_find_recursive(sysbus_get_default(), NULL, TYPE_I2C_BUS);
    BusState *ssibus = qbus_find_recursive(sysbus_get_default(), NULL, TYPE_SSI_BUS);
    BusState *idebus =  qbus_find_recursive(sysbus_get_default(), NULL, TYPE_IDE_BUS);
    BusState *isabus = qbus_find_recursive(sysbus_get_default(), NULL, TYPE_ISA_BUS);
    BusState *usbbus = qbus_find_recursive(sysbus_get_default(), NULL, TYPE_USB_BUS);
}
static void xx_machine_class_init(ObjectClass *oc, const void *data)
{
    XXMachineClass *kmc = XX_MACHINE_CLASS(oc);
    MachineClass *mc = MACHINE_CLASS(oc);
    mc->init = xx_board_init;
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