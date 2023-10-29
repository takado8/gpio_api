from device.device_service import DeviceService
from rest_controller import app

root = '/relay/'


@app.post(root + '<device_name>')
def switch(device_name):
    device = DeviceService.get_device(device_name)
    if device:
        device.switch()
        return f'Switching {device}'
    else:
        return f'Unknown device: {device_name}.'


@app.post(root + '<device_name>/<state>')
def set_state(device_name, state):
    device = DeviceService.get_device(device_name)
    if device:
        device.set_state(state)
        return f'Setting {device} to {state}'
    else:
        return f'Unknown device: {device_name}.'
