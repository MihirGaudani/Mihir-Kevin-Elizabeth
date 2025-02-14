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

# Create library object, use 'slow' 100KHz frequency!
#i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
# Connect to a PM2.5 sensor over I2C
#pm25 = PM25_I2C(i2c, reset_pin)

print("Found PM2.5 sensor, reading data...")

while True:
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




    file = open("data.csv", "w", newline=none)
    file_writer = csv.writer(file)
    file_writer.writerow(["time", "data1", "data2", "data3", "data4", "data5", "data6", "data7", "data8"])
    data1 = "PM 1.0: %d\tPM2.5: %d\tPM10: %d"  % (aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"])
    data2 = "PM 1.0: %d\tPM2.5: %d\tPM10: %d" % (aqdata["pm10 env"], aqdata["pm25 env"], aqdata["pm100 env"])

    data3 = "Particles > 0.3um / 0.1L air:", aqdata["particles 03um"]
    data4 = "Particles > 0.5um / 0.1L air:", aqdata["particles 05um"]
    data5 = "Particles > 1.0um / 0.1L air:", aqdata["particles 10um"]
    data6 = "Particles > 2.5um / 0.1L air:", aqdata["particles 25um"]
    data7 = "Particles > 5.0um / 0.1L air:", aqdata["particles 50um"]
    data8 = "Particles > 10 um / 0.1L air:", aqdata["particles 100um"]
    time = time.time()
    file_writer.writerow([time, data1, data2, data3, data4, data5, data6, data7, data8])
