#!/usr/bin/env python3
import time
import board
import busio
import Adafruit_CCS811

i2c = busio.I2C(board.SCL, board.SDA)
print(Adafruit_CCS811.Adafruit_CCS811(mode))
ccs811 = Adafruit_CCS811.Adafruit_CCS811(i2c)


# Wait for the sensor to be ready
while not ccs811.data_ready:
    pass

while True:
    print("CO2: {} PPM, TVOC: {} PPB"
          .format(ccs811.eco2, ccs811.tvoc))
    time.sleep(0.5)
