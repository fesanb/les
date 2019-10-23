#!/usr/bin/env python3
import busio
import Adafruit_CCS811

from board import *
i2c_bus = busio.I2C(SCL, SDA)

ccs = Adafruit_CCS811.Adafruit_CCS811(i2c_bus)

print(ccs.eco2)
print(ccs.tvoc)
