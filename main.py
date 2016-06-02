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
        dec_point = p.get_dec_point()
        ry1, ry2, ry3, ry4 = p.get_relay_state()
        logging.info("Voltage: %s", voltage)
        logging.info("Ampere: %s", ampere)
        logging.info("Watt: %s", watt)
        logging.info("+WH: %s", p_wh)
        logging.info("-WH: %s", n_wh)
        logging.info("Relay State: RY1: %s, RY2: %s, RY3: %s, RY4: %s", ry1,
                     ry2, ry3, ry4)
        logging.info("Decimal Point: %s", dec_point)
        sleep(1)
