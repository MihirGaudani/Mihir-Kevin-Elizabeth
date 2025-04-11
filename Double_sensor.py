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
file_writer.writerow(["time", "PM10_Standard", "PM25_Standard", "PM100_Standard", "PM10_Enviornment", "PM25_Enviornment", "PM100_Enviornment", "Particles_03um", "Particles_05um", "Particles_10um", "Particles_25um", "Particles_50um", "Particles_100um", "Tempurature", "Relative_Humidity", "Pressure", "Altitude", "Gas"])
print("Found PM2.5 sensor, reading data...")
print(sys.argv)

print("how long do you want this to run for (in seconds)")
runtime = int(sys.argv[1])
print("enter 1 for integer /n 2 for string")
variable_type = int(sys.argv[2])
count = 0
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
    print("\n", time.ctime(),"Temperature %0.1f C" % bme680.temperature,"Gas %d ohm" % bme680.gas,"Humidity: %0.1f %%" % bme680.relative_humidity,"Pressure: %0.3f hPa" % bme680.pressure,"Altitude = %0.2f meters" % bme680.altitude,time.ctime())
    if variable_type == 1:
         PM10_Standard = int(aqdata["pm10 standard"])
         PM25_Standard = int(aqdata["pm25 standard"])
         PM100_Standard = int(aqdata["pm100 standard"])
         PM10_Enviornment = int(aqdata["pm10 env"])
         PM25_Enviornment = int(aqdata["pm25 env"]) 
         PM100_Enviornment = int(aqdata["pm100 env"])
         Particles_03um = int(aqdata["particles 03um"])
         Particles_05um = int(aqdata["particles 05um"])
         Particles_10um = int(aqdata["particles 10um"])
         Particles_25um = int(aqdata["particles 25um"])
         Particles_50um = int(aqdata["particles 50um"])
         Particles_100um = int(aqdata["particles 100um"])
         Tempurature = int(bme680.temperature)
         Relative_Humidity = int(bme680.relative_humidity)
         Pressure = int(bme680.pressure)
         Altitude = int(bme680.altitude)
         time1 = int(time.time())
         Gas = int(bme680.gas)
    elif variable_type == 2:
         PM10_Standard = str(aqdata["pm10 standard"])
         PM25_Standard = str(aqdata["pm25 standard"])
         PM100_Standard = str(aqdata["pm100 standard"])
         PM10_Enviornment = str(aqdata["pm10 env"])
         PM25_Enviornment = str(aqdata["pm25 env"]) 
         PM100_Enviornment = str(aqdata["pm100 env"])
         Particles_03um = str(aqdata["particles 03um"])
         Particles_05um = str(aqdata["particles 05um"])
         Particles_10um = str(aqdata["particles 10um"])
         Particles_25um = str(aqdata["particles 25um"])
         Particles_50um = str(aqdata["particles 50um"])
         Particles_100um = str(aqdata["particles 100um"])
         Tempurature = str(bme680.temperature)
         Relative_Humidity = str(bme680.relative_humidity)
         Pressure = str(bme680.pressure)
         Altitude = str(bme680.altitude)
         time1 = str(time.time())
         Gas = str(bme680.gas)
    elif variable_type == 3:
         PM10_Standard = float(aqdata["pm10 standard"])
         PM25_Standard = float(aqdata["pm25 standard"])
         PM100_Standard = float(aqdata["pm100 standard"])
         PM10_Enviornment = float(aqdata["pm10 env"])
         PM25_Enviornment = float(aqdata["pm25 env"]) 
         PM100_Enviornment = float(aqdata["pm100 env"])
         Particles_03um = float(aqdata["particles 03um"])
         Particles_05um = float(aqdata["particles 05um"])
         Particles_10um = float(aqdata["particles 10um"])
         Particles_25um = float(aqdata["particles 25um"])
         Particles_50um = float(aqdata["particles 50um"])
         Particles_100um = float(aqdata["particles 100um"])
         Tempurature = float(bme680.temperature)
         Relative_Humidity = float(bme680.relative_humidity)
         Pressure = float(bme680.pressure)
         Altitude = float(bme680.altitude)
         time1 = float(time.time())
         Gas = float(bme680.gas)
   
    file_writer.writerow([time1, PM10_Standard, PM25_Standard, PM100_Standard, PM10_Enviornment, PM25_Enviornment, PM100_Enviornment, Particles_03um, Particles_05um, Particles_10um, Particles_25um, Particles_50um, Particles_100um, Tempurature, Relative_Humidity, Pressure, Altitude, Gas])
    count = count + 1
		
	

	

    
