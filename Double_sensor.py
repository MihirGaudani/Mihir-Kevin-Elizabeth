# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
Example sketch to connect to PM2.5 sensor with either I2C or UART.
"""

# pylint: disable=unused-import
import time
import board
import busio
from digitalio import DigitalInOut, Direction, Pull
import adafruit_pm25
import csv
import adafruit_bme680
import sys

reset_pin = None
# If you have a GPIO, its not a bad idea to connect it to the RESET pin
# reset_pin = DigitalInOut(board.G0)
# reset_pin.direction = Direction.OUTPUT
# reset_pin.value = False


# For use with a computer running Windows:
# import serial
# uart = serial.Serial("COM30", baudrate=9600, timeout=1)

# For use with microcontroller board:
# (Connect the sensor TX pin to the board/computer RX pin)
# uart = busio.UART(board.TX, board.RX, baudrate=9600)

# For use with Raspberry Pi/Linux:
import serial
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.25)

# For use with USB-to-serial cable:
# import serial
# uart = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=0.25)

# Connect to a PM2.5 sensor over UART
from adafruit_pm25.uart import PM25_UART
pm25 = PM25_UART(uart, reset_pin)

i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)

bme680.sea_level_pressure = 1013.25
i = 0

file = open("data.csv", "w", newline=None)
file_writer = csv.writer(file)
file_writer.writerow(["time", "data1", "data2", "data3", "data4", "data5", "data6", "data7", "data8", "data9", "data10", "data11", "data12"])
print("Found PM2.5 sensor, reading data...")
print(sys.argv)

print("how long do you want this to run for (in seconds)")
runtime = int(sys.argv[1])
print("enter 1 for integer /n 2 for string /n 3 for float")
variable_type = int(sys.argv[2])

while count < runtime:
    time.sleep(1)

    try:
        aqdata = pm25.read()
        # print(aqdata)
    except RuntimeError:
        print("Unable to read from sensor, retrying...")
        continue

    print()
    print("Concentration Units (standard)")
    print("---------------------------------------")
    print(
        "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
        % (aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"])
    )
    print("Concentration Units (environmental)")
    print("---------------------------------------")
    print(
        "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
        % (aqdata["pm10 env"], aqdata["pm25 env"], aqdata["pm100 env"])
    )
    print("---------------------------------------")
    print("Particles > 0.3um / 0.1L air:", aqdata["particles 03um"])
    print("Particles > 0.5um / 0.1L air:", aqdata["particles 05um"])
    print("Particles > 1.0um / 0.1L air:", aqdata["particles 10um"])
    print("Particles > 2.5um / 0.1L air:", aqdata["particles 25um"])
    print("Particles > 5.0um / 0.1L air:", aqdata["particles 50um"])
    print("Particles > 10 um / 0.1L air:", aqdata["particles 100um"])
    print("---------------------------------------")
    print("\n", time.ctime(),"Temperature %0.1f C" % bme680.temperature,"Gas %d ohm" % bme680.temperature,"Humidity: %0.1f %%" % bme680.relative_humidity,"Pressure: %0.3f hPa" % bme680.pressure,"Altitude = %0.2f meters" % bme680.altitude,time.ctime())
    data1 = aqdata["pm10 standard"]
    data2 = aqdata["pm25 standard"]
    data3 = aqdata["pm100 standard"]
    data4 = aqdata["pm10 env"] 
    data5 = aqdata["pm25 env"] 
    data6 = aqdata["pm100 env"]
    data7 = aqdata["particles 03um"]
    data8 = aqdata["particles 05um"]
    data9 = aqdata["particles 10um"]
    data10 = aqdata["particles 25um"]
    data11 = aqdata["particles 50um"]
    data12 = aqdata["particles 100um"]
    data13 = bme680.temperature
    data14 = bme680.relative_humidity
    data15 = bme680.pressure
    data16 = bme680.altitude
    time1 = time.time()
    if variable_type == 1:
        file_writer.writerow(int([time1, data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13, data14, data15, data16]))
    elif variable_type == 2:
        file_writer.writerow(str([time1, data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13, data14, data15, data16]))
    elif variable_type == 3:
        file_writer.writerow(float([time1, data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13, data14, data15, data16]))

		
	

	

    
