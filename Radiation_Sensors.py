import RPi.GPIO as GPIO
import datetime
import time
#write a script that prints out the time-stamp each time a count is detected by your sensor
#NOTE: you will want to use a falling-edge event detection
#NOTE: call-back methods are functions that only run when some external property changes, 
#in this case, the change in voltage on the GPIO pin
Count = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN)
        GPIO.add_event_detect(6, GPIO.BOTH, callback=my_callback)
def my_callback(channel):
    if GPIO.input(channel) == GPIO.LOW:
        print('\n▼  at ' + str(datetime.datetime.now()))
        Count = Count + 1
    else:
        print('\n ▲ at ' + str(datetime.datetime.now())) 
        
        Count = Count + 1
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN)
GPIO.add_event_detect(6, GPIO.BOTH, callback=my_callback)
a = 1
while a < 3:
    GPIO.add_event_detect(channel, GPIO.RISING)
    if GPIO.event_detected(channel):
        print("I did it")
finally:
    GPIO.cleanup()
