import Domoticz
from devices.device import Device


class PushOnButton(Device):
    def create_device(self, unit, device_id, device_name):
        return Domoticz.Device(Unit=unit, DeviceID=device_id, Name=device_name, Type=244, Subtype=73, Switchtype=9).Create()

    def get_numeric_value(self, value, device):
        return 1 if value.lower() == 'on' else 0

    def get_string_value(self, value, device):
        return 'On' if value.lower() == 'on' else 'Off'

    def handle_command(self, device_data, command, level, color):
        device_address = device_data['ieee_addr']
        device = self.get_device(device_address, self.alias)

        Domoticz.Debug('Command "' + command + '" from device "' + device.Name + '"')

        device.Update(
            nValue=self.get_numeric_value(command, device),
            sValue=self.get_string_value(command, device)
        )