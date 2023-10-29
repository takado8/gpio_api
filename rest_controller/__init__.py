from flask import Flask


app = Flask(__name__)

import rest_controller.relay_devices_controller
import rest_controller.pwm_devices_controler