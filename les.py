import busio
import adafruit_ccs811

from board import *
i2c_bus = busio.I2C(SCL, SDA)

ccs = adafruit_ccs811.CCS811(i2c_bus)

print(ccs.eco2)
print(ccs.tvoc)
