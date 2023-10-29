import RPi.GPIO as gpio
import time


PULL_UP = gpio.PUD_UP
PULL_DOWN = gpio.PUD_DOWN
EDGE_RISING = gpio.RISING
EDGE_FALLING = gpio.FALLING

print("initializing gpio...")
gpio.setmode(gpio.BCM)
gpio.setwarnings(0)

SWITCH_DEBOUNCE_TIME = 0.33
last_switch_time = time.time()


def is_event_detected(pin_nr):
    return gpio.event_detected(pin_nr)


def add_event_detect(pin_nr, edge_type=None, callback=None):
    if callback and edge_type:
        gpio.add_event_detect(pin_nr, edge_type, callback, bouncetime=200)
    elif edge_type:
        gpio.add_event_detect(pin_nr, edge_type, bouncetime=200)
    elif callback:
        gpio.add_event_detect(pin_nr, gpio.BOTH, callback, bouncetime=200)
    else:
        gpio.add_event_detect(pin_nr, gpio.BOTH, bouncetime=200)


def wait_for_edge(pin_nr, timeout=None, edge_type=None):
    if timeout and edge_type:
        channel = gpio.wait_for_edge(pin_nr, edge_type, timeout=timeout)
    elif timeout:
        channel = gpio.wait_for_edge(pin_nr, gpio.BOTH, timeout=timeout)
    elif edge_type:
        gpio.wait_for_edge(pin_nr, edge_type)
        return True
    else:
        gpio.wait_for_edge(pin_nr, gpio.BOTH)
        return True

    if channel is None:
        return False
    return True


def init_PWM_pin(pin_nr, freq):
    return gpio.PWM(pin_nr, freq)


def init_output_pin(pin_nr, initial_state):
    print('setting pin nr {} for initial state {}'.format(pin_nr, initial_state))
    gpio.setup(pin_nr, gpio.OUT, initial=initial_state)


def init_input_pin(pin_nr, pud=None):
    print('setting pin nr {} for input'.format(pin_nr))
    if pud:
        gpio.setup(pin_nr, gpio.IN, pull_up_down=pud)
    else:
        gpio.setup(pin_nr, gpio.IN)


def get_state(pin_nr):
    state = gpio.input(pin_nr)
    print('input {} for pin nr {}'.format(state, pin_nr))
    return state


def set_state(pin_nr, state):
    gpio.output(pin_nr, state)
    print('output {} for pin nr {}'.format(state, pin_nr))


def switch_state(pin_nr):
    time_now = time.time()
    global last_switch_time
    if time_now - last_switch_time > SWITCH_DEBOUNCE_TIME:
        last_switch_time = time_now
        print('switching pin nr {}'.format(pin_nr))
        set_state(pin_nr, not bool(get_state(pin_nr)))
        print('pin nr {} state is {}'.format(pin_nr, get_state(pin_nr)))


