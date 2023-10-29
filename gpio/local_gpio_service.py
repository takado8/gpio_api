from gpio.gpio import set_state, switch_state, init_output_pin


class LocalGPIOService:
    @staticmethod
    def init_output_pin(pin_nr, initial_state):
        init_output_pin(pin_nr, initial_state)

    @staticmethod
    def set_state(pin_nr, on_state):
        set_state(pin_nr, on_state)

    @staticmethod
    def switch_state(pin_nr):
        switch_state(pin_nr)
