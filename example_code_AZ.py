import RPi.GPIO as GPIO
import time

# GPIO SETUP
sensorpin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensorpin, GPIO.IN)


def checkmoinsture_cb(sensorpin):
    if GPIO.input(sensorpin):
        print("no water detected")
    else:
        print("water detected")


# detect pin goes HIGH or LOW
GPIO.add_event_detect(sensorpin, GPIO.BOTH,
                      bouncetime=300)
# Lunch callback
GPIO.add_event_callback(sensorpin, checkmoinsture_cb)
# infinite loop
while True:
    time.sleep(1)
