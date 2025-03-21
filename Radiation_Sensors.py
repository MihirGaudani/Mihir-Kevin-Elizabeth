import RPi.GPIO as GPIO
import datetime
#write a script that prints out the time-stamp each time a count is detected by your sensor
#NOTE: you will want to use a falling-edge event detection
#NOTE: call-back methods are functions that only run when some external property changes, 
#in this case, the change in voltage on the GPIO pin

def my_callback(channel):
    if GPIO.input(channel) == GPIO.HIGH:
        print('\n▼  at ' + str(datetime.datetime.now()))
    else:
        print('\n ▲ at ' + str(datetime.datetime.now())) 
 
try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(6, GPIO.IN)
    GPIO.add_event_detect(6, GPIO.BOTH, callback=my_callback)
 
    message = raw_input('\nPress any key to exit.\n')
 
finally:
    GPIO.cleanup()
 
print("Goodbye!")
