import RPi.GPIO as GPIO
import datetime
import time
import sys
import csv
#write a script that prints out the time-stamp each time a count is detected by your sensor
#NOTE: you will want to use a falling-edge event detection
#NOTE: call-back methods are functions that only run when some external property changes, 
#in this case, the change in voltage on the GPIO pin
global Count
Count = 0
file = open("RadiationData.csv", "w", newline=None)
file_writer = csv.writer(file)
file_writer.writerow(["time", "count"])
def my_callback(channel):
     print('\n▼  at ' + str(datetime.datetime.now()))
     global Count
     Count = Count + 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN)
GPIO.add_event_detect(6, GPIO.FALLING, callback=my_callback)
thirds = 0
while thirds < int(sys.argv[1]):
    time.sleep(int(sys.argv[2]))
    thirds = thirds + int(sys.argv[2])
    print("I'm not dead")
    if thirds == int(sys.argv[2])*6:
        print(Count)
    file_writer.writerow([thirds, Count])
print(Count)
file.close()
GPIO.cleanup()
