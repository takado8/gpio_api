
class Device:
    def __init__(self, name, pin_nr, off_state, initial_state, gpio_service):
        self.name = name
        self.pin_nr = pin_nr
        self.off_state = off_state
        self.on_state = int(not bool(off_state))
        self.initial_state = initial_state
        self.gpio_service = gpio_service
        gpio_service.init_output_pin(pin_nr, self.on_state if initial_state else off_state)

    def on(self):
        self.gpio_service.set_state(self.pin_nr, self.on_state)

    def off(self):
        self.gpio_service.set_state(self.pin_nr, self.off_state)

    def switch(self):
        self.gpio_service.switch_state(self.pin_nr)

    def __str__(self):
        return 'Device(name={}, pin_nr={})'.format(self.name, self.pin_nr)
