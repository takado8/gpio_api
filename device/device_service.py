from device.devices import DEVICES


class DeviceService:
    @staticmethod
    def get_device(device):
        if device in DEVICES:
            return DEVICES[device]
