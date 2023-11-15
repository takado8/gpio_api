from device.device import Device
from gpio.local_gpio_service import LocalGPIOService

local_gpio_service = LocalGPIOService()

DEVICES = {
    'heater': Device('heater', pin_nr=25, off_state=1, initial_state=0, gpio_service=local_gpio_service),
    'desk_lamp': Device('desk_lamp', pin_nr=24, off_state=1, initial_state=0, gpio_service=local_gpio_service),
    'fan': Device('fan', pin_nr=23, off_state=1, initial_state=0, gpio_service=local_gpio_service),
    'lamp': Device('lamp', pin_nr=8, off_state=1, initial_state=0, gpio_service=local_gpio_service),
    'ceiling_light': Device('ceiling_light', pin_nr=17, off_state=0, initial_state=0, gpio_service=local_gpio_service)
}
