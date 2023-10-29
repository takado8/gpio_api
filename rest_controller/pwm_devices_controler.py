from rest_controller import app

root = '/pwm/'


@app.post(root + '<device>/<value>')
def set_percent(device, value):
    return f'Setting {device} to {value}'
