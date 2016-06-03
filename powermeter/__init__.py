from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
from cachetools import cached

from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import registers as reg

SLAVE_ID = 50


class PowerMeter(object):
    def __init__(self, port='/dev/ttyUSB0'):
        self.client = ModbusClient(method='rtu', port=port, timeout=1,
                                   stopbits=1, baudrate=9600, bytesize=8)
        self.client.connect()

    def _get_holding_register_first(self, address, count):
        """
        Retrieve value from required register
        :param address: starting address to read from
        :param count: number of bytes to read
        """
        raw = self.client.read_holding_registers(address, count, unit=SLAVE_ID)
        return raw.registers[0]

    @cached(cache={})
    def _get_dec_point(self):
        """
        Retrieve decimal point state, True for W, False for KW
        """
        value = self._get_holding_register_first(reg.DEC_POINT, 2)
        value >>= 12
        return (value & 0b0000) == 0b0000

    def get_voltage_value(self):
        """
        Retrieve voltage value, returns a float value
        """
        value = self._get_holding_register_first(reg.VOLTAGE, 2)
        # voltage calculations
        # the value is computed as:
        # value/10
        return value/10

    def get_ampere_value(self):
        """
        Retrieve ampere value, returns a float value
        """
        value = self._get_holding_register_first(reg.AMPERE, 2)
        # ampere calculations
        # the value is computed as:
        # value/10
        return value/10

    def get_watt_value(self):
        """
        Retrieve watt value, returns a float value
        """
        value = self._get_holding_register_first(reg.WATT, 2)
        measure_unit = self._get_dec_point()
        # watt calculations
        # the value is computed as:
        # value/10
        return value/10 if measure_unit else value * 100

    def get_plus_wh(self):
        """
        Retrieve total consumed power, returns a float value
        """
        high_wh = self._get_holding_register_first(reg.P_WH_HIGH, 2)
        low_wh = self._get_holding_register_first(reg.P_WH_LOW, 2)
        measure_unit = self._get_dec_point()
        value = high_wh << 16
        value += low_wh
        return value/10 if measure_unit else value * 100

    def get_minus_wh(self):
        """
        Retrieve total generated power, returns a float value
        """
        high_wh = self._get_holding_register_first(reg.N_WH_HIGH, 2)
        low_wh = self._get_holding_register_first(reg.N_WH_LOW, 2)
        measure_unit = self._get_dec_point()
        value = high_wh << 16
        value += low_wh
        return value/10 if measure_unit else value * 100

    def get_relay_state(self):
        """
        Retrieve relay state, True if it's ON, False otherwise,
        returns a tuple of booleans (ry_1, ry_2, ry_3, ry_4)
        """
        value = self._get_holding_register_first(reg.RELAY_STATE, 2)
        ry_1 = (value & 0x0001) == 0x0001
        ry_2 = (value & 0x0010) == 0x0010
        ry_3 = (value & 0x0100) == 0x0100
        ry_4 = (value & 0x1000) == 0x1000
        return ry_1, ry_2, ry_3, ry_4
