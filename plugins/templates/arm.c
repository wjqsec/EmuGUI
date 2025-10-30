#include "qemu/osdep.h"
#include "qapi/error.h"
#include "hw/boards.h"
#include "hw/arm/boot.h"
#include "system/system.h"
#include "system/address-spaces.h"
#include "hw/arm/nrf51_soc.h"
#include "hw/i2c/microbit_i2c.h"
#include "hw/qdev-properties.h"
#include "qom/object.h"
#include "qemu/osdep.h"
#include "cpu.h"
#include "elf.h"
#include "hw/boards.h"
#include "qemu/error-report.h"
#include "qemu/osdep.h"
#include "qapi/error.h"
#include "hw/boards.h"
#include "hw/qdev-properties.h"
#include "hw/qdev-clock.h"
#include "qemu/error-report.h"
#include "hw/arm/stm32f205_soc.h"
#include "hw/arm/boot.h"
#include "hw/intc/armv7m_nvic.h"

#include "hw/pci/pci.h"
#include "hw/i2c/i2c.h"
#include "hw/ide/ide-bus.h"
#include "hw/usb.h"
typedef struct XXMachineClass
{
    /*< private >*/
    MachineClass parent_class;
} XXMachineClass;
typedef struct XXMachineState
{
    /*< private >*/
    MachineState parent_obj;
    ARMv7MState armv7m;
    Clock *sysclk;
    Clock *refclk;
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
    object_initialize_child(OBJECT(pcms), "armv7m", &pcms->armv7m, TYPE_ARMV7M);
    pcms->sysclk = clock_new(OBJECT(machine), "SYSCLK");
    clock_set_hz(pcms->sysclk, 25000000);
    pcms->refclk = clock_new(OBJECT(machine), "REFCLK");
    clock_set_hz(pcms->refclk, 1000000);
    qdev_connect_clock_in(OBJECT(&pcms->armv7m), "cpuclk", pcms->sysclk);
    qdev_connect_clock_in(OBJECT(&pcms->armv7m), "refclk", pcms->refclk);
    qdev_prop_set_string(&pcms->armv7m, "cpu-type",ARM_CPU_TYPE_NAME("cortex-m7"));
    object_property_set_link(OBJECT(&pcms->armv7m), "memory",
                             OBJECT(system_memory), &error_fatal);
    sysbus_realize(SYS_BUS_DEVICE(&pcms->armv7m), &error_fatal);


    // BusState *pcibus = qbus_find_recursive(sysbus_get_default(), NULL, TYPE_PCI_BUS);
    // BusState *i2cbus = qbus_find_recursive(sysbus_get_default(), NULL, TYPE_I2C_BUS);
    // BusState *ssibus = qbus_find_recursive(sysbus_get_default(), NULL, "SSI");
    // BusState *idebus =  qbus_find_recursive(sysbus_get_default(), NULL, TYPE_IDE_BUS);
    // BusState *isabus = qbus_find_recursive(sysbus_get_default(), NULL, TYPE_ISA_BUS);
    // BusState *usbbus = qbus_find_recursive(sysbus_get_default(), NULL, TYPE_USB_BUS);
    // BusState *scsibus = qbus_find_recursive(sysbus_get_default(), NULL, TYPE_ISA_BUS);
    // BusState *virtiobus = qbus_find_recursive(sysbus_get_default(), NULL, TYPE_USB_BUS);
    // printf("pci:%p i2c:%p ssi:%p ide:%p isa:%p usb:%p scsi:%p virt:%p\n", pcibus, i2cbus, ssibus, idebus, isabus, usbbus, scsibus, virtiobus);
    








    // armv7m_load_kernel(pcms->armv7m.cpu, machine->kernel_filename,
    //                    0, 0x2000000);
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