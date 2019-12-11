# Available pins are: 0, 1, 2, 3, 4, 5, 12, 13, 14, 15, 16, which correspond to the actual GPIO pin numbers of
# ESP8266 chip

import utils
import utime


def main():
    try:
        # ifconfig = utils.wifi_setup()
        # print(ifconfig)
        # mqtt_client = utils.mqtt_setup()
        # lcd = utils.i2c_setup()
        pass
    except OSError as e:
        utils.module_reset()
    while True:
        try:
            pass
        except OSError as e:
            utils.module_reset()


if __name__ == '__main__':
    main()
