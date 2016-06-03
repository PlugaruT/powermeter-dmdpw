import logging
from time import sleep
from powermeter import PowerMeter


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)-8s '
                                                    '%(''message)s')

    p = PowerMeter()

    while True:
        voltage = p.get_voltage_value()
        ampere = p.get_ampere_value()
        watt = p.get_watt_value()
        p_wh = p.get_plus_wh()
        n_wh = p.get_minus_wh()
        ry1, ry2, ry3, ry4 = p.get_relay_state()
        logging.info("Voltage: %s V", voltage)
        logging.info("Ampere: %s A", ampere)
        logging.info("Watt: %s W", watt)
        logging.info("+WH: %s W", p_wh)
        logging.info("-WH: %s W", n_wh)
        logging.info("Relay State: RY1: %s, RY2: %s, RY3: %s, RY4: %s", ry1,
                     ry2, ry3, ry4)
        sleep(1)
