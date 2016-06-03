Overview
--------

Python library for getting readings from DMDPW power meters, via Modbus, over a serial port.

Example of use
--------------
::

    from powermeter import PowerMeter

    p = PowerMeter()

    voltage = p.get_voltage_value()
    ampere = p.get_ampere_value()
    watt = p.get_watt_value()
    p_wh = p.get_plus_wh()
    n_wh = p.get_minus_wh()
    ry1, ry2, ry3, ry4 = p.get_relay_state()
    print("Voltage: %s V", voltage)
    print("Ampere: %s A", ampere)
    print("Watt: %s W", watt)
    print("+WH: %s W", p_wh)
    print("-WH: %s W", n_wh)
    print("Relay State: RY1: %s, RY2: %s, RY3: %s, RY4: %s", ry1, ry2, ry3, ry4)

References
----------

- http://pymodbus.readthedocs.org/en/latest/library/sync-client.html - examples of Modbus clients