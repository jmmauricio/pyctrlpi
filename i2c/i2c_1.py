'''

sudo i2cdetect -y 1
http://www.ti.com.cn/cn/lit/ug/sprufb0d/sprufb0d.pdf
https://www.element14.com/community/docs/DOC-73950/l/raspberry-pi-2-model-b-gpio-40-pin-block-pinout

DSP f28335
----------

GPIO33 SCLA I2C
GPIO32 SCLA I2C

RASPi f28335
------------

GPIO33 SCLA I2C
GPIO32 SCLA I2C


'''

import smbus
import time
bus = smbus.SMBus(1)
address = 0x80

while 1==1:
    try:
        bear = bus.write_byte_data(address, 12)
        time.sleep(0.5)
        bear = bus.read_byte_data(address, 1)
        print(bear)
        time.sleep(0.5)
    except:
        pass



