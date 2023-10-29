from rest_controller import app
from gpio.gpio import switch_state

root = '/relay/'


@app.post(root + '<device>')
def switch(device):
    return f'Switching {device}'


@app.post(root + '<device>/<state>')
def turn(device, state):
    return f'Turning {device} to {state}'
