import RPi.GPIO as GPIO
import datetime
import time
#write a script that prints out the time-stamp each time a count is detected by your sensor
#NOTE: you will want to use a falling-edge event detection
#NOTE: call-back methods are functions that only run when some external property changes, 
#in this case, the change in voltage on the GPIO pin
global Count
Count = 0
def my_callback(channel):
     print('\n▼  at ' + str(datetime.datetime.now()))
     global Count
     Count = Count + 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN)
GPIO.add_event_detect(6, GPIO.FALLING, callback=my_callback)
seconds = time()
thirds = 0
while thirds > 120:
    time.sleep(10)
    thirds = thirds + 10
    if thirds == 60:
        print(count)
 
print("Goodbye!")
